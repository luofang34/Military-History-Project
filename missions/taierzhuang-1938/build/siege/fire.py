"""Every recorded fire mission, as rounds in flight from the battery to the target.

Each entry is a time the reports give (or, where marked, the replay's estimate: see the
concentration-times and afternoon-bombardments disputes). Rounds fly at an average 280 m/s, so
a 15 cm round to 13 km is in the air about 45 s; the story slows to show each flight.
"""
from .sites import (CANGLANGMIAO, HANSHAN, LIUJIAHU, MENG_E, MENG_NW, NW_CORNER, PENGCUN,
                    SANLI_NE, SANLIZHUANG, SFH_POSITION, STATION_SOUTH, TOWN, TOWN_WEST,
                    XIONGSHAN, YANZIJING, ZHAISHAN, ZHAOCUN, BIANZHUANG, L)
from .sites import (LIUJIAHU_N, NE_CORNER, NORTH_OUT, PEI_E, PEIZHUANG, SANLI_RAIL, TANSHAN,
                    TYPE96_POS, YIXIAN_SW)
from track import distance_m

MPS = 280.0
WEST_GATE = (117.7330, 34.5590)
WEST_VILLAGE = (117.7300, 34.5580)
NE_MENG = (117.7560, 34.5700)


NORTH_WALL_W = (117.7375, 34.5632)  # the breaches west of the north gate, 24 March
WATCHTOWER = (117.7410, 34.5600)  # 「敵觀測所タル望樓」, in the town; placed at its centre
ASSEMBLY = (117.7240, 34.5895)  # the 5th Company's hamlet east of the railway, 600 m WSW of 劉家湖
BEHIND_HEAVY_3 = (117.7287, 34.5828)  # 「其射彈右砲兵陣地ノ後方約百米」
PANZHUI = (117.7480, 34.6050)  # 潘墜; not on OSM, north of 邵庄 on the Type 96 company's sketch
BEHIND_PEIZHUANG = (117.7480, 34.5765)  # where the Type 96 company's vehicles were gathered
CANGLANGMIAO_NE = (117.7640, 34.5625)

# (rounds entity, time, from, to, what)
MISSIONS = [
    ("JP ROUNDS", "24 16:15", MENG_NW, NORTH_WALL_W, "breaching the wall west of the north gate"),
    ("CN ROUNDS", "25 08:00", SANLI_RAIL, ASSEMBLY, "the armoured train's gun on the 5th Company"),
    ("JP 15CM ROUNDS", "25 12:40", YIXIAN_SW, TANSHAN, "warning fire on the heights by Yixian"),
    ("CN ROUNDS", "25 16:00", XIONGSHAN, NORTH_OUT, "guns south of the canal on the battalion"),
    ("JP 15CM ROUNDS", "25 17:30", LIUJIAHU_N, SANLIZHUANG, "the Type 96 opens on Sanlizhuang"),
    ("JP 15CM ROUNDS", "26 12:45", PEIZHUANG, WATCHTOWER, "a watchtower used for observation"),
    ("CN ROUNDS", "26 17:00", STATION_SOUTH, PEIZHUANG, "rounds round the battery positions"),
    ("JP ROUNDS", "27 06:00", MENG_NW, NE_CORNER, "assault fire on the north wall"),
    ("JP 15CM ROUNDS", "27 06:00", PEIZHUANG, NE_CORNER, "assault fire on the north wall"),
    ("CN ROUNDS", "27 17:30", STATION_SOUTH, LIUJIAHU, "shells from west of the town on Liujiahu"),
    ("CN ROUNDS", "27 19:15", STATION_SOUTH, LIUJIAHU, "twenty more from by the station"),
    ("JP 15CM ROUNDS", "28 06:40", SANLI_NE, NW_CORNER, "ranging on the north-west corner"),
    ("CN ROUNDS", "28 06:41", HANSHAN, BEHIND_HEAVY_3, "the reply, 100 m behind the battery"),
    ("JP 15CM ROUNDS", "28 07:50", PEIZHUANG, NW_CORNER, "breaching the north-west corner"),
    ("CN ROUNDS", "28 10:05", PANZHUI, LIUJIAHU, "shells from the north-east on Liujiahu"),
    ("JP 15CM ROUNDS", "28 15:30", PEIZHUANG, NW_CORNER, "the second breaching shoot"),
    ("CN ROUNDS", "28 16:00", PENGCUN, PEIZHUANG, "field guns from the east on the field guns"),
    ("JP ROUNDS", "29 08:20", MENG_NW, MENG_E, "four mountain guns east of Mengzhuang"),
    ("CN ROUNDS", "29 11:10", MENG_E, BEHIND_PEIZHUANG, "a concentration on the vehicles"),
    ("JP 15CM ROUNDS", "29 13:00", LIUJIAHU, CANGLANGMIAO_NE, "four guns by Canglangmiao"),
    ("JP 15CM ROUNDS", "29 15:30", LIUJIAHU, PEI_E, "mortars and mountain guns east of Peizhuang"),
    ("CN ROUNDS", "30 06:00", ZHAOCUN, MENG_NW, "Chinese guns towards Zhaocun on the field guns"),
    ("JP ROUNDS", "30 06:03", MENG_NW, ZHAOCUN, "the field guns answer: two Chinese guns hit"),
    ("JP 15CM ROUNDS", "30 10:10", TYPE96_POS, PENGCUN, "Type 96 on the positions near Pengcun"),
    ("JP 15CM ROUNDS", "30 12:40", TYPE96_POS, YANZIJING, "Type 96 on troops at Yanzijing"),
    ("JP 15CM ROUNDS", "30 14:05", TYPE96_POS, YANZIJING, "Type 96 on Yanzijing's west end"),
    ("JP 15CM ROUNDS", "30 17:30", SANLI_NE, MENG_E,
     "breaking up a night attack east of Mengzhuang"),
    ("JP 15CM ROUNDS", "31 08:50", TYPE96_POS, TOWN_WEST, "Type 96 on the town's west half"),
    ("JP 15CM ROUNDS", "31 11:14", SANLI_NE, TOWN, "first of four concentrations on the town"),
    ("JP ROUNDS", "31 11:14:30", MENG_NW, TOWN, "the field guns join the concentration"),
    ("CN ROUNDS", "31 11:18", XIONGSHAN, LIUJIAHU, "the Chinese reply on Liujiahu"),
    ("CN ROUNDS", "31 11:19", HANSHAN, SANLI_NE, "and on the guns at Sanlizhuang"),
    ("CN ROUNDS", "31 11:23", STATION_SOUTH, SANLIZHUANG, "rounds from south of the station"),
    ("JP 15CM ROUNDS", "31 12:20", TYPE96_POS, TOWN, "second concentration (time estimated)"),
    ("JP 15CM ROUNDS", "31 13:30", SANLI_NE, TOWN, "third concentration (time estimated)"),
    ("JP 15CM ROUNDS", "31 14:40", TYPE96_POS, TOWN, "fourth concentration"),
    ("JP 15CM ROUNDS", "31 15:05", SANLI_NE, CANGLANGMIAO,
     "a Chinese battery found at Canglangmiao"),
    ("CN 15CM ROUNDS", "31 15:46", SFH_POSITION, SANLI_NE,
     "15 cm-class rounds: one Type 4 knocked out"),
    ("JP 15CM ROUNDS", "31 16:15", TYPE96_POS, HANSHAN, "Type 96 on a battery at Hanshan"),
    ("JP 15CM ROUNDS", "31 16:50", TYPE96_POS, BIANZHUANG, "Type 96 on guns near Bianzhuang"),
    ("JP 15CM ROUNDS", "31 17:50", SANLI_NE, TOWN, "harassing fire on the town"),
    ("JP 15CM ROUNDS", "31 20:00", SANLI_NE, WEST_VILLAGE,
     "covering the 11th Company's withdrawal"),
    ("JP 15CM ROUNDS", "1 05:15", SANLI_NE, TOWN_WEST, "on the mortars in the town's west"),
    ("JP 15CM ROUNDS", "1 05:40", SANLI_NE, TOWN_WEST, "the mortars again"),
    ("JP ROUNDS", "1 06:00", MENG_NW, NE_MENG,
     "the field guns on mortars north-east of Mengzhuang"),
    ("CN ROUNDS", "1 08:00", ZHAISHAN, LIUJIAHU, "field-gun rounds on Liujiahu from the morning"),
    ("JP 15CM ROUNDS", "1 08:30", TYPE96_POS, NW_CORNER, "Type 96 on machine guns on the wall"),
    ("CN 15CM ROUNDS", "1 09:30", SFH_POSITION, LIUJIAHU,
     "15 cm rounds on Liujiahu (time estimated)"),
    ("JP 15CM ROUNDS", "1 10:00", TYPE96_POS, WEST_GATE, "Type 96 on a covered machine gun"),
    ("CN 15CM ROUNDS", "1 13:00", SFH_POSITION, SANLI_NE, "15 cm rounds at intervals (estimated)"),
    ("CN 15CM ROUNDS", "1 14:30", SFH_POSITION, LIUJIAHU, "15 cm rounds at intervals (estimated)"),
    ("CN 15CM ROUNDS", "1 16:00", SFH_POSITION, SANLI_NE, "15 cm rounds at intervals (estimated)"),
    ("JP 15CM ROUNDS", "1 17:25", TYPE96_POS, STATION_SOUTH,
     "Type 96 on the guns south of the station"),
    ("CN 15CM ROUNDS", "1 17:30", SFH_POSITION, LIUJIAHU, "15 cm rounds at intervals (estimated)"),
    ("JP 15CM ROUNDS", "1 18:10", TYPE96_POS, NW_CORNER, "Type 96 on the north-west corner"),
    ("CN ROUNDS", "1 19:00", STATION_SOUTH, SANLIZHUANG, "rounds on Sanlizhuang and Liujiahu"),
]


def flight_ms(a, b):
    return int(distance_m(a, b) / MPS * 1000)


def emit(em):
    """Each mission as two fixes, battery then target, joined in flight; then out of sight."""
    for entity, at, start, end, _ in MISSIONS:
        t0 = L(at)
        t1 = t0 + flight_ms(start, end)
        em.fix("reconstruction-fire", entity, t0, start, 0.0, 300.0, t1, "reconstructed", [],
               reference="ground")
        em.fix("reconstruction-fire", entity, t1, end, 0.0, 300.0, t1 + 15_000, "reconstructed",
               [], reference="ground")
        em.gap("reconstruction-fire", entity, t1 + 15_000, None, "reconstructed", [])


FLIGHT_VIEWING_S = 4.0


def flight_windows():
    """(launch, arrival) ms of each fire mission."""
    return [(L(at), L(at) + flight_ms(start, end)) for _, at, start, end, _ in MISSIONS]


def beats():
    """(from, until, speed) of each flight, for the story to slow through: a few seconds of
    viewing whatever the range, so a long shot is not slower to watch than a short one."""
    out = []
    for _, at, start, end, _ in MISSIONS:
        a, b = L(at) - 5_000, L(at) + flight_ms(start, end) + 5_000
        out.append((a, b, max(1.0, (b - a) / 1000 / FLIGHT_VIEWING_S)))
    return out
