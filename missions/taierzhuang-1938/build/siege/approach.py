"""The road south, 18–22 March: from Lincheng the Seya Detachment's two pursuit forces, one south
to Hanzhuang on the canal and one east along the branch railway to Yixian, then the 63rd
Infantry's main body to Yixian; the Chinese 20th Army Corps drawing off into the hills, the
110th Division to the canal and the 31st into Taierzhuang.

Each Japanese track that the Tengxian part began starts where it leaves the unit
(tengxian.moves); the times are the 63rd Infantry's report and the detachment's orders as Jiang
2017 gives them, the Chinese arrivals Chinese Wikipedia's (build/evidence/, road).
"""
from tengxian.moves import GUANLUKOU, LINCHENG_NORTH
from tengxian.sites import DONGSHAHE, SHANJIAZHUANG

from .routes import Mover
from .sites import (EAST_HILLS, HANZHUANG_N, LINCHENG, LIUCUN, QUBAI, SHANJIALIN, XINZHUANG,
                    YIXIAN, YIXIAN_HEIGHT, YIXIAN_SOUTH_GATE, ZAOZHUANG, ZOUWU)

PART_START = "18 14:30"
TO_YIXIAN = [ZOUWU, YIXIAN]  # the road by 西鄒塢 the main body took on the 22nd
BRANCH = [LINCHENG, SHANJIALIN, ZOUWU, ZAOZHUANG]  # the branch railway to the coal-mine town
ROAD_SOUTH = [(117.2300, 34.9500), LINCHENG]  # from Tengxian's south-east by Guanqiao
WEST_OF_YIXIAN = (117.5750, 34.7700)  # the railway line and villages west of the town


def pursuit(t):
    t["63 REGT I"] = Mover(LINCHENG_NORTH, PART_START).hold("18 15:30") \
        .to(HANZHUANG_N, "19 13:00")
    t["63 REGT II"] = Mover(LINCHENG_NORTH, PART_START).hold("18 15:00") \
        .to(QUBAI, "18 18:30").hold("18 21:00").to(XINZHUANG, "19 02:30").to(LIUCUN, "19 04:00") \
        .hold("19 09:00").to(YIXIAN_HEIGHT, "19 12:20").to(WEST_OF_YIXIAN, "19 15:00") \
        .to(YIXIAN_SOUTH_GATE, "19 17:00").hold("19 18:40").to(YIXIAN, "20 00:30")


def main_body(t):
    t["63 REGT"] = Mover(LINCHENG_NORTH, PART_START).to(LINCHENG, "18 16:00") \
        .hold("22 05:00").along(TO_YIXIAN, "22 17:30")
    t["ARMOUR"] = Mover(LINCHENG_NORTH, PART_START).to(LINCHENG, "18 16:00") \
        .hold("22 05:00").along(TO_YIXIAN, "22 12:00")
    t["FIELD ARTY"] = Mover(DONGSHAHE, PART_START).along(ROAD_SOUTH, "19 18:00") \
        .hold("22 05:00").along(TO_YIXIAN, "22 17:30")
    t["HEAVY ARTY"] = Mover(SHANJIAZHUANG, PART_START).along(ROAD_SOUTH, "20 12:00") \
        .hold("25 08:00").along(BRANCH, "25 20:00").hold("26 12:00") \
        .to(YIXIAN, "26 19:40")
    t["GARRISON ARTY"] = Mover(GUANLUKOU, PART_START).along(ROAD_SOUTH, "19 12:00") \
        .hold("25 06:30")
    t["SEYA"] = Mover(GUANLUKOU, PART_START).along(ROAD_SOUTH, "19 12:00").hold("25 14:00") \
        .along(BRANCH, "25 22:00")
    t["TYPE 96"] = Mover(LINCHENG, "25 06:30")


def chinese(t):
    """Tang Enbo's corps gives way into the hills; the 110th Division comes up to the canal."""
    t["20 ARMY CORPS"] = Mover((117.6200, 34.7800), "20 01:00").to(EAST_HILLS, "22 12:00")
    t["110 DIV"] = Mover((117.4500, 34.4500), "20 06:00").to((117.4500, 34.5600), "21 18:00")


def plan(t):
    pursuit(t)
    main_body(t)
    chinese(t)
