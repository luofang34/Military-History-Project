"""Clock, the places of March 1938 and the order of battle for the defence of Tengxian.

The clock is China's coastal standard time, UTC+8. Chinese records are read on it as written; so
are the Japanese 10th Infantry Regiment's, whose sunrise (06:20) and dusk (18:40) fit it and not
Tokyo time (see the japanese-clock dispute).

Tengxian's walls were pulled down from 1952 to 1984; new streets were laid on the wall and moat
(the county gazetteer), so the circuit, the gates and the breaches are placed on those streets.
The railway station of 1938 stood west of the walls, in the west suburb.
"""
import datetime as dt

OP = "taierzhuang-1938"
CST_S = 8 * 3600
LOCAL = dt.timezone(dt.timedelta(seconds=CST_S))
START = dt.datetime(1938, 3, 14, 4, 0, tzinfo=LOCAL)


def L(clock):
    """Operation milliseconds for `DD HH:MM[:SS]`, a day of March 1938 on the UTC+8 clock."""
    day, hms = clock.split(" ")
    parts = [float(p) for p in hms.split(":")]
    h, m, s = (parts + [0.0])[:3]
    t = dt.datetime(1938, 3, int(day), int(h), int(m), tzinfo=LOCAL) + dt.timedelta(seconds=s)
    return int(round((t - START).total_seconds() * 1000))


def unix_ms():
    return int(START.timestamp() * 1000)


DURATION = L("18 14:30")

# (lon, lat), WGS84; OpenStreetMap unless noted.
YANZHOU = (116.8359, 35.5563)
ZOUXIAN = (116.9527, 35.4013)
TANGCUN = (116.940, 35.328)
LIANGXIADIAN = (116.9985, 35.3085)
SHIQIANG = (116.907, 35.263)
XIANGCHENG = (117.1312, 35.2918)
PUYANGSHAN = (117.110, 35.275)  # between 香城 and 界河; the peak is not on OSM
JIEHE = (117.065, 35.217)
JIEHE_STATION = (117.0670, 35.2055)
LONGSHAN = (117.1442, 35.2158)
LONGSHANDIAN = (117.1247, 35.1914)
FANGLING = (117.0497, 35.1946)
ANLOU = (117.050, 35.203)
CHITOUJI = (116.947, 35.160)
DONGCAO = (117.030, 35.206)
BEISHAHE = (117.1140, 35.1540)
DONGGUO = (117.256, 35.187)
DAWUGOU = (117.2602, 35.1601)
CHENGTOU = (117.305, 35.150)
WANGMIAO = (117.291, 35.097)
DANGSHAN = (117.260, 35.050)
JIANGJIALOU = (117.2444, 35.1142)
XIAOGONGSHAN = (117.2505, 35.1087)
DONGSHAHE = (117.218, 35.093)
DAWU = (116.983, 35.118)
SHENJING = (116.965, 35.225)  # between 石牆 and 池頭集; estimated from the text
XIACUN = (117.175, 35.068)  # "滕県城南東2キロ"; the village is not on OSM, ±700 m
SHANJIAZHUANG = (117.1677, 35.0707)  # 単家荘, today's 善国社区
TUCHENGZI = (117.172, 35.087)
WANGZHUANG = (117.185, 35.044)  # 王荘 = 王開; see the wangzhuang dispute
XISIYUAN = (117.1522, 35.0690)  # 四彦村
WULIHE = (117.155, 35.071)
WULITUN = (117.1229, 35.0780)
NANSHAHE = (117.1704, 35.0150)
GUANQIAO = (117.1979, 34.9211)
LINCHENG = (117.244, 34.798)  # the 1938 station, 500 m north of today's 枣庄西
BEILOU = (117.150, 35.098)  # 北樓, north of the city; placed on the north road

# The walled city: corners and gates on the streets laid over the wall and moat.
WALL_NW, WALL_NE = (117.1518, 35.0872), (117.1600, 35.0872)
WALL_SE, WALL_SW = (117.1600, 35.0807), (117.1518, 35.0807)
WEST_GATE = (117.1522, 35.0828)
SOUTH_GATE = (117.1578, 35.0806)
EAST_GATE = (117.1602, 35.0848)
NORTH_GATE = (117.1551, 35.0873)
OUTER_EAST_GATE = (117.1650, 35.0850)  # 東関の寨門, where the 府前路 axis meets the suburb wall
OUTER_SOUTH_GATE = (117.1608, 35.0810)  # 善国門
EAST_BREACH = (117.1601, 35.0844)  # 40 m south of the east gate
SOUTH_BREACH = (117.1598, 35.0808)  # 20 m west of the south-east corner tower
CROSSROADS = (117.1565, 35.0840)
YAMEN = (117.1587, 35.0853)
CITY = (117.1559, 35.0840)
DONGGUAN = (117.1625, 35.0845)  # the east suburb inside its earth wall
STATION = (117.1483, 35.0835)
POWER_PLANT = (117.1500, 35.0830)  # 西關 電燈廠; estimated, ±150 m
WEST_MOAT = (117.1512, 35.0830)  # where Wang fell; estimated, ±80 m
PAGODA = (117.16705, 35.08568)  # 龍泉塔, the Japanese "喇嘛塔"

FRIENDLY_PREFIX, HOSTILE_PREFIX = "SFGPUCI", "SHGPUCI"
ECHELON = {"company": "E", "battalion": "F", "regiment": "G", "brigade": "H", "division": "I",
           "corps": "J", "army": "K", "group": "L"}


def unit(side, echelon, hq=False, function="UCI"):
    """A 2525C unit symbol: `side` F or H, `function` as UCI infantry, UCF field artillery, UCA
    armour."""
    return f"S{side}GP{function}---{'A' if hq else '-'}{ECHELON[echelon]}---"


LEADER_CN = "10032700711101010000"  # dismounted individual, leader
MAN_CN = "10032700001101010000"
CN_TRAIN = "SFGPEVT--------"
CN_SITE = "SFGPIB----H----"
NEUTRAL_SITE = "SNGPIB----H----"
FRIENDLY_FAN = "11032500002422000000"
HOSTILE_FAN = "11062500002422000000"
RAILWAY_LINE = "11042500003303000000"

# (id, name, symbol, kind, parent)
CHINESE = [
    ("22 GROUP ARMY", "22nd Group Army (Sun Zhen)", unit("F", "group", True), "formation",
     None),
    ("41 ARMY", "41st Army", unit("F", "corps"), "formation", "22 GROUP ARMY"),
    ("45 ARMY", "45th Army (Chen Dingxun)", unit("F", "corps"), "formation",
     "22 GROUP ARMY"),
    ("122 DIV", "122nd Division", unit("F", "division"), "formation", "41 ARMY"),
    ("124 DIV", "124th Division", unit("F", "division"), "formation", "41 ARMY"),
    ("WANG", "Wang Mingzhang, 122nd Division", LEADER_CN, "person", "122 DIV"),
    ("ZHANG", "Zhang Xuanwu, 727th Regiment, city defence", MAN_CN, "person", "122 DIV"),
    ("727 REGT", "727th Regiment (Zhang Xuanwu)", unit("F", "regiment"), "unit", "122 DIV"),
    ("731 REGT", "731st Regiment (Wang Wenzhen)", unit("F", "regiment"), "unit",
     "122 DIV"),
    ("YAN BN", "1st Battalion, 731st Regiment (Yan Yi)", unit("F", "battalion"), "unit",
     "122 DIV"),
    ("SPECIAL BN", "41st Army Special Service Battalion", unit("F", "battalion"), "unit",
     "41 ARMY"),
    ("370 BDE", "370th Brigade (Lü Kang)", unit("F", "brigade"), "unit", "124 DIV"),
    ("740 REGT", "740th Regiment (Wang Lin)", unit("F", "regiment"), "unit", "124 DIV"),
    ("372 BDE", "372nd Brigade (Zeng Suyuan)", unit("F", "brigade"), "unit", "124 DIV"),
    ("125 DIV", "125th Division", unit("F", "division"), "unit", "45 ARMY"),
    ("379 BDE", "379th Brigade, 127th Division", unit("F", "brigade"), "unit", "45 ARMY"),
    ("381 BDE", "381st Brigade, 127th Division", unit("F", "brigade"), "unit", "45 ARMY"),
    ("ARMOURED TRAIN", "Chinese armoured train, 75 mm", CN_TRAIN, "train", "22 GROUP ARMY"),
]
JAPANESE = [
    ("SEYA", "Seya Detachment (Maj. Gen. Seya)", unit("H", "brigade", True),
     "unit", None),
    ("10 REGT", "10th Infantry Regiment (Col. Akashiba)", unit("H", "regiment"), "formation",
     "SEYA"),
    ("10 REGT I", "I Battalion, 10th Infantry", unit("H", "battalion"), "unit", "10 REGT"),
    ("10 REGT III", "III Battalion, 10th Infantry", unit("H", "battalion"), "unit", "10 REGT"),
    ("10 REGT II", "II Battalion group, 10th Infantry", unit("H", "battalion"), "unit",
     "10 REGT"),
    ("63 REGT", "63rd Infantry Regiment (Col. Fukuei)", unit("H", "regiment"), "unit",
     "SEYA"),
    ("ARMOUR", "Independent Light Armoured Car Companies 10 and 12", unit("H", "company",
                                                                          function="UCA"),
     "unit", "SEYA"),
    ("CENTRE COLUMN", "Centre column (Kinoshita's artillery group)", unit("H", "battalion"),
     "unit", "SEYA"),
    ("FIELD ARTY", "I Battalion, 10th Field Artillery (Type 38, 8 guns)",
     unit("H", "battalion", function="UCF"), "unit", "SEYA"),
    ("HEAVY ARTY", "I Battalion, 2nd Field Heavy Artillery (12 guns)",
     unit("H", "battalion", function="UCF"), "unit", "SEYA"),
    ("GARRISON ARTY", "China Garrison heavy artillery (Type 96 15 cm)",
     unit("H", "company", function="UCF"), "unit", "SEYA"),
]

# (id, symbol, name, point, bound m, source)
FIXED = [
    ("TENGXIAN", CN_SITE, "Tengxian, the walled city", CITY, 60.0, "tengxian-gazetteer"),
    ("STATION", NEUTRAL_SITE, "Tengxian station (1938 site)", STATION, 200.0,
     "tengxian-gazetteer"),
    ("PAGODA", NEUTRAL_SITE, "Longquan pagoda, the Japanese observation post", PAGODA,
     20.0, "osm"),
    ("LINCHENG", CN_SITE, "Lincheng, 22nd Group Army headquarters", LINCHENG, 500.0,
     "xuecheng-gazetteer"),
]
