"""The engagement from the 09:34 sighting to egress.

Anchors: sighting 09:34 (13th FC report), Bettys at 4,500 ft and Zeros 1,500 ft
above, Barber's attack from directly astern (wreck inspection), the T1-323 wreck
and the T1-326 ditching off Moila Point (Pacific Wrecks), Hine last seen near
Shortland (MACRs 599/609). Manoeuvres between anchors are reconstructed.
"""
import math

from track import Track, destination, distance_m, offset
from routes import slot_point
from sites import (L, KAHILI, BALLALE, CRASH_T1_323, DITCH_T1_326, BANIKA, FIGHTER_TWO, COVER,
                   COVER_TOP_M, YAMAMOTO, UGAKI, ZERO_1, ZERO_2)

E1 = (155.63, -7.15)   # between Shortland and the Treasuries
E2 = (155.95, -7.60)
R2 = (156.30, -8.40)   # 27 km west of Simbo
HINE_LAST = (155.77, -6.905)  # MACR 599: four miles north of Shortland
COVER_ORBIT = (155.40, -6.76)


def go(track, specs, kmh=480):
    """Appends (time|None, point, alt) waypoints; None times follow at `kmh`."""
    for at, point, alt in specs:
        if at is None:
            last = track.waypoints[-1]
            at = last.at_ms + distance_m(last.point, point) / (kmh / 3.6) * 1000
        else:
            at = L(at)
        track.add(at, point, alt)
    return track


def home(track, via, final, kmh, alt=900):
    """Return route; the record ends before any aircraft lands. Its turns are rounded,
    from the last engagement waypoint onward."""
    start = track.end
    go(track, [(None, p, alt) for p in via + [final]], kmh)
    return track.round_corners(start - 1, track.end)


def attack_section(tracks):
    go(tracks["LANPHIER"], [
        ("09:34:40", (155.385, -6.775), 300),
        ("09:35:40", (155.420, -6.790), 1000),
        ("09:36:10", (155.430, -6.758), 1500),   # head-on pass with the diving escort
        ("09:36:40", (155.450, -6.725), 1900),
        ("09:37:40", (155.530, -6.735), 1800),   # noses over from 6,000 ft
        ("09:38:30", (155.600, -6.740), 300),    # treetops, two Zeros behind
        ("09:39:30", (155.675, -6.745), 80),     # across a corner of Kahili
        ("09:41:20", (155.800, -6.850), 500),
    ])
    home(tracks["LANPHIER"], [(155.85, -7.20), E2, R2], FIGHTER_TWO, 420)
    go(tracks["BARBER"], [
        ("09:34:40", (155.390, -6.778), 300),
        ("09:35:40", (155.425, -6.793), 1000),
        ("09:36:15", (155.442, -6.780), 900),    # hard left behind the bombers
        ("09:36:40", (155.462, -6.773), 650),
        ("09:37:10", (155.502, -6.779), 220),    # firing from directly astern
        ("09:37:25", (155.522, -6.776), 250),
        ("09:38:05", (155.540, -6.830), 150),
        ("09:38:50", (155.556, -6.858), 40),     # joins the attack on T1-326
        ("09:39:10", (155.582, -6.866), 50),
        ("09:40:20", (155.620, -6.950), 30),
    ])
    home(tracks["BARBER"], [E1, E2, R2], FIGHTER_TWO, 420)
    go(tracks["HOLMES"], [
        ("09:34:20", (155.360, -6.775), 30),     # tanks hang: turns out to sea
        ("09:35:00", (155.350, -6.820), 60),
        ("09:35:40", (155.360, -6.870), 100),
        ("09:36:40", (155.420, -6.865), 300),
        ("09:37:30", (155.480, -6.845), 400),
        ("09:38:00", (155.515, -6.828), 300),    # drives the Zeros off Barber's tail
        ("09:38:22", (155.527, -6.851), 80),
        ("09:38:40", (155.548, -6.858), 40),     # firing on T1-326
        ("09:39:00", (155.572, -6.866), 60),
        ("09:40:00", (155.600, -6.920), 300),
        ("09:40:30", (155.635, -6.930), 600),    # "whipped up and around" at a Zero
        ("09:41:00", (155.630, -6.970), 200),
    ])
    home(tracks["HOLMES"], [E1, E2, R2], BANIKA, 380)
    hine = tracks["HINE"]
    for wp in tracks["HOLMES"].waypoints:
        if L("09:34:00") < wp.at_ms <= L("09:39:00"):
            hine.add(wp.at_ms, offset(wp.point, 220, -160), wp.alt_m + 20)
    go(hine, [(None, HINE_LAST, 40)], 540)


def bombers(tracks):
    go(tracks[YAMAMOTO], [
        ("09:35:50", (155.434, -6.767), 1250),
        ("09:36:30", (155.468, -6.772), 700),    # dives for the jungle
        ("09:37:10", (155.510, -6.780), 200),
        ("09:37:40", (155.535, -6.783), 60),
        ("09:38:00", CRASH_T1_323, 0),
    ])
    go(tracks[UGAKI], [
        ("09:35:50", (155.428, -6.770), 1200),
        ("09:36:30", (155.440, -6.806), 500),    # turns for the sea
        ("09:37:40", (155.500, -6.842), 60),
        ("09:38:40", (155.555, -6.859), 25),
        ("09:39:20", DITCH_T1_326, 0),
    ])


def escorts(tracks):
    """13th FC report: three Zeros peel down in a string at Lanphier and chase him past
    Kahili; others make passes on Barber until Holmes and Hine drive them off, then fight
    again past Shortland. Yanagiya: he fired one burst, dived to Buin to fire an alarm
    burst, and Okazaki landed at Ballale with engine trouble. Pairings are inferred."""
    first = [
        ("09:36:40", (155.452, -6.770), 900),    # passes on Barber astern of T1-323
        ("09:37:10", (155.490, -6.777), 400),
        ("09:37:35", (155.515, -6.790), 250),
        ("09:38:00", (155.533, -6.815), 150),    # chasing Barber to the coast
        ("09:38:20", (155.545, -6.835), 250),    # broken up by Holmes and Hine
        ("09:39:00", (155.575, -6.845), 400),
        ("09:39:45", (155.620, -6.875), 200),
        ("09:40:10", (155.650, -6.885), 80),     # Sugita hits Hine's left engine
        ("09:40:55", (155.710, -6.895), 60),
        ("09:41:35", (155.760, -6.905), 60),     # passes on Hine north of Shortland
        ("09:42:00", (155.770, -6.885), 150),
    ]
    chase = [
        ("09:36:10", (155.432, -6.752), 1550),   # head-on with Lanphier
        ("09:36:50", (155.440, -6.730), 1800),
        ("09:37:50", (155.520, -6.738), 1700),
        ("09:38:45", (155.590, -6.742), 400),
        ("09:39:40", (155.660, -6.748), 150),    # Lanphier outruns them
    ]
    betty = tracks[YAMAMOTO]

    def station(entity, at):
        """Escort station relative to the bombers, held until the dive."""
        t = tracks[entity]
        (zx, zy), z_alt = t.at(L("09:34:00"))
        (bx, by), b_alt = betty.at(L("09:34:00"))
        (cx, cy), c_alt = betty.at(L(at))
        t.add(L(at), (cx + zx - bx, cy + zy - by), c_alt + z_alt - b_alt)
        return t

    for entity, (east, north) in zip(ZERO_1, [(0, 0), (130, -110), (-130, -110)]):
        t = station(entity, "09:35:50")
        for at, p, alt in first:
            t.add(L(at), offset(p, east, north), alt)
    # Second section in a string: Hidaka, Okazaki 300 m and Yanagiya 600 m behind.
    for entity, north in zip(ZERO_2, [0, 300, 600]):
        t = station(entity, "09:35:40")
        t.add(L("09:36:10"), offset(chase[0][1], 0, north), chase[0][2] + north / 3)
        if entity == "YANAGIYA":
            go(t, [
                ("09:36:40", (155.440, -6.740), 2100),   # one burst, pulls up
                ("09:40:00", KAHILI, 200),               # alarm burst over Buin
                ("09:40:40", (155.700, -6.715), 400),
                ("09:41:20", (155.670, -6.710), 400),
                ("09:42:00", (155.680, -6.735), 300),
            ])
            continue
        for at, p, alt in chase[1:]:
            t.add(L(at), offset(p, 0, north), alt)
        if entity == "OKAZAKI":
            go(t, [("09:44:30", (155.870, -6.975), 100), ("09:45:20", BALLALE, 0)])
        else:
            go(t, [("09:40:40", (155.700, -6.800), 300), ("09:41:40", (155.720, -6.860), 300)])


def cover(tracks, mitchell_lead):
    """Mitchell's twelve climb toward 18,000 ft and orbit above the fight."""
    lead = Track()
    p, _ = mitchell_lead.at(L("09:34:00"))
    lead.add(L("09:34:00"), p, 6)
    lead.add(L("09:35:00"), destination(p, 40, 5000), 700)
    radius = 10_000
    entry = destination(COVER_ORBIT, 20, radius)
    lead.add(L("09:36:00"), entry, 1700)
    omega = 100 / radius
    t = L("09:36:00")
    while t < L("09:42:30"):
        t += 10_000
        angle = 20 + math.degrees(omega * (t - L("09:36:00")) / 1000)
        climb = min(1.0, (t - L("09:36:00")) / (L("09:39:30") - L("09:36:00")))
        lead.add(t, destination(COVER_ORBIT, angle, radius), 1700 + (COVER_TOP_M - 1700) * climb)
    for entity in COVER:
        track = tracks[entity]
        t = L("09:34:00") + 10_000
        while t <= lead.end:
            point, alt = slot_point(lead, entity, t)
            track.add(t, point, alt)
            t += 10_000
        if entity == "CANNING":
            # Canning escorts Holmes, short of fuel, to the Russell Islands.
            home(track, [E1, E2, R2], BANIKA, 380, alt=1500)
        else:
            home(track, [E1, E2, R2], FIGHTER_TWO, 420, alt=3000)


def engagement(tracks, mitchell_lead):
    bombers(tracks)
    escorts(tracks)
    attack_section(tracks)
    cover(tracks, mitchell_lead)
