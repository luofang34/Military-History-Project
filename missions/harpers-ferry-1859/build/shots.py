"""The camera: one shot per beat of the story, each with what it is for and what it shows.

The town lies in a gorge some 300 m deep between Maryland Heights, Loudoun Heights and Bolivar
Heights, so close shots of it look up the Potomac from over the confluence (bearing about 300)
and keep their pitch at 45° or less, which keeps the eye in the open air above the rivers.
"""
from pacing import after_viewing

from sites import (BEALL_AIR, BRIDGE_MID, CAMDEN_STATION, DURATION, ENGINE_HOUSE, KENNEDY_FARM,
                   L, MONOCACY)
from story import pacing

TOWN = (-77.7320, 39.3236)
TWO_FIGHTS = (-77.7347, 39.3230)
EAST_LINE = (-77.15, 39.33)
RAIL_WEST = (-77.30, 39.20)
SANDY_HOOK_VIEW = (-77.7180, 39.3262)
FARM_TO_FERRY = (-77.7240, 39.3515)

# (from, until, target, zoom, pitch, bearing, intent, entities it shows, options): the target is
# a (lon, lat) point or an entity id; moves take 1.5 s of viewing unless `move` says.
SHOTS = [
    ("16 14:30", "16 20:00", KENNEDY_FARM, 16.0, 40, 200,
     "The Kennedy farm on Sunday: the Provisional Army's headquarters, five miles from the "
     "Ferry.", ["KENNEDY FARM", "BROWN"], {"move": 0}),
    ("16 20:00", "16 21:30", "BROWN", 14.6, 40, 200,
     "The march leaves the farm: Brown's wagon, Cook and Tidd ahead, the men in pairs behind.",
     ["BROWN", "TIDD"], {"focus": "BROWN"}),
    ("16 21:30", "16 22:18", (-77.7330, 39.3420), 13.2, 30, 180,
     "Where they are going: down the river road to the bridge into Harpers Ferry.",
     ["BROWN", "B&O BRIDGE"], {"move": 2.5}),
    ("16 22:18", "16 22:27", "TIDD", 15.6, 35, 20,
     "Cook and Tidd cut the telegraph east, where the road meets the railroad at the bridge.",
     ["TIDD", "WIRE EAST"], {"focus": "TIDD"}),
    ("16 22:27", "16 22:45", BRIDGE_MID, 16.4, 45, 260,
     "Over the covered bridge on the line of its surviving piers: the watchman taken, the column "
     "into town.", ["KAGI", "BROWN", "B&O BRIDGE"], {}),
    ("16 22:45", "16 23:40", TOWN, 15.3, 40, 300,
     "The town taken without a shot: armory gate, arsenal, Shenandoah bridge, rifle works, and "
     "the line west cut.", ["BROWN", "HAZLETT", "OLIVER", "KAGI", "WIRE WEST"], {"move": 2}),
    ("16 23:40", "17 01:20", "STEVENS", 14.2, 40, 270,
     "Stevens's party out the Charlestown pike toward Beall-Air.", ["STEVENS"],
     {"focus": "STEVENS", "move": 2}),
    ("17 01:20", "17 01:34", (-77.7335, 39.3250), 15.1, 40, 300,
     "Cut to the bridge: the express arrives and backs off, and Heyward Shepherd is shot.",
     ["EXPRESS", "STATION", "WATSON"], {"move": 0}),
    ("17 01:34", "17 02:30", BEALL_AIR, 16.0, 40, 250,
     "Cut to Beall-Air: Washington taken from his bed, with his slaves and his weapons.",
     ["STEVENS", "BEALL-AIR"], {"move": 0}),
    ("17 02:30", "17 02:50", "STEVENS", 15.0, 40, 90,
     "Back along the pike with the carriage, the wagon and the prisoners.", ["STEVENS"],
     {"focus": "STEVENS"}),
    ("17 02:50", "17 03:25", (-77.7557, 39.3163), 16.0, 40, 90,
     "Allstadt's house on the pike: the second hostage.", ["STEVENS", "ALLSTADT HOUSE"],
     {"move": 0}),
    ("17 03:25", "17 04:10", "STEVENS", 15.2, 40, 100,
     "The hostages are brought into the armory.", ["STEVENS"], {"focus": "STEVENS"}),
    ("17 04:10", "17 05:50", TOWN, 15.3, 40, 300,
     "The town before dawn: the train still held, the wagon off to Maryland for the arms.",
     ["EXPRESS", "BROWN"], {"move": 2}),
    ("17 05:50", "17 06:15", BRIDGE_MID, 16.4, 45, 280,
     "Brown walks the express over the bridge.", ["BROWN", "EXPRESS"], {}),
    ("17 06:15", "17 07:03", "EXPRESS", 12.6, 30, 100,
     "Stay with the express as it runs east down the Potomac with the news, all the way to "
     "Monocacy.", ["EXPRESS"], {"focus": "EXPRESS", "move": 2}),
    ("17 07:03", "17 07:12", MONOCACY, 14.0, 40, 90,
     "Monocacy: the first telegraph east, and Phelps's dispatch.", ["EXPRESS", "MONOCACY"],
     {"move": 0}),
    ("17 07:12", "17 08:55", EAST_LINE, 9.0, 20, 0,
     "The line from the Ferry to Baltimore: the train and the news travel east.",
     ["EXPRESS", "CAMDEN STATION"], {"move": 2.5}),
    ("17 08:55", "17 09:12", CAMDEN_STATION, 15.0, 40, 0,
     "Baltimore: the railroad doubts the dispatch.", ["CAMDEN STATION"], {"move": 2}),
    ("17 09:12", "17 10:25", TOWN, 15.3, 40, 300,
     "Morning in the town: the raiders hold their posts as the militia gather.",
     ["CITIZENS", "BROWN", "OLIVER"], {"move": 0}),
    ("17 10:25", "17 10:40", CAMDEN_STATION, 15.0, 40, 0,
     "Baltimore: Garrett raises the alarm in Washington and Richmond.", ["CAMDEN STATION"],
     {"move": 0}),
    ("17 10:40", "17 11:50", "JEFFERSON GUARDS", 14.0, 35, 20,
     "The Jefferson Guards' way round to the Maryland bank.", ["JEFFERSON GUARDS"],
     {"focus": "JEFFERSON GUARDS", "move": 0}),
    ("17 11:50", "17 12:20", BRIDGE_MID, 16.2, 45, 280,
     "The Guards take the bridge; Newby falls; Brown withdraws into the engine house.",
     ["JEFFERSON GUARDS", "NEWBY", "ENGINE HOUSE"], {}),
    ("17 12:20", "17 13:02", ENGINE_HOUSE, 16.8, 45, 300,
     "Flags of truce at the engine house, and Leeman's run for the river.",
     ["WATSON", "STEVENS", "LEEMAN"], {}),
    ("17 13:02", "17 14:35", TOWN, 15.3, 40, 300,
     "Afternoon: the ring closes round the armory.",
     ["CITIZENS", "BOTTS COMPANY", "JEFFERSON GUARDS"], {"move": 2}),
    ("17 14:35", "17 14:58", ENGINE_HOUSE, 16.8, 45, 300,
     "Beckham shot near the water station; Thompson killed on the bridge.",
     ["E COPPOC", "ENGINE HOUSE", "W THOMPSON"], {}),
    ("17 14:58", "17 15:30", TWO_FIGHTS, 15.4, 40, 300,
     "Two fights at once: the Martinsburg company at the watch-house, citizens at the rifle "
     "works.", ["MARTINSBURG COMPANY", "KAGI", "IRWIN PARTY"], {}),
    ("17 15:30", "17 17:28", ENGINE_HOUSE, 16.4, 45, 300,
     "The siege of the engine house into the evening.", ["BROWN", "ENGINE HOUSE"], {}),
    ("17 17:28", "17 17:50", "HAZLETT", 15.8, 40, 300,
     "Hazlett and Anderson slip away at dusk.", ["HAZLETT", "O ANDERSON"],
     {"focus": "HAZLETT"}),
    ("17 17:50", "17 19:45", RAIL_WEST, 9.4, 20, 0,
     "Troops by rail: the marines from Washington and the militia from Baltimore.",
     ["MARINES", "BALTIMORE MILITIA"], {"move": 2.5}),
    ("17 19:45", "17 22:44", "MARINES", 11.6, 30, 290,
     "The troop train west, with Lee following in his special.", ["MARINES"],
     {"focus": "MARINES", "move": 2}),
    ("17 22:44", "17 23:55", SANDY_HOOK_VIEW, 14.3, 40, 290,
     "Sandy Hook: Lee arrives and sends the marines over the bridge.",
     ["MARINES", "LEE", "B&O BRIDGE"], {"move": 2}),
    ("17 23:55", "18 06:56:30", ENGINE_HOUSE, 16.0, 40, 300,
     "Night round the engine house.", ["MARINES", "ENGINE HOUSE"], {"move": 2}),
    ("18 06:56:30", "18 07:00:30", ENGINE_HOUSE, 17.4, 45, 300,
     "Stuart carries the summons to the door.", ["STUART", "ENGINE HOUSE"], {}),
    ("18 07:00:30", "18 07:06", ENGINE_HOUSE, 17.6, 45, 300,
     "The storming party breaks in, and Brown is cut down.", ["STORMING PARTY", "BROWN"], {}),
    ("18 07:06", "18 07:45", FARM_TO_FERRY, 12.1, 20, 200,
     "Pull back over the road from the farm to the Ferry as the story is told out.",
     ["ENGINE HOUSE", "KENNEDY FARM"], {"move": 4}),
]


def camera():
    """(camera cues, each shot's intent and the entities it shows, by start_ms)."""
    pace = pacing()
    cues, intents = [], {}
    for start, end, target, zoom, pitch, bearing, intent, shows, opts in SHOTS:
        a, b = L(start), (DURATION if end == "18 07:45" else L(end))
        aim = ({"kind": "entity", "value": target} if isinstance(target, str)
               else {"kind": "point", "value": {"lon": target[0], "lat": target[1]}})
        move = after_viewing(pace, a, opts.get("move", 1.5)) - a
        cue = {"start_ms": a, "end_ms": b, "target": aim, "zoom": zoom, "pitch": pitch,
               "bearing": bearing, "orbit_deg_s": opts.get("orbit", 0.0),
               "transition_ms": min(move, b - a)}
        if "focus" in opts:
            cue["focus"] = opts["focus"]
        cues.append(cue)
        intents[str(a)] = {"intent": intent, "shows": shows}
    return cues, intents
