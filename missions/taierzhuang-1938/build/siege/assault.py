"""The first battle for the town, 22–30 March: the 63rd Infantry's advance from Yixian, its II
Battalion's assaults, the guns that came up behind it and the Chinese attacks on them.

Times and places are the 63rd Infantry's report and the Type 96 company's (build/evidence/,
assault); the places round the town are its sketch maps' villages (sites). A battalion's track is
its main body; a battery's its guns.
"""
from .routes import Mover
from .sites import (BEILUO, CANGLANGMIAO, CROSSING, EAST_REAR, KANGZHUANG, LIUJIAHU,
                    LIUJIAHU_N,
                    LIUJIAHU_WSW, MENG_E, MENG_NW, MENG_SE, NANLUO_E, NE_CORNER, NIGOU,
                    NORTH_OUT, NW_CORNER, PEI_E, PEIZHUANG, PENGCUN, SANLI_N,
                    SANLI_NE, SANLI_RAIL, SANLI_S, SANLI_S600, SANLIZHUANG, SHAOZHUANG,
                    SOUTH_STATION, STATION, SUNZHUANG, TOWN, TOWN_EAST, TYPE96_POS, WEST_OF_STATION,
                    YIXIAN, YIXIAN_SW, YULIN, ZHAOCUN)

START_LINE = (117.7385, 34.5645)  # 「第一線ト臺兒庄城壁トノ距離約二百米」, crept up to by 16:15
BREACHED = (117.7395, 34.5622)  # inside the breaches west of the north gate, where ten men got in
NW_APPROACH = (117.7290, 34.5660)  # how far the III Battalion got towards the north-west corner


def the_ii_battalion(t):
    """Yixian to Beiluo on the 23rd; the first assault on the 24th; the break-in on the 27th."""
    t["63 REGT II"].hold("23 07:00").to(KANGZHUANG, "23 09:00").to(NIGOU, "23 13:00") \
        .to(BEILUO, "23 19:30") \
        .hold("24 06:00").to(LIUJIAHU, "24 08:40").to(NORTH_OUT, "24 11:30") \
        .to(START_LINE, "24 16:15") \
        .to(BREACHED, "24 16:40").hold("24 17:10").to(NORTH_OUT, "24 18:00").hold("27 06:00") \
        .to(NE_CORNER, "27 07:50").hold("27 12:00").to(TOWN_EAST, "27 18:00")
    t["FIELD I"] = Mover(YIXIAN, "23 07:00").to(NIGOU, "23 13:00").to(BEILUO, "23 19:30") \
        .hold("24 06:00").to(LIUJIAHU, "24 08:40").to(MENG_NW, "24 11:30")
    t["FIELD I 3"] = Mover(YIXIAN, "26 04:00").to(LIUJIAHU, "26 11:00") \
        .to(PEIZHUANG, "26 13:15")


def the_guns(t):
    """The China Garrison's Type 96 platoon by lorry on the 25th; the 2nd Field Heavy Artillery's
    3rd Company on the 26th; its main body with the regiment on the 27th."""
    t["TYPE 96"].to(YIXIAN, "25 12:00").to(YIXIAN_SW, "25 12:40").hold("25 13:00") \
        .to(CROSSING, "25 16:30").to(LIUJIAHU_N, "25 17:00").hold("26 06:00") \
        .to(PEIZHUANG, "26 06:30").hold("29 11:40").to(LIUJIAHU, "29 12:30").hold("29 18:00") \
        .to(TYPE96_POS, "29 18:40")
    t["HEAVY 3"] = Mover(YIXIAN, "26 14:40").hold("26 15:50").to(LIUJIAHU, "26 22:00") \
        .hold("27 07:00").to(SANLI_NE, "27 08:30")
    t["HEAVY ARTY"].hold("27 08:00").to(NIGOU, "27 11:30").to(NANLUO_E, "27 13:30") \
        .hold("27 16:30").to(YULIN, "27 18:30").hold("28 00:00").to(LIUJIAHU_WSW, "28 02:00") \
        .hold("30 00:30").to(SANLI_N, "30 01:30")


def the_regiment(t):
    """The 63rd's main body and its III Battalion from Yixian on the 27th; the north-west corner
    stormed on the 28th; the tanks."""
    t["63 REGT"].hold("27 07:30").to(NIGOU, "27 11:00").to(BEILUO, "27 13:30") \
        .to(LIUJIAHU, "27 17:20")
    t["63 REGT III"] = Mover(YIXIAN, "27 08:00").to(NIGOU, "27 11:30").to(BEILUO, "27 13:30") \
        .to(SANLI_RAIL, "27 16:30").to(SANLI_S, "27 18:00").hold("28 07:00") \
        .to(SANLI_S600, "28 08:10").to(NW_APPROACH, "28 12:00").hold("28 15:30") \
        .to(SANLI_S, "28 17:00")
    t["11 COY"] = Mover(SANLI_S, "28 17:30").to(NW_CORNER, "28 19:25")
    t["TANKS"] = Mover(YIXIAN, "27 07:30").to(NIGOU, "27 09:30").to(SANLIZHUANG, "27 12:30") \
        .to(NW_APPROACH, "27 14:30").hold("27 15:30").to(SANLIZHUANG, "27 17:00") \
        .hold("28 21:00").to(SUNZHUANG, "28 22:30")
    t["ARMOUR"].hold("27 07:30").to(NIGOU, "27 09:30").to(LIUJIAHU, "27 13:00") \
        .to(SHAOZHUANG, "27 16:00").to(PEIZHUANG, "27 16:40").hold("28 06:00") \
        .to(SHAOZHUANG, "28 07:00")


def chinese_attacks(t):
    """The Chinese attacks the Japanese report on its batteries round Peizhuang and Mengzhuang
    from the east, and from west of the railway on Sanlizhuang; the armoured train's runs."""
    t["EAST FORCE"] = Mover(MENG_SE, "25 18:00").to((117.7510, 34.5655), "25 21:00") \
        .to(MENG_SE, "25 22:30").to(EAST_REAR, "26 01:00").to(PEI_E, "26 05:30") \
        .hold("26 07:00").to(SHAOZHUANG, "26 11:10").hold("26 13:00").to(EAST_REAR, "26 15:00") \
        .hold("26 23:00").to((117.7520, 34.5680), "27 00:00").hold("27 01:00") \
        .to(EAST_REAR, "27 02:30").to(PEI_E, "27 06:30").hold("27 07:00") \
        .to((117.7490, 34.5790), "27 15:30").to(PENGCUN, "27 17:00").hold("28 05:00") \
        .to((117.7520, 34.5680), "28 06:30").to(PENGCUN, "28 08:00").hold("29 03:00") \
        .to((117.7515, 34.5752), "29 09:15").hold("29 10:00").to(EAST_REAR, "29 12:00")
    t["WEST FORCE"] = Mover((117.7360, 34.5710), "24 22:30").to((117.7470, 34.5680), "25 00:10") \
        .to((117.7360, 34.5710), "25 01:30").to(WEST_OF_STATION, "25 04:00").hold("27 09:00") \
        .to((117.7150, 34.5780), "27 10:20") \
        .to((117.7195, 34.5795), "27 11:30").hold("27 12:00").to(WEST_OF_STATION, "27 13:30") \
        .hold("28 14:00").to(SANLI_S600, "28 15:00").to(WEST_OF_STATION, "28 16:00") \
        .hold("28 17:00")
    t["TRAIN"] = Mover(SOUTH_STATION, "25 06:30").to(STATION, "25 07:30") \
        .to(SANLI_RAIL, "25 08:00").hold("25 09:00").to(STATION, "25 09:30") \
        .to(SOUTH_STATION, "25 10:30").hold("27 13:30").to(STATION, "27 14:30") \
        .hold("27 15:30").to(SOUTH_STATION, "27 16:30")
    t["31 DIV"] = Mover((117.7300, 34.5000), "22 02:00").to(TOWN, "22 08:00")
    t["185 REGT"] = Mover(TOWN, "22 08:00").to((117.7000, 34.6300), "23 06:00") \
        .hold("23 19:30") \
        .to((117.7270, 34.5800), "24 04:00").hold("24 10:00").to(STATION, "24 13:00")
    t["EAST GUNS"] = Mover(MENG_E, "29 08:00").hold("29 08:40").to(CANGLANGMIAO, "29 12:40") \
        .hold("29 13:10").to(ZHAOCUN, "29 16:00")


# The Chinese guns south of the canal, from when the Japanese first report them:
# 「運河南側高地脚ニ十數門ノ砲」, received 16:35 on the 25th.
GUNS_FROM = "25 16:00"
ENDS = {"185 REGT": "24 13:00", "WEST FORCE": "28 17:00", "TANKS": "28 22:30",
        "FIELD ARTY": "26 04:00",
        "GARRISON ARTY": "25 06:30"}
CONDITIONS = [("FIELD I 3", "28 16:00", "damaged"), ("TYPE 96", "29 11:20", "damaged"),
              ("EAST GUNS", "29 08:25", "damaged"), ("EAST GUNS", "29 13:05", "damaged"),
              ("TANKS", "27 15:00", "damaged")]


def plan(t):
    the_ii_battalion(t)
    the_guns(t)
    the_regiment(t)
    chinese_attacks(t)
    return CONDITIONS, ENDS
