"""Tracks for the Gulf of Sidra reconstruction, in a local nautical-mile frame around the merge.

The closure follows the Biddle tape's range calls, the fight stays within the distances the
aircraft could cover between the tape's kill calls, and Nimitz sits on the TACAN fix Fast
Eagle 107 reported. No source gives coordinates for any of it. The merge is placed where the
Pentagon briefing puts the fight, "30 miles below" 32°30′N and "60 miles from the nearest land"
(Washington Post, 20 Aug 1981): 26 nm below the line and about 53 nm (61 statute miles) from
the Natural Earth shore. It lies a little east of north of Ghurdabiya, close to Stanik's "due
south" contact.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from track import Track, slerp  # noqa: E402

MERGE = (17.05, 32.07)  # lon, lat of the head-on merge: 26 nm below the line, 53 nm off land
GHURDABIYA = (16.61167, 31.06056)  # Wikipedia / ICAO HLGD
LOD_WEST = (14.60, 32.50)  # 32°30′N where it meets the coast (Natural Earth 10 m)
LOD_EAST = (20.48, 32.50)
FT = 0.3048

SU_LEAD, SU_WING = "SU22-LEAD", "SU22-WING"
FE102, FE107 = "FE102", "FE107"
AA2, AIM_102, AIM_107 = "AA2-ATOLL", "AIM9-102", "AIM9-107"
NIMITZ = "NIMITZ"
S3A = "DC702"  # VS-30 S-3A from Forrestal, "Diamond Cutter 702" (Sanders)
LOD_W, LOD_E = "LOD-WEST", "LOD-EAST"
MISSILES = (AA2, AIM_102, AIM_107)

# Seconds after 07:15:00 for the moments the tape fixes (its 00:00 is placed at 07:15).
MERGE_S, ATOLL_S = 84, 83
HIT_WING_S, HIT_LEAD_S = 141, 173
SEA_S = 40  # seconds a hit Su-22 takes to fall to the sea from about 20,000 ft
# The sea impact is 1 ms off the whole second: verify.py samples every 250 ms and cannot
# order an open-ended fix that starts exactly on its grid.
DME_S = 194  # "123 DME on the 180"
REJOIN_S = 240  # Stanik: rejoin at 07:19; tape: "vector north" at 03:59
T15 = 15 * 60_000  # operation ms at 07:15
# The southernmost CAP station (Stanik), placed just north of 32°30′N; not sourced to a point.
CAP_Y = 32.0
KM_PER_NM = 1.852


def nm(x, y):
    """Local frame: x nm east and y nm north of the merge, as (lon, lat)."""
    lat = MERGE[1] + y / 60.0
    return (MERGE[0] + x / (60.0 * math.cos(math.radians(lat))), lat)


def s_ms(seconds):
    return T15 + int(round(seconds * 1000))


def _path(points):
    """`[(seconds after 07:15, x nm, y nm, altitude m), ...]` as a track."""
    tr = Track()
    for s, x, y, alt in points:
        tr.add(s_ms(s), nm(x, y), alt)
    return tr


def _racetrack(tr, start_ms, end_ms, west, east, y, radius, speed_kt, shift=(0.0, 0.0), alt=0.0):
    """Waypoints every 15 s around an east-west oval at `speed_kt`, starting on the north leg
    heading east. Orientation and size are not sourced; Stanik gives only 300 kt."""
    length = east - west
    perimeter = 2 * length + 2 * math.pi * radius
    for at in range(start_ms, end_ms + 1, 15_000):
        d = ((at - start_ms) / 3_600_000 * speed_kt) % perimeter
        if d < length:
            x, yy = west + d, y + radius
        elif d < length + math.pi * radius:
            a = (d - length) / radius
            x, yy = east + radius * math.sin(a), y + radius * math.cos(a)
        elif d < 2 * length + math.pi * radius:
            x, yy = east - (d - length - math.pi * radius), y - radius
        else:
            a = (d - 2 * length - math.pi * radius) / radius
            x, yy = west - radius * math.sin(a), y - radius * math.cos(a)
        tr.add(at, nm(x + shift[0], yy + shift[1]), alt)
    return tr


def _climb(start, end, start_ms, end_ms, profile):
    """Great-circle climb from `start` to `end` with `(fraction, altitude)` steps."""
    tr = Track()
    for f, alt in profile:
        tr.add(start_ms + (end_ms - start_ms) * f, slerp(start, end, f), alt)
    return tr


def aircraft():
    """Su-22s climb north from Ghurdabiya; F-14s hold a CAP, are vectored south at 07:11, and
    meet the Libyans head-on at about 0.29 nm/s closure (20 nm at 00:15 to 6 nm at 01:03)."""
    climb = [(0.0, 0.0), (0.05, 300.0), (0.4, 3000.0), (0.8, 6100.0), (1.0, 6100.0)]
    lead = _climb(GHURDABIYA, nm(-0.10, -11.76), 0, T15, climb)
    wing = _climb((GHURDABIYA[0] + 0.004, GHURDABIYA[1] - 0.002), nm(0.0, -11.81), 0, T15,
                  climb)
    for tr, pts in [
        (lead, [(MERGE_S, -0.10, 0.0, 6100), (100, -1.0, 1.8, 6300), (130, -3.5, 4.0, 6500),
                (HIT_LEAD_S, -5.5, 6.0, 6500), (HIT_LEAD_S + SEA_S + 0.001, -5.8, 6.3, 0)]),
        (wing, [(MERGE_S, 0.0, -0.05, 6100), (100, 1.2, -1.2, 5800),
                (HIT_WING_S, 4.0, -4.5, 5200), (HIT_WING_S + SEA_S + 0.001, 4.3, -4.8, 0)]),
    ]:
        for s, x, y, alt in pts:
            tr.add(s_ms(s), nm(x, y), alt)

    a102, a107 = 18_000 * FT, 22_000 * FT  # Stanik: Kleemann 18,000 ft, Muczynski 4,000 higher
    f102 = _racetrack(Track(), 0, 11 * 60_000, -5.0, 10.0, CAP_Y, 1.5, 300, alt=a102)
    f107 = _racetrack(Track(), 0, 11 * 60_000, -5.0, 10.0, CAP_Y, 1.5, 300, (1.0, 0.8), a107)
    for tr, pts in [
        (f102, [(0, 0.2, 12.6, a102), (MERGE_S, 0.3, 0.0, a102), (95, 0.4, -1.3, a102),
                (110, 1.5, -2.2, 5300), (128, 2.9, -3.5, 5200), (138, 3.4, -3.9, 5200),
                (180, 2.0, -1.0, 5500), (REJOIN_S, -1.0, 4.5, 6100), (600, -1.0, 47.5, 6100)]),
        (f107, [(0, 1.5, 12.9, a107), (MERGE_S, 1.5, 0.3, a107), (95, 1.8, -1.0, a107),
                (108, 2.8, -0.5, 6400), (125, 2.2, 1.8, 6400), (150, -1.5, 4.8, 6500),
                (170, -4.8, 5.5, 6500), (DME_S, -3.5, 5.3, 6500), (REJOIN_S, -0.7, 4.8, 6100),
                (600, -0.7, 47.8, 6100)]),
    ]:
        for s, x, y, alt in pts:
            tr.add(s_ms(s), nm(x, y), alt)
    return {SU_LEAD: lead, SU_WING: wing, FE102: f102, FE107: f107}


def missiles(tracks):
    """Each missile leaves its shooter at launch and ends on its target at impact, at the
    target's altitude. The AA-2 is fired head-on from about 300 m, passes FE102 and is lost."""
    def shot(shooter, target, launch_ms, hit_ms):
        tr = Track()
        p, a = tracks[shooter].at(launch_ms)
        tr.add(launch_ms, p, a)
        p, a = tracks[target].at(hit_ms)
        return tr.add(hit_ms, p, a)

    atoll = Track()
    p, a = tracks[SU_LEAD].at(s_ms(ATOLL_S))
    atoll.add(s_ms(ATOLL_S), p, a)
    p, a = tracks[FE102].at(s_ms(MERGE_S))
    atoll.add(s_ms(MERGE_S), p, a - 60)  # passes under 102 (Stanik)
    atoll.add(s_ms(MERGE_S + 3), nm(0.5, 1.4), a - 200)
    return {
        AA2: atoll,
        AIM_102: shot(FE102, SU_WING, s_ms(HIT_WING_S - 3), s_ms(HIT_WING_S)),
        AIM_107: shot(FE107, SU_LEAD, s_ms(HIT_LEAD_S - 3), s_ms(HIT_LEAD_S)),
    }


def s3a():
    """Diamond Cutter 702 flies a racetrack parallel to the shore at 10,000 ft, about 15 miles
    out (Sanders), and outside the 12 nm limit (Wikipedia). When the E-2C reports the Su-22s
    lifting off, Nimitz calls "Buster North": it dives at 10,000 ft/min to 300 ft and runs north
    at about 450 mph past the carriers. Where along the shore it orbited is not sourced; it is
    placed east of Sirte, its inshore leg about 14 nm from the Natural Earth shore."""
    tr = Track()
    inshore = [(17.75, 31.23), (17.25, 31.36)]  # heading west-northwest, parallel to shore
    for i, at in enumerate(range(0, 60_001, 15_000)):
        tr.add(at, slerp(inshore[0], inshore[1], i / 4 * 0.5), 10_000 * FT)
    turn = slerp(inshore[0], inshore[1], 0.5)
    tr.add(75_000, (turn[0] - 0.02, turn[1] + 0.08), 6_000 * FT)
    tr.add(120_000, (turn[0] - 0.02, turn[1] + 0.25), 300 * FT)
    north = turn[1] + 0.25 + 390 * 23 / 60 / 60  # 390 kt for the remaining 23 minutes
    return tr.add(25 * 60_000, (turn[0] - 0.02, north), 300 * FT)


def nimitz_position(tracks):
    """Nimitz on the 123 nm DME fix 107 reported on the 180 radial at 03:14, assuming the
    TACAN was the carrier's. That lands about 190 nm off Sirte, close to UPI's 200 miles."""
    lon, lat = tracks[FE107].at(s_ms(DME_S))[0]
    return (lon, lat + 123 / 60.0)


def statics(tracks):
    """Fixed points: (entity, position, bound m, source, provenance, reference)."""
    return [
        (NIMITZ, nimitz_position(tracks), 40_000.0, "reconstruction-carrier", "reconstructed",
         "ship"),
        (LOD_W, LOD_WEST, 500.0, "natural-earth-10m", "reported", "coast"),
        (LOD_E, LOD_EAST, 500.0, "natural-earth-10m", "reported", "coast"),
    ]


def separation_nm(tracks, a, b, at_ms):
    pa, pb = tracks[a].at(at_ms)[0], tracks[b].at(at_ms)[0]
    dy = (pa[1] - pb[1]) * 60.0
    dx = (pa[0] - pb[0]) * 60.0 * math.cos(math.radians((pa[1] + pb[1]) / 2))
    return math.hypot(dx, dy)


# Range calls on the Biddle tape: (seconds after 07:15, nm). "Miles" read as nautical miles.
RANGE_CALLS = [(15, 20.0), (27, 16.0), (38, 14.0), (54, 8.0), (63, 6.0)]


def check_ranges(tracks):
    """The closure must match the tape's range calls within 30 %, or the build fails."""
    for s, called in RANGE_CALLS:
        got = separation_nm(tracks, FE102, SU_LEAD, s_ms(s))
        if abs(got - called) > 0.3 * called:
            raise ValueError(f"FE102 to SU22-LEAD at +{s}s is {got:.1f} nm; tape says {called}")
