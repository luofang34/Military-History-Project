"""Clock, sourced fixed sites and the order of battle for 18 April 1943."""
import datetime as dt

OP = "operation-vengeance"
LOCAL = dt.timezone(dt.timedelta(hours=11))
START = dt.datetime(1943, 4, 18, 7, 24, 30, tzinfo=LOCAL)


def L(hms):
    """Operation milliseconds for a Henderson Field (UTC+11) clock time `HH:MM[:SS.s]`."""
    parts = [float(p) for p in hms.split(":")]
    h, m, s = (parts + [0.0])[:3]
    t = dt.datetime(1943, 4, 18, int(h), int(m), 0, tzinfo=LOCAL) + dt.timedelta(seconds=s)
    return int(round((t - START).total_seconds() * 1000))


DURATION = L("10:05:00")

# (lon, lat). Sources: Wikipedia airfield articles, Pacific Wrecks site pages.
FIGHTER_TWO = (160.0108, -9.4261)
LAKUNAI = (152.183, -4.217)
KAHILI = (155.6836, -6.7301)
BALLALE = (155.8867, -6.9908)
BANIKA = (159.1939, -9.0981)
PEARL_HARBOR = (-157.95, 21.35)
CRASH_T1_323 = (155.55228, -6.78608)
MOILA = (155.58679, -6.84710)
# "About 100 m offshore at Moila Point" (Pacific Wrecks), placed 150 m off the OSM
# shoreline; the Pacific Wrecks point label lies ~1 km inland. The wreck has not been found.
DITCH_T1_326 = (155.586, -6.8567)

FRIENDLY_FIGHTER = "SFAPMFF--------"
HOSTILE_BOMBER = "SHAPMFB--------"
HOSTILE_FIGHTER = "SHAPMFF--------"

# Cover-flight roster order of the 13th Fighter Command report, read as three flights of four.
MITCHELL_FLIGHT = ["MITCHELL", "JACOBSON", "CANNING", "GOERKE"]
KITTEL_FLIGHT = ["KITTEL", "WHITTAKER", "AMES", "GRAEBNER"]
ANGLIN_FLIGHT = ["ANGLIN", "SMITH", "LONG", "STRATTON"]
COVER = MITCHELL_FLIGHT + KITTEL_FLIGHT + ANGLIN_FLIGHT
KILLER = ["LANPHIER", "BARBER", "HOLMES", "HINE"]
ABORTS = ["MOORE", "MCLANAHAN"]
P38S = COVER + KILLER + ABORTS
YAMAMOTO = "T1-323 YAMAMOTO"
UGAKI = "T1-326 UGAKI"
BETTYS = [YAMAMOTO, UGAKI]
ZERO_1 = ["MORISAKI", "TSUJINOUE", "SUGITA"]
ZERO_2 = ["HIDAKA", "OKAZAKI", "YANAGIYA"]
ZEROS = ZERO_1 + ZERO_2
ENGAGED = set(KILLER + BETTYS + ZEROS)


# Pilots' names follow the 13th Fighter Command roster and the Japanese escort accounts;
# Japanese names are family name first.
NAMES = {
    "MITCHELL": "John W. Mitchell", "JACOBSON": "Julius Jacobson", "CANNING": "Douglas S. Canning",
    "GOERKE": "Delton C. Goerke", "KITTEL": "Louis R. Kittel", "WHITTAKER": "Gordon Whittaker",
    "AMES": "Roger J. Ames", "GRAEBNER": "Lawrence A. Graebner", "ANGLIN": "Everett H. Anglin",
    "SMITH": "William E. Smith", "LONG": "Albert R. Long", "STRATTON": "Eldon E. Stratton",
    "LANPHIER": "Thomas G. Lanphier Jr.", "BARBER": "Rex T. Barber", "HOLMES": "Besby F. Holmes",
    "HINE": "Raymond K. Hine", "MOORE": "Joseph F. Moore", "MCLANAHAN": "James D. McLanahan",
    YAMAMOTO: "T1-323 · Adm. Yamamoto Isoroku", UGAKI: "T1-326 · V.Adm. Ugaki Matome",
    "MORISAKI": "Morisaki Takeshi", "TSUJINOUE": "Tsujinoue Toyomitsu", "SUGITA": "Sugita Shōichi",
    "HIDAKA": "Hidaka Yoshimi", "OKAZAKI": "Okazaki", "YANAGIYA": "Yanagiya Kenji",
}

# Declared formations as (id, name, symbol, members, parent); members are drawn as one
# symbol when they overlap on screen, under the closest formation they share.
FORMATIONS = [
    ("COVER FLIGHT", "Mitchell's cover flight", FRIENDLY_FIGHTER, [], None),
    ("MITCHELL FLIGHT", "Mitchell's flight", FRIENDLY_FIGHTER, MITCHELL_FLIGHT, "COVER FLIGHT"),
    ("KITTEL FLIGHT", "Kittel's flight", FRIENDLY_FIGHTER, KITTEL_FLIGHT, "COVER FLIGHT"),
    ("ANGLIN FLIGHT", "Anglin's flight", FRIENDLY_FIGHTER, ANGLIN_FLIGHT, "COVER FLIGHT"),
    # As briefed, before Moore and McLanahan dropped out and Holmes and Hine replaced them.
    ("ATTACK SECTION", "Lanphier's attack section", FRIENDLY_FIGHTER, ABORTS, None),
    ("LANPHIER ELEMENT", "Lanphier and Barber", FRIENDLY_FIGHTER, ["LANPHIER", "BARBER"],
     "ATTACK SECTION"),
    ("HOLMES ELEMENT", "Holmes and Hine", FRIENDLY_FIGHTER, ["HOLMES", "HINE"],
     "ATTACK SECTION"),
    ("BETTYS", "705th Kōkūtai G4M1 pair", HOSTILE_BOMBER, BETTYS, None),
    ("ESCORT", "204th Kōkūtai escort", HOSTILE_FIGHTER, [], None),
    ("ZERO SECTION 1", "Morisaki's section", HOSTILE_FIGHTER, ZERO_1, "ESCORT"),
    ("ZERO SECTION 2", "Hidaka's section", HOSTILE_FIGHTER, ZERO_2, "ESCORT"),
]


def entities():
    parent = {member: group for group, _, _, members, _ in FORMATIONS for member in members}
    rows = [(e, FRIENDLY_FIGHTER, "P-38G") for e in P38S]
    rows += [(e, HOSTILE_BOMBER, "G4M1") for e in BETTYS]
    rows += [(e, HOSTILE_FIGHTER, "A6M") for e in ZEROS]
    out = [{"id": e, "sidc": s, "camera": False, "name": NAMES[e], "kind": k, "parent": parent[e]}
           for e, s, k in rows]

    def strength(group):
        children = [g for g, _, _, _, up in FORMATIONS if up == group]
        own = next(members for g, _, _, members, _ in FORMATIONS if g == group)
        return len(own) + sum(strength(child) for child in children)

    for group, name, sidc, _, up in FORMATIONS:
        row = {"id": group, "sidc": sidc, "camera": False, "name": name, "kind": "formation",
               "quantity": strength(group)}
        if up:
            row["parent"] = up
        out.append(row)
    return out


def unix_ms():
    return int(START.timestamp() * 1000)


FT_M = 0.3048
WAVE_TOP_M = 20 * FT_M  # "10 to 30 feet" (13th Fighter Command report)
BETTY_CRUISE_M = 6500 * FT_M
BETTY_SIGHTED_M = 4500 * FT_M
ZERO_ABOVE_M = 1500 * FT_M
COVER_TOP_M = 18000 * FT_M

# Formation slots: (right_m, ahead_m) relative to Mitchell's lead track.
SLOTS = {
    "MITCHELL": (0, 0), "JACOBSON": (140, -90), "CANNING": (-140, -90), "GOERKE": (280, -180),
    "KITTEL": (-650, -350), "WHITTAKER": (-510, -440), "AMES": (-790, -440),
    "GRAEBNER": (-930, -530),
    "ANGLIN": (650, -350), "SMITH": (790, -440), "LONG": (510, -440), "STRATTON": (930, -530),
    "LANPHIER": (0, -800), "BARBER": (140, -890), "HOLMES": (-140, -890), "HINE": (280, -980),
    "MOORE": (-280, -980),
}

# Take-off order is not sourced: Mitchell's flight first, the attack section last.
TAKEOFF_ORDER = [
    "MITCHELL", "JACOBSON", "CANNING", "GOERKE", "KITTEL", "WHITTAKER", "AMES", "GRAEBNER",
    "ANGLIN", "SMITH", "LONG", "STRATTON", "LANPHIER", "BARBER", "MCLANAHAN", "MOORE",
    "HOLMES", "HINE",
]
