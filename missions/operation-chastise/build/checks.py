"""Build checks: the reconstruction must keep to the sources it is built from.

- Every airborne leg of 1 s or more stays within the Lancaster's low-level envelope with an
  Upkeep, 120–245 mph ground speed; legs on the ground are only held to the upper bound.
- Spun releases are at 60 ft ±10 ft and 400–450 yards short of the dam, or flagged late
  (Hopgood, Maudslay); the Sorpe's unspun releases are at 30–60 ft over the crest.
- B.976's three minutes separate successive releases at each dam.
- Take-offs and landings fall on the ORB's minute and losses on their sourced minute, at the
  crash site.
- The ORB's crew lists give the sourced totals: 133 flew, 53 killed, three captured.
- Each timed estimate in build/evidence.py lies within its records' times, or is flagged as
  lying outside them with its reason.
- AJ-T turns at each point its navigator logged, within a kilometre of it at the logged
  time, and passes the two turns the replay does not time, the Haltern lakes and the
  Afsluitdijk, within two minutes of the log.
- No airborne Lancaster changes heading by more than MAX_SNAP_DEG at a single waypoint: the
  replay draws straight lines between fixes, so a turn must be flown as an arc.
- Both flood fronts are drawn with the APP-6D flood symbol, and the Eder's reaches Wabern
  at its sourced time.
- The Möhne and Eder are reported destroyed and the Sorpe damaged, each only after a mine
  released at it has gone off; an aircraft shot down by flak is reported hit first.
- Each dam photograph is shown only once its dam's flood front is on the map, from a camera
  above the ground, as an overlay under one shot that selects its dam, at the photographs'
  pace.
"""
import json

import ledger
import photographs
import waypoints as w
from targets import SORPE_RUN, STEEPLE
from crews import ORB_CREWS, PRISONERS
from evidence import DISPUTES, time_of
from flights import LOSS, MCCARTHY_HOME, MCCARTHY_OUT, SHOT_DOWN
from sites import (CRASH, DURATION, EDER, ENNEPE, L, LANDED, MOHNE, SORPE, TAKE_OFF, WABERN,
                   entities)
from manoeuvre import ENVELOPE_MPH
from track import FT, MPH, bearing_deg, distance_m

DAMS = {"MÖHNE": MOHNE, "EDER": EDER, "SORPE": SORPE, "ENNEPE": ENNEPE}


def speeds(plan):
    """Ground speed extremes over legs of at least a second, airborne and on the ground."""
    fast, slow = (0.0, None), (1e9, None)
    for code, t in plan.tracks.items():
        for a, b in zip(t.waypoints, t.waypoints[1:]):
            dt = (b.at_ms - a.at_ms) / 1000
            if dt < 1:
                continue
            v = distance_m(a.point, b.point) / dt / MPH
            if v > fast[0]:
                fast = (v, (code, a.at_ms))
            if a.alt_m > 0 and b.alt_m > 0 and v < slow[0]:
                slow = (v, (code, a.at_ms))
    return fast, slow


def check_speeds(plan):
    (fast, where_fast), (slow, where_slow) = speeds(plan)
    if fast > ENVELOPE_MPH[1]:
        raise ValueError(f"{where_fast[0]} flies {fast:.0f} mph at {where_fast[1]} ms")
    if slow < ENVELOPE_MPH[0]:
        raise ValueError(f"{where_slow[0]} flies {slow:.0f} mph at {where_slow[1]} ms")


def check_releases(plan):
    by_dam = {}
    for r in plan.releases:
        _, alt = plan.tracks[r.code].at(r.at_ms)
        rng = distance_m(r.point, DAMS[r.target])
        if r.spun and not r.late:
            if not 50 * FT <= alt <= 70 * FT:
                raise ValueError(f"{r.code} releases at {alt / FT:.0f} ft, not 60")
            if not 400 * 0.9144 <= rng <= 450 * 0.9144:
                raise ValueError(f"{r.code} releases {rng / 0.9144:.0f} yd out, not 400–450")
        if not r.spun and (not 30 * FT - 0.01 <= alt <= 60 * FT + 0.01 or rng > 150):
            raise ValueError(f"{r.code} drops {rng:.0f} m from the Sorpe crest at "
                             f"{alt / FT:.0f} ft")
        by_dam.setdefault(r.target, []).append(r.at_ms)
    for dam, times in by_dam.items():
        times.sort()
        for a, b in zip(times, times[1:]):
            if b - a < 180_000:
                raise ValueError(f"releases at the {dam} only {(b - a) / 1000:.0f} s apart")


def check_anchors(plan):
    for code, track in plan.tracks.items():
        up = L(TAKE_OFF[code])
        parked, rolling = track.at(up - 30_000)[0], track.at(up + 10_000)[0]
        if parked != track.at(up)[0] or rolling == track.at(up)[0]:
            raise ValueError(f"{code} does not start its roll at the ORB's {TAKE_OFF[code]}")
        if code in LANDED and plan.landed.get(code) != L(LANDED[code]):
            raise ValueError(f"{code} does not land at the ORB's {LANDED[code]}")
        if code in LOSS:
            site, _, _ = CRASH[code]
            if track.end != L(LOSS[code]) or distance_m(track.at(track.end)[0], site) > 1:
                raise ValueError(f"{code} does not end at its crash site at {LOSS[code]}")
        if track.end > DURATION:
            raise ValueError(f"{code} outlasts the record")
    if set(LANDED) | set(LOSS) != set(plan.tracks):
        raise ValueError("every Lancaster must either land or be lost")


def check_crews():
    """133 flew; 53 were killed and three taken prisoner (Wikipedia, dambustersblog)."""
    flew = sum(len(c) for c in ORB_CREWS.values())
    taken = sum(len(p) for p in PRISONERS.values())
    killed = sum(len(ORB_CREWS[c]) for c in LOSS) - taken
    if (flew, killed, taken) != (133, 53, 3):
        raise ValueError(f"crews give {flew} flown, {killed} killed, {taken} captured")


def check_evidence():
    """A timed estimate lies within its records' times, or says why not."""
    ledger.check(DISPUTES, L)


MAX_SNAP_DEG = 25.0


def check_turns(plan):
    """Every airborne turn is spread over an arc of waypoints, none snapping by more than
    MAX_SNAP_DEG."""
    for code, track in plan.tracks.items():
        wps = track.waypoints
        for a, v, b in zip(wps, wps[1:], wps[2:]):
            short = min(distance_m(a.point, v.point), distance_m(v.point, b.point)) < 20
            if v.alt_m < 1 or short:
                continue
            snap = abs((bearing_deg(v.point, b.point) - bearing_deg(a.point, v.point) + 180)
                       % 360 - 180)
            if snap > MAX_SNAP_DEG:
                raise ValueError(f"{code} snaps {snap:.0f}° onto a new heading at {v.at_ms} ms")


# Turns on the AJ-T log the replay does not use as anchors: a check on the legs between.
UNANCHORED = [(w.HALTERN_LAKES, "01:14"), (w.AFSLUITDIJK, "02:00:30")]


def check_mccarthy(plan):
    """AJ-T keeps to its navigator's logged turns, and its release run comes in over
    Langscheid's steeple and reaches the release on the crest's heading."""
    track = plan.tracks["AJ-T"]
    release = next(r.at_ms for r in plan.releases if r.code == "AJ-T")
    nearest = min(distance_m(track.at(t)[0], STEEPLE)
                  for t in range(release - 20_000, release, 250))
    if nearest > 150:
        raise ValueError(f"AJ-T's run passes {nearest:.0f} m from Langscheid's steeple")
    heading = bearing_deg(track.at(release - 500)[0], track.at(release)[0])
    if abs((heading - SORPE_RUN + 180) % 360 - 180) > 5:
        raise ValueError(f"AJ-T releases on {heading:.0f}°, off the crest's {SORPE_RUN:.0f}°")
    for points, at in MCCARTHY_OUT + MCCARTHY_HOME:
        off = distance_m(track.at(L(at))[0], points[-1])
        if off > 1000:
            raise ValueError(f"AJ-T is {off:.0f} m from its logged turn at {at}")
    for point, at in UNANCHORED:
        near = min(abs(p.at_ms - L(at)) for p in track.waypoints
                   if distance_m(p.point, point) < 1000)
        if near > 120_000:
            raise ValueError(f"AJ-T passes its logged turn at {at} {near / 60_000:.0f} min out")


def check_floods(plan):
    """The flood fronts use the standard flood symbol, and the Eder's keeps its anchor."""
    fronts = [e for e in entities(plan.mine_owners) if e["kind"] == "flood front"]
    if {e["id"] for e in fronts} != {"MÖHNE FLOOD", "EDER FLOOD"}:
        raise ValueError(f"flood fronts are {[e['id'] for e in fronts]}")
    for e in fronts:
        if e["sidc"] != APP6_FLOOD:
            raise ValueError(f"{e['id']} is drawn as {e['sidc']}, not the APP-6D flood")
    arrive = L(time_of("eder-flood"))
    if distance_m(plan.eder_flood.at(arrive)[0], WABERN) > 100:
        raise ValueError("the Eder flood front is not at Wabern at its sourced time")


# APP-6D symbol set 40 (activities), natural event, flood (170202).
APP6_FLOOD = "10044000001702020000"

DAMAGE = {"MÖHNE": "destroyed", "EDER": "destroyed", "SORPE": "damaged"}


def check_damage(plan):
    """Each dam in DAMAGE reports its state, after the first mine at it has gone off, and
    each aircraft shot down by flak is reported hit before it is lost."""
    for code in SHOT_DOWN:
        hits = [at for _, e, at, c in plan.conditions if e == code and c == "damaged"]
        if not any(at < plan.lost[code] for at in hits):
            raise ValueError(f"{code} is lost to flak without first being reported hit")
    for dam, state in DAMAGE.items():
        reported = [at for _, entity, at, c in plan.conditions if entity == dam and c == state]
        bursts = [plan.mines[f"UPKEEP {r.code}"].end for r in plan.releases if r.target == dam]
        if not reported:
            raise ValueError(f"{dam} is never reported {state}")
        if min(reported) < min(bursts):
            raise ValueError(f"{dam} is reported {state} before any mine at it goes off")


def check_photographs(plan, out, cues, pace):
    debrief = json.loads((out / photographs.MEDIA / "debrief.json").read_text())
    tours = {m["id"]: m.get("tour") for u in debrief["units"] for m in u["media"]}
    for key, dam, a, b in photographs.windows(out):
        if tours.get(key) != "overlay":
            raise ValueError(f"{key} is toured as {tours.get(key)}, not laid over the story")
        flood = {"MÖHNE": plan.flood, "EDER": plan.eder_flood}[dam]
        if a < flood.start:
            raise ValueError(f"{key} is shown before the {dam}'s flood front is on the map")
        agl = photographs.replay(out, key)["reconstruction"]["review"]["camera_agl_m"]
        if agl < 1:
            raise ValueError(f"{key}'s camera is {agl:.1f} m above the ground")
        if not any(c["start_ms"] == a and c["end_ms"] == b and c.get("focus") == dam
                   for c in cues):
            raise ValueError(f"no shot selects the {dam} for exactly {key}'s window")
        if any(s != photographs.SPEED for c, d, s in pace if c < b and a < d):
            raise ValueError(f"{key}'s window is not paced at {photographs.SPEED}×")


def all(plan):  # noqa: A001 - the module's one entry point, called as checks.all
    check_evidence()
    check_crews()
    check_speeds(plan)
    check_releases(plan)
    check_anchors(plan)
    check_damage(plan)
    check_mccarthy(plan)
    check_turns(plan)
    check_floods(plan)


def summary(plan):
    (fast, _), (slow, _) = speeds(plan)
    return (f"{len(plan.releases)} releases, ground speed {slow:.0f}–{fast:.0f} mph, "
            f"{len(plan.lost)} lost, {len(plan.landed)} landed")
