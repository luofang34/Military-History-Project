"""The reach of each battery, and the branch railway. The 1938 canal is the basemap's 月河.

Each battery's reach is a MIL-STD-2525D sector range fan (symbol set 25, entity 242200), opening
90° about the bearing to the other side's guns, out to the gun's maximum range: the Chinese sFH
18/32L's 15,000 m (standard charge 7), the Type 96's 11,900 m, the Type 4's 8,800 m with its charge
increased, the improved Type 38 field gun's 11,600 m. No range is recorded for the Chinese field
guns, so they have no fan.
"""
from .sites import (BRANCH_RAILWAY, FRIENDLY_FAN, GUANZHUANG, HOSTILE_FAN, LIUJIAHU,
                    MENG_NW, RAILWAY_LINE, SANLI_N, SANLI_NE, SFH_POSITION, XIONGSHAN, L)
from .sites import TYPE96_POS
from track import bearing_deg

SPREAD_DEG = 90.0
# (id, battery entity, symbol, from, until or None, position, aimed at, reach m)
FANS = [
    ("fan-sfh", "SFH", FRIENDLY_FAN, "30 01:30", None, SFH_POSITION, LIUJIAHU, 15_000.0),
    ("fan-type96", "TYPE 96", HOSTILE_FAN, "30 01:30", None, TYPE96_POS, XIONGSHAN, 11_900.0),
    ("fan-heavy3", "HEAVY 3", HOSTILE_FAN, "30 01:30", None, SANLI_NE, XIONGSHAN, 8_800.0),
    ("fan-heavy2", "HEAVY 2", HOSTILE_FAN, "30 01:30", None, SANLI_N, XIONGSHAN, 8_800.0),
    ("fan-field1", "FIELD I", HOSTILE_FAN, "30 01:30", None, MENG_NW, XIONGSHAN, 11_600.0),
    ("fan-field10i", "FIELD 10I", HOSTILE_FAN, "1 10:30", "1 14:00", GUANZHUANG, XIONGSHAN,
     11_600.0),
]


def point(p):
    return {"lon": round(p[0], 5), "lat": round(p[1], 5)}


def fan(id_, symbol, at, aim, reach_m):
    left = (bearing_deg(at, aim) - SPREAD_DEG / 2) % 360
    return {"schema": 1, "id": id_, "symbol": symbol, "points": [point(at)],
            "modifiers": {"AM": [reach_m],
                          "AN": [round(left, 1), round(left + SPREAD_DEG, 1)]},
            "revision": 0}


def line(id_, points, name):
    return {"schema": 1, "id": id_, "symbol": RAILWAY_LINE, "points": [point(p) for p in points],
            "modifiers": {"T": name}, "revision": 0}


def emit(em):
    em.graphic("reconstruction-railway", 0, "branch-railway",
               line("branch-railway", BRANCH_RAILWAY, "Lincheng–Zhaodun branch, 1938"))
    for id_, _, symbol, start, until, at, aim, reach in FANS:
        em.graphic("reconstruction-guns", L(start), id_, fan(id_, symbol, at, aim, reach))
        if until is not None:
            em.graphic("reconstruction-guns", L(until), id_, None)
