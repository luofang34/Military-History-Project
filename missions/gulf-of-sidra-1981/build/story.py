"""Chapters, briefing notes and pacing for the Gulf of Sidra reconstruction.

Times are operation milliseconds from 07:00 Tripoli time (UTC+2). The fight's beats are the
Biddle tape's calls, whose 00:00 is placed at 07:15; quiet stretches play fast and the three
missile flights play at half speed.
"""
from geometry import (AA2, AIM_102, AIM_107, ATOLL_S, DME_S, FE102, FE107, HIT_LEAD_S,
                      HIT_WING_S, MERGE_S, NIMITZ, REJOIN_S, S3A, SU_LEAD, SU_WING, s_ms)

DURATION = 25 * 60_000  # 07:00 to 07:25, past the Pentagon's 07:20 shootdown time


def t(clock):
    """Operation milliseconds for `MM:SS` after 07:00."""
    m, s = clock.split(":")
    return (int(m) * 60 + int(s)) * 1000


CHAPTERS = [
    ("The Line of Death", 0),
    ("Two Fitters leave Ghurdabiya", t("00:20")),
    ("Buster North", t("01:00")),
    ("Fast Eagles on CAP", t("06:00")),
    ("Radar contact, 80 nm", t("11:00")),
    ("Head-on: twenty miles", s_ms(15)),
    ("The Atoll", s_ms(ATOLL_S)),
    ("Kleemann's Sidewinder", s_ms(HIT_WING_S - 3)),
    ("Muczynski's Sidewinder", s_ms(HIT_LEAD_S - 3)),
    ("Clear to defend yourself", s_ms(209)),
    ("Vector north", s_ms(REJOIN_S)),
]

# (from ms, until ms, speed); about three minutes of viewing in all.
PACING = [
    (0, t("00:20"), 4),
    (t("00:20"), t("01:00"), 8),
    (t("01:00"), t("02:30"), 12),
    (t("02:30"), t("11:00"), 48),
    (t("11:00"), t("14:30"), 24),
    (t("14:30"), s_ms(15), 6),
    (s_ms(15), s_ms(ATOLL_S), 3),
    (s_ms(ATOLL_S), s_ms(MERGE_S + 3), 0.5),
    (s_ms(MERGE_S + 3), s_ms(HIT_WING_S - 3), 1.25),
    (s_ms(HIT_WING_S - 3), s_ms(HIT_WING_S), 0.5),
    (s_ms(HIT_WING_S), s_ms(HIT_LEAD_S - 3), 1.25),
    (s_ms(HIT_LEAD_S - 3), s_ms(HIT_LEAD_S), 0.5),
    (s_ms(HIT_LEAD_S), s_ms(186), 1),
    (s_ms(186), s_ms(REJOIN_S), 3),
    (s_ms(REJOIN_S), t("21:00"), 16),
    (t("21:00"), DURATION, 48),
]


def uncertain(a, b):
    return {"kind": "uncertain", "earliest": a, "latest": b}


def notes():
    """(entity or None, from ms, until ms, source, provenance, text, occurrence or None)."""
    S = s_ms
    return [
        (None, 0, DURATION, "ratner-yale-1984", "reported",
         "Line of Death. Libya's October 1973 declaration takes the Gulf of Surt north to "
         "32°30'N as internal waters: a line about 297 nm long from west of Misrata to "
         "northeast of Benghazi. The US rejected it in 1974, and on 19 August 1981 it invoked "
         "high-seas freedom beyond the territorial sea.", None),
        (NIMITZ, 0, t("00:20"), "reconstruction-carrier", "reconstructed",
         "USS Nimitz, north of the line, with Forrestal and a 16-ship task force. The "
         "Pentagon put the carriers \"well to the north, about 100 miles away from the gulf\" "
         "(Washington Post); UPI says 200 miles off the coast. Her position here is inferred "
         "from 107's \"123 DME on the 180\" call, read as her TACAN; bound 40 km.", None),
        (None, 0, t("06:00"), "stanik-1996", "reported",
         "OOMEX exercise, 18–19 August, notified to mariners on 12 August. The carriers stay "
         "north of 32°30'N; one F-14 CAP station lies south of it (Stanik).", None),
        (SU_LEAD, t("00:20"), t("06:00"), "cooper-acig", "reported",
         "About 07:00 (Libyan account: \"7 A.M.\"), two Su-22M3s of 1022 Squadron take off "
         "from Ghurdabiya, near Sirte. Cooper names the pilots as Capt Belkacem Emsik Az Zintani "
         "(lead) and 1st Lt Mokhtar El Arabi Al Jafari; US sources do not name them. An E-2C "
         "of VAW-124, the Bear Aces off Nimitz (cruise book), sees them take off heading north "
         "(ACIG). Its crew, aircraft and orbit are not published.", None),
        (S3A, t("01:00"), t("02:30"), "sanders-2012", "reported",
         "Diamond Cutter 702, a VS-30 S-3A from Forrestal, is orbiting at 10,000 ft about 15 "
         "miles off the shore. On the Hawkeye's warning Nimitz calls \"Buster North, I say "
         "again, Buster North!\" It dives at 10,000 ft a minute to 300 ft and runs north at 450 "
         "mph (Sanders, the copilot). Sanders recalls the Fitters lifting off from Okba Ben "
         "Nafi near Tripoli, not Ghurdabiya; its orbit position is not sourced.", None),
        (FE102, t("06:00"), t("11:00"), "stanik-1996", "reported",
         "Fast Eagle 102 (Cdr Hank Kleemann, Lt Dave Venlet, BuNo 160403) and 107 (Lt Larry "
         "Muczynski, Lt(jg) Jim Anderson, BuNo 160390) of VF-41, off Nimitz since about 06:00, "
         "fly a racetrack CAP at about 300 kt (Stanik). Kleemann is at 18,000 ft, Muczynski "
         "4,000 ft above. The racetrack's shape is not sourced.", None),
        (FE102, t("11:00"), t("14:30"), "stanik-1996", "reported",
         "About 07:11: Venlet has a radar contact due south at 80 nm, coming from Ghurdabiya "
         "(Stanik). The Pentagon briefing gave 30 to 40 miles at about 07:00 (Washington "
         "Post). The E-2C, which also holds the contact, vectors the section south.", None),
        (FE102, t("14:30"), S(15), "reconstruction-engagement", "reconstructed",
         "The Biddle tape starts at about 07:15. Its times are relative; the replay places "
         "them on the Pentagon's 0520Z for the shootdowns.", None),
        (FE102, S(7), S(15), "biddle-tape", "reported",
         "00:07 Bare Ace, the E-2C controller (VAW-124's patch reads BEAR ACE), to 102: "
         "\"226, 36.\" 00:19: \"225 at 33.\" The reference point is not stated.", None),
        (FE102, S(15), S(27), "biddle-tape", "reported",
         "00:15 102: \"Twenty miles ... twenty thousand feet.\"", None),
        (FE102, S(27), S(38), "biddle-tape", "reported", "00:27 102: \"16 miles out.\"", None),
        (FE102, S(38), S(54), "biddle-tape", "reported",
         "00:38 102: \"14 miles, 21,000.\" Closure about 1,000 kt, head-on.", None),
        (FE102, S(54), S(63), "biddle-tape", "reported",
         "00:54 102: \"8 miles.\" Tally-ho: two Fitters in welded wing, under 500 ft apart "
         "(Stanik).", None),
        (FE102, S(63), S(ATOLL_S), "biddle-tape", "reported",
         "01:03 102: \"Twenty thousand feet, 6 miles.\" Kleemann holds the nose on the leader "
         "to pass close aboard; Muczynski is above and to one side.", None),
        (AA2, S(ATOLL_S), S(MERGE_S + 4), "stanik-1996", "reported",
         "The Libyan lead fires one AA-2 Atoll head-on from about 300 m. It passes under 102 "
         "and misses (Stanik; Cooper calls it an R-13M, and ACIG notes a claim that it was a "
         "dropped tank). Launch time is reconstructed from the closure.", None),
        (FE107, S(MERGE_S + 4), S(100), "biddle-tape", "reported",
         "01:31 107: \"Two fitters has shot at my leader.\"", None),
        (SU_WING, S(100), S(HIT_WING_S - 3), "stanik-1996", "reported",
         "The Libyans break: the leader climbs northwest, the wingman turns southeast toward "
         "the coast. The F-14s cross over and turn hard port: Kleemann takes the wingman, "
         "Muczynski the leader (Stanik; Wikipedia citing Brown).", None),
        (AIM_102, S(HIT_WING_S - 3), S(HIT_WING_S), "stanik-1996", "reported",
         "Kleemann waits for the Fitter to clear the sun, then fires one AIM-9L.", None),
        (SU_WING, S(HIT_WING_S), S(154), "biddle-tape", "reported",
         "The wingman is hit in the tailpipe and goes down. 02:21 102: \"It was a clean "
         "target.\" First kill to Fast Eagle 102.", None),
        (FE107, S(154), S(HIT_LEAD_S - 3), "biddle-tape", "reported",
         "02:34 107: \"Want me shoot my guy down?\" 102: \"Shoot him down.\" Muczynski is behind "
         "the leader with one good Sidewinder; his second had failed its pre-launch check "
         "(Cooper).", None),
        (AIM_107, S(HIT_LEAD_S - 3), S(HIT_LEAD_S), "stanik-1996", "reported",
         "Muczynski fires one AIM-9L from about 1,000 yd.", None),
        (SU_LEAD, S(HIT_LEAD_S), S(185), "biddle-tape", "reported",
         "The leader's tail comes off. 02:53 107: \"Fox 2 kill from music.\"", None),
        (SU_LEAD, S(185), S(DME_S), "biddle-tape", "reported",
         "03:05 107: \"His chute is not deploying. He is falling free.\" Libya says both "
         "pilots were picked up by helicopter, and Cooper says Zintani swam for hours. The "
         "Pentagon saw one parachute and a Libyan helicopter and ship heading for the area "
         "(Washington Post); Biddle's Lt Sasser: \"No survivors were ever found.\"",
         uncertain(S(185), S(DME_S))),
        (FE107, S(DME_S), S(209), "biddle-tape", "reported",
         "03:14 107: \"123 DME on the 180,\" fuel 10.2. If the TACAN is Nimitz's, the carrier "
         "is 123 nm due north, which is where the replay puts her.", None),
        (None, S(209), S(REJOIN_S), "biddle-tape", "reported",
         "03:29 \"102, 107, you are clear to defend yourself. Pass from the ship.\" On the tape "
         "the relay comes after both kills; DVIDS describes it as coming before.", None),
        (None, S(REJOIN_S), S(270), "stanik-1996", "reported",
         "03:59 \"Vector north.\" The section rejoins at about 07:19 and heads for Nimitz "
         "(Stanik). UPI: about one minute; the Nimitz cruise book: 45 seconds.", None),
        (None, S(ATOLL_S), S(REJOIN_S), "cooper-acig", "reported",
         "Libyan account (Cooper): Zintani's R-13M destroyed an F-14, and fishermen later "
         "found wreckage. A Libyan radio report put a downed F-14 near Sardinia. The two "
         "claims conflict, and US sources record no F-14 loss.",
         uncertain(S(ATOLL_S), S(REJOIN_S))),
        (None, t("21:00"), DURATION, "upi-1981", "reported",
         "The Pentagon timed the shootdowns at 0520Z, 07:20 here. Within the hour two "
         "MiG-25s ran toward Nimitz at about Mach 1.5 and turned back from VF-41 and VF-84 "
         "Tomcats (Cooper). Libyan helicopters searched for the pilots for hours.", None),
    ]


def annotations(em):
    for entity, start, until, source, provenance, text, occurrence in notes():
        em.note(source, entity, start, until, text, provenance, [], occurrence=occurrence)


def document(operation, camera_track):
    return {
        "format": "sokoly-presentation",
        "version": 1,
        "id": "default",
        "name": "Gulf of Sidra incident, 19 August 1981",
        "operation": operation,
        "chapters": [{"title": title, "at_ms": at, "available_ms": at} for title, at in CHAPTERS],
        "camera_track": camera_track,
        "playback_track": [{"start_ms": a, "end_ms": b, "speed": s} for a, b, s in PACING],
    }
