"""Building blocks for the Lancaster tracks: timed legs, orbits, take-off and landing, and the
attack run with its Upkeep.

The attack run follows B.976: 60 ft (spotlight altimeter) at 220 mph ground speed, releasing
about 400–450 yards short of the dam. The mine's path is choreographed from the bounce counts
the crews reported; its timing is not sourced.
"""
import math

from sites import SCAMPTON
from track import FT, MPH, Track, bearing_deg, destination, distance_m

RUN_ALT_M = 60 * FT
RUN_SPEED = 220 * MPH
RELEASE_M = 425 * 0.9144  # midway through 400–450 yd
CIRCUIT_ALT_M = 300.0
CIRCUIT_MPS = (55.0, 100.0)  # 125–225 mph round a holding circuit
RUNWAY = 250.0  # Scampton's take-off and landing direction is not sourced
THRESHOLD = destination(SCAMPTON, RUNWAY + 180, 600)
FINAL = destination(THRESHOLD, RUNWAY + 180, 6000)


def go(track, specs, kmh):
    """Appends (time ms or None, point, alt) waypoints; untimed ones follow at `kmh`."""
    for at, point, alt in specs:
        if at is None:
            last = track.waypoints[-1]
            at = last.at_ms + distance_m(last.point, point) / (kmh / 3.6) * 1000
        track.add(at, point, alt)
    return track


def between(track, points, t1, alts):
    """Appends `points` so the track arrives at the last one at `t1`, at constant speed from
    its current end; returns that ground speed in m/s."""
    last = track.waypoints[-1]
    legs, prev = [], last.point
    for p in points:
        legs.append(distance_m(prev, p))
        prev = p
    total = sum(legs)
    if total < 1 or t1 <= last.at_ms:
        raise ValueError(f"cannot reach {points[-1]} by {t1} ms from {last.at_ms} ms")
    run = 0.0
    for p, leg, alt in zip(points, legs, alts):
        run += leg
        track.add(last.at_ms + (t1 - last.at_ms) * run / total, p, alt)
    return total / ((t1 - last.at_ms) / 1000)


def circuit(start, heading, radius):
    """Centre of the left-hand circuit that runs tangent into a run starting at `start` on
    `heading`: the centre lies to port of the run."""
    return destination(start, heading - 90, radius)


def circuit_to(track, start, heading, radius, t1, alt, mps=72.0, step=10_000):
    """Joins a left-hand (anticlockwise) circuit, as B.976 orders for aircraft waiting their
    turn, and leaves it tangentially at `start` on `heading` at `t1`. The lap count, then the
    radius within ±30 %, is chosen to keep the speed round the circle nearest `mps` within
    CIRCUIT_MPS; the build fails if none can."""
    last = track.waypoints[-1]
    options = []
    for r in (radius * f for f in (1.0, 1.15, 0.85, 1.3, 0.7)):
        centre = circuit(start, heading, r)
        a0 = bearing_deg(centre, last.point)
        entry = destination(centre, a0, r)
        t0 = last.at_ms + max(distance_m(last.point, entry) / mps * 1000, 2000)
        seconds = (t1 - t0) / 1000
        if seconds <= 0:
            continue
        sweep = (a0 - bearing_deg(centre, start)) % 360  # anticlockwise: bearing decreases
        lap_m = 2 * math.pi * r
        for n in range(40):
            v = (sweep / 360 + n) * lap_m / seconds
            if CIRCUIT_MPS[0] <= v <= CIRCUIT_MPS[1]:
                options.append((abs(v - mps), r != radius, centre, r, entry, t0, a0,
                                sweep + 360 * n))
    if not options:
        raise ValueError(f"no circuit near radius {radius} m holds {CIRCUIT_MPS} m/s to "
                         f"{start} by {t1} ms")
    _, _, centre, r, entry, t0, a0, sweep = min(options, key=lambda o: (o[1], o[0]))
    track.add(t0, entry, alt)
    n = max(1, int((t1 - t0) // step))
    for i in range(1, n):
        track.add(t0 + (t1 - t0) * i / n, destination(centre, a0 - sweep * i / n, r), alt)
    track.add(t1, start, alt)
    return r


def take_off(at_ms, slot=0):
    """Rolling from the grass field at the ORB's take-off minute; runway heading and slot
    offsets are not sourced."""
    start = destination(SCAMPTON, RUNWAY + 180, 500 - 60 * slot)
    start = destination(start, RUNWAY - 90, 70 * slot)
    t = Track().add(0, start, 0)  # at dispersal from the start of the record
    t.add(at_ms, start, 0)
    t.add(at_ms + 35_000, destination(start, RUNWAY, 1000), 0)
    t.add(at_ms + 80_000, destination(start, RUNWAY, 4500), 120)
    return t


def land(track, at_ms):
    """Touches down at the ORB's landing minute from FINAL, where the track must already
    end, and rolls out; the last fix persists."""
    if distance_m(track.waypoints[-1].point, FINAL) > 1:
        raise ValueError(f"landing at {at_ms} ms does not start from the final approach")
    track.add(at_ms, THRESHOLD, 0)
    track.add(at_ms + 40_000, destination(THRESHOLD, RUNWAY, 1100), 0)
    return track


def attack_run(track, dam, heading, release_at, alt=RUN_ALT_M, release_m=RELEASE_M,
               lead_in_m=4500.0, climb_turn=-60.0, pull_up_m=2500.0):
    """The bombing run: established at 60 ft about 2 km out, release `release_m` short of the
    dam at `release_at`, then over the crest and a climbing turn (`climb_turn`, negative to
    port). Returns the release point."""
    v = RUN_SPEED
    back = heading + 180
    release = destination(dam, back, release_m)
    start = destination(release, back, lead_in_m)
    settled = destination(release, back, 2000.0)
    start_at = round(release_at - (lead_in_m / v) * 1000)
    if track.end < start_at:
        track.add(start_at, start, 90.0)
    track.add(release_at - (2000.0 / v) * 1000, settled, alt)
    track.add(release_at, release, alt)
    over = destination(dam, heading, 150.0)
    track.add(release_at + ((release_m + 150.0) / v) * 1000, over, alt + 10)
    out = destination(over, heading + climb_turn / 2, pull_up_m)
    track.add(release_at + ((release_m + 150.0 + pull_up_m) / v) * 1000, out, 150.0)
    return release


def alongside(track, leader, release_at, side_m, ahead_m=120.0, before_s=25, after_s=12):
    """Flies beside another aircraft's run, guns on the defences, as Gibson and Martin did for
    Young and Maltby. `side_m` is positive to the leader's starboard."""
    t = release_at - before_s * 1000
    shifted = leader.shifted(side_m, ahead_m)
    while t <= release_at + after_s * 1000:
        p, alt = shifted.at(t)
        track.add(t, p, alt + 15)
        t += 4000
    return track


def upkeep(release, aim, release_at, bounces, end_m=None, alt=RUN_ALT_M, spun=True):
    """The mine from release toward `aim` until it sank or burst, as a track of bounces.
    `end_m` is how far short of `aim` (negative: beyond) it ended; default the dam face."""
    course = bearing_deg(release, aim)
    total = distance_m(release, aim) - (end_m if end_m is not None else 8.0)
    m = Track().add(release_at, release, alt)
    if not spun:
        # Dropped along the Sorpe crest without spin: carried forward onto the water face.
        m.add(release_at + 1800, destination(release, course, total), 0)
        return m
    hops = [0.32, 0.26, 0.2, 0.14, 0.08][:max(bounces, 1)]
    run, t = 0.1 * total, release_at + 900
    scale = (total - run) / sum(hops)
    m.add(t, destination(release, course, 0.1 * total), 0)
    for i, hop in enumerate(hops):
        mid = run + scale * hop / 2
        run += scale * hop
        apex = 6.0 * (0.6 ** i)
        dt = 1800 * hop / hops[0]
        m.add(t + dt / 2, destination(release, course, mid), apex)
        t += dt
        m.add(t, destination(release, course, run), 0)
    return m
