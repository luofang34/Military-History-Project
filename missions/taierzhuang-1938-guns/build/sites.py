"""Clock, the places of 1938 and the batteries of the artillery battle at Taierzhuang.

The clock is UTC+8: the Japanese 10th Infantry's report says so (「時刻ハ西部標準時トス」) and the
63rd Infantry's daily sunrise and sunset fit it to within three minutes.

The town of 1938 stood on the north bank of the Grand Canal, whose reach through it was
straightened in 1959; the old channel is today's 月河. The branch railway from Zaozhuang crossed
the canal west of the town and was taken up in 1945; the station, rebuilt in 1995 on its site, is
the Li Zongren museum. Villages carry today's names on OpenStreetMap where they match the Japanese
sketch maps; the south-bank hills the Japanese called 寨山, 韓山 and 雄山 are hilltops on an
elevation model at the bearings and distances the reports give.
"""
import datetime as dt

OP = "taierzhuang-1938-guns"
CST_S = 8 * 3600
LOCAL = dt.timezone(dt.timedelta(seconds=CST_S))
START = dt.datetime(1938, 3, 30, 1, 30, tzinfo=LOCAL)


def L(clock):
    """Operation milliseconds for `DD HH:MM[:SS]`, a day of March (30, 31) or April (1, 2)
    1938 on the UTC+8 clock."""
    day, hms = clock.split(" ")
    parts = [float(p) for p in hms.split(":")]
    h, m, s = (parts + [0.0])[:3]
    month = 3 if int(day) >= 25 else 4
    t = dt.datetime(1938, month, int(day), int(h), int(m), tzinfo=LOCAL) \
        + dt.timedelta(seconds=s)
    return int(round((t - START).total_seconds() * 1000))


def unix_ms():
    return int(START.timestamp() * 1000)


DURATION = L("1 19:05")

# (lon, lat), WGS84.
TOWN = (117.7396, 34.5583)  # the old town's centre
NW_CORNER = (117.7340, 34.5625)
TOWN_WEST = (117.7350, 34.5590)
TOWN_EAST = (117.7440, 34.5610)
STATION = (117.7211, 34.5592)
SOUTH_STATION = (117.7180, 34.5400)
LIUJIAHU = (117.7300, 34.5929)
SANLIZHUANG = (117.7248, 34.5793)
SANLI_NE = (117.7280, 34.5820)  # the village north-east of 三里庄
SANLI_N = (117.7250, 34.5815)
SANLI_S = (117.7230, 34.5750)  # the nameless village south of 三里庄
MENGZHUANG = (117.7526, 34.5660)
MENG_NW = (117.7490, 34.5680)  # the village north-west of 孟庄
MENG_S = (117.7526, 34.5640)
MENG_E = (117.7580, 34.5670)  # the village east of 孟庄
PEIZHUANG = (117.7490, 34.5750)  # not on OSM; between 邵庄 and 孟庄, ±500 m
SHAOZHUANG = (117.7463, 34.5846)
CANGLANGMIAO = (117.7622, 34.5605)
BIANZHUANG = (117.7634, 34.5570)
PENGCUN = (117.7619, 34.5775)
ZHAOCUN = (117.7585, 34.5689)
YANZIJING = (117.7626, 34.6093)
BEILUO = (117.6926, 34.6389)
GUANZHUANG = (117.7446, 34.5831)
ZHAISHAN = (117.6650, 34.5275)  # 132 m summit, 7.5 km SW
HANSHAN = (117.7275, 34.5075)  # 5.7 km SSW; weak match
XIONGSHAN = (117.7375, 34.5100)  # 5.3 km S; weak match
STATION_SOUTH = (117.7150, 34.5480)  # the south bank south-west of the station
SFH_POSITION = (117.7150, 34.4620)  # estimated; see the sfh-position dispute

FRIENDLY_FAN = "11032500002422000000"
HOSTILE_FAN = "11062500002422000000"
RAILWAY_LINE = "11042500003303000000"
ECHELON = {"platoon": "D", "company": "E", "battalion": "F", "regiment": "G", "division": "I"}


def unit(side, echelon, function="UCI"):
    return f"S{side}GP{function}----{ECHELON[echelon]}---"


ARTY_CN = unit("F", "company", "UCF")
ARTY_JP = unit("H", "company", "UCF")
ROUNDS_CN = "SFGPEWH--------"  # shown in flight between a battery and its target
ROUNDS_JP = "SHGPEWH--------"

# (id, name, symbol, kind, parent)
CHINESE = [
    ("CHINESE ARTY", "Chinese artillery south of the canal", unit("F", "regiment", "UCF"),
     "formation", None),
    ("SFH", "10th Artillery Regiment, 15 cm sFH 18/32L (two guns)", ARTY_CN, "battery",
     "CHINESE ARTY"),
    ("ZHAISHAN GUNS", "Field guns at Zhaishan", ARTY_CN, "battery", "CHINESE ARTY"),
    ("HANSHAN GUNS", "Field guns at Hanshan", ARTY_CN, "battery", "CHINESE ARTY"),
    ("XIONGSHAN GUNS", "Field guns at the north foot of Xiongshan", ARTY_CN, "battery",
     "CHINESE ARTY"),
    ("STATION GUNS", "Guns on the south bank south-west of the station", ARTY_CN, "battery",
     "CHINESE ARTY"),
    ("EAST GUNS", "Chinese guns east of the Japanese line", ARTY_CN, "battery", "CHINESE ARTY"),
    ("31 DIV", "31st Division in the town (Chi Fengcheng)", unit("F", "division"), "unit", None),
    ("EAST FORCE", "Chinese troops east of Mengzhuang", unit("F", "regiment"), "unit", None),
    ("NIGHT ATTACK", "About 1,000 Chinese from the station", unit("F", "battalion"), "unit",
     None),
    ("TRAIN", "Chinese armoured train", "SFGPEVT--------", "train", None),
    ("CN 15CM ROUNDS", "15 cm rounds, Chinese", ROUNDS_CN, "rounds", "CHINESE ARTY"),
    ("CN ROUNDS", "Field-gun rounds, Chinese", ROUNDS_CN, "rounds", "CHINESE ARTY"),
]
JAPANESE = [
    ("JAPANESE ARTY", "Seya Detachment artillery (Col. Kinoshita)", unit("H", "regiment", "UCF"),
     "formation", None),
    ("TYPE 96", "China Garrison Type 96 15 cm company (two guns)", ARTY_JP, "battery",
     "JAPANESE ARTY"),
    ("HEAVY 3", "3rd Company, 2nd Field Heavy Artillery (Type 4 15 cm)", ARTY_JP, "battery",
     "JAPANESE ARTY"),
    ("HEAVY 2", "2nd Company, 2nd Field Heavy Artillery (Type 4 15 cm)", ARTY_JP, "battery",
     "JAPANESE ARTY"),
    ("FIELD I", "I Battalion, 10th Field Artillery (Type 38)", unit("H", "battalion", "UCF"),
     "battery", "JAPANESE ARTY"),
    ("FIELD 10I", "II and IV Battalions, 10th Field Artillery (Type 38)",
     unit("H", "battalion", "UCF"), "battery", "JAPANESE ARTY"),
    ("OP", "Observation party of the Type 96 company", unit("H", "platoon", "UUS"), "unit",
     "JAPANESE ARTY"),
    ("63 REGT II", "II Battalion, 63rd Infantry, in the town", unit("H", "battalion"), "unit",
     None),
    ("63 REGT III", "III Battalion, 63rd Infantry, reserve south of Sanlizhuang",
     unit("H", "battalion"), "unit", None),
    ("11 COY", "11th Company, 63rd Infantry, at the north-west corner", unit("H", "company"),
     "unit", None),
    ("JP 15CM ROUNDS", "15 cm rounds, Japanese", ROUNDS_JP, "rounds", "JAPANESE ARTY"),
    ("JP ROUNDS", "Field-gun rounds, Japanese", ROUNDS_JP, "rounds", "JAPANESE ARTY"),
]

FIXED = [
    ("TAIERZHUANG", "SFGPIB----H----", "Taierzhuang, the walled town (1938)", TOWN, 100.0,
     "osm"),
    ("STATION", "SNGPIB----H----", "Taierzhuang station (1938 site)", STATION, 50.0,
     "zhwiki-taierzhuang-site"),
    ("LIUJIAHU", "SHGPIB----H----", "Liujiahu, the Japanese artillery's command post", LIUJIAHU,
     200.0, "osm"),
]

# The branch railway, north of the town past Sanlizhuang to the station, over the canal to the
# south station; drawn on the sketch maps' line, within about 300 m.
BRANCH_RAILWAY = [(117.7220, 34.6100), (117.7210, 34.5900), (117.7215, 34.5780), STATION,
                  (117.7190, 34.5520), SOUTH_STATION]
