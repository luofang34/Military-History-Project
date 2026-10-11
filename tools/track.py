"""Great-circle track sampling and operation-package event emission, shared by missions.

Tracks are piecewise great-circle paths between timed waypoints. Positions are
sampled at an explicit interval and each fix stays valid until the next one, so
the App holds the last reconstructed fix rather than inventing motion.
"""
import json
import math
from dataclasses import dataclass, field

EARTH_M = 6_371_008.8
FT = 0.3048
MPH = 0.44704  # metres per second


def distance_m(a, b):
    lon1, lat1, lon2, lat2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = (math.sin((lat2 - lat1) / 2) ** 2
         + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2)
    return 2 * EARTH_M * math.asin(math.sqrt(h))


def bearing_deg(a, b):
    lon1, lat1, lon2, lat2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    y = math.sin(lon2 - lon1) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(lon2 - lon1)
    return math.degrees(math.atan2(y, x)) % 360


def destination(a, bearing, metres):
    lon1, lat1 = map(math.radians, a)
    d = metres / EARTH_M
    b = math.radians(bearing)
    lat2 = math.asin(math.sin(lat1) * math.cos(d) + math.cos(lat1) * math.sin(d) * math.cos(b))
    lon2 = lon1 + math.atan2(math.sin(b) * math.sin(d) * math.cos(lat1),
                             math.cos(d) - math.sin(lat1) * math.sin(lat2))
    return (math.degrees(lon2), math.degrees(lat2))


def offset(a, east_m, north_m):
    """Small local offset, used for formation slots."""
    lat = a[1] + north_m / 111_320.0
    lon = a[0] + east_m / (111_320.0 * math.cos(math.radians(a[1])))
    return (lon, lat)


def slerp(a, b, t):
    if t <= 0:
        return a
    if t >= 1:
        return b
    d = distance_m(a, b)
    if d < 0.01:
        return a
    return destination(a, bearing_deg(a, b), d * t)


@dataclass
class Waypoint:
    at_ms: int
    point: tuple
    alt_m: float


@dataclass
class Track:
    """Timed waypoints; altitude interpolates linearly, position along great circles."""
    waypoints: list = field(default_factory=list)

    def add(self, at_ms, point, alt_m):
        if self.waypoints and int(round(at_ms)) <= self.waypoints[-1].at_ms:
            raise ValueError(f"waypoint time {at_ms} does not advance")
        self.waypoints.append(Waypoint(int(round(at_ms)), tuple(point), float(alt_m)))
        return self

    @property
    def start(self):
        return self.waypoints[0].at_ms

    @property
    def end(self):
        return self.waypoints[-1].at_ms

    def at(self, t):
        w = self.waypoints
        if t <= w[0].at_ms:
            return w[0].point, w[0].alt_m
        for a, b in zip(w, w[1:]):
            if t <= b.at_ms:
                f = (t - a.at_ms) / (b.at_ms - a.at_ms)
                return slerp(a.point, b.point, f), a.alt_m + (b.alt_m - a.alt_m) * f
        return w[-1].point, w[-1].alt_m

    def heading(self, t, dt=2000):
        a, _ = self.at(max(self.start, t - dt))
        b, _ = self.at(min(self.end, t + dt))
        return bearing_deg(a, b) if distance_m(a, b) > 1 else 0.0

    def round_corners(self, t0, t1, passes=2):
        """Cuts the corners of the path strictly between `t0` and `t1` (Chaikin, in time,
        position and height), so turns read as turns; waypoints at or outside the bounds
        stay where the sources or the choreography put them."""
        for _ in range(passes):
            inside = [i for i, w in enumerate(self.waypoints) if t0 < w.at_ms < t1]
            if not inside:
                return self
            first, last = inside[0] - 1, inside[-1] + 1
            if first < 0 or last >= len(self.waypoints):
                return self
            span = self.waypoints[first:last + 1]
            cut = [span[0]]
            for a, b in zip(span, span[1:]):
                for f in (0.25, 0.75):
                    at = round(a.at_ms + (b.at_ms - a.at_ms) * f)
                    if cut[-1].at_ms < at < span[-1].at_ms:
                        cut.append(Waypoint(at, slerp(a.point, b.point, f),
                                            a.alt_m + (b.alt_m - a.alt_m) * f))
            cut.append(span[-1])
            self.waypoints[first:last + 1] = cut
        return self

    def fillet(self, bank_deg=30.0, min_turn=20.0, slow=0.08, step_deg=8.0, min_mps=0.0,
               keep=()):
        """Rounds each corner the path turns more than `min_turn` degrees at into an arc an
        aircraft banked `bank_deg` could fly, as far as keeping both neighbouring legs within
        `slow` of their speed, and above `min_mps`, allows, so the replay turns rather than
        snapping onto its next heading. The arc is centred on the corner's time; waypoints at
        the times in `keep`, points on the ground and the ends of the path stay where they
        are."""
        wps = self.waypoints
        out = [wps[0]]
        for a, v, b in zip(wps, wps[1:], wps[2:]):
            arc = None if v.at_ms in keep else _corner(a, v, b, bank_deg, min_turn, slow,
                                                        step_deg, min_mps)
            if arc is None or arc[0].at_ms <= out[-1].at_ms or arc[-1].at_ms >= b.at_ms:
                out.append(v)
            else:
                out.extend(arc)
        out.append(wps[-1])
        self.waypoints = out
        return self

    def shifted(self, east_m, north_m):
        """A formation slot rotated with the instantaneous heading of this track."""
        out = Track()
        for wp in self.waypoints:
            h = math.radians(self.heading(wp.at_ms))
            # Slot axes: +north_m is ahead, +east_m is to the right of the heading.
            e = east_m * math.cos(h) + north_m * math.sin(h)
            n = -east_m * math.sin(h) + north_m * math.cos(h)
            out.add(wp.at_ms, offset(wp.point, e, n), wp.alt_m)
        return out


def _corner(a, v, b, bank_deg, min_turn, slow, step_deg, min_mps):
    """The waypoints of the arc that replaces corner `v` between `a` and `b` (see
    Track.fillet), or None to keep the corner."""
    l1, l2 = distance_m(a.point, v.point), distance_m(v.point, b.point)
    if l1 < 20 or l2 < 20 or v.alt_m < 1 or v.at_ms <= a.at_ms or b.at_ms <= v.at_ms:
        return None
    h1, h2 = bearing_deg(a.point, v.point), bearing_deg(v.point, b.point)
    theta = (h2 - h1 + 180) % 360 - 180
    if abs(theta) < min_turn or abs(theta) > 170:
        return None
    half = math.radians(abs(theta)) / 2
    v1, v2 = l1 / (v.at_ms - a.at_ms) * 1000, l2 / (b.at_ms - v.at_ms) * 1000
    mps = (v1 + v2) / 2
    # A leg can be trimmed at both its ends, so each corner spends half its headroom.
    slow = min(slow, 1 - min_mps / min(v1, v2)) / 2
    if slow <= 0:
        return None
    ratio = 2 * half / math.tan(half)  # arc length over the cut length d
    # Cutting d off each leg shortens the path by d(2 - ratio); the legs absorb half each.
    cap = min(slow * l / (1 - ratio / 2 + slow * ratio / 2) for l in (l1, l2))
    d = min(mps ** 2 / (9.81 * math.tan(math.radians(bank_deg))) * math.tan(half), cap,
            0.4 * min(l1, l2))
    length = d * ratio
    n = max(2, math.ceil(abs(theta) / step_deg))
    # Each half of the arc keeps the speed of the leg it leaves or joins.
    t_in = v.at_ms - length / 2 / v1 * 1000

    def at(s):
        if s <= length / 2:
            return t_in + s / v1 * 1000
        return v.at_ms + (s - length / 2) / v2 * 1000
    alt_in = v.alt_m + (a.alt_m - v.alt_m) * d / l1
    alt_out = v.alt_m + (b.alt_m - v.alt_m) * d / l2
    point = destination(v.point, h1 + 180, d)
    arc = [Waypoint(round(t_in), point, alt_in)]
    for k in range(1, n + 1):
        point = destination(point, h1 + theta * (k - 0.5) / n, length / n)
        arc.append(Waypoint(round(at(length * k / n)), point,
                            alt_in + (alt_out - alt_in) * k / n))
    return arc


class Emitter:
    def __init__(self, operation_id):
        self.operation = operation_id
        self.events = []
        self.sequence = 0

    def _event(self, source, entity, observed, received, valid_until, provenance, evidence,
               payload, occurrence=None, raw=True):
        self.sequence = self.sequence + 1
        event = {
            "id": f"{self.operation}:{self.sequence}",
            "operation": self.operation,
            "source": {
                "id": source,
                "epoch": 0,
                "sequence": self.sequence,
                "raw_ns": observed * 1_000_000 if raw else None,
                "scale": "monotonic",
                "uncertainty_ns": 0,
            },
            "entity": entity,
            "observed_ms": int(observed),
            "received_ms": int(received),
        }
        if occurrence:
            event["occurrence"] = occurrence
        event.update({
            "valid_until_ms": None if valid_until is None else int(valid_until),
            "provenance": provenance,
            "supersedes": None,
            "evidence": list(evidence),
            "payload": payload,
        })
        self.events.append(event)
        return event

    def fix(self, source, entity, at, point, alt_m, bound_m, valid_until, provenance, evidence,
            received=None, reference="aircraft"):
        return self._event(source, entity, at, at if received is None else max(at, received),
                           valid_until, provenance, evidence, {
                               "kind": "position",
                               "data": {
                                   "point": {"lon": round(point[0], 5), "lat": round(point[1], 5)},
                                   "agl_m": None if alt_m is None else round(max(alt_m, 0.0), 1),
                                   "height_assumed": False,
                                   "bound_m": bound_m,
                                   "reference": reference,
                                   "calibration": None,
                               },
                           })

    def gap(self, source, entity, at, valid_until, provenance, evidence):
        return self._event(source, entity, at, at, valid_until, provenance, evidence,
                           {"kind": "position", "data": None})

    def condition(self, source, entity, at, condition, provenance, evidence):
        """A persistent MIL-STD-2525 condition report: fully_capable, damaged or destroyed."""
        return self._event(source, entity, at, at, None, provenance, evidence,
                           {"kind": "condition", "data": condition})

    def note(self, source, entity, at, until, text, provenance, evidence, occurrence=None):
        return self._event(source, entity, at, at, until, provenance, evidence,
                           {"kind": "annotation", "data": text}, occurrence)

    def track(self, source, entity, track, step_for, bound_for, provenance, evidence,
              received_for=None, start=None, end=None, final_valid=None):
        """Samples a track; step_for/bound_for/received_for map operation time to values."""
        t = track.start if start is None else start
        stop = track.end if end is None else end
        while t <= stop:
            step = step_for(t)
            nxt = min(t + step, stop) if t < stop else None
            point, alt = track.at(t)
            valid = nxt if nxt is not None else final_valid
            received = received_for(t) if received_for else None
            self.fix(source, entity, t, point, alt, bound_for(t), valid, provenance, evidence,
                     received)
            if nxt is None:
                break
            t = nxt

    def write(self, path):
        self.events.sort(key=lambda e: (e["observed_ms"], e["source"]["sequence"]))
        with open(path, "w", encoding="utf-8") as out:
            for e in self.events:
                out.write(json.dumps(e, separators=(",", ":"), ensure_ascii=False) + "\n")
