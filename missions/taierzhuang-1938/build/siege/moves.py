"""Where the batteries and the troops round them are, on the UTC+8 clock, 30 March – 1 April.

The Japanese batteries hold the positions the 63rd Infantry's report and the Type 96 company's
give them from the evening of the 29th; the Chinese ones stand where the Japanese placed them on
the south bank, the 15 cm battery where the sfh-position dispute estimates it. The moves are the
reports' night attacks, the armoured train's night run, the 11th Company's withdrawal and the
guns that changed position.
"""

from . import approach, assault
from .assault import GUNS_FROM
from .routes import Mover
from .sites import (BEILUO, BIANZHUANG, CANGLANGMIAO, GUANZHUANG, HANSHAN, MENG_E, MENG_NW,
                    MENG_S, NW_CORNER, SANLI_N, SANLI_NE, SANLI_S, SANLIZHUANG, SFH_POSITION,
                    SOUTH_STATION, STATION, STATION_SOUTH, TOWN, TOWN_EAST, XIONGSHAN,
                    TYPE96_POS, ZHAISHAN, ZHAOCUN, EAST_REAR)

T0 = "30 01:30"
WEST_OF_RAILWAY = (117.7120, 34.5720)
WITHDRAWN = (117.7280, 34.5670)
MAZHUANG = (117.7789, 34.6387)  # 馬庄; a weak match on OSM


def at(t, name, point, when=T0):
    """`name`'s mover, brought to `point` by `when` if an earlier part of the story moved it,
    or starting there then."""
    if name not in t:
        t[name] = Mover(point, when)
    elif t[name].point != point:
        t[name].to(point, when)
    return t[name].hold(when)


def batteries(t):
    for name, point in (("TYPE 96", TYPE96_POS), ("HEAVY 3", SANLI_NE), ("HEAVY 2", SANLI_N),
                        ("FIELD I", MENG_NW), ("SFH", SFH_POSITION)):
        at(t, name, point).hold("1 19:05")
    for name, point in (("ZHAISHAN GUNS", ZHAISHAN), ("HANSHAN GUNS", HANSHAN),
                        ("XIONGSHAN GUNS", XIONGSHAN), ("STATION GUNS", STATION_SOUTH)):
        at(t, name, point, GUNS_FROM).hold("1 19:05")
    # Enemy batteries "often changed position" (the Type 96 company's lessons).
    at(t, "EAST GUNS", ZHAOCUN, "30 05:30").hold("30 06:06").to(EAST_REAR, "30 06:40") \
        .hold("31 14:00").to(CANGLANGMIAO, "31 15:00").hold("31 15:10") \
        .to(BIANZHUANG, "31 16:40").hold("1 19:05")
    t["FIELD 10I"] = Mover(BEILUO, T0).hold("1 07:35").to(GUANZHUANG, "1 10:30") \
        .hold("1 14:00").to(MAZHUANG, "1 16:30").hold("1 19:05")
    t["OP"] = Mover(MENG_S, T0).hold("1 01:00").to(SANLIZHUANG, "1 02:00").hold("1 19:05")


def troops(t):
    at(t, "31 DIV", TOWN).hold("1 19:05")
    at(t, "63 REGT II", TOWN_EAST).hold("1 19:05")
    at(t, "63 REGT III", SANLI_S).hold("1 19:05")
    at(t, "11 COY", NW_CORNER).hold("31 20:00").to(WITHDRAWN, "31 20:40") \
        .hold("1 19:05")
    t["NIGHT ATTACK"] = Mover(STATION, "30 01:30").to(SANLI_S, "30 03:00") \
        .to(SANLI_N, "30 03:30").to(WEST_OF_RAILWAY, "30 04:30").hold("30 06:00")
    at(t, "EAST FORCE", EAST_REAR).hold("30 17:00").to(MENG_E, "30 17:25") \
        .hold("30 17:40").to(EAST_REAR, "30 18:30").hold("1 19:05")
    at(t, "TRAIN", SOUTH_STATION, "31 00:00").to(STATION, "31 00:30").hold("31 06:22") \
        .to(SOUTH_STATION, "31 06:40").hold("1 19:05")


CONDITIONS = [
    ("EAST GUNS", "30 06:06", "damaged"), ("HEAVY 3", "31 15:46:45", "damaged"),
]
ENDS = {"NIGHT ATTACK": "30 06:00", "HEAVY ARTY": "30 01:30"}


def plan():
    movers = {}
    approach.plan(movers)
    conditions, ends = assault.plan(movers)
    batteries(movers)
    troops(movers)
    for name in ("63 REGT", "ARMOUR", "FIELD I 3", "SEYA", "63 REGT I", "20 ARMY CORPS",
                 "110 DIV"):
        if name in movers:
            movers[name].hold("1 19:05")
    return ({k: m.track for k, m in movers.items()}, conditions + CONDITIONS,
            {**ends, **ENDS})
