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


def entities():
    rows = [(e, FRIENDLY_FIGHTER) for e in P38S]
    rows += [(e, HOSTILE_BOMBER) for e in BETTYS]
    rows += [(e, HOSTILE_FIGHTER) for e in ZEROS]
    return [{"id": e, "sidc": s, "camera": False} for e, s in rows]


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
