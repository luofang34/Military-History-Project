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
"""
import ledger
from crews import ORB_CREWS, PRISONERS
from evidence import DISPUTES
from flights import LOSS
from sites import CRASH, DURATION, L, LANDED, MOHNE, EDER, ENNEPE, SORPE, TAKE_OFF
from track import FT, MPH, distance_m

ENVELOPE_MPH = (120.0, 245.0)
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


def all(plan):  # noqa: A001 - the module's one entry point, called as checks.all
    check_evidence()
    check_crews()
    check_speeds(plan)
    check_releases(plan)
    check_anchors(plan)


def summary(plan):
    (fast, _), (slow, _) = speeds(plan)
    return (f"{len(plan.releases)} releases, ground speed {slow:.0f}–{fast:.0f} mph, "
            f"{len(plan.lost)} lost, {len(plan.landed)} landed")
