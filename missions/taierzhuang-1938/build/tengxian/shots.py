"""The camera: wide over the plain for the advance, close over the walled city for the assault.

The plain round Tengxian is flat; the city's walls are gone and the streets on their line are
today's, so close shots look at the places the replay puts in 1938, not at what the map draws.
"""
from pacing import after_viewing

from .sites import CITY, OUTER_EAST_GATE, L
from .story import pacing

WIDE = (117.100, 35.100)
NORTH = (117.030, 35.270)
JIEHE_AREA = (117.030, 35.200)
EAST_OF_CITY = (117.200, 35.100)
EAST_APPROACH = (117.200, 35.090)
GUN_LINE = (117.163, 35.074)
CITY_WIDE = (117.160, 35.080)
SOUTH_WALL = (117.1570, 35.0812)
WEST_SIDE = (117.1515, 35.0835)
STATION_SIDE = (117.1500, 35.0835)
SOUTH_PLAIN = (117.200, 34.940)

# (from, until, target, zoom, pitch, bearing, intent, entities it shows, options)
SHOTS = [
    ("14 04:00", "14 06:30", WIDE, 8.9, 20, 0,
     "The ground: the railway from 鄒縣 down to Tengxian and Lincheng, and the Japanese "
     "columns about to start.", ["TENGXIAN", "LINCHENG", "10 REGT I"], {"move": 0}),
    ("14 06:30", "15 00:00", NORTH, 10.4, 30, 0,
     "The three Japanese columns break the line north of the city.",
     ["10 REGT I", "63 REGT", "370 BDE"], {"move": 2.5}),
    ("15 00:00", "15 10:00", JIEHE_AREA, 10.8, 35, 0,
     "Before 界河: the detachment gathers on the Chinese line.",
     ["10 REGT I", "63 REGT", "379 BDE"], {"move": 2}),
    ("15 10:00", "15 15:30", "63 REGT", 11.0, 35, 160,
     "Follow the swing round the east: 龍山店 and 東郭.",
     ["63 REGT", "ARMOUR"], {"focus": "63 REGT", "move": 2}),
    ("15 15:30", "15 21:00", "ARMOUR", 11.6, 35, 200,
     "The armour scatters the 731st at 城頭 and takes 王廟.", ["ARMOUR", "63 REGT"],
     {"focus": "ARMOUR", "move": 1.5}),
    ("15 21:00", "16 06:00", EAST_OF_CITY, 11.4, 30, 250,
     "Night: the Japanese bivouac east of the city as its defenders gather.",
     ["10 REGT I", "TENGXIAN"], {"move": 2}),
    ("16 06:00", "16 10:00", EAST_APPROACH, 12.6, 40, 270,
     "The approach from the east, to the suburb wall.", ["10 REGT I", "TENGXIAN"],
     {"move": 2}),
    ("16 10:00", "16 11:40", GUN_LINE, 13.0, 35, 300,
     "The guns at 夏村 and their reach; the armoured train's duel.",
     ["FIELD ARTY", "ARMOURED TRAIN", "HEAVY ARTY"], {"move": 1.5}),
    ("16 11:40", "16 15:00", OUTER_EAST_GATE, 15.3, 40, 270,
     "The east suburb's gate: the failed rush, the breach, the corner held.",
     ["10 REGT I", "TENGXIAN"], {"move": 1.5}),
    ("16 15:00", "16 19:30", CITY_WIDE, 14.2, 40, 300,
     "The 3rd Battalion comes round to the south suburb by moonlight.",
     ["10 REGT III", "HEAVY ARTY"], {"move": 1.5}),
    ("16 19:30", "17 07:00", CITY, 14.6, 40, 300,
     "Night: the brigades from outside come in by the west gate.",
     ["TENGXIAN", "WANG"], {"move": 1.5}),
    ("17 07:00", "17 10:30", GUN_LINE, 13.6, 35, 300,
     "The batteries open on the walls; the two breaches.",
     ["GARRISON ARTY", "HEAVY ARTY", "TENGXIAN"], {"move": 2}),
    ("17 10:30", "17 13:30", CITY, 15.2, 40, 300,
     "Inside the walls: Wang Mingzhang's headquarters and his last telegram.",
     ["WANG", "TENGXIAN"], {"move": 1.5}),
    ("17 13:30", "17 16:30", SOUTH_WALL, 15.6, 40, 330,
     "The south breach: thrown back, then over the wall.", ["10 REGT III"], {"move": 1.5}),
    ("17 16:30", "17 17:45", WEST_SIDE, 16.0, 40, 80,
     "The west gate and its moat, where Wang Mingzhang fell.", ["WANG", "10 REGT III"],
     {"move": 1.5}),
    ("17 17:45", "17 21:00", STATION_SIDE, 15.0, 40, 60,
     "The way out west, shut at the station.", ["372 BDE", "10 REGT II"], {"move": 1.5}),
    ("17 21:00", "17 23:30", CITY, 14.5, 40, 300,
     "The break-out by the north gate, and the east wall taken.",
     ["10 REGT I", "TENGXIAN"], {"move": 1.5}),
    ("17 23:30", "18 14:30", SOUTH_PLAIN, 9.9, 25, 0,
     "Pull back over the plain to Lincheng, where the pursuit is heading.",
     ["TENGXIAN", "LINCHENG", "63 REGT"], {"move": 3}),
]


def camera():
    """(camera cues, each shot's intent and the entities it shows, by start_ms)."""
    pace = pacing()
    cues, intents = [], {}
    for start, end, target, zoom, pitch, bearing, intent, shows, opts in SHOTS:
        a, b = L(start), L(end)
        aim = ({"kind": "entity", "value": target} if isinstance(target, str)
               else {"kind": "point", "value": {"lon": target[0], "lat": target[1]}})
        move = after_viewing(pace, a, opts.get("move", 1.5)) - a
        cue = {"start_ms": a, "end_ms": b, "target": aim, "zoom": zoom, "pitch": pitch,
               "bearing": bearing, "orbit_deg_s": 0.0, "transition_ms": min(move, b - a)}
        if "focus" in opts:
            cue["focus"] = opts["focus"]
        cues.append(cue)
        intents[str(a)] = {"intent": intent, "shows": shows}
    return cues, intents
