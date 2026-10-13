"""Where everyone goes, on the clock, from the farm on Sunday to the engine house on Tuesday.

Times come from build/evidence/ where a source gives them; between them the moves are
reconstructed at a walking pace on foot, a wagon's on the roads and the B&O's 1859 limit on the
railroad. `plan()` returns every track, the conditions the sources report and the times tracks end.
"""
import datetime as dt

from routes import (BYRNE_ROAD, EAST, FROM_WEST, LOCK_34, LOCK_34_ROAD, PIKE, ROAD,
                    SANDY_HOOK_TRACK, SCHOOLHOUSE_ROAD, TO_BALTIMORE, WASHINGTON_BRANCH, Mover,
                    reverse)
from sites import (ALLSTADT_HOUSE, ARMORY_GATE, ARSENAL, BEALL_AIR, BRIDGE_MD, BRIDGE_MID,
                   BRIDGE_VA, CAMDEN_STATION, CHARLES_TOWN, ELLICOTTS_MILLS, ENGINE_HOUSE,
                   FREDERICK, GALT_HOUSE, KENNEDY_FARM, L, MONOCACY, RELAY, RIFLE_WORKS,
                   SANDY_HOOK, SCHOOLHOUSE, SHENANDOAH_BRIDGE, START, STATION, TELEGRAPH_EAST,
                   TELEGRAPH_WEST, WASHINGTON_DEPOT)

T0 = "16 14:30"
POTOMAC_POST = BRIDGE_MID
POTOMAC_TOWN_POST = (-77.72780, 39.32337)  # the town half of the bridge, Monday morning
STABLE = (-77.8115, 39.3148)  # Beall-Air's outbuildings; placed, within the site's bound
# The cabin across the road where the pikes were kept, "about 600 yards" from the house (Unseld).
CABIN = (-77.7095, 39.3790)
TO_RIFLE_WORKS = [ARMORY_GATE, ARSENAL, (-77.7340, 39.3222), (-77.7375, 39.3218), RIFLE_WORKS]
NEWBY_SPOT = (-77.72935, 39.32322)  # "just outside the Armory gate" (De Witt)
TRUCE_SPOT = (-77.72925, 39.32315)  # in the street, under the Galt House windows
UPPER_YARD = (-77.7310, 39.3248)
LEEMAN_ISLET = (-77.7290, 39.3248)  # "a little above the bridge", "a tiny islet" (Villard)
KAGI_ROCK = (-77.7392, 39.3205)  # "a large flat rock near the middle of the stream" (Villard)
COPELAND_TAKEN = (-77.7340, 39.3225)
HALLTOWN_RAIL = (-77.7950, 39.3120)
BOLIVAR_HEIGHTS = (-77.7550, 39.3260)
CROSSING_VA = (-77.7405, 39.3305)  # "by boat, a mile or more above the arsenal" (Villard)
CROSSING_MD = (-77.7395, 39.3322)
WEST_YARD = (-77.7330, 39.3256)  # the armory yard's upper end, on the railroad
WATCH_HOUSE = (-77.72995, 39.32350)
MARINE_POST = (-77.73050, 39.32400)  # in the yard above the engine house
LEE_POST = (-77.73003, 39.32352)  # "a slight elevation, about forty feet from the engine-house"
DOOR = (-77.72982, 39.32341)
PAYMASTER = (-77.73080, 39.32420)  # an office in the yard; placed
ESCAPE_SHENANDOAH = (-77.7345, 39.3222)
ESCAPE_HILL = (-77.7390, 39.3270)
POTOMAC_VA = (-77.7430, 39.3300)
POTOMAC_MD = (-77.7425, 39.3320)

# Behind Brown's wagon, the men walked "in couples, at some distance apart" (Anderson, order 3),
# close enough to read as one column; Cook and Tidd walked ahead as scouts. Seconds behind the
# wagon.
COLUMN = {"TIDD": -240, "COOK": -240, "KAGI": -10, "STEVENS": -10, "BROWN": 0,
          "WATSON": 4, "TAYLOR": 4, "OLIVER": 8, "W THOMPSON": 8, "J ANDERSON": 12,
          "D THOMPSON": 12, "HAZLETT": 16, "E COPPOC": 16, "COPELAND": 20, "LEARY": 20,
          "O ANDERSON": 24, "GREEN": 24, "NEWBY": 28, "LEEMAN": 28}
REAR_GUARD = ["OWEN", "B COPPOC", "MERIAM"]


def clock(ms_):
    """`DD HH:MM:SS` for operation milliseconds, the inverse of L."""
    t = START + dt.timedelta(milliseconds=ms_)
    return f"{t.day} {t:%H:%M:%S}"


def march(name):
    """From the farm at eight on Sunday evening to the Maryland end of the bridge."""
    lag = COLUMN[name]
    m = Mover(KENNEDY_FARM, T0).hold(clock(L("16 20:00") + lag * 1000))
    return m.along(ROAD, clock(L("16 22:25") + lag * 1000))


def into_town(m):
    """Over the bridge behind Kagi and Stevens, to the armory gate."""
    return m.hold("16 22:29").to(BRIDGE_MID, "16 22:33").to(BRIDGE_VA, "16 22:37") \
        .to(ARMORY_GATE, "16 22:42").hold("16 22:45")


def night(t):
    """Sunday night, from the bridge to the hostages' arrival at four."""
    t["KAGI"] = march("KAGI").hold("16 22:27").to(BRIDGE_MID, "16 22:30").hold("16 22:33") \
        .to(BRIDGE_VA, "16 22:37").to(ARMORY_GATE, "16 22:42").hold("16 22:55") \
        .along(TO_RIFLE_WORKS, "16 23:12")
    t["COPELAND"] = into_town(march("COPELAND")).hold("16 22:55") \
        .along(TO_RIFLE_WORKS, "16 23:12")
    t["BROWN"] = into_town(march("BROWN")).hold("16 22:55").along(TO_RIFLE_WORKS, "16 23:12") \
        .along(reverse(TO_RIFLE_WORKS), "16 23:30")
    for name in ("WATSON", "TAYLOR"):
        t[name] = march(name).hold("16 22:29").to(POTOMAC_POST, "16 22:33")
    for name in ("OLIVER", "W THOMPSON"):
        t[name] = into_town(march(name)).to(SHENANDOAH_BRIDGE, "16 22:55")
    for name in ("J ANDERSON", "D THOMPSON"):
        t[name] = into_town(march(name)).to(ENGINE_HOUSE, "16 22:46")
    for name in ("HAZLETT", "E COPPOC"):
        t[name] = into_town(march(name)).to(ARSENAL, "16 22:50")
    for name in ("NEWBY", "LEEMAN"):
        t[name] = into_town(march(name))
    # Cook and Tidd cut the line east on the way in, and the line west once the town is taken.
    for name in ("COOK", "TIDD"):
        t[name] = march(name).to(TELEGRAPH_EAST, "16 22:23:30").hold("16 22:25") \
            .to(BRIDGE_MD, "16 22:28").hold("16 22:29")
        into_town(t[name]).to(TELEGRAPH_WEST, "16 23:02").hold("16 23:08") \
            .to(ARMORY_GATE, "16 23:30")
    t["STEVENS"] = march("STEVENS").hold("16 22:27").to(BRIDGE_MID, "16 22:30") \
        .hold("16 22:33").to(BRIDGE_VA, "16 22:37").to(ARMORY_GATE, "16 22:42") \
        .hold("16 22:55").along(TO_RIFLE_WORKS, "16 23:12") \
        .along(reverse(TO_RIFLE_WORKS), "16 23:30")
    for name in ("O ANDERSON", "GREEN", "LEARY"):
        t[name] = into_town(march(name))
    country = ["STEVENS", "TIDD", "COOK", "O ANDERSON", "GREEN", "LEARY"]
    beall_air = PIKE.index(BEALL_AIR)
    allstadt = PIKE.index(ALLSTADT_HOUSE)
    for name in country:
        t[name].hold("16 23:40").along(PIKE, "17 01:29")
    # Green brings round Washington's carriage, with the farm wagon hitched behind (Washington).
    t["GREEN"].to(STABLE, "17 01:50").hold("17 02:00").to(BEALL_AIR, "17 02:12")
    for name in country:
        t[name].hold("17 02:25").along(reverse(PIKE[allstadt:beall_air + 1]), "17 02:55") \
            .hold("17 03:15").along(reverse(PIKE[:allstadt + 1]), "17 04:00")
    for name in REAR_GUARD:
        t[name] = Mover(KENNEDY_FARM, T0)


def wagon_to_maryland(t):
    """Washington's wagon to Maryland at five, for the arms at the farm (Starry, Byrne, Cook)."""
    byrne = ROAD.index(BYRNE_ROAD)
    school = ROAD.index(SCHOOLHOUSE_ROAD)
    for name in ("TIDD", "COOK", "LEEMAN"):
        t[name].hold("17 05:00").to(BRIDGE_VA, "17 05:02").to(BRIDGE_MD, "17 05:05") \
            .along(reverse(ROAD[byrne:]), "17 05:50")
    t["LEEMAN"].hold("17 08:15").along(ROAD[byrne:], "17 09:25").to(BRIDGE_VA, "17 09:29") \
        .to(ARMORY_GATE, "17 09:35")
    for name in ("TIDD", "COOK"):
        # Loading at the house and at the cabin across the road, where the pikes were.
        t[name].along(reverse(ROAD[:byrne + 1]), "17 06:15").to(CABIN, "17 06:40") \
            .hold("17 07:00").to(KENNEDY_FARM, "17 07:25").hold("17 07:30") \
            .to(CABIN, "17 07:55").hold("17 08:00").to(KENNEDY_FARM, "17 08:25") \
            .hold("17 08:30") \
            .along(ROAD[:school + 1], "17 09:10").to(SCHOOLHOUSE, "17 09:15")
    t["TIDD"].to(ROAD[school], "17 09:20").along(reverse(ROAD[:school + 1]), "17 10:00") \
        .hold("17 15:00").along(ROAD[:school + 1], "17 15:55").to(SCHOOLHOUSE, "17 16:00")
    for name in REAR_GUARD:
        t[name].hold("17 15:00").along(ROAD[:school + 1], "17 15:55") \
            .to(SCHOOLHOUSE, "17 16:00")
    t["COOK"].hold("17 16:05").to(ROAD[school], "17 16:10") \
        .along(ROAD[school:ROAD.index(LOCK_34_ROAD) + 1], "17 16:30").to(LOCK_34, "17 16:35") \
        .hold("17 17:00")


def express(t):
    """The eastbound express: held at the bridge from 1:25 to its release, then to Baltimore."""
    m = Mover(FROM_WEST[0], "17 01:15").along(FROM_WEST, "17 01:25").to(BRIDGE_VA, "17 01:27") \
        .to(STATION, "17 01:29").hold("17 06:00").to(BRIDGE_VA, "17 06:00:40") \
        .to(BRIDGE_MD, "17 06:05").along(EAST, "17 07:05").hold("17 08:00")
    em_index = TO_BALTIMORE.index(ELLICOTTS_MILLS)
    m.along(TO_BALTIMORE[:em_index + 1], "17 10:50").hold("17 11:00") \
        .along(TO_BALTIMORE[em_index:], "17 11:55")
    t["EXPRESS"] = m
    # Brown walks the train across the bridge ahead of it (Phelps).
    t["BROWN"].hold("17 05:55").to(BRIDGE_VA, "17 05:58").to(BRIDGE_MD, "17 06:04") \
        .to(BRIDGE_VA, "17 06:10").to(ARMORY_GATE, "17 06:13")


def monday_morning(t):
    """Posts at daylight: the bridge guard changes and Leary joins Kagi (Anderson, Villard)."""
    for name in ("WATSON", "TAYLOR"):
        t[name].hold("17 06:30").to(BRIDGE_VA, "17 06:33").to(ARMORY_GATE, "17 06:36")
    for name in ("OLIVER", "W THOMPSON"):
        t[name].hold("17 06:30").to(BRIDGE_VA, "17 06:36").to(POTOMAC_TOWN_POST, "17 06:38")
    t["NEWBY"].hold("17 06:30").to(BRIDGE_VA, "17 06:34").to(POTOMAC_TOWN_POST, "17 06:36")
    for name in ("O ANDERSON", "GREEN"):
        t[name].hold("17 06:30").to(ARSENAL, "17 06:33")
    t["E COPPOC"].hold("17 06:30").to(ARMORY_GATE, "17 06:33")
    t["LEARY"].hold("17 06:30").along(TO_RIFLE_WORKS, "17 06:45")
    t["CITIZENS"] = Mover((-77.7330, 39.3242), "17 06:50").hold("17 14:30") \
        .to((-77.7312, 39.3238), "17 14:40")


def noon(t):
    """The Jefferson Guards take the bridge; Brown withdraws to the engine house."""
    t["JEFFERSON GUARDS"] = Mover(CHARLES_TOWN, "17 10:00").to(HALLTOWN_RAIL, "17 10:30") \
        .to(BOLIVAR_HEIGHTS, "17 11:00").to(CROSSING_VA, "17 11:20") \
        .to(CROSSING_MD, "17 11:30").along(ROAD[13:], "17 12:00").to(BRIDGE_VA, "17 12:05") \
        .to(STATION, "17 12:08")
    t["BOTTS COMPANY"] = Mover(CHARLES_TOWN, "17 10:00").to(HALLTOWN_RAIL, "17 10:30") \
        .to(BOLIVAR_HEIGHTS, "17 11:00").hold("17 11:45").to(GALT_HOUSE, "17 12:15")
    t["NEWBY"].hold("17 12:01").to(NEWBY_SPOT, "17 12:06")
    for name in ("OLIVER", "W THOMPSON"):
        t[name].hold("17 12:01").to(ARMORY_GATE, "17 12:05")
    t["OLIVER"].to(ENGINE_HOUSE, "17 12:07")
    for name in ("BROWN", "WATSON", "TAYLOR", "E COPPOC", "STEVENS", "LEEMAN"):
        t[name].hold("17 12:04").to(ENGINE_HOUSE, "17 12:07")
    t["GREEN"].hold("17 12:12").to(ENGINE_HOUSE, "17 12:16")
    # Thompson goes out with a flag and is taken to the Wager House; then Stevens and Watson.
    t["W THOMPSON"].hold("17 12:17").to(STATION, "17 12:24")
    for name in ("STEVENS", "WATSON"):
        t[name].hold("17 12:28").to(TRUCE_SPOT, "17 12:31").hold("17 12:32")
    t["WATSON"].to(ENGINE_HOUSE, "17 12:37")
    t["STEVENS"].to(STATION, "17 12:45")
    t["LEEMAN"].hold("17 12:46").to(UPPER_YARD, "17 12:53").to(LEEMAN_ISLET, "17 12:59")


def afternoon(t):
    """The rifle works, Beckham and Thompson, the Martinsburg company, and dusk."""
    t["IRWIN PARTY"] = Mover((-77.7420, 39.3236), "17 14:30").to((-77.7400, 39.3230), "17 14:45") \
        .to(RIFLE_WORKS, "17 15:00")
    for name in ("KAGI", "LEARY", "COPELAND"):
        t[name].hold("17 15:01").to(KAGI_ROCK, "17 15:08")
    t["COPELAND"].hold("17 15:20").to(COPELAND_TAKEN, "17 15:40")
    t["LEARY"].hold("17 15:20").to((-77.7385, 39.3215), "17 15:30")
    t["W THOMPSON"].hold("17 15:00").to((-77.72840, 39.32330), "17 15:04")
    t["MARTINSBURG COMPANY"] = Mover(FROM_WEST[0], "17 14:20").along(FROM_WEST[:4], "17 14:40") \
        .to(WATCH_HOUSE, "17 15:00").hold("17 15:10").to(UPPER_YARD, "17 15:20")
    for name in ("HAZLETT", "O ANDERSON"):
        t[name].hold("17 17:30").to(ESCAPE_SHENANDOAH, "17 17:45").to(ESCAPE_HILL, "17 18:30") \
            .to(POTOMAC_VA, "17 19:00").to(POTOMAC_MD, "17 19:30").to(SCHOOLHOUSE, "18 02:00")


def reinforcements(t):
    """Frederick's companies at dusk; Baltimore's, the marines and Lee by night (B&O file)."""
    sandy_hook = reverse(EAST[SANDY_HOOK_TRACK:])
    to_relay = reverse(TO_BALTIMORE)
    relay = to_relay.index(RELAY)
    t["FREDERICK MILITIA"] = Mover(FREDERICK, "17 15:45").to(MONOCACY, "17 16:05") \
        .along(sandy_hook, "17 17:20").to(BRIDGE_MD, "17 17:30").to(BRIDGE_VA, "17 17:35") \
        .to(STATION, "17 17:40")
    t["BALTIMORE MILITIA"] = Mover(CAMDEN_STATION, "17 16:00").along(to_relay[:relay + 1],
                                                                     "17 16:30")
    t["MARINES"] = Mover(WASHINGTON_DEPOT, "17 15:30").along(WASHINGTON_BRANCH, "17 16:55")
    for name in ("BALTIMORE MILITIA", "MARINES"):
        t[name].hold("17 17:05").along(to_relay[relay:relay + 2], "17 17:31") \
            .along(to_relay[relay + 1:], "17 20:10").along(sandy_hook, "17 22:45") \
            .to(SANDY_HOOK, "17 22:50")
    for name in ("LEE", "STUART"):
        t[name] = Mover(RELAY, "17 19:45").along(to_relay[relay:], "17 21:50") \
            .along(sandy_hook, "17 23:00").to(SANDY_HOOK, "17 23:05")
    for name in ("MARINES", "LEE", "STUART"):
        t[name].hold("17 23:10").to(BRIDGE_MD, "17 23:40").to(BRIDGE_VA, "17 23:45") \
            .to(ARMORY_GATE, "17 23:47")
    t["MARINES"].to(MARINE_POST, "17 23:52").hold("18 06:59").to(WATCH_HOUSE, "18 07:01")
    for name in ("LEE", "STUART"):
        t[name].to(LEE_POST, "17 23:50")
    t["STUART"].hold("18 06:56:30").to(DOOR, "18 06:58").hold("18 07:00") \
        .to(LEE_POST, "18 07:00:30")
    t["STORMING PARTY"] = Mover(MARINE_POST, "18 06:30").hold("18 07:00:30") \
        .to(DOOR, "18 07:01").hold("18 07:02").to(ENGINE_HOUSE, "18 07:02:30") \
        .hold("18 07:04").to(DOOR, "18 07:06")
    # Greene: Brown "carried … up to the paymaster's office"; Coppoc and Green led out.
    t["BROWN"].hold("18 07:08").to(PAYMASTER, "18 07:14")
    for name in ("E COPPOC", "GREEN"):
        t[name].hold("18 07:03:30").to(LEE_POST, "18 07:05:30")
    # The Baltimore companies "did not enter the town from Sandy Hook until morning" (Villard).
    t["BALTIMORE MILITIA"].hold("18 07:10").to(BRIDGE_MD, "18 07:38") \
        .to(BRIDGE_VA, "18 07:42").to(STATION, "18 07:45")


# (entity, time, condition) as the sources report them; see build/evidence/ for the times.
CONDITIONS = [
    ("WIRE EAST", "16 22:24", "destroyed"), ("WIRE WEST", "16 23:05", "destroyed"),
    ("NEWBY", "17 12:06", "destroyed"), ("STEVENS", "17 12:32", "damaged"),
    ("WATSON", "17 12:32", "damaged"), ("LEEMAN", "17 12:59:30", "destroyed"),
    ("W THOMPSON", "17 15:04", "destroyed"), ("KAGI", "17 15:08", "destroyed"),
    ("LEARY", "17 15:08", "damaged"), ("TAYLOR", "17 16:30", "destroyed"),
    ("OLIVER", "17 16:30", "damaged"), ("OLIVER", "18 02:00", "destroyed"),
    ("WIRE EAST", "18 00:00", "fully_capable"), ("J ANDERSON", "18 07:02:50", "destroyed"),
    ("D THOMPSON", "18 07:02:50", "destroyed"), ("BROWN", "18 07:02:40", "damaged"),
]

# Where a track ends with the man out of the sources' sight: they escaped.
ESCAPED = {"COOK": "17 17:00", "TIDD": "17 17:45", "OWEN": "17 17:45", "B COPPOC": "17 17:45",
           "MERIAM": "17 17:45", "HAZLETT": "18 02:00", "O ANDERSON": "18 02:00"}


def plan():
    """(tracks by entity, conditions, escapes): every track runs to the end unless it escapes."""
    movers = {}
    night(movers)
    express(movers)
    wagon_to_maryland(movers)
    monday_morning(movers)
    noon(movers)
    afternoon(movers)
    reinforcements(movers)
    return {k: m.track for k, m in movers.items()}, CONDITIONS, ESCAPED
