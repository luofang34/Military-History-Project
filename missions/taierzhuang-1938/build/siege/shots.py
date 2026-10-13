"""The camera: wide over both banks when the fans and the long shots matter, close over the gun
line and the town for the night attacks and the counter-battery fire."""
from pacing import after_viewing

from .sites import (CANGLANGMIAO, MENG_E, NW_CORNER, L)
from .story import pacing

BOTH_BANKS = (117.7350, 34.5250)
SANLI = (117.7230, 34.5780)
EAST_LINE = (117.7540, 34.5680)
GUN_LINE = (117.7450, 34.5850)
STATION_VIEW = (117.7200, 34.5510)
TOWN_AND_GUNS = (117.7330, 34.5700)
SOUTH_HILLS = (117.7330, 34.5450)
NORTH_WEST = (117.7200, 34.6100)
GUN_PARK = (117.7270, 34.5850)  # between Liujiahu and Sanlizhuang

# (from, until, target, zoom, pitch, bearing, intent, entities it shows, options)
SHOTS = [
    ("18 14:30", "19 12:00", (117.400, 34.920), 9.3, 20, 0,
     "Pull out from Tengxian: the detachment goes on down the railway to Lincheng and sends its "
     "pursuit forces out.", ["63 REGT", "HEAVY ARTY", "63 REGT II"], {"move": 3}),
    ("19 12:00", "20 12:00", (117.480, 34.730), 10.0, 25, 0,
     "Closer on the two pursuits: Hanzhuang taken on the canal, Yixian stormed at night.",
     ["63 REGT I", "63 REGT II"], {"move": 2.5}),
    ("20 12:00", "21 18:00", (117.550, 34.680), 9.4, 25, 20,
     "The Chinese regroup: Tang Enbo's corps into the hills, the 110th Division to the canal.",
     ["20 ARMY CORPS", "110 DIV"], {"move": 2.5}),
    ("21 18:00", "22 17:30", (117.500, 34.720), 9.6, 25, 20,
     "The 31st Division into Taierzhuang; the 63rd's main body along the branch to Yixian.",
     ["31 DIV", "63 REGT"], {"move": 2.5}),
    ("22 17:30", "24 08:00", (117.640, 34.700), 10.3, 30, 150,
     "On towards the canal: one battalion and a battery, and the Chinese who meet them at Nigou "
     "and Beiluo.", ["63 REGT II", "FIELD I"], {"move": 2.5}),
    ("24 08:00", "25 06:00", (117.7385, 34.5720), 14.0, 40, 180,
     "Close on the north wall for the first assault, and the battalion cut off outside it.",
     ["63 REGT II", "TAIERZHUANG", "FIELD I"], {"move": 2.5}),
    ("25 06:00", "25 15:30", (117.480, 34.720), 9.2, 25, 30,
     "Wide again: the Type 96 howitzers' run by lorry from Lincheng to Liujiahu.",
     ["TYPE 96"], {"move": 2.5}),
    ("25 15:30", "26 06:00", (117.7350, 34.5450), 11.8, 30, 0,
     "Both banks: the Chinese guns at the foot of the hills, the Type 96 at Liujiahu, and the "
     "night attacks on the Japanese batteries.", ["XIONGSHAN GUNS", "TYPE 96", "EAST FORCE"],
     {"move": 2.5}),
    ("26 06:00", "26 23:00", (117.7420, 34.5800), 13.2, 35, 200,
     "Closer on the gun line north of the town as the Type 96 moves up to Peizhuang and more "
     "guns arrive.", ["TYPE 96", "FIELD I 3", "LIUJIAHU"], {"move": 2.5}),
    ("26 23:00", "27 12:00", (117.7440, 34.5680), 14.3, 40, 200,
     "Close on the north-east corner for the break-in.", ["63 REGT II", "TAIERZHUANG"],
     {"move": 2.5}),
    ("27 12:00", "27 22:00", (117.7200, 34.6000), 12.2, 35, 180,
     "Up the railway: the main body and the heavy guns arrive, the tanks go in, Chinese shells "
     "fall on Liujiahu.", ["63 REGT", "TANKS", "LIUJIAHU"], {"move": 2.5}),
    ("27 22:00", "28 12:00", (117.7150, 34.5500), 11.6, 30, 0,
     "Across the canal for the first duel: the heavy guns at Sanlizhuang against the guns in "
     "the hills.", ["HEAVY 3", "HANSHAN GUNS", "ZHAISHAN GUNS"], {"move": 2.5}),
    ("28 12:00", "29 06:00", (117.7310, 34.5660), 14.6, 40, 200,
     "Close on the north-west corner, breached twice and stormed at dusk.",
     ["11 COY", "TAIERZHUANG"], {"move": 2.5}),
    ("29 06:00", "30 01:30", (117.7420, 34.5800), 13.1, 40, 160,
     "The fight for the gun line round Peizhuang, where the Type 96's vehicles burn.",
     ["TYPE 96", "EAST FORCE", "EAST GUNS"], {"move": 2.5}),
    ("30 01:30", "30 02:20", BOTH_BANKS, 11.0, 30, 0,
     "Both banks and each battery's reach: the Chinese 15 cm fan covers the Japanese guns; no "
     "Japanese fan reaches it.", ["SFH", "TYPE 96", "TAIERZHUANG"], {"move": 0}),
    ("30 02:20", "30 05:00", SANLI, 14.6, 40, 200,
     "The night attack from the station on the reserve and the heavy guns.",
     ["NIGHT ATTACK", "HEAVY 2", "63 REGT III"], {"move": 2}),
    ("30 05:00", "30 09:30", EAST_LINE, 14.5, 40, 120,
     "The duel with the Chinese guns towards Zhaocun.", ["EAST GUNS", "FIELD I"], {"move": 2}),
    ("30 09:30", "30 16:30", GUN_LINE, 13.3, 35, 90,
     "The Type 96 searches the villages east of the town.", ["TYPE 96"], {"move": 2}),
    ("30 16:30", "30 19:15", MENG_E, 14.6, 40, 120,
     "A night attack forms east of Mengzhuang and is broken up.", ["EAST FORCE"], {"move": 2}),
    ("30 19:15", "31 00:00", NW_CORNER, 15.0, 45, 160,
     "Across the town to its north-west corner for the dare-to-die squad's night attack.",
     ["SQUAD", "11 COY"], {"move": 2}),
    ("31 00:00", "31 08:30", STATION_VIEW, 14.2, 40, 180,
     "The armoured train's night run into the station, and the guns on it at dawn.",
     ["TRAIN", "TZZ STATION"], {"move": 2}),
    ("31 08:30", "31 11:10", TOWN_AND_GUNS, 13.4, 35, 180,
     "The Japanese gun line and the town it fires on.", ["TYPE 96", "TAIERZHUANG"],
     {"move": 2}),
    ("31 11:10", "31 11:40", SOUTH_HILLS, 11.8, 30, 0,
     "The first concentration on the town, and the Chinese reply from the hills.",
     ["TAIERZHUANG", "XIONGSHAN GUNS", "TYPE 96"], {"move": 2}),
    ("31 11:40", "31 14:50", TOWN_AND_GUNS, 13.2, 35, 200,
     "Closer again for the second, third and fourth concentrations, from the heavy guns at "
     "Sanlizhuang.", ["HEAVY 3", "TAIERZHUANG"], {"move": 2}),
    ("31 14:50", "31 15:30", CANGLANGMIAO, 14.0, 40, 90,
     "A Chinese battery at Canglangmiao, found and fired on.", ["EAST GUNS"], {"move": 2}),
    ("31 15:30", "31 16:05", BOTH_BANKS, 11.0, 30, 0,
     "The first 15 cm-class rounds, from beyond the Japanese reach onto the 3rd Heavy Company.",
     ["SFH", "HEAVY 3"], {"move": 2}),
    ("31 16:05", "31 19:30", SOUTH_HILLS, 12.0, 30, 0,
     "The Type 96 hunts the batteries at Hanshan and Bianzhuang.",
     ["HANSHAN GUNS", "TYPE 96"], {"move": 2}),
    ("31 19:30", "1 05:00", NW_CORNER, 15.0, 40, 200,
     "The 11th Company leaves the north-west corner under the heavy guns' cover.",
     ["11 COY", "TAIERZHUANG"], {"move": 2}),
    ("1 05:00", "1 09:00", NORTH_WEST, 12.3, 30, 180,
     "Morning, 1 April: the observation post moves up; the 10th's field guns come forward.",
     ["FIELD 10I", "OP"], {"move": 2}),
    ("1 09:00", "1 13:30", BOTH_BANKS, 11.0, 30, 0,
     "The 15 cm rounds fall on Liujiahu and Sanlizhuang from guns no one can find.",
     ["SFH", "LIUJIAHU"], {"move": 2}),
    ("1 13:30", "1 17:00", GUN_PARK, 13.8, 45, 160,
     "Close on the Japanese gun line, looking south the way the rounds come: the afternoon's "
     "bombardments land at fixed intervals.", ["LIUJIAHU", "HEAVY 3"], {"move": 2}),
    ("1 17:00", "1 19:05", BOTH_BANKS, 10.8, 25, 0,
     "Pull back over both banks: two guns the Japanese never reached.",
     ["SFH", "TYPE 96", "TAIERZHUANG"], {"move": 3}),
]


def camera():
    pace = pacing()
    cues, intents = [], {}
    for start, end, target, zoom, pitch, bearing, intent, shows, opts in SHOTS:
        a, b = L(start), L(end)
        aim = ({"kind": "entity", "value": target} if isinstance(target, str)
               else {"kind": "point", "value": {"lon": target[0], "lat": target[1]}})
        move = after_viewing(pace, a, opts.get("move", 1.5)) - a
        cue = {"start_ms": a, "end_ms": b, "target": aim, "zoom": zoom, "pitch": pitch,
               "bearing": bearing, "orbit_deg_s": 0.0, "transition_ms": min(move, b - a)}
        cues.append(cue)
        intents[str(a)] = {"intent": intent, "shows": shows}
    return cues, intents
