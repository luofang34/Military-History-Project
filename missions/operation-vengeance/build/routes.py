"""Departures and transit legs up to the 09:34 sighting.

The P-38 route keeps Condon's 20 nmi island stand-off and reads the published
290° and 305° legs as magnetic headings (about 7.5° E variation). It reproduces
the sourced 08:20 first turn about 180 mi west of Henderson, the 08:47 turn
abreast of Vella Lavella and the report's 435 mi at about 200 mph.
"""
import math

from track import Track, destination, distance_m, bearing_deg, offset
from sites import (L, FIGHTER_TWO, LAKUNAI, P38S, TAKEOFF_ORDER, SLOTS, WAVE_TOP_M,
                   BETTY_CRUISE_M, BETTY_SIGHTED_M, ZERO_ABOVE_M, YAMAMOTO, UGAKI)

JOIN = (160.00, -9.36)
P38_ROUTE = [
    ("07:31:00", JOIN),
    (None, (159.62, -9.17)),     # out past Cape Esperance
    (None, (157.40, -9.20)),     # first turn, ~182 mi west of Henderson
    (None, (156.20, -8.62)),     # second turn, abreast of Vella Lavella
    (None, (155.02, -7.50)),     # final turn north-east, 47 km off the Treasuries
    ("09:34:00", (155.35, -6.76)),  # sighting, ~4 km off the SW coast
]
RUNWAY_HEADING = 270.0  # Fighter Two orientation is not sourced; bound_m covers it
JAPANESE_ROUTE = [
    (152.60, -4.62),   # climb-out over Blanche Bay / St George's Channel
    (155.10, -6.30),   # landfall at Empress Augusta Bay
    (155.21, -6.50),
    (155.30, -6.64),
    (155.36, -6.715),  # 09:34 position, descending along the coast
]


def constant_speed(track, points, t0, t1, alts):
    """Appends points between t0 and t1 at constant ground speed."""
    legs = [distance_m(a, b) for a, b in zip(points, points[1:])]
    total = sum(legs)
    run = 0.0
    for p, leg, alt in zip(points[1:], legs, alts[1:]):
        run += leg
        track.add(t0 + (t1 - t0) * run / total, p, alt)
    return total / ((t1 - t0) / 1000)


def lead_route():
    """Mitchell's navigation track from join-up to the sighting."""
    pts = [p for _, p in P38_ROUTE]
    lead = Track().add(L("07:31:00"), JOIN, 150)
    alts = [150] + [WAVE_TOP_M] * (len(pts) - 1)
    speed = constant_speed(lead, pts, L("07:31:00"), L("09:34:00"), alts)
    # The flights' slots swing with the lead's heading; rounded turns keep them flying.
    lead.round_corners(L("07:31:00"), L("09:34:00"))
    return lead, speed


def slot_point(lead, entity, t, scale=1.0):
    right, ahead = (scale * v for v in SLOTS[entity])
    h = math.radians(lead.heading(t))
    east = right * math.cos(h) + ahead * math.sin(h)
    north = -right * math.sin(h) + ahead * math.cos(h)
    p, alt = lead.at(t)
    return offset(p, east, north), alt


def in_formation(track, lead, entity, t0, t1, step=20_000):
    t = t0
    while t < t1:
        p, alt = slot_point(lead, entity, t)
        track.add(t, p, alt)
        t += step
    p, alt = slot_point(lead, entity, t1)
    track.add(t1, p, alt)


def parked(i):
    return offset(FIGHTER_TWO, 900 + 45 * i, -160)


ROLL_M = 1400
ORBIT_MS = 80.0  # about 290 km/h round the join-up orbit
ABORT_STOP_M = 700


def roll(track, threshold, start, end, accel, step=4_000):
    """Waypoints of a uniformly accelerating take-off roll down the runway, ending at `end`."""
    at = start + step
    while at < end:
        s = 0.5 * accel * ((at - start) / 1000) ** 2
        track.add(at, destination(threshold, RUNWAY_HEADING, s), 0)
        at += step
    rolled = 0.5 * accel * ((end - start) / 1000) ** 2
    track.add(end, destination(threshold, RUNWAY_HEADING, rolled), 0)


def join_time(takeoff):
    """When an aircraft takes its slot: 07:31, or on a later lap for the last ones off, who
    need about three minutes from brake release to reach the orbit."""
    return max(L("07:31:00"), takeoff + 200_000)


def p38_departure(entity, slot_index, lead, abort_tire=False):
    """Taxi, take-off roll, climb-out and a left-hand orbit into the join-up slot."""
    takeoff = L("07:25:00") + 20_000 * (slot_index // 2) + 4_000 * (slot_index % 2)
    threshold = offset(FIGHTER_TWO, 1200, 0)
    if takeoff - 30_000 <= L("07:24:30"):
        # The lead pair is already lined up when the record starts.
        t = Track().add(L("07:24:30"), threshold, 0)
    else:
        t = Track().add(L("07:24:30"), parked(slot_index), 0)
        if takeoff - 56_000 > L("07:24:30"):
            t.add(takeoff - 56_000, parked(slot_index), 0)
        t.add(takeoff - 30_000, threshold, 0)
    # Lined up, then a uniformly accelerating roll: 1,400 m to lift-off at about 58 m/s.
    roll_start = takeoff - 26_000
    t.add(roll_start, threshold, 0)
    accel = 2 * ROLL_M / ((takeoff + 22_000 - roll_start) / 1000) ** 2
    if abort_tire:
        # The tyre fails 26 s into the roll; braking stops the aircraft at 700 m.
        roll(t, threshold, roll_start, takeoff, accel)
        speed = accel * (takeoff - roll_start) / 1000
        rolled = 0.5 * accel * ((takeoff - roll_start) / 1000) ** 2
        brake = speed ** 2 / (2 * (ABORT_STOP_M - rolled))
        stop_after = speed / brake
        for k in range(1, 5):
            s = speed * stop_after * k / 4 - 0.5 * brake * (stop_after * k / 4) ** 2
            t.add(takeoff + stop_after * k / 4 * 1000,
                  destination(threshold, RUNWAY_HEADING, rolled + s), 0)
        return t, takeoff
    roll(t, threshold, roll_start, takeoff + 22_000, accel)
    liftoff = destination(threshold, RUNWAY_HEADING, ROLL_M)
    climb = destination(liftoff, RUNWAY_HEADING - 20, 4500)
    t.add(takeoff + 75_000, climb, 300)
    joined_at = join_time(takeoff)
    joined, alt = slot_point(lead, entity, joined_at)
    # Orbit backwards from the slot so every aircraft arrives at 07:31:00.
    centre = destination(JOIN, 180, 3500)
    radius = distance_m(centre, joined)
    angle0 = bearing_deg(centre, joined)
    omega = ORBIT_MS / max(radius, 1.0)
    climbed = takeoff + 75_000

    def on_orbit(tt):
        ang = angle0 + math.degrees(omega * (joined_at - tt) / 1000)
        return destination(centre, ang, radius)

    # A left turn off the climb-out, then join the orbit ahead of it where flying straight
    # there takes the orbit's own speed, so no leg doubles back or is flown slower than the
    # aircraft can fly.
    heading = RUNWAY_HEADING - 110
    turned = climbed + 30_000
    turn = destination(climb, heading, ORBIT_MS * 30)
    t.add(turned, turn, 375)

    def mismatch(tt):
        p = on_orbit(tt)
        off = abs((bearing_deg(turn, p) - heading + 180) % 360 - 180)
        speed = distance_m(turn, p) / ((tt - turned) / 1000)
        return abs(speed - ORBIT_MS) + 2.0 * max(0.0, off - 60)

    entry = min(range(turned + 20_000, joined_at - 15_000, 1000), key=mismatch)
    tt = joined_at - 15_000
    samples = []
    while tt > entry:
        samples.append((tt, on_orbit(tt)))
        tt -= 15_000
    samples.append((entry, on_orbit(entry)))
    for tt, p in reversed(samples):
        t.add(tt, p, 450)
    t.add(joined_at, joined, alt)
    # Rounding the turns before the orbit would shorten their legs below flying speed.
    return t.round_corners(entry, joined_at), takeoff


def moore_return(track, lead):
    """Drop tanks would not feed; Moore turns back after join-up."""
    t = L("07:36:00")
    p, _ = slot_point(lead, "MOORE", t)
    track.add(L("07:37:00"), destination(p, 120, 3500), 150)
    track.add(L("07:42:30"), offset(FIGHTER_TWO, -6000, 1200), 200)
    touchdown = offset(FIGHTER_TWO, -900, 0)
    track.add(L("07:43:30"), touchdown, 0)
    track.add(L("07:44:15"), offset(FIGHTER_TWO, 700, 0), 0)
    track.add(L("07:45:00"), offset(FIGHTER_TWO, 900 + 45 * 15, -200), 0)


def p38_tracks():
    lead, speed = lead_route()
    tracks = {}
    for index, entity in enumerate(TAKEOFF_ORDER):
        track, takeoff = p38_departure(entity, index, lead, abort_tire=entity == "MCLANAHAN")
        if entity != "MCLANAHAN":
            end = L("07:36:00") if entity == "MOORE" else L("09:34:00")
            in_formation(track, lead, entity, join_time(takeoff) + 20_000, end)
        if entity == "MOORE":
            moore_return(track, lead)
        tracks[entity] = track
    if set(tracks) != set(P38S):
        raise ValueError(f"P-38 tracks {sorted(set(tracks) ^ set(P38S))} do not match the roster")
    return tracks, lead, speed


def japanese_tracks():
    """Lakunai departure 06:05–06:10 Tokyo; the reconstructed path follows US accounts
    placing the formation over Bougainville's south-west coast at the sighting."""
    zero_slots = {
        "MORISAKI": (450, -350), "TSUJINOUE": (560, -440), "SUGITA": (340, -440),
        "HIDAKA": (750, -650), "OKAZAKI": (860, -740), "YANAGIYA": (640, -740),
    }
    runway_end = offset(LAKUNAI, 700, -900)
    lead = Track().add(L("08:04:30"), offset(LAKUNAI, 0, 600), 0)
    lead.add(L("08:06:00"), offset(LAKUNAI, 0, 600), 0)
    lead.add(L("08:06:35"), runway_end, 0)
    climb_out, landfall = JAPANESE_ROUTE[0], JAPANESE_ROUTE[1]
    cruise_from = destination(climb_out, bearing_deg(climb_out, landfall),
                              0.2 * distance_m(climb_out, landfall))
    route = [runway_end, climb_out, cruise_from] + JAPANESE_ROUTE[1:]
    # Cruise at 6,500 ft, descending to 4,500 ft by the sighting (13th FC report).
    alts = [0, 900, BETTY_CRUISE_M, BETTY_CRUISE_M, 1800, 1550, BETTY_SIGHTED_M]
    speed = constant_speed(lead, route, L("08:06:35"), L("09:34:00"), alts)

    def follower(right, ahead, up, after):
        out = Track()
        for wp in lead.waypoints:
            if wp.at_ms <= after:
                continue
            h = math.radians(lead.heading(wp.at_ms))
            east = right * math.cos(h) + ahead * math.sin(h)
            north = -right * math.sin(h) + ahead * math.cos(h)
            out.add(wp.at_ms, offset(wp.point, east, north), wp.alt_m + up)
        return out

    tracks = {YAMAMOTO: lead}
    ugaki = Track().add(L("08:04:30"), offset(LAKUNAI, -60, 600), 0)
    ugaki.add(L("08:06:40"), offset(LAKUNAI, -60, 600), 0)
    ugaki.add(L("08:07:15"), offset(runway_end, -60, 0), 0)
    for wp in follower(-160, -120, 0, L("08:08:30")).waypoints:
        ugaki.add(wp.at_ms, wp.point, wp.alt_m)
    tracks[UGAKI] = ugaki
    for i, (entity, (right, ahead)) in enumerate(zero_slots.items()):
        rolling = L("08:05:00") + 10_000 * i
        z = Track().add(L("08:04:30"), offset(LAKUNAI, 40 * i, 600), 0)
        if rolling > L("08:04:30"):
            z.add(rolling, offset(LAKUNAI, 40 * i, 600), 0)
        z.add(rolling + 25_000, offset(runway_end, 40 * i, 0), 0)
        for wp in follower(right, ahead, ZERO_ABOVE_M, rolling + 150_000).waypoints:
            z.add(wp.at_ms, wp.point, wp.alt_m)
        tracks[entity] = z
    return tracks, speed * 3.6
