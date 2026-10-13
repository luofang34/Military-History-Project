"""Build checks: the reconstruction keeps to the pace of 1938 and the places the sources give.

- Infantry never marches faster than 7 km/h; the light armour, trains and the armoured train
  never pass 25 km/h, a pace the armour kept off the roads of the North China plain.
- Each battery stands where its range fan is drawn for as long as the fan is shown.
- Wang Mingzhang falls in the moat outside the west gate; the Japanese battalions are at the
  outer east gate at 14:15 on the 16th and on the south breach at 16:05 on the 17th.
- Each timed estimate in build/evidence/ lies within its records' times or says why not, and
  every moment's records agree on its time.
"""
from . import graphics
import ledger
from evidence import DISPUTES, MOMENTS
from .sites import L, OUTER_EAST_GATE, SOUTH_BREACH, WEST_MOAT
from track import distance_m

FOOT_KMH, FAST_KMH = 7.0, 25.0
FAST = {"ARMOUR", "ARMOURED TRAIN", "SPECIAL BN"}  # the battalion rode the train from Lincheng
PLACES = [
    ("WANG", WEST_MOAT, "17 17:30", 20.0),
    ("10 REGT I", OUTER_EAST_GATE, "16 14:15", 20.0),
    ("10 REGT III", SOUTH_BREACH, "17 16:05", 20.0),
]


def fastest(tracks):
    """Per entity, its fastest leg of 1 s or more, in km/h; raises past its limit."""
    out = {}
    for entity, track in tracks.items():
        cap = FAST_KMH if entity in FAST else FOOT_KMH
        for a, b in zip(track.waypoints, track.waypoints[1:]):
            seconds = (b.at_ms - a.at_ms) / 1000
            if seconds < 1:
                continue
            kmh = distance_m(a.point, b.point) / seconds * 3.6
            if kmh > cap + 1e-6:
                raise ValueError(f"{entity} moves at {kmh:.1f} km/h at {a.at_ms} ms, over "
                                 f"{cap:.0f}")
            out[entity] = max(out.get(entity, 0.0), kmh)
    return out


def check_places(tracks):
    for entity, place, at, metres in PLACES:
        point, _ = tracks[entity].at(L(at))
        if distance_m(point, place) > metres:
            raise ValueError(f"{entity} is {distance_m(point, place):.0f} m from where the "
                             f"sources put it at {at}")


def check_batteries(tracks, end_ms):
    """A range fan is drawn only while its battery stands at the fan's centre."""
    for id_, entity, start, until, at, _ in graphics.FANS:
        stop = end_ms if until is None else L(until)
        for t in range(L(start), stop + 1, 600_000):
            point, _ = tracks[entity].at(t)
            if distance_m(point, at) > 50:
                raise ValueError(f"{id_}: {entity} is {distance_m(point, at):.0f} m from its "
                                 f"fan at {t} ms")


def all(tracks, end_ms):  # noqa: A001 - the module's one entry point, called as checks.all
    ledger.check(DISPUTES, L)
    ledger.check_moments(MOMENTS, L)
    fastest(tracks)
    check_places(tracks)
    check_batteries(tracks, end_ms)


def summary(tracks):
    speeds = fastest(tracks)
    foot = max(v for e, v in speeds.items() if e not in FAST)
    return f"fastest march {foot:.1f} km/h, armour {speeds['ARMOUR']:.1f} km/h"
