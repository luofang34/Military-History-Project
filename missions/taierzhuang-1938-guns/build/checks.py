"""Build checks for the artillery battle.

- Every battery stands where its range fan is drawn while the fan is shown.
- Every fire mission starts at a battery that is in position at that moment and, for a gun with a
  drawn fan, lands within that gun's reach: no round flies further than the gun could throw it.
- The Chinese 15 cm position lies beyond every Japanese fan's reach (Ohashi) and
  within its own reach of Liujiahu and Sanlizhuang, where its rounds fell.
- Troops on foot never move faster than 7 km/h; the armoured train no faster than 25 km/h.
- The ledger's estimates and moments keep to their records.
"""
import fire
import graphics
import ledger
from evidence import DISPUTES, MOMENTS
from sites import LIUJIAHU, SANLI_NE, SFH_POSITION, L
from track import distance_m

FOOT_KMH, TRAIN_KMH = 7.0, 25.0
REACH = {"CN 15CM ROUNDS": 15_000.0}


def check_fans(tracks, end_ms):
    for id_, entity, _, start, until, at, _, _ in graphics.FANS:
        stop = end_ms if until is None else L(until)
        for t in range(L(start), stop + 1, 600_000):
            point, _ = tracks[entity].at(t)
            if distance_m(point, at) > 50:
                raise ValueError(f"{id_}: {entity} is {distance_m(point, at):.0f} m from its fan")


def check_reach():
    reach = {at: r for _, _, _, _, _, at, _, r in graphics.FANS}
    for entity, at, start, end, _ in fire.MISSIONS:
        limit = reach.get(start) or REACH.get(entity)
        if limit and distance_m(start, end) > limit:
            raise ValueError(f"{entity} at {at} flies {distance_m(start, end):.0f} m, beyond "
                             f"{limit:.0f}")
    for id_, entity, symbol, _, _, at, _, reach_m in graphics.FANS:
        if symbol == graphics.HOSTILE_FAN and distance_m(at, SFH_POSITION) <= reach_m:
            raise ValueError(f"{id_}: {entity} could reach the 15 cm position")
    for target in (LIUJIAHU, SANLI_NE):
        if distance_m(SFH_POSITION, target) > 15_000:
            raise ValueError("the 15 cm guns could not reach the guns they hit")


def check_speeds(tracks):
    for entity, track in tracks.items():
        cap = TRAIN_KMH if entity in ("TRAIN", "FIELD 10I") else FOOT_KMH
        for a, b in zip(track.waypoints, track.waypoints[1:]):
            seconds = (b.at_ms - a.at_ms) / 1000
            if seconds >= 1 and distance_m(a.point, b.point) / seconds * 3.6 > cap + 1e-6:
                raise ValueError(f"{entity} moves too fast at {a.at_ms} ms")


def all(tracks, end_ms):  # noqa: A001 - the module's one entry point, called as checks.all
    ledger.check(DISPUTES, L)
    ledger.check_moments(MOMENTS, L)
    check_fans(tracks, end_ms)
    check_reach()
    check_speeds(tracks)


def summary(tracks):
    fastest = {}
    for entity, track in tracks.items():
        for a, b in zip(track.waypoints, track.waypoints[1:]):
            seconds = (b.at_ms - a.at_ms) / 1000
            if seconds >= 1:
                kmh = distance_m(a.point, b.point) / seconds * 3.6
                fastest[entity] = max(fastest.get(entity, 0.0), kmh)
    foot = max(v for e, v in fastest.items() if e not in ("TRAIN", "FIELD 10I"))
    return f"fastest march {foot:.1f} km/h, train {fastest.get('TRAIN', 0.0):.1f} km/h"
