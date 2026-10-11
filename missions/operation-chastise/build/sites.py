"""Clock, sourced fixed sites and the order of battle for the night of 16/17 May 1943.

British Double Summer Time and German summer time were both UTC+2 that night (tzdb
Europe/London BDST, Europe/Berlin CEST), so one clock serves both sides. Points are (lon, lat).
"""
import datetime as dt

OP = "operation-chastise"
ZONE = dt.timezone(dt.timedelta(hours=2))
START = dt.datetime(1943, 5, 16, 21, 25, 0, tzinfo=ZONE)


def L(hms):
    """Operation milliseconds for a BDST clock time `HH:MM[:SS]`; hours before noon fall on
    17 May."""
    parts = [float(p) for p in hms.split(":")]
    h, m, s = (parts + [0.0])[:3]
    day = 17 if h < 12 else 16
    t = dt.datetime(1943, 5, day, int(h), int(m), 0, tzinfo=ZONE) + dt.timedelta(seconds=s)
    return int(round((t - START).total_seconds() * 1000))


def unix_ms():
    return int(START.timestamp() * 1000)


DURATION = L("06:20:00")

# England. Scampton from Wikipedia; it was a grass field until concrete runways were laid
# from August 1943. 5 Group HQ at St Vincents, Grantham (road geocode, ±150 m).
SCAMPTON = (-0.55083, 53.30778)
GRANTHAM = (-0.6293, 52.9051)

# Dam crests from OpenStreetMap geometry (±20 m): (centre, crest axis bearing, attack heading).
# The attack heading is perpendicular to the crest, toward the water face, except at the Sorpe,
# where the run was along the crest and the mine was not spun.
MOHNE = (8.05892, 51.48985)
MOHNE_AXIS, MOHNE_RUN = 53.0, 323.0
EDER = (9.0586, 51.1835)
EDER_AXIS, EDER_RUN = 34.0, 124.0
SORPE = (7.96872, 51.35181)
SORPE_AXIS = 132.0
ENNEPE = (7.4092, 51.2415)
ENNEPE_AXIS = 91.0
BEVER = (7.37026, 51.14183)
LISTER = (7.83772, 51.09413)
DIEMEL = (8.72797, 51.37788)

# Möhne valley (OSM / Nominatim, ±1 km for village centroids).
POWER_STATION = (8.05425, 51.49046)
GUNNE = (8.0498, 51.4992)
HIMMELPFORTEN = (8.0076, 51.4925)
NIEDERENSE = (7.9971, 51.4934)
NEHEIM_CAMP = (7.9697, 51.4573)  # Möhnewiesen forced-labour camp memorial
WICKEDE = (7.870, 51.496)
FRONDENBERG = (7.7618, 51.4713)
SCHWERTE = (7.567, 51.446)
# Down the Eder from the dam (OpenStreetMap).
AFFOLDERN = (9.0855, 51.1667)
BERGHEIM_EDER = (9.1364, 51.1689)
WEGA = (9.1757, 51.1304)
FRITZLAR = (9.2645, 51.1537)
WABERN = (9.3292, 51.0941)
WALDECK = (9.05538, 51.20381)
HAMMERBERG = (9.04810, 51.19147)
LANGSCHEID = (7.9575, 51.3585)

# Crash sites: dambustersblog's memorials and nearest access points (S4), not impact points.
CRASH = {
    "AJ-M": ((7.996486, 51.535276), 1500.0, "memorial near Ostönnen"),
    "AJ-B": ((6.868116, 51.808419), 300.0, "field behind the Marbeck memorial"),
    "AJ-E": ((6.442784, 51.79662), 500.0, "Haldern memorial"),
    "AJ-Z": ((6.276442, 51.8565), 500.0, "Klein-Netterden, end of Flasserweg"),
    "AJ-S": ((4.926065, 51.577043), 1500.0, "Gilze-Rijen airfield"),
    "AJ-A": ((4.6050, 52.5450), 2000.0, "sea off Castricum aan Zee"),
    "AJ-C": ((7.792254, 51.724373), 1500.0, "Heessen, north of Hamm"),
    "AJ-K": ((4.98, 53.18), 10_000.0, "Waddenzee west of Harlingen"),
}

LANCASTER = "SFAPMFB--------"
DAM = "SHGPIUED--H----"
POWER = "SHGPIUE---H----"
FLAK = "SHGPUCDG---E---"  # light air-defence guns, battery
AIRFIELD = "SFGPIBA---H----"
HQ = "SFGPUCVF--A----"  # fixed-wing aviation HQ; no echelon, as mapping an RAF group is a judgement
FLOOD = "10044000001702020000"  # APP-6D activity, natural event: flood (170202), neutral

# 617 Squadron, as listed in the ORB (AIR 27/2128): code, serial, captain, wave, section.
# Young's serial is ED887/G and McCarthy's ED825/G; the ORB transcript reads ED877 and ED923.
CREWS = [
    ("AJ-G", "ED932/G", "W/Cdr Guy Gibson", 1, 1),
    ("AJ-M", "ED925/G", "F/Lt John Hopgood", 1, 1),
    ("AJ-P", "ED909/G", "F/Lt Mick Martin", 1, 1),
    ("AJ-A", "ED887/G", "S/Ldr Melvin Young", 1, 2),
    ("AJ-J", "ED906/G", "F/Lt David Maltby", 1, 2),
    ("AJ-L", "ED929/G", "F/Lt David Shannon", 1, 2),
    ("AJ-Z", "ED937/G", "S/Ldr Henry Maudslay", 1, 3),
    ("AJ-B", "ED864/G", "F/Lt Bill Astell", 1, 3),
    ("AJ-N", "ED912/G", "P/O Les Knight", 1, 3),
    ("AJ-E", "ED927/G", "F/Lt Norman Barlow", 2, None),
    ("AJ-W", "ED921/G", "F/Lt Les Munro", 2, None),
    ("AJ-K", "ED934/G", "P/O Vernon Byers", 2, None),
    ("AJ-H", "ED936/G", "P/O Geoff Rice", 2, None),
    ("AJ-T", "ED825/G", "F/Lt Joe McCarthy", 2, None),
    ("AJ-C", "ED910/G", "P/O Warner Ottley", 3, None),
    ("AJ-S", "ED865/G", "P/O Lewis Burpee", 3, None),
    ("AJ-F", "ED918/G", "F/Sgt Ken Brown", 3, None),
    ("AJ-O", "ED886/G", "F/Sgt Bill Townsend", 3, None),
    ("AJ-Y", "ED924/G", "F/Sgt Cyril Anderson", 3, None),
]
LANCASTERS = [c for c, *_ in CREWS]
WAVE = {c: w for c, _, _, w, _ in CREWS}

# Times from the ORB sheets (BDST): take-off and landing; None where the aircraft was lost.
TAKE_OFF = {
    "AJ-G": "21:39", "AJ-M": "21:39", "AJ-P": "21:39",
    "AJ-A": "21:47", "AJ-J": "21:47", "AJ-L": "21:47",
    "AJ-Z": "21:59", "AJ-B": "21:59", "AJ-N": "21:59",
    "AJ-E": "21:28", "AJ-W": "21:29", "AJ-K": "21:30", "AJ-H": "21:31", "AJ-T": "22:01",
    "AJ-C": "00:09", "AJ-S": "00:11", "AJ-F": "00:12", "AJ-O": "00:14", "AJ-Y": "00:15",
}
LANDED = {
    "AJ-G": "04:15", "AJ-P": "03:19", "AJ-J": "03:11", "AJ-L": "04:06", "AJ-N": "04:20",
    "AJ-W": "00:36", "AJ-H": "00:47", "AJ-T": "03:23",
    "AJ-F": "05:33", "AJ-O": "06:15", "AJ-Y": "05:30",
}

# Order of battle: (id, name, symbol, members, parent). The RAF chain runs from No. 5 Group
# through 617 Squadron to its waves and sections (ORB); the German chain is the LWL's "3.
# Batterie leichte Flakabteilung 840, die zur Flakgruppe Dortmund gehörte", with 2525 echelon
# amplifiers for regiment-level group, battalion and battery.
FORMATIONS = [
    ("5 GROUP", "No. 5 Group, RAF Bomber Command", LANCASTER, ["SCAMPTON", "5 GROUP HQ"],
     None),
    ("617 SQUADRON", "No. 617 Squadron", LANCASTER, [], "5 GROUP"),
    ("WAVE 1", "First wave · Möhne and Eder", LANCASTER, [], "617 SQUADRON"),
    ("WAVE 1 SECTION 1", "Gibson's section", LANCASTER, ["AJ-G", "AJ-M", "AJ-P"], "WAVE 1"),
    ("WAVE 1 SECTION 2", "Young's section", LANCASTER, ["AJ-A", "AJ-J", "AJ-L"], "WAVE 1"),
    ("WAVE 1 SECTION 3", "Maudslay's section", LANCASTER, ["AJ-Z", "AJ-B", "AJ-N"], "WAVE 1"),
    ("WAVE 2", "Second wave · Sorpe", LANCASTER, ["AJ-E", "AJ-W", "AJ-K", "AJ-H", "AJ-T"],
     "617 SQUADRON"),
    ("WAVE 3", "Third wave · mobile reserve", LANCASTER,
     ["AJ-C", "AJ-S", "AJ-F", "AJ-O", "AJ-Y"], "617 SQUADRON"),
    ("FLAKGRUPPE DORTMUND", "Flakgruppe Dortmund", "SHGPUCD----G---", [], None),
    ("LE. FLAK-ABT. 840", "leichte Flak-Abteilung 840", "SHGPUCDG---F---", ["MÖHNE FLAK"],
     "FLAKGRUPPE DORTMUND"),
]

FIXED = [
    # (id, sidc, name, kind, point, bound m, source)
    ("SCAMPTON", AIRFIELD, "RAF Scampton", "airfield", SCAMPTON, 300.0, "wikipedia-scampton"),
    ("5 GROUP HQ", HQ, "No. 5 Group HQ, St Vincents, Grantham", "group headquarters", GRANTHAM,
     150.0, "wikipedia-st-vincents"),
    ("MÖHNE", DAM, "Möhne dam (target X)", "masonry gravity dam", MOHNE, 20.0, "osm"),
    ("EDER", DAM, "Eder dam (target Y)", "masonry gravity dam", EDER, 20.0, "osm"),
    ("SORPE", DAM, "Sorpe dam (target Z)", "earth dam with concrete core", SORPE, 20.0, "osm"),
    ("ENNEPE", DAM, "Ennepe dam (target E)", "masonry dam", ENNEPE, 20.0, "osm"),
    ("LISTER", DAM, "Lister dam (target D)", "masonry dam", LISTER, 20.0, "osm"),
    ("DIEMEL", DAM, "Diemel dam (target F)", "masonry dam", DIEMEL, 20.0, "osm"),
    ("BEVER", DAM, "Bever dam", "earth and rockfill dam", BEVER, 20.0, "osm"),
    ("MÖHNE POWER STATION", POWER, "Möhne power station", "hydroelectric plant", POWER_STATION,
     100.0, "osm"),
    ("MÖHNE FLAK", FLAK, "3./le. Flak-Abt. 840 · six 2 cm guns", "light flak battery", MOHNE, 300.0,
     "lwl-moehne"),
]


def entities(mines):
    """Entity rows, formations first so the order of battle reads top down; `mines` maps each
    Upkeep id to the aircraft that dropped it, which is its parent."""
    parent = {m: g for g, _, _, members, _ in FORMATIONS for m in members}
    aircraft = set(LANCASTERS)

    def strength(group):
        """Aircraft under `group`, at any depth; airfields and headquarters are not counted."""
        own = next(m for g, _, _, m, _ in FORMATIONS if g == group)
        return (sum(m in aircraft for m in own)
                + sum(strength(g) for g, _, _, _, up in FORMATIONS if up == group))

    out = []
    for group, name, sidc, _, up in FORMATIONS:
        row = {"id": group, "sidc": sidc, "camera": False, "name": name, "kind": "formation"}
        if strength(group):
            row["quantity"] = strength(group)
        if up:
            row["parent"] = up
        out.append(row)
    for code, serial, captain, _, _ in CREWS:
        out.append({"id": code, "sidc": LANCASTER, "camera": False,
                    "name": f"{code} · {captain}", "kind": f"Lancaster B.III Type 464 {serial}",
                    "parent": parent[code]})
    for mine, owner in mines.items():
        out.append({"id": mine, "sidc": "SFAPWB---------", "camera": False,
                    "name": f"Upkeep · {owner}", "kind": "Upkeep mine, 9,250 lb",
                    "parent": owner})
    for id_, sidc, name, kind, *_ in FIXED:
        row = {"id": id_, "sidc": sidc, "camera": False, "name": name, "kind": kind}
        if id_ in parent:
            row["parent"] = parent[id_]
        out.append(row)
    out.append({"id": "MÖHNE FLOOD", "sidc": FLOOD, "camera": False,
                "name": "Möhne flood wave", "kind": "flood front"})
    out.append({"id": "EDER FLOOD", "sidc": FLOOD, "camera": False,
                "name": "Eder flood wave", "kind": "flood front"})
    return out
