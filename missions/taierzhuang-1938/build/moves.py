"""Where each unit goes, on the UTC+8 clock, from the Japanese advance on 14 March to the end of
the mopping-up in Tengxian on the 18th.

Times are the sources' where they give them (build/evidence/); between them the moves are
reconstructed at the pace of infantry on foot, horse-drawn guns and the Japanese light armour.
`plan()` returns every track, the conditions the sources report and the times tracks end.
"""
import datetime as dt

from routes import Mover, railway_between
from sites import (ANLOU, BEILOU, BEISHAHE, CHENGTOU, CHITOUJI, CROSSROADS, DANGSHAN, DAWU,
                   DAWUGOU, DONGCAO, DONGGUAN, DONGGUO, DONGSHAHE, EAST_BREACH,
                   FANGLING, GUANQIAO, JIANGJIALOU, JIEHE, JIEHE_STATION, LIANGXIADIAN,
                   LINCHENG, LONGSHAN, LONGSHANDIAN, NANSHAHE, NORTH_GATE, OUTER_EAST_GATE,
                   OUTER_SOUTH_GATE, POWER_PLANT, PUYANGSHAN, SHANJIAZHUANG, SHENJING,
                   SHIQIANG, SOUTH_BREACH, SOUTH_GATE, START, STATION, TANGCUN, TUCHENGZI,
                   WALL_NW, WALL_SW, WANGMIAO, WANGZHUANG, WEST_GATE, WEST_MOAT, WULIHE, XIACUN,
                   XIANGCHENG, XIAOGONGSHAN, XISIYUAN)

T0 = "14 04:00"
ZHANGJIA_TAOYUAN = (117.020, 35.360)  # 張家桃園, "邹县东南"; not on OSM, placed on the road
CUIJIAZHUANG = (117.090, 35.190)  # 崔家荘, the first echelon's noon assembly south of 界河
YUJIAYUAN = (117.120, 35.220)  # 于家園, "界河东5公里"
WOHUSHAN = (117.030, 35.250)  # 臥虎山, "界河 NW 6 km"
JIUQU = (117.045, 35.235)  # 九曲庄
GULLY = (117.1675, 35.0850)  # the gully 200 m east of the outer east gate
WALL_FOOT = (117.1660, 35.0852)  # 50 m from the outer wall, where the noon assault stopped
EAST_CORNER = (117.1640, 35.0850)  # the corner of the east suburb the 3rd Company held
SOUTH_APPROACH = (117.1620, 35.0780)
SOUTH_SUBURB = (117.1620, 35.0825)
SOUTH_START = (117.1598, 35.0802)  # outside the south-east breach
HQ_IN_CITY = (117.1570, 35.0850)  # 張景湖's house, the 122nd Division's HQ from the 15th; placed
NORTH_WALL = (117.1555, 35.0869)
NORTH_OUT = (117.1500, 35.1100)
WEST_WALL_OUT = (117.1512, 35.0860)
CITY_SOUTH = (117.1570, 35.0815)
CITY_EAST = (117.1585, 35.0845)
CITY_NE = (117.1580, 35.0860)
CITY_SW = (117.1535, 35.0835)
TRAIN_FIRING = (117.1555, 35.0600)
NORTH_EAST_OF_JIEHE = (117.200, 35.170)
LINCHENG_NORTH = (117.236, 34.808)
GUANLUKOU = (117.2201, 35.0339)  # 関路口, on the road south-east toward 臨城


def clock(ms_):
    """`DD HH:MM:SS` for operation milliseconds, the inverse of L."""
    t = START + dt.timedelta(milliseconds=ms_)
    return f"{t.day} {t:%H:%M:%S}"


def tenth_regiment(t):
    """The right column: 唐村 by 石牆 to 池頭集, round the east by 東郭, and the city."""
    for name, bivouac in (("10 REGT I", JIANGJIALOU), ("10 REGT III", XIAOGONGSHAN)):
        t[name] = Mover(TANGCUN, T0).to(SHIQIANG, "14 09:00").to(CHITOUJI, "15 00:00") \
            .to(DONGCAO, "15 04:40").to(ANLOU, "15 09:00").hold("15 11:55") \
            .to(CUIJIAZHUANG, "15 15:00").to(LONGSHANDIAN, "15 16:30") \
            .to(DONGGUO, "15 19:30").to(DAWUGOU, "15 20:50").to(bivouac, "15 23:40")
    t["10 REGT I"].hold("16 06:00").to(XIACUN, "16 08:00").to(TUCHENGZI, "16 08:40") \
        .to(WALL_FOOT, "16 12:00").to(GULLY, "16 12:30").hold("16 14:05") \
        .to(OUTER_EAST_GATE, "16 14:15").to(EAST_CORNER, "16 14:40").hold("17 21:30") \
        .to(EAST_BREACH, "17 21:40").to(NORTH_GATE, "17 23:00").to(CITY_NE, "18 13:00") \
        .hold("18 14:00")
    t["10 REGT III"].hold("16 07:00").to(WANGZHUANG, "16 10:20").to(XISIYUAN, "16 12:00") \
        .to(WULIHE, "16 15:00").to(SOUTH_APPROACH, "16 17:00").to(OUTER_SOUTH_GATE, "16 18:40") \
        .to(SOUTH_SUBURB, "16 19:30").hold("17 08:00").to(SOUTH_START, "17 08:50") \
        .hold("17 16:00").to(SOUTH_BREACH, "17 16:05").to(WALL_SW, "17 16:45") \
        .to(WEST_GATE, "17 17:00").to(WALL_NW, "17 18:30").to(CITY_SW, "18 13:30") \
        .hold("18 14:00")
    t["10 REGT II"] = Mover(BEILOU, "17 14:30").to(STATION, "17 15:15").hold("18 14:00")


def sixty_third(t):
    """The left column: 香城 and 界河, the advance guard of the eastern swing, the railway at
    南沙河 and the pursuit toward 臨城."""
    for name in ("63 REGT", "ARMOUR"):
        t[name] = Mover(ZHANGJIA_TAOYUAN, "14 07:00").to(XIANGCHENG, "14 11:00") \
            .to(YUJIAYUAN, "14 14:00").to(FANGLING, "14 16:20").to(JIEHE, "14 18:10") \
            .hold("15 10:30").to(LONGSHANDIAN, "15 12:00")
    t["63 REGT"].to(DONGGUO, "15 14:00").to(WANGMIAO, "15 18:00").hold("15 21:30") \
        .to(DANGSHAN, "15 23:30").hold("16 06:00").to(NANSHAHE, "16 09:00").hold("16 18:00") \
        .along(railway_between(NANSHAHE, GUANQIAO), "17 05:30").hold("17 10:00") \
        .to(LINCHENG_NORTH, "17 17:00").hold("18 14:00")
    t["ARMOUR"].to(DONGGUO, "15 14:00").to(CHENGTOU, "15 16:00").to(WANGMIAO, "15 17:30") \
        .hold("15 21:30").to(DANGSHAN, "15 23:30").hold("16 09:00").to(NANSHAHE, "16 12:30") \
        .hold("17 03:00").along(railway_between(NANSHAHE, GUANQIAO), "17 05:30") \
        .hold("17 10:00").to(LINCHENG_NORTH, "17 14:00").hold("18 14:00")


def guns_and_staff(t):
    """The centre column down the railway; the guns that followed the 10th round the east; the
    detachment's headquarters."""
    t["CENTRE COLUMN"] = Mover(LIANGXIADIAN, "14 06:30").to(WOHUSHAN, "14 14:00") \
        .to(JIUQU, "14 16:30").hold("15 08:00").to(JIEHE_STATION, "15 10:00").hold("18 14:00")
    for name, arrive in (("FIELD ARTY", "16 10:20"), ("HEAVY ARTY", "16 11:15")):
        t[name] = Mover(JIUQU, "15 08:00").to(ANLOU, "15 11:00").to(CUIJIAZHUANG, "15 15:30") \
            .to(LONGSHANDIAN, "15 17:30").to(DONGGUO, "15 21:30").to(DAWUGOU, "16 01:00") \
            .to(XIACUN, arrive)
    t["HEAVY ARTY"].hold("16 15:00").to(SHANJIAZHUANG, "16 15:40").hold("18 14:00")
    t["FIELD ARTY"].hold("17 05:00").to(SHANJIAZHUANG, "17 06:00").hold("17 15:00") \
        .to(DONGSHAHE, "17 18:00").hold("18 14:00")
    t["GARRISON ARTY"] = Mover(DONGSHAHE, "16 20:00").to(XIACUN, "17 06:00").hold("17 12:30") \
        .to(GUANLUKOU, "17 15:30").hold("18 14:00")
    t["SEYA"] = Mover(LIANGXIADIAN, "14 06:30").to(JIUQU, "14 16:30").to(JIEHE, "15 10:30") \
        .to(LONGSHANDIAN, "15 13:00").to(DONGGUO, "15 17:00").to(DAWUGOU, "15 19:00") \
        .to(XIACUN, "16 15:00").to(DONGSHAHE, "16 17:00").hold("17 07:30") \
        .to(XIACUN, "17 08:40").to(GUANLUKOU, "17 11:30").hold("18 14:00")


def chinese_front(t):
    """The 45th Army's line north of the city and the 124th Division's brigades west of it."""
    t["125 DIV"] = Mover(XIANGCHENG, T0).hold("14 10:30").to(PUYANGSHAN, "14 12:00") \
        .hold("15 13:00").to(NORTH_EAST_OF_JIEHE, "15 16:00").to(CHENGTOU, "15 20:00") \
        .hold("18 14:00")
    t["379 BDE"] = Mover(JIEHE, T0).hold("14 17:30").to((117.080, 35.205), "14 18:30") \
        .hold("15 13:00").to(NORTH_EAST_OF_JIEHE, "15 16:00").hold("18 14:00")
    t["381 BDE"] = Mover(LONGSHAN, T0).hold("15 14:30").to(NORTH_EAST_OF_JIEHE, "15 16:30") \
        .to(CHENGTOU, "15 20:00").hold("18 14:00")
    t["370 BDE"] = Mover(SHIQIANG, T0).hold("14 09:00").to(SHENJING, "14 11:00") \
        .hold("14 19:00").to(DAWU, "14 23:30").hold("16 21:00").to(WEST_GATE, "17 00:00") \
        .to(CITY_SOUTH, "17 00:30").hold("18 14:00")
    t["740 REGT"] = Mover(SHENJING, T0).hold("14 19:00").to(DAWU, "14 23:30").hold("15 05:00") \
        .to(WEST_GATE, "15 09:00").to(DONGGUAN, "15 10:00").hold("17 04:00") \
        .to(CITY_EAST, "17 05:00").hold("18 14:00")
    t["372 BDE"] = Mover(DAWU, T0).hold("16 21:00").to(STATION, "16 23:40").hold("18 14:00")
    t["731 REGT"] = Mover(CHENGTOU, T0).hold("15 16:00").to(GUANQIAO, "16 12:00") \
        .hold("18 14:00")


def the_city(t):
    """The defenders of the city, Wang Mingzhang and the armoured train."""
    t["727 REGT"] = Mover(BEISHAHE, T0).hold("15 16:30").to(NORTH_GATE, "15 18:15") \
        .to(NORTH_WALL, "15 18:30").hold("17 21:00").to(NORTH_GATE, "17 21:10") \
        .to(NORTH_OUT, "17 23:00")
    t["ZHANG"] = Mover(BEISHAHE, T0).hold("15 16:30").to(NORTH_GATE, "15 18:15") \
        .to(HQ_IN_CITY, "15 21:00").hold("17 17:00").to((117.1597, 35.0848), "17 17:40") \
        .hold("18 14:00")
    t["WANG"] = Mover(POWER_PLANT, T0).hold("15 17:30").to(NORTH_GATE, "15 18:15") \
        .hold("15 19:00").to(HQ_IN_CITY, "15 21:30").hold("17 13:00").to(CROSSROADS, "17 13:10") \
        .hold("17 16:50").to(WALL_NW, "17 17:10").to(WEST_WALL_OUT, "17 17:20") \
        .to(WEST_MOAT, "17 17:30")
    t["YAN BN"] = Mover((117.215, 35.095), "15 15:30").to(OUTER_EAST_GATE, "15 17:00") \
        .to(DONGGUAN, "15 17:20").hold("17 04:00").to(CITY_EAST, "17 05:00").hold("18 14:00")
    t["SPECIAL BN"] = Mover(LINCHENG, "15 18:00").along(railway_between(LINCHENG, STATION),
                                                        "15 20:30") \
        .to(SOUTH_GATE, "15 21:00").hold("18 14:00")
    t["ARMOURED TRAIN"] = Mover(STATION, "16 08:00").hold("16 10:50") \
        .to(TRAIN_FIRING, "16 11:00").hold("16 11:10").to(NANSHAHE, "16 12:20").hold("18 14:00")


# (entity, time, condition) as the sources report them; see build/evidence/ for the times.
CONDITIONS = [
    ("731 REGT", "15 16:00", "damaged"), ("ARMOURED TRAIN", "16 12:30", "destroyed"),
    ("740 REGT", "17 09:00", "damaged"), ("370 BDE", "17 15:00", "damaged"),
    ("SPECIAL BN", "17 16:05", "damaged"), ("WANG", "17 17:30", "destroyed"),
    ("372 BDE", "17 17:30", "destroyed"), ("YAN BN", "17 21:40", "destroyed"),
    ("740 REGT", "17 21:40", "destroyed"), ("370 BDE", "17 23:00", "destroyed"),
    ("SPECIAL BN", "17 23:00", "destroyed"), ("ZHANG", "17 17:40", "damaged"),
]

# Where a track ends: the 727th broke out, and Wang Mingzhang's body is no longer shown once the
# story has told of his death.
ESCAPED = {"727 REGT": "17 23:00", "WANG": "17 19:00"}


def plan():
    """(tracks by entity, conditions, escapes)."""
    movers = {}
    tenth_regiment(movers)
    sixty_third(movers)
    guns_and_staff(movers)
    chinese_front(movers)
    the_city(movers)
    return {k: m.track for k, m in movers.items()}, CONDITIONS, ESCAPED
