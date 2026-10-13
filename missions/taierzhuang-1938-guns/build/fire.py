"""Every recorded fire mission, as rounds in flight from the battery to the target.

Each entry is a time the reports give (or, where marked, the replay's estimate: see the
concentration-times and afternoon-bombardments disputes). Rounds fly at an average 280 m/s, so
a 15 cm round to 13 km is in the air about 45 s; the story slows to show each flight.
"""
from sites import (CANGLANGMIAO, HANSHAN, LIUJIAHU, MENG_E, MENG_NW, NW_CORNER, PENGCUN,
                   SANLI_NE, SANLIZHUANG, SFH_POSITION, STATION_SOUTH, TOWN, TOWN_WEST,
                   XIONGSHAN, YANZIJING, ZHAISHAN, ZHAOCUN, BIANZHUANG, L)
from moves import TYPE96_POS
from track import distance_m

MPS = 280.0
WEST_GATE = (117.7330, 34.5590)
WEST_VILLAGE = (117.7300, 34.5580)
NE_MENG = (117.7560, 34.5700)


# (rounds entity, time, from, to, what)
MISSIONS = [
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
