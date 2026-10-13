"""Lines and areas drawn on the map: the Tianjin–Pukou railway, and the reach of each Japanese
battery while it stood in position round Tengxian.

A range fan is a MIL-STD-2525D sector range fan (symbol set 25, entity 242200) from the battery,
opening 90° about the bearing to the city, out to the gun's maximum range: the improved Type 38
field gun's 11,600 m, the Type 4 15 cm howitzer's 8,800 m with its charge increased, the Type 96
15 cm howitzer's 11,900 m (Jiang 2015; the guns' Japanese specifications). The defenders had no
gun to draw: see the chinese-heavy-guns dispute.
"""
from .routes import RAILWAY
from .sites import (CITY, END, HOSTILE_FAN, RAILWAY_LINE, SHANJIAZHUANG, XIACUN, L)
from track import bearing_deg

SPREAD_DEG = 90.0
# (id, battery entity, from, until or None for the end of the part, position, maximum range m)
FANS = [
    ("fan-field-xiacun", "FIELD ARTY", "16 10:20", "17 05:00", XIACUN, 11_600.0),
    ("fan-heavy-xiacun", "HEAVY ARTY", "16 11:15", "16 15:00", XIACUN, 8_800.0),
    ("fan-heavy-shanjia", "HEAVY ARTY", "16 15:40", None, SHANJIAZHUANG, 8_800.0),
    ("fan-field-shanjia", "FIELD ARTY", "17 06:00", "17 15:00", SHANJIAZHUANG, 11_600.0),
    ("fan-garrison-xiacun", "GARRISON ARTY", "17 06:00", "17 12:30", XIACUN, 11_900.0),
]


def point(p):
    return {"lon": round(p[0], 5), "lat": round(p[1], 5)}


def fan(id_, at, reach_m):
    """The sector range fan of a battery at `at` facing the city."""
    centre = bearing_deg(at, CITY)
    left = (centre - SPREAD_DEG / 2) % 360
    return {"schema": 1, "id": id_, "symbol": HOSTILE_FAN, "points": [point(at)],
            "modifiers": {"AM": [reach_m],
                          "AN": [round(left, 1), round(left + SPREAD_DEG, 1)]},
            "revision": 0}


def emit(em):
    em.graphic("reconstruction-railway", 0, "jinpu-railway", {
        "schema": 1, "id": "jinpu-railway", "symbol": RAILWAY_LINE,
        "points": [point(p) for p in RAILWAY], "modifiers": {"T": "Tianjin–Pukou Railway"},
        "revision": 0})
    for id_, _, start, until, at, reach in FANS:
        em.graphic("reconstruction-guns", L(start), id_, fan(id_, at, reach))
        em.graphic("reconstruction-guns", END if until is None else L(until), id_, None)
