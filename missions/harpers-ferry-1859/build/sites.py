"""Clock, the sourced places of 1859 and the order of battle for 16–18 October 1859.

The clock is Harpers Ferry local mean time. In 1859 every town kept its own; the records' times
are as their writers gave them, and the few minutes between the towns along the railroad (Monocacy
1.4 min ahead, Baltimore 4.4 min ahead of Harpers Ferry) are not corrected, being finer than the
records themselves.

Places are where they stood in 1859, not where today's map puts their successors: the engine house
at the B&O's 1895 obelisk, which marks its original site under the railroad's later embankment; the
B&O's covered bridge on the line of the pier ruins at the Point, not the 1894 bridge upstream; the
station and Wager House at the town end of that bridge.
"""
import datetime as dt

OP = "harpers-ferry-1859"
LMT_S = -18655  # 77°43′47″ W: Harpers Ferry local mean time, UTC−5:10:55
LOCAL = dt.timezone(dt.timedelta(seconds=LMT_S))
START = dt.datetime(1859, 10, 16, 14, 30, tzinfo=LOCAL)


def L(clock):
    """Operation milliseconds for `DD HH:MM[:SS]`, a day of October 1859 and a Harpers Ferry
    local mean time."""
    day, hms = clock.split(" ")
    parts = [float(p) for p in hms.split(":")]
    h, m, s = (parts + [0.0])[:3]
    t = dt.datetime(1859, 10, int(day), int(h), int(m), tzinfo=LOCAL) + dt.timedelta(seconds=s)
    return int(round((t - START).total_seconds() * 1000))


def unix_ms():
    return int(START.timestamp() * 1000)


DURATION = L("18 07:45")

# (lon, lat), WGS84.
KENNEDY_FARM = (-77.71556, 39.37972)  # NHL nomination form, as Wikipedia
PLAQUE = (-77.71473, 39.37998)  # HMdb 151957, "In Memoriam" plaque
SCHOOLHOUSE = (-77.7380, 39.3420)  # estimated; see the schoolhouse-site dispute
BRIDGE_MD = (-77.72631, 39.32392)  # Maryland end of the pier-ruin line (OSM way 549095499)
BRIDGE_VA = (-77.72829, 39.32318)  # town end of the same line
BRIDGE_MID = (-77.72730, 39.32355)
STATION = (-77.72900, 39.32335)  # B&O station and Wager House, at the bridge's town end
ARMORY_GATE = (-77.72945, 39.32330)  # "about 60 yards" from the bridge (Starry)
ENGINE_HOUSE = (-77.729889, 39.323456)  # B&O obelisk of 1895, OSM node 356535602
ARSENAL = (-77.72981, 39.32280)  # Arsenal Square ruins, OSM way 1154283641
GALT_HOUSE = (-77.72870, 39.32280)  # on the Shenandoah side of the Point; approximate
SHENANDOAH_BRIDGE = (-77.72805, 39.32210)  # middle of the later piers on the 1859 crossing
WATER_STATION = (-77.73000, 39.32370)  # "on the trusseling just above the hotel" (Chambers)
RIFLE_WORKS = (-77.739888, 39.322078)  # Hall's Island, the pulp-mill ruins on the Rifle Factory
BOLIVAR = (-77.7420, 39.3236)
ALLSTADT_HOUSE = (-77.755683, 39.316258)  # NRHP, Allstadt House and Ordinary
BEALL_AIR = (-77.812222, 39.315278)  # NRHP, Lewis W. Washington's house
CHARLES_TOWN = (-77.859811, 39.289106)  # Jefferson County courthouse
SANDY_HOOK = (-77.70528, 39.32861)
MONOCACY = (-77.39065, 39.37188)  # Frederick Junction, the 1859 "Monocacy"
FREDERICK = (-77.4105, 39.4143)
ELLICOTTS_MILLS = (-76.79528, 39.26722)  # the 1830 station, extant
RELAY = (-76.71075, 39.22394)
CAMDEN_STATION = (-76.61955, 39.28346)  # B&O headquarters, Baltimore
WASHINGTON_DEPOT = (-77.0105, 38.8960)  # B&O Washington Branch depot, New Jersey Ave; approx.
MARTINSBURG = (-77.9636, 39.4568)

# Men, as dismounted individuals (MIL-STD-2525D symbol set 27, entity 110101), leaders marked
# with the leadership amplifier 71; units keep the 2525C unit symbols with their echelons.
FRIENDLY = "10032700001101010000"
COMMANDER = "10032700711101010000"
HOSTILE_MAN = "10062700001101010000"
HOSTILE_LEADER = "10062700711101010000"
FRIENDLY_TEAM = "SFGPUCI----A---"
FRIENDLY_PLATOON = "SFGPUCI----D---"
HOSTILE = "SHGPUCI--------"
HOSTILE_SQUAD = "SHGPUCI----B---"
HOSTILE_HQ = "SHGPUCI---A----"
HOSTILE_COMPANY = "SHGPUCI----E---"
HOSTILE_BATTALION = "SHGPUCI----F---"
TRAIN = "SNGPEVT--------"
TELEGRAPH = "SNGPIUT---H----"
FRIENDLY_SITE = "SFGPIB----H----"
NEUTRAL_SITE = "SNGPIB----H----"

# Brown's men by their ranks in Anderson's eleven orders (1861) and the Chatham convention's
# offices; ages are the Kennedy Farm plaque's.
RAIDERS = {
    "BROWN": "John Brown, Commander-in-Chief, 59",
    "KAGI": "John Henry Kagi, Adjutant General, 24",
    "STEVENS": "Aaron D. Stevens, Captain, 28",
    "WATSON": "Watson Brown, Captain, 20",
    "TAYLOR": "Stewart Taylor, 22",
    "OLIVER": "Oliver Brown, Captain, 19",
    "W THOMPSON": "William Thompson, Captain, 26",
    "J ANDERSON": "Jeremiah G. Anderson, Lieutenant, 26",
    "D THOMPSON": "Dauphin Thompson, 21",
    "HAZLETT": "Albert Hazlett, Lieutenant, 22",
    "E COPPOC": "Edwin Coppoc, 24",
    "COPELAND": "John A. Copeland Jr., 25",
    "COOK": "John E. Cook, Captain, 29",
    "TIDD": "Charles P. Tidd, Captain, 25",
    "O ANDERSON": "Osborne P. Anderson, 29",
    "GREEN": "Shields Green, 23",
    "LEARY": "Lewis S. Leary, 24",
    "NEWBY": "Dangerfield Newby, 44",
    "LEEMAN": "William H. Leeman, 20",
    "OWEN": "Owen Brown, Captain, 34",
    "B COPPOC": "Barclay Coppoc, 20",
    "MERIAM": "Francis J. Meriam, 21",
}

ARMY = "PROVISIONAL ARMY"
# Declared formations as (id, name, symbol, members, parent): each man under the post Brown gave
# him on Sunday afternoon (Anderson's orders); Newby and Leeman, whom the orders do not name, with
# Brown. The Potomac-bridge pair follows the orders; see the potomac-bridge-guard dispute.
FORMATIONS = [
    # Shortened on the map, where a folded column reads "Provisional US Army ×17".
    (ARMY, "Provisional US Army", FRIENDLY_PLATOON, [], None),
    ("ARMORY PARTY", "Brown's party at the armory", FRIENDLY_TEAM,
     ["BROWN", "J ANDERSON", "D THOMPSON", "HAZLETT", "E COPPOC", "NEWBY", "LEEMAN"], ARMY),
    ("BRIDGE GUARDS", "The bridge guards", FRIENDLY_TEAM,
     ["WATSON", "TAYLOR", "OLIVER", "W THOMPSON"], ARMY),
    ("RIFLE WORKS PARTY", "Kagi's party at the rifle works", FRIENDLY_TEAM,
     ["KAGI", "COPELAND"], ARMY),
    ("STEVENS PARTY", "Stevens's party in the country", FRIENDLY_TEAM,
     ["STEVENS", "O ANDERSON", "GREEN", "LEARY"], ARMY),
    # Ahead of the march to cut the wires (order 4), then with Stevens.
    ("COOK AND TIDD", "Cook and Tidd", FRIENDLY_TEAM, ["COOK", "TIDD"], "STEVENS PARTY"),
    ("REAR GUARD", "Owen Brown's rear guard", FRIENDLY_TEAM, ["OWEN", "B COPPOC", "MERIAM"],
     ARMY),
    ("VIRGINIA MILITIA", "Virginia militia and volunteers", HOSTILE_BATTALION, [], None),
    ("MARYLAND MILITIA", "Maryland militia", HOSTILE_BATTALION, [], None),
    ("US FORCES", "United States forces", HOSTILE_HQ, [], None),
]

# (id, name, symbol, kind, parent)
OPPONENTS = [
    ("CITIZENS", "Armed citizens of Harpers Ferry", HOSTILE, "citizens", None),
    ("JEFFERSON GUARDS", "Jefferson Guards, Charlestown (Capt. J. W. Rowan)", HOSTILE_COMPANY,
     "company", "VIRGINIA MILITIA"),
    ("BOTTS COMPANY", "Charlestown citizens' company (Capt. Botts)", HOSTILE_COMPANY,
     "company", "VIRGINIA MILITIA"),
    ("IRWIN PARTY", "Starry's party under Irwin", HOSTILE, "citizens", None),
    ("MARTINSBURG COMPANY", "Martinsburg company, B&O men (Capt. E. G. Alburtis)",
     HOSTILE_COMPANY, "company", "VIRGINIA MILITIA"),
    ("FREDERICK MILITIA", "Three Frederick companies (Col. Shriver)", HOSTILE_COMPANY, "company",
     "MARYLAND MILITIA"),
    ("BALTIMORE MILITIA", "Five Baltimore companies (Gen. Charles C. Edgerton)", HOSTILE_COMPANY,
     "company", "MARYLAND MILITIA"),
    ("MARINES", "U.S. Marines from the Washington Navy Yard (Lt. Israel Greene)",
     HOSTILE_COMPANY, "company", "US FORCES"),
    ("STORMING PARTY", "Greene's storming party of twelve marines", HOSTILE_SQUAD, "party",
     "US FORCES"),
    ("LEE", "Bvt. Col. Robert E. Lee, commanding", HOSTILE_LEADER, "officer", "US FORCES"),
    ("STUART", "Lt. J. E. B. Stuart, Lee's aide", HOSTILE_MAN, "officer", "US FORCES"),
]

TRAINS = [
    ("EXPRESS", "B&O express, Wheeling to Baltimore (conductor A. J. Phelps)", TRAIN, "train"),
]

# (id, symbol, name, kind, point, bound m, source)
FIXED = [
    ("KENNEDY FARM", FRIENDLY_SITE, "Kennedy farm, the Provisional Army's headquarters", "site",
     KENNEDY_FARM, 50.0, "nhl-kennedy-farm"),
    ("SCHOOLHOUSE", FRIENDLY_SITE, "Schoolhouse, the arms depot of 17 October (site estimated)",
     "site", SCHOOLHOUSE, 1500.0, "reconstruction-estimate"),
    ("ENGINE HOUSE", NEUTRAL_SITE, "Armory fire-engine house and watch-house (original site)",
     "site", ENGINE_HOUSE, 15.0, "osm"),
    ("ARSENAL", NEUTRAL_SITE, "U.S. Arsenal", "site", ARSENAL, 40.0, "osm"),
    ("RIFLE WORKS", NEUTRAL_SITE, "Hall's rifle works, U.S. Rifle Factory", "site", RIFLE_WORKS,
     150.0, "osm"),
    ("STATION", NEUTRAL_SITE, "B&O station and Wager House (site)", "site", STATION, 40.0,
     "mason-report"),
    ("B&O BRIDGE", NEUTRAL_SITE, "B&O covered bridge over the Potomac (1859 line)", "site",
     BRIDGE_MID, 30.0, "osm"),
    ("SHENANDOAH BRIDGE", NEUTRAL_SITE, "Shenandoah bridge (1859 crossing)", "site",
     SHENANDOAH_BRIDGE, 80.0, "osm"),
    ("BEALL-AIR", NEUTRAL_SITE, "Beall-Air, Col. Lewis W. Washington's house", "site", BEALL_AIR,
     50.0, "nrhp"),
    ("ALLSTADT HOUSE", NEUTRAL_SITE, "John H. Allstadt's house", "site", ALLSTADT_HOUSE, 50.0,
     "nrhp"),
    ("MONOCACY", NEUTRAL_SITE, "Monocacy station, the first open telegraph east", "site",
     MONOCACY, 300.0, "osm"),
    ("CAMDEN STATION", NEUTRAL_SITE, "Camden Station, the B&O's offices in Baltimore", "site",
     CAMDEN_STATION, 100.0, "osm"),
]

# The two wires Cook and Tidd cut, where the replay places the cuts; see the telegraph-cut dispute.
TELEGRAPH_EAST = (-77.7245, 39.3243)
TELEGRAPH_WEST = (-77.7360, 39.3266)
WIRES = [
    ("WIRE EAST", "Telegraph east, along the B&O on the Maryland side", TELEGRAPH_EAST),
    ("WIRE WEST", "Telegraph west, along the B&O on the Virginia side", TELEGRAPH_WEST),
]


def entities():
    parent = {m: group for group, _, _, members, _ in FORMATIONS for m in members}
    out = [{"id": e, "sidc": COMMANDER if e == "BROWN" else FRIENDLY, "camera": False,
            "name": name, "kind": "person", "parent": parent[e]} for e, name in RAIDERS.items()]
    for id_, name, sidc, kind, up in OPPONENTS:
        row = {"id": id_, "sidc": sidc, "camera": False, "name": name, "kind": kind}
        if up:
            row["parent"] = up
        out.append(row)

    def strength(group):
        own = next(members for g, _, _, members, _ in FORMATIONS if g == group)
        return len(own) + sum(strength(g) for g, _, _, _, up in FORMATIONS if up == group)

    for group, name, sidc, members, up in FORMATIONS:
        row = {"id": group, "sidc": sidc, "camera": False, "name": name, "kind": "formation"}
        if members or any(u == group for *_, u in FORMATIONS):
            row["quantity"] = strength(group)
        if up:
            row["parent"] = up
        out.append(row)
    out += [{"id": id_, "sidc": sidc, "camera": False, "name": name, "kind": kind}
            for id_, name, sidc, kind in TRAINS]
    out += [{"id": id_, "sidc": TELEGRAPH, "camera": False, "name": name, "kind": "telegraph"}
            for id_, name, _ in WIRES]
    out += [{"id": id_, "sidc": sidc, "camera": False, "name": name, "kind": kind}
            for id_, sidc, name, kind, *_ in FIXED]
    return out
