"""Chapters, briefing notes, camera shots and pacing for the Gulf of Sidra reconstruction.

Times are operation milliseconds from 07:00 Tripoli time. Each group shot frames the aircraft
it names, centred on where they are at the shot's start and zoomed to fit their spread, so the
camera never frames empty sea. Once the Su-22s are down, the camera pulls back to the F-14s.
"""
import math

DURATION = 1_500_000  # 07:00 to 07:25, after the Pentagon's 07:20 shootdown time

SU_LEAD, SU_WING, FE102, FE107 = "SU22-LEAD", "SU22-WING", "FE102", "FE107"
AA2, AIM_102, AIM_107 = "AA2-ATOLL", "AIM9-102", "AIM9-107"
LOD_CENTRE = (17.5, 32.5)  # middle of the Line of Death, between its two coast endpoints

CHAPTERS = [
    ("Su-22s from Ghurdabiya", "00:00"),
    ("Racetrack over the Gulf", "03:00"),
    ("Vectored south, 07:15 contact", "09:00"),
    ("The Atoll, 07:16", "16:31"),
    ("The break", "16:45"),
    ("First Fitter down", "17:21"),
    ("Second Fitter down", "17:53"),
    ("Clear to defend yourself", "18:29"),
    ("Egress, Line of Death", "19:10"),
]

# (from, until, speed); viewing time is the sum of duration over speed.
PACING = [
    ("00:00", "03:00", 12),
    ("03:00", "09:00", 10),
    ("09:00", "15:00", 8),
    ("15:00", "16:20", 2),
    ("16:20", "17:15", 1),
    ("17:15", "18:10", 1),
    ("18:10", "19:10", 2),
    ("19:10", "25:00", 8),
]

# (entity or None, from, until, source, provenance, text, occurrence or None)
NOTES = [
    (None, "00:00", "25:00", "ratner-yale-1984", "reported",
     "Line of Death. Libya's October 1973 declaration takes the Gulf of Surt north to "
     "32°30′N as internal waters. The line runs from the coast west of Misrata to the coast "
     "northeast of Benghazi, about 297 nm. The US rejected it in 1974 and on 19 August 1981 "
     "invoked high-seas freedom beyond the territorial sea.", None),
    (None, "00:00", "15:00", "stanik-1996", "reported",
     "OOMEX exercise, 18–19 August. The carriers stayed north of 32°30′N, and one CAP "
     "station lay south of it (Stanik; secondary, from a search summary).", None),
    (FE102, "00:00", "09:00", "stanik-1996", "reported",
     "Fast Eagle 102 and 107 hold a racetrack CAP at 20,000 ft, about 300 kt, from about "
     "06:00 (Stanik). Kleemann's jet is at 18,000 ft and Muczynski's 4,000 ft higher.", None),
    (FE102, "09:00", "15:00", "reconstruction-cap", "reconstructed",
     "The F-14s are vectored south. This leg is inferred from the 07:15 contact.", None),
    (None, "07:11", "07:15", "stanik-1996", "reported",
     "About 80 nm, 07:11: Venlet's first radar contact, coming from Ghurdabiya (Stanik). "
     "The Biddle tape starts at 07:15 with \"twenty miles, twenty thousand feet\".", None),
    (None, "15:27", "16:31", "biddle-tape", "reported",
     "Biddle calls the range closing: 16 miles at 00:27, 14 at 00:38, 8 at 00:54, 6 at 01:03 "
     "(relative to 07:15). Head-on closure, the Libyans climbing to 20,000 ft.", None),
    (SU_LEAD, "16:31", "16:38", "biddle-tape", "reported",
     "16:31 Biddle: \"two fitters has shot at my leader\". The Libyan lead fires one AA-2 "
     "Atoll at FE102, which misses (US account; Cooper calls it an R-13M).", None),
    (SU_WING, "16:45", "17:21", "biddle-tape", "reported",
     "The Libyan pair breaks: the leader turns northwest, the wingman southeast (Stanik; "
     "Wikipedia citing Brown).", None),
    (FE107, "16:45", "17:53", "biddle-tape", "reported",
     "The F-14s cross over and turn hard port. Muczynski takes the leader, Kleemann the "
     "wingman.", None),
    (AIM_102, "17:11", "17:21", "biddle-tape", "reported",
     "Kleemann (102) fires one AIM-9L at the wingman.", None),
    (SU_WING, "17:21", "17:26", "biddle-tape", "reported",
     "17:21 Kleemann (102) kills the wingman with one AIM-9L into the tailpipe (Biddle: "
     "\"It was a clean target\"; Stanik says the first kill was 102).", None),
    (AIM_107, "17:43", "17:53", "biddle-tape", "reported",
     "Muczynski (107) fires one AIM-9L at the leader from about 1,000 yd.", None),
    (SU_LEAD, "17:53", "17:58", "biddle-tape", "reported",
     "17:53 Muczynski (107) kills the leader with one AIM-9L (Biddle: \"Fox 2 kill from "
     "music\"). Stanik says his second Sidewinder failed its check.", None),
    (SU_LEAD, "18:05", "18:14", "biddle-tape", "reported",
     "18:05 Biddle: \"His chute is not deploying. He is falling free.\" Libyan accounts say "
     "both pilots were recovered by helicopter. The tape and the Libyan account disagree.",
     ("uncertain", "18:05", "18:14")),
    (FE107, "18:14", "18:29", "biddle-tape", "reported",
     "18:14 Muczynski reports 123 DME on the 180 and fuel of 10.2 (Biddle). The TACAN "
     "reference is not named in any source.", None),
    (None, "18:29", "19:00", "biddle-tape", "reported",
     "18:29 \"102, 107, you are clear to defend yourself. Pass from the ship\" (Biddle). "
     "DVIDS places this before the kills; the tape places it after both.", None),
    (None, "19:00", "20:00", "stanik-1996", "reported",
     "19:00 Stanik: the F-14s rejoin and head back to Nimitz. UPI says the dogfight lasted "
     "about one minute.", None),
    (None, "16:31", "19:00", "cooper-acig", "reported",
     "Libyan account (Cooper): an F-14 destroyed by Zintani's R-13M, and a wreck found by "
     "fishermen. A Libyan radio report puts a downed F-14 near Sardinia. The two claims "
     "cannot both be true, and US sources record no F-14 loss.",
     ("uncertain", "16:31", "19:00")),
    (None, "19:10", "25:00", "upi-1981", "reported",
     "The Pentagon gave the shootdowns as 0520Z, which is 07:20 Tripoli time. The Libyan "
     "clock is inferred from the Biddle relative times, so the anchor is ±15 minutes.", None),
]


def annotations(em, t):
    ms = lambda x: x if isinstance(x, int) else t(x)  # noqa: E731
    for entity, start, until, source, provenance, text, occ in NOTES:
        occurrence = None
        if occ:
            occurrence = {"kind": occ[0], "earliest": ms(occ[1]), "latest": ms(occ[2])}
        em.note(source, entity, ms(start), ms(until), text, provenance, [],
                occurrence=occurrence)


def point(p):
    return {"kind": "point", "value": {"lon": p[0], "lat": p[1]}}


def entity(e):
    return {"kind": "entity", "value": e}


def cue(start, end, target, zoom, pitch, bearing, orbit=0.0, transition=0, focus=None):
    """A camera shot. The viewer rejects a transition longer than its shot, so clamp it."""
    transition = min(transition, end - start)
    c = {"start_ms": start, "end_ms": end, "target": target, "zoom": zoom, "pitch": pitch,
         "bearing": bearing, "orbit_deg_s": orbit, "transition_ms": transition}
    if focus:
        c["focus"] = focus
    return c


def km_between(a, b):
    """Rough flat-earth distance in km; good enough to choose a zoom."""
    dy = (a[1] - b[1]) * 111.0
    dx = (a[0] - b[0]) * 111.0 * math.cos(math.radians((a[1] + b[1]) / 2))
    return math.hypot(dx, dy)


def group(tracks, names, when):
    """Centre and zoom for a shot framing `names` at `when`: the centre of their positions,
    and a zoom that fits their spread (tighter for a close fight, wider for a spread-out one)."""
    pts = [tracks[n].at(when)[0] for n in names]
    centre = (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))
    spread = max(km_between(a, b) for a in pts for b in pts)
    if spread < 3:
        zoom = 12.5
    elif spread < 8:
        zoom = 11.0
    elif spread < 20:
        zoom = 10.0
    elif spread < 40:
        zoom = 9.0
    elif spread < 80:
        zoom = 8.0
    else:
        zoom = 7.0
    return point(centre), zoom


def camera(t, tracks):
    """Shots are contiguous. Missile launches are followed on the missile, zoomed to keep both
    aircraft in frame; entity targets only span times that aircraft has fixes."""
    shots = []

    def add(start, end, names, pitch, bearing, **kw):
        target, zoom = group(tracks, names, t(start))
        shots.append(cue(t(start), t(end), target, zoom, pitch, bearing, **kw))

    def follow(start, end, name, zoom, pitch, bearing, **kw):
        shots.append(cue(t(start), t(end), entity(name), zoom, pitch, bearing, focus=name, **kw))

    shots.append(cue(0, t("03:00"), entity(SU_LEAD), 8.2, 30, 340, focus=SU_LEAD,
                     transition=2000))
    add("03:00", "09:00", [SU_LEAD, SU_WING], 30, 340, transition=60_000)
    add("09:00", "15:00", [SU_LEAD, FE102, FE107], 30, 0, transition=60_000)
    add("15:00", "16:20", [SU_LEAD, SU_WING, FE102, FE107], 35, 200, transition=10_000)
    add("16:20", "16:31", [SU_LEAD, FE102, FE107], 45, 200, transition=6000)
    follow("16:31", "16:38", AA2, 10.5, 40, 200, transition=1000)
    add("16:38", "16:55", [SU_LEAD, SU_WING, FE102, FE107], 40, 140, transition=1500)
    add("16:55", "17:11", [SU_LEAD, SU_WING, FE102, FE107], 40, 140, transition=1500)
    follow("17:11", "17:21", AIM_102, 10.5, 40, 330, transition=1000)
    follow("17:21", "17:24", SU_WING, 11.5, 45, 330, transition=1000)
    add("17:24", "17:43", [FE102, FE107, SU_LEAD], 35, 200, orbit=0.2, transition=6000)
    follow("17:43", "17:53", AIM_107, 10.5, 40, 0, transition=1000)
    follow("17:53", "18:00", SU_LEAD, 11.5, 45, 330, transition=1000)
    add("18:00", "18:10", [SU_LEAD, FE107], 40, 0, transition=3000)
    add("18:10", "18:30", [FE102, FE107], 30, 0, transition=10_000)
    follow("18:30", "19:10", FE102, 8.5, 30, 0, transition=20_000)
    shots.append(cue(t("19:10"), DURATION, point(LOD_CENTRE), 5.4, 0, 0, transition=60_000))
    return shots


def pacing(t):
    return [{"start_ms": t(a), "end_ms": t(b), "speed": s} for a, b, s in PACING]


def document(operation, t, tracks):
    return {
        "format": "sokoly-presentation",
        "version": 1,
        "id": "default",
        "name": "Gulf of Sidra incident, 19 August 1981",
        "operation": operation,
        "chapters": [{"title": title, "at_ms": t(at_), "available_ms": t(at_)}
                     for title, at_ in CHAPTERS],
        "camera_track": camera(t, tracks),
        "playback_track": pacing(t),
    }
