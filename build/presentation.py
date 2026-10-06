"""Chapters, briefing text, camera shots and pacing for the reconstruction."""
from sites import (L, DURATION, PEARL_HARBOR, LAKUNAI, CRASH_T1_323, DITCH_T1_326, YAMAMOTO,
                   UGAKI)
from engagement import HINE_LAST

CHAPTERS = [
    ("Decrypted itinerary", "07:24:30"),
    ("Take-off from Fighter Two", "07:25:00"),
    ("Moore turns back", "07:36:00"),
    ("Yamamoto departs Lakunai", "08:05:00"),
    ("Wave-top transit", "08:08:30"),
    ("Final leg to Bougainville", "09:18:00"),
    ("Bogeys, eleven o'clock high", "09:34:00"),
    ("Attack on T1-323", "09:35:40"),
    ("T1-326 off Moila Point", "09:38:10"),
    ("Hine missing", "09:39:40"),
    ("Egress", "09:42:30"),
]

PACING = [
    ("07:24:30", "07:24:42", 1),
    ("07:24:42", "07:25:00", 6),
    ("07:25:00", "07:28:30", 20),
    ("07:28:30", "07:31:00", 48),
    ("07:31:00", "07:35:30", 64),
    ("07:35:30", "07:38:00", 32),
    ("07:38:00", "08:04:30", 64),
    ("08:04:30", "08:08:30", 24),
    ("08:08:30", "09:28:00", 64),
    ("09:28:00", "09:32:00", 32),
    ("09:32:00", "09:34:00", 12),
    ("09:34:00", "09:35:40", 6),
    ("09:35:40", "09:38:10", 3),
    ("09:38:10", "09:39:40", 3),
    ("09:39:40", "09:42:30", 8),
    ("09:42:30", "10:05:00", 64),
]

REPORT = "13th-fighter-command-report"
PW = "pacific-wrecks"
DECRYPT = "decrypt-ntf131755"
MACR = "macr-599-609"
REVIEW = "barber-v-widnall"

# (entity, from, until, source, text)
BRIEFINGS = [
    ("MITCHELL", "07:24:30", "07:25:00", DECRYPT,
     "14 April 1943 (Hawaii date): US Navy codebreakers read JN-25 message NTF131755. "
     "Admiral Yamamoto will fly Rabaul to Ballale on 18 April, departing 06:00 Tokyo time "
     "(08:00 here) with six fighters. Nimitz authorised the intercept on 17 April. "
     "Clock: Henderson Field time, UTC+11; Tokyo time is two hours behind."),
    ("JACOBSON", "07:25:00", "07:27:20", REPORT,
     "Wheels-up 07:25 from Fighter Two, Guadalcanal: 18 P-38Gs of the 339th, 12th and 70th "
     "Fighter Squadrons, each carrying a 165-gal and a 310-gal drop tank. "
     "Take-off order and runway heading are reconstructed."),
    ("MCLANAHAN", "07:27:20", "07:31:00", "wikipedia-operation-vengeance",
     "Lt James McLanahan blows a tyre on the take-off roll. Holmes takes his place in "
     "Lanphier's attack section."),
    ("MOORE", "07:36:00", "07:45:00", "wikipedia-operation-vengeance",
     "Lt Joseph Moore's drop tanks will not feed; he turns back and Hine fills the fourth attack slot. Sixteen "
     "P-38s continue under radio silence, 10 to 30 ft above the sea."),
    ("GOERKE", "07:45:00", "08:04:30", "reconstruction",
     "Mitchell navigates by compass, clock and airspeed. Track reconstructed from the "
     "published 290° and 305° legs read as magnetic headings and Condon's 20 nmi island "
     "stand-off; it reproduces the reported 08:20 turn 180 mi west of Henderson and about "
     "435 mi at about 215 mph (the report implies about 200). Position bound ±20 km."),
    ("MORISAKI", "08:04:30", "08:08:30", PW,
     "Lakunai, Rabaul, 06:05–06:10 Tokyo time: Yamamoto boards G4M1 T1-323 (FWO Takeo "
     "Kotani); Vice Admiral Ugaki follows in T1-326 (FPO2c Hiroshi Hayashi). Six A6M Zeros "
     "of the 204th Kōkūtai escort. The route south-east is a low-confidence reconstruction."),
    ("SUGITA", "08:08:30", "08:30:00", REPORT,
     "The bombers cruise at 6,500 ft; the Zeros fly 1,500 ft above and behind in two "
     "sections of three. Ceiling and visibility unlimited."),
    ("KITTEL", "08:30:00", "08:52:00", "historynet-death-by-p38",
     "08:20 and 08:47: the P-38s turn north-west, then again abreast of Vella Lavella, "
     "keeping clear of Japanese lookouts on New Georgia and the Treasuries."),
    ("WHITTAKER", "08:52:00", "09:18:00", "air-and-space-forces",
     "Mitchell's plan aims for 09:35, ten minutes before the expected landing at Ballale "
     "(09:45; the decrypt itself gives 08:00 Tokyo, i.e. 10:00 here). Both formations "
     "converge on Bougainville's south-west coast."),
    ("AMES", "09:18:00", "09:34:00", "reconstruction",
     "Final turn north-east toward the coast. Sources place it between 09:00 and 09:25; "
     "the reconstruction turns at 09:18, 56 mi out."),
    ("CANNING", "09:34:00", "09:35:40", REPORT,
     "09:34 — Lt Doug Canning: “Bogeys, eleven o'clock high.” The Bettys are "
     "descending through 4,500 ft. Tanks drop and Mitchell's twelve climb toward 18,000 ft. "
     "Holmes's tanks hang; he and Hine turn out to sea to shake them."),
    ("LANPHIER", "09:35:40", "09:36:40", "wikipedia-operation-vengeance",
     "Three Zeros (which section is inferred) peel down in a string at Lanphier; he turns up into them firing and climbs "
     "to 6,000 ft. Barber banks hard behind the bombers, which split — T1-323 for the "
     "jungle, T1-326 for the sea."),
    ("BARBER", "09:36:40", "09:37:40", PW,
     "Barber fires from directly astern of T1-323 while Zeros make passes on him; its right "
     "engine and tail are hit. Inspection of the wreck found only rear-quarter hits."),
    (YAMAMOTO, "09:38:00", "09:38:10", PW,
     "T1-323 crashes into the jungle inland of Moila Point (6°47.2'S 155°33.1'E). "
     "Admiral Yamamoto and all ten others aboard are killed."),
    ("HOLMES", "09:38:10", "09:39:20", PW,
     "Holmes and Hine, back from shedding tanks, drive the Zeros off Barber, then catch "
     "T1-326 low over the water off Moila Point; Barber joins and is hit by its debris. "
     "Two Zeros chase Lanphier past Kahili at treetop height; he outruns them with two "
     "7.7 mm hits in his tailplane."),
    (UGAKI, "09:39:20", "09:39:40", PW,
     "T1-326 ditches about 100 m off Moila Point. Ugaki, Hayashi and Captain Kitamura survive; "
     "11 of 14 aboard die."),
    ("HINE", "09:39:40", "09:42:30", MACR,
     "Past Ballale and Shortland the fighters clash again: Holmes and Barber each fire on a "
     "Zero, and Sugita (by his account) hits Hine's left engine. Hine is last seen with Zeros making passes — "
     "MACR 599: four miles north of Shortland; MACR 609: south of it, 09:40. He is never "
     "found. Yanagiya has dived to Buin to fire an alarm burst over the airfield."),
    ("GRAEBNER", "09:42:30", "09:52:00", REPORT,
     "Mitchell calls the flight home as Kahili's fighters raise dust taking off; the cover "
     "flight never fires. Claimed: three Bettys and three Zeros. Actual Japanese losses: "
     "two Bettys, no Zeros."),
    ("STRATTON", "09:52:00", "10:05:00", REVIEW,
     "Holmes, nearly dry, lands in the Russell Islands escorted by Canning; the rest are back "
     "at Guadalcanal about 11:40. A Japanese army patrol under Lt Hamasuna finds the wreck on "
     "19 April; Japan announces Yamamoto's death on 21 May. Credit for T1-323 remains "
     "officially shared between Lanphier and Barber."),
]

# Disputed occurrence windows: marked on the timeline, excluded from definite state.
UNCERTAIN = [
    ("ANGLIN", "09:36:00", "09:50:00", "ja-wikipedia-kaigun-ko-jiken",
     "T1-323 down: US accounts 09:36–09:40, Japanese accounts 07:45–07:50 Tokyo (09:45–09:50)."),
    ("SMITH", "09:38:00", "09:50:00", PW,
     "T1-326 ditching: US accounts about 09:38–09:45; Japanese accounts as late as 07:50 Tokyo."),
    ("LONG", "09:40:00", "09:42:00", MACR, "Hine last seen: MACR 609 gives 09:40."),
]


def annotations(em):
    for entity, start, until, source, text in BRIEFINGS:
        end = DURATION + 1 if until == "10:05:00" else L(until)
        em.note(source, entity, L(start), end, text, "reported", [])
    for entity, start, latest, source, text in UNCERTAIN:
        em.note(source, entity, L(start), L(latest) + 1, text, "reported", [],
                occurrence={"kind": "uncertain", "earliest": L(start), "latest": L(latest)})


def point(p):
    return {"kind": "point", "value": {"lon": p[0], "lat": p[1]}}


def entity(e):
    return {"kind": "entity", "value": e}


def cue(start, end, target, zoom, pitch, bearing, orbit=0.0, transition=0, focus=None):
    c = {
        "start_ms": start if isinstance(start, int) else L(start),
        "end_ms": end if isinstance(end, int) else L(end),
        "target": target, "zoom": zoom, "pitch": pitch, "bearing": bearing,
        "orbit_deg_s": orbit, "transition_ms": transition,
    }
    if focus:
        c["focus"] = focus
    return c


def camera():
    runway = (160.012, -9.4265)
    t0 = L("07:24:30")
    return [
        cue(t0, t0 + 300, point(PEARL_HARBOR), 11.5, 35, 0),
        cue(t0 + 300, t0 + 2300, point(PEARL_HARBOR), 1.9, 0, 0, transition=2000),
        cue(t0 + 2300, t0 + 5500, point((162.0, -8.0)), 1.7, 0, 0, transition=3200),
        cue(t0 + 5500, t0 + 7000, point((159.8, -9.3)), 6.0, 0, 0, transition=1500),
        cue(t0 + 7000, t0 + 10_000, point(runway), 14.2, 45, 340, transition=3000,
            focus="MITCHELL"),
        cue(t0 + 10_000, "07:25:00", point(runway), 14.2, 45, 340, orbit=-0.1,
            focus="MITCHELL"),
        cue("07:25:00", "07:27:10", point(runway), 13.6, 50, 340 - 2.0, orbit=-0.01,
            transition=8000, focus="MITCHELL"),
        cue("07:27:10", "07:28:30", point((160.006, -9.4265)), 14.4, 50, 330, transition=6000,
            focus="MCLANAHAN"),
        cue("07:28:30", "07:31:00", point((160.0, -9.385)), 11.6, 35, 300, transition=40_000,
            focus="LANPHIER"),
        cue("07:31:00", "07:35:30", entity("MITCHELL"), 10.4, 40, 280, transition=40_000,
            focus="MITCHELL"),
        cue("07:35:30", "07:38:00", entity("MOORE"), 10.8, 40, 110, transition=20_000,
            focus="MOORE"),
        cue("07:38:00", "08:04:30", entity("MITCHELL"), 8.3, 25, 280, transition=120_000,
            focus="MITCHELL"),
        cue("08:04:30", "08:06:30", point(LAKUNAI), 13.8, 50, 150, focus="MORISAKI"),
        cue("08:06:30", "08:08:30", entity(YAMAMOTO), 12.6, 45, 140, transition=40_000,
            focus=YAMAMOTO),
        cue("08:08:30", "08:30:00", entity(YAMAMOTO), 8.6, 30, 130, transition=180_000,
            focus=YAMAMOTO),
        cue("08:30:00", "08:52:00", entity("MITCHELL"), 8.5, 25, 300, focus="MITCHELL"),
        cue("08:52:00", "09:08:00", point((156.3, -7.6)), 6.4, 10, 0, transition=240_000),
        cue("09:08:00", "09:22:00", entity("MITCHELL"), 8.8, 30, 330, transition=180_000,
            focus="MITCHELL"),
        cue("09:22:00", "09:28:00", entity(YAMAMOTO), 9.6, 40, 130, focus=YAMAMOTO),
        cue("09:28:00", "09:32:00", entity("MITCHELL"), 10.8, 50, 40, focus="MITCHELL"),
        cue("09:32:00", "09:34:00", entity("MITCHELL"), 11.4, 45, 20, transition=40_000,
            focus="CANNING"),
        cue("09:34:00", "09:35:40", point((155.39, -6.76)), 12.6, 50, 30, orbit=0.12,
            transition=20_000, focus="CANNING"),
        cue("09:35:40", "09:36:40", point((155.45, -6.765)), 13.1, 55, 50, transition=10_000,
            focus="LANPHIER"),
        cue("09:36:40", "09:37:50", entity("BARBER"), 13.8, 55, 100, transition=8000,
            focus="BARBER"),
        cue("09:37:50", "09:38:10", point(CRASH_T1_323), 14.2, 55, 110, transition=6000,
            focus=YAMAMOTO),
        cue("09:38:10", "09:39:20", point((155.555, -6.853)), 13.6, 55, 80, transition=8000,
            focus="HOLMES"),
        cue("09:39:20", "09:39:40", point(DITCH_T1_326), 13.4, 55, 80, transition=6000,
            focus=UGAKI),
        cue("09:39:40", "09:41:10", entity("HINE"), 12.4, 50, 95, transition=10_000,
            focus="HINE"),
        cue("09:41:10", "09:42:30", point(HINE_LAST), 12.2, 45, 95, transition=10_000,
            focus="HINE"),
        cue("09:42:30", "09:52:00", entity("MITCHELL"), 9.5, 35, 150, transition=120_000,
            focus="MITCHELL"),
        cue("09:52:00", DURATION, point((157.5, -8.0)), 1.8, 0, 0, transition=600_000),
    ]


def operation_presentation():
    return {
        "chapters": [{"title": t, "at_ms": L(at), "available_ms": L(at)} for t, at in CHAPTERS],
        "camera_track": camera(),
        "playback_track": [{"start_ms": L(a), "end_ms": L(b), "speed": s} for a, b, s in PACING],
    }

