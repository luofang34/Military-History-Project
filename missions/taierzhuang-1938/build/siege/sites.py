"""The places of 1938 and the batteries of the artillery battle at Taierzhuang.

The town of 1938 stood on the north bank of the Grand Canal, whose reach through it was
straightened in 1959; the old channel is today's 月河. The branch railway from Zaozhuang crossed
the canal west of the town and was taken up in 1945; the station, rebuilt in 1995 on its site, is
the Li Zongren museum. Villages carry today's names on OpenStreetMap where they match the Japanese
sketch maps; the south-bank hills the Japanese called 寨山, 韓山 and 雄山 are hilltops on an
elevation model at the bearings and distances the reports give.
"""
from clock import L

BEGIN, END = L("18 14:30"), L("1 19:05")

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

# The road from Lincheng: the Lincheng–Zaozhuang branch and the Taierzhuang–Zaozhuang branch
# (台棗支線, taken up in 1945), its stations from the county gazetteers.
LINCHENG = (117.2427, 34.8000)  # the 1938 station, 500 m north of today's 枣庄西
HANZHUANG_N = (117.3677, 34.6145)  # 韓莊 north of the canal, by its station
QUBAI = (117.4000, 34.8150)  # 東西曲柏; not on OSM, placed on the road to 嶧縣, within 5 km
XINZHUANG = (117.5100, 34.8300)  # 辛莊, 「嶧縣西北方約十粁」; placed
LIUCUN = (117.5450, 34.8000)  # 劉村, 「嶧縣西北方約五粁」; placed
YIXIAN_HEIGHT = (117.5800, 34.7950)  # 「嶧縣北微西約三粁高地」
YIXIAN_SOUTH_GATE = (117.5860, 34.7640)
EAST_HILLS = (117.7500, 34.8500)  # the hills north-east of 嶧縣 the 20th Army Corps drew into
KANGZHUANG = (117.6300, 34.7200)  # 康庄, on the road from 嶧縣 to 泥溝; placed, within 3 km
SHANJIALIN = (117.3627, 34.8479)
ZOUWU = (117.4180, 34.8490)  # moved 1.5 km east when rebuilt in 1956
ZAOZHUANG = (117.5431, 34.8677)  # the 中興 coal-mine town at the branch's end; estimated
YIXIAN = (117.5860, 34.7680)  # 嶧縣, the old county seat at today's 峄城
YIXIAN_SW = (117.5800, 34.7600)  # south-west of the town, east of the railway
TANSHAN = (117.6000, 34.7850)  # 潭山, the heights north-east of 嶧縣; placed, within 2 km
NIGOU = (117.6826, 34.6719)  # the station, 1 km east of 泥溝
NANLUO = (117.6953, 34.6176)
NANLUO_E = (117.7000, 34.6170)  # the east side of 南洛, a battery position on 27 March
SUNZHUANG = (117.7183, 34.6120)
YULIN = (117.7050, 34.5920)  # 魚鱗, west of the railway between 南洛 and 板橋; estimated

# Round the town, from the 63rd Infantry's sketches, within about 300 m.
NORTH_GATE = (117.7385, 34.5630)  # slightly west of the middle of the north wall
NE_CORNER = (117.7465, 34.5622)  # where the II Battalion broke in on 27 March
NORTH_OUT = (117.7385, 34.5657)  # 300 m outside the north gate, the II Battalion's position
LIUJIAHU_N = (117.7300, 34.5950)  # the north side of 劉家湖
LIUJIAHU_WSW = (117.7235, 34.5905)  # the village west-south-west of 劉家湖
CROSSING = (117.7212, 34.5900)  # the level crossing west of 劉家湖
SANLI_RAIL = (117.7215, 34.5770)  # on the railway south-west of 三里庄
SANLI_S600 = (117.7240, 34.5740)  # the position 600 m south of 三里庄, taken on 28 March
PEI_SE = (117.7505, 34.5735)  # the hamlet south-east of 裴庄, the field artillery's trains
PEI_E = (117.7530, 34.5752)  # east of 裴庄
MENG_SE = (117.7560, 34.5630)  # the village south-east of 孟庄
WEST_OF_STATION = (117.7120, 34.5650)
EAST_REAR = (117.7680, 34.5700)  # about a kilometre back from the Japanese gun line
TYPE96_POS = (117.7255, 34.5830)  # west of the 3rd Company, south of 劉家湖, from the 29th

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
    ("WEST FORCE", "Chinese troops west of the railway", unit("F", "regiment"), "unit", None),
    ("SQUAD", "Dare-to-die squad of the 31st Division (Shi Shangbin, 57 men)",
     unit("F", "platoon"), "unit", "31 DIV"),
    ("185 REGT", "185th Regiment, 31st Division, forward at Beiluo", unit("F", "regiment"),
     "unit", "31 DIV"),
    ("20 ARMY CORPS", "20th Army Corps (Tang Enbo)", unit("F", "division"), "formation", None),
    ("110 DIV", "110th Division, on the canal's south bank", unit("F", "division"), "unit",
     None),
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
    ("FIELD I 3", "3rd Battery, 10th Field Artillery (Type 38)", ARTY_JP, "battery",
     "JAPANESE ARTY"),
    ("TANKS", "China Garrison tank company (7 medium tanks, 5 tankettes)",
     unit("H", "company", "UCA"), "unit", None),
    ("OP", "Observation party of the Type 96 company", unit("H", "platoon", "UUS"), "unit",
     "JAPANESE ARTY"),
    ("63 REGT I", "I Battalion, 63rd Infantry, the right pursuit force", unit("H", "battalion"),
     "unit", None),
    ("63 REGT II", "II Battalion, 63rd Infantry (Lt-Col Yasunaga)", unit("H", "battalion"),
     "unit", None),
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
    ("TZZ STATION", "SNGPIB----H----", "Taierzhuang station (1938 site)", STATION, 50.0,
     "zhwiki-taierzhuang-site"),
    ("LIUJIAHU", "SHGPIB----H----", "Liujiahu, the Japanese artillery's command post", LIUJIAHU,
     200.0, "osm"),
]

# The branch railway from Lincheng by Zaozhuang, Yixian and Nigou, through the gazetteers'
# stations and, to Zaozhuang, on today's line, within about a kilometre; then north of the town
# past Sanlizhuang to the station and over the canal to the south station on the sketch maps'
# line, within about 300 m.
BRANCH_RAILWAY = [LINCHENG, (117.2800, 34.8394), (117.3200, 34.8508), SHANJIALIN, ZOUWU,
                  (117.4800, 34.8584), ZAOZHUANG, YIXIAN, NIGOU, (117.6950, 34.6400),
                  (117.7220, 34.6100), (117.7210, 34.5900), (117.7215, 34.5780), STATION,
                  (117.7190, 34.5520), SOUTH_STATION]
