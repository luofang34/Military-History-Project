"""Build checks: the reconstruction keeps to the pace of 1859 and the places the sources give.

- Men on foot never outwalk 7 km/h, wagons and carriages 12 km/h; a charge of a few metres is
  held only to a run, 15 km/h.
- Trains never pass 25 mph (40 km/h), the B&O's own limit for passenger trains in the year to
  September 1859, which is also the basis of the replay's time for the express's release.
- The express is at Monocacy when Phelps telegraphs, and Kagi, Newby, Leeman and Thompson die
  where the sources put them.
- Each timed estimate in build/evidence/ lies within its records' times or says why not, and
  every moment's records agree on its time.
"""
import ledger
from evidence import DISPUTES, MOMENTS
from sites import L, MONOCACY, RAIDERS
from track import distance_m

FOOT_KMH, WAGON_KMH, RUN_KMH, TRAIN_KMH = 7.0, 12.0, 15.0, 40.2
TRAINS = {"EXPRESS", "MARINES", "BALTIMORE MILITIA", "FREDERICK MILITIA", "LEE", "STUART",
          "JEFFERSON GUARDS", "BOTTS COMPANY", "MARTINSBURG COMPANY"}
# Legs ridden in a wagon or carriage: (entity, from, until).
RIDES = [(name, "17 02:25", "17 03:20") for name in
         ("STEVENS", "TIDD", "COOK", "O ANDERSON", "GREEN", "LEARY")]
RIDES += [(name, "17 05:00", "17 09:20") for name in ("TIDD", "COOK", "LEEMAN")]
RIDES += [("TIDD", "17 09:20", "17 16:00")]
RUNS = {"STORMING PARTY"}
# (entity, place, the time the build expects it there, metres)
PLACES = [
    ("EXPRESS", MONOCACY, "17 07:05", 300.0),
    ("NEWBY", (-77.72935, 39.32322), "17 12:06", 30.0),
    ("LEEMAN", (-77.7290, 39.3248), "17 13:00", 50.0),
    ("KAGI", (-77.7392, 39.3205), "17 15:08", 50.0),
]


def limit(entity, at):
    if entity in RUNS:
        return RUN_KMH
    if any(e == entity and L(a) <= at < L(b) for e, a, b in RIDES):
        return WAGON_KMH
    return FOOT_KMH


def fastest(tracks):
    """Per entity, its fastest leg of 1 s or more: (km/h, ms)."""
    out = {}
    for entity, track in tracks.items():
        for a, b in zip(track.waypoints, track.waypoints[1:]):
            seconds = (b.at_ms - a.at_ms) / 1000
            if seconds < 1:
                continue
            kmh = distance_m(a.point, b.point) / seconds * 3.6
            cap = TRAIN_KMH if entity in TRAINS else limit(entity, a.at_ms)
            if kmh > cap + 1e-6:
                raise ValueError(f"{entity} moves at {kmh:.1f} km/h at {a.at_ms} ms, over "
                                 f"{cap:.0f}")
            if kmh > out.get(entity, (0.0, 0))[0]:
                out[entity] = (kmh, a.at_ms)
    return out


def check_places(tracks):
    for entity, place, at, metres in PLACES:
        point, _ = tracks[entity].at(L(at))
        if distance_m(point, place) > metres:
            raise ValueError(f"{entity} is {distance_m(point, place):.0f} m from where the "
                             f"sources put it at {at}")


def all(tracks):  # noqa: A001 - the module's one entry point, called as checks.all
    ledger.check(DISPUTES, L)
    ledger.check_moments(MOMENTS, L)
    missing = set(RAIDERS) - set(tracks)
    if missing:
        raise ValueError(f"raiders without a track: {sorted(missing)}")
    fastest(tracks)
    check_places(tracks)


def summary(tracks):
    speeds = fastest(tracks)
    on_foot = max(v for e, (v, _) in speeds.items() if e in RAIDERS)
    train = speeds["EXPRESS"][0]
    return f"fastest raider leg {on_foot:.1f} km/h, express {train / 1.609:.1f} mph"
