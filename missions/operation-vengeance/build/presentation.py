"""Chapters, briefing text, camera shots and pacing for the reconstruction."""
from composition import INTENTS
from pacing import after_viewing
from sites import (L, DURATION, PEARL_HARBOR, LAKUNAI, CRASH_T1_323, DITCH_T1_326, YAMAMOTO,
                   UGAKI)
import ledger
from evidence import DISPUTES

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
    ("09:42:30", "09:45:40", 16),
    ("09:45:40", "10:05:00", 64),
]

REPORT = "13th-fighter-command-report"
PW = "pacific-wrecks"
DECRYPT = "decrypt-ntf131755"
REVIEW = "barber-v-widnall"

# (entity the note is about, or None for the whole operation; from, until, source, text)
BRIEFINGS = [
    (None, "07:24:30", "07:25:00", DECRYPT,
     "14 April 1943 (Hawaii date): US Navy codebreakers read JN-25 message NTF131755. "
     "Admiral Yamamoto will fly Rabaul to Ballale on 18 April, departing 06:00 Tokyo time "
     "(08:00 here) with six fighters. Nimitz authorised the intercept on 17 April. "
     "Clock: Henderson Field time, UTC+11; Tokyo time is two hours behind."),
    (None, "07:25:00", "07:31:00", "wikipedia-operation-vengeance",
     "Wheels-up 07:25 from Fighter Two (Kukum), Guadalcanal: 18 P-38Gs of the 339th Fighter "
     "Squadron, 347th Fighter Group, with pilots from its 12th and 70th Squadrons, on drop "
     "tanks. Take-off order and runway heading are reconstructed."),
    ("MCLANAHAN", "07:27:20", "07:35:30", "wikipedia-operation-vengeance",
     "Lt James McLanahan blows a tyre on the take-off roll. Holmes takes his place in "
     "Lanphier's attack section."),
    ("MOORE", "07:36:00", "07:45:00", "wikipedia-operation-vengeance",
     "Lt Joseph Moore's drop tanks will not feed; he turns back and Hine fills the fourth "
     "attack slot. Sixteen P-38s continue under radio silence, 10 to 30 ft above the sea."),
    ("MITCHELL", "07:45:00", "08:04:30", "reconstruction-p38-route",
     "Mitchell navigates by compass, clock and airspeed alone, 10 to 30 ft above the sea. "
     "The track is reconstructed from the published headings, within 20 km."),
    (YAMAMOTO, "08:04:30", "08:20:00", PW,
     "Lakunai, Rabaul, 06:05–06:10 Tokyo time: Yamamoto boards G4M1 T1-323 (FWO Takeo "
     "Kotani); Vice Admiral Ugaki follows in T1-326 (FPO2c Hiroshi Hayashi). Six A6M Zeros "
     "of the 204th Kōkūtai escort. The route south-east is a low-confidence reconstruction."),
    (None, "08:08:30", "08:30:00", "wikipedia-operation-vengeance",
     "The bombers climb to 6,500 ft; the six Zeros fly 1,500 ft higher at their four "
     "o'clock, in two V-formations of three."),
    (None, "08:30:00", "08:52:00", "historynet-death-by-p38",
     "08:20, slightly more than 180 miles west of Henderson: Mitchell turns, then flies 27 "
     "minutes on 290° and 38 minutes on 305°. The plan kept the track 20 nautical miles off "
     "every island (Condon)."),
    (None, "08:52:00", "09:18:00", REPORT,
     "Mitchell's plan is to meet the bombers at 09:35, before they reach Ballale. Both "
     "formations converge on Bougainville's south-west coast."),
    (None, "09:18:00", "09:34:00", "reconstruction-p38-route",
     "Final turn north-east toward the coast, 56 mi out; when it was made is disputed."),
    ("CANNING", "09:34:00", "09:35:40", "warfare-history-network-ames",
     "Lt Doug Canning breaks radio silence: “Bogeys! Eleven o'clock, high!” (Ames; the "
     "report has a quiet “Eleven O' clock”). The Bettys are at 4,500 ft. Tanks drop and "
     "Mitchell's twelve climb toward 18,000 ft. Holmes's tanks hang; he and Hine turn out "
     "to sea to shake them."),
    ("LANPHIER", "09:35:40", "09:36:40", "wikipedia-operation-vengeance",
     "Three Zeros (which section is inferred) peel down in a string at Lanphier; he turns up "
     "into them firing and climbs to 6,000 ft. Barber banks hard behind the bombers, which "
     "split — T1-323 for the "
     "jungle, T1-326 for the sea."),
    ("BARBER", "09:36:40", "09:37:40", PW,
     "Barber fires from directly astern of T1-323 while Zeros make passes on him; its right "
     "engine and tail are hit. Inspection of the wreck found only rear-quarter hits."),
    (YAMAMOTO, "09:38:00", "09:39:20", PW,
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
    ("HINE", "09:39:40", "09:45:40", "13th-fighter-command-report",
     "Past Ballale and Shortland the fighters clash again; Holmes and Barber each claim a "
     "Zero. Hine, his left engine smoking, is last seen south of Shortland, losing height on "
     "the way home."),
    (None, "09:42:30", "09:52:00", REPORT,
     "Mitchell calls the flight home as Kahili's fighters raise dust taking off; the cover "
     "flight never fires. Claimed: three Bettys and three Zeros. Actual Japanese losses: "
     "two Bettys, no Zeros."),
    (None, "09:52:00", "10:05:00", REVIEW,
     "Holmes, nearly out of fuel, lands in the Russell Islands escorted by Canning; the rest "
     "are back on Guadalcanal about 11:40. Japan announces Yamamoto's death on 21 May. Credit "
     "for T1-323 remains officially shared between Lanphier and Barber."),
]

# What the cover flight does while the attack section fights below it.
COVER_NOTE = ("MITCHELL", "09:35:40", "09:42:30", REPORT,
              "Top cover: Mitchell's twelve climb to 18,000 ft over Empress Augusta Bay, "
              "orbiting to meet fighters expected up from Kahili. None come up in time; the "
              "cover flight never fires.")


def annotations(em, names):
    """Briefings, then each disputed fact as tools/ledger.py emits it; `names` maps source
    ids to their names."""
    for entity, start, until, source, text in BRIEFINGS:
        end = DURATION + 1 if until == "10:05:00" else L(until)
        em.note(source, entity, L(start), end, text, "reported", [])
    entity, start, until, source, text = COVER_NOTE
    em.note(source, entity, L(start), L(until), text, "reported", [])
    ledger.emit(em, DISPUTES, L, "reconstruction-estimate")


RUNWAY = (160.012, -9.4265)
T0 = L("07:24:30")
Y, U = YAMAMOTO, UGAKI

# (from, until, target, zoom, pitch, bearing, intent, entities it shows, options): the target
# is a (lon, lat) point or an entity id; moves take 1.5 s of viewing unless `move` says.
SHOTS = [
    (T0, T0 + 1500, PEARL_HARBOR, 11.5, 35, 0,
     "Pearl Harbor, where the codebreakers read the itinerary: the story starts with the "
     "intercept.", [], {"move": 0}),
    (T0 + 1500, T0 + 3500, PEARL_HARBOR, 1.9, 0, 0,
     "Pull back to the whole Pacific: the reach of one decrypted message.", [], {"move": 2}),
    (T0 + 3500, T0 + 6700, (162.0, -8.0), 1.7, 0, 0,
     "Swing across the ocean to the Solomons.", [], {"move": 3.2}),
    (T0 + 6700, T0 + 8200, (159.8, -9.3), 6.0, 0, 0,
     "Down onto Guadalcanal and its fighter strip.", ["FIGHTER TWO"], {"move": 1.5}),
    (T0 + 8200, T0 + 11_200, RUNWAY, 14.2, 45, 340,
     "Down to Fighter Two, Mitchell's P-38 at the head of the line.",
     ["MITCHELL", "FIGHTER TWO"], {"move": 3, "focus": "MITCHELL"}),
    (T0 + 11_200, "07:25:00", RUNWAY, 14.2, 45, 340,
     "Hold on the line of P-38s while the briefing finishes.", ["MITCHELL"],
     {"move": 0, "orbit": -0.1, "focus": "MITCHELL"}),
    ("07:25:00", "07:27:10", RUNWAY, 13.6, 50, 338,
     "The take-off roll, Lanphier's attack section among the first away.", ["LANPHIER"],
     {"orbit": -0.01, "focus": "LANPHIER"}),
    ("07:27:10", "07:28:30", (160.006, -9.4265), 14.4, 50, 330,
     "McLanahan's tyre blows on the roll: the attack section loses its first man.",
     ["MCLANAHAN"], {"focus": "MCLANAHAN"}),
    ("07:28:30", "07:31:00", (160.0, -9.385), 11.6, 35, 300,
     "The formation gathers over the field.", ["LANPHIER"], {"focus": "LANPHIER"}),
    ("07:31:00", "07:35:30", "MITCHELL", 10.4, 40, 280,
     "Mitchell leads them out to sea.", ["MITCHELL"], {"focus": "MITCHELL"}),
    # Moore heads home down the screen; turning the camera with him would spin the view.
    ("07:35:30", "07:38:00", "MOORE", 10.8, 40, 280,
     "Moore turns back with tanks that will not feed; Hine takes his place.", ["MOORE"],
     {"focus": "MOORE"}),
    ("07:38:00", "07:52:00", "MITCHELL", 8.3, 25, 280,
     "Sixteen P-38s settle at wave-top height under radio silence.", ["MITCHELL"],
     {"move": 2, "focus": "MITCHELL"}),
    ("07:52:00", "08:04:30", (158.6, -8.95), 7.8, 20, 280,
     "The long run west along the Solomons, below the islanders' lookouts.", ["MITCHELL"],
     {"move": 2.5}),
    ("08:04:30", "08:06:30", LAKUNAI, 13.8, 50, 150,
     "Cut to Rabaul: Yamamoto boards T1-323 at Lakunai, and the target is on the map.",
     [Y, "LAKUNAI"], {"move": 0, "focus": Y}),
    ("08:06:30", "08:08:30", Y, 12.6, 45, 140,
     "The two Bettys and their six Zeros take off.", [Y, U], {"move": 1.5, "focus": Y}),
    ("08:08:30", "08:30:00", Y, 8.6, 30, 130,
     "The admiral's formation climbs south-east toward Bougainville.", [Y, U],
     {"move": 2.5, "focus": Y}),
    ("08:30:00", "08:52:00", "MITCHELL", 8.5, 25, 300,
     "Cut back to the hunters on their dog-legs, kept out of sight of land.", ["MITCHELL"],
     {"move": 0, "focus": "MITCHELL"}),
    ("08:52:00", "09:08:00", (156.3, -7.6), 6.4, 10, 0,
     "Both formations on one map, converging on Bougainville's coast.", ["MITCHELL", Y],
     {"move": 3}),
    ("09:08:00", "09:22:00", "MITCHELL", 8.8, 30, 330,
     "The P-38s' final leg toward the coast.", ["MITCHELL"],
     {"move": 2.5, "focus": "MITCHELL"}),
    ("09:22:00", "09:28:00", Y, 9.6, 40, 130,
     "Cut to the Bettys, on schedule for Ballale.", [Y], {"move": 0, "focus": Y}),
    ("09:28:00", "09:32:00", "MITCHELL", 10.8, 50, 40,
     "Cut back to the P-38s: the cross-cutting quickens as they close.", ["MITCHELL"],
     {"move": 0, "focus": "MITCHELL"}),
    ("09:32:00", "09:34:00", "MITCHELL", 11.4, 45, 20,
     "Turn toward the coast with Canning, the man who will see them first.",
     ["MITCHELL", "CANNING"], {"move": 2, "focus": "CANNING"}),
    ("09:34:00", "09:35:40", (155.39, -6.76), 12.6, 50, 30,
     "The sighting: P-38s and bombers in one frame as the tanks drop and the climb begins.",
     ["CANNING", Y], {"move": 2, "orbit": 0.12, "focus": "CANNING"}),
    ("09:35:40", "09:36:40", (155.45, -6.765), 12.6, 55, 50,
     "Lanphier turns into the diving Zeros as the bombers split.", ["LANPHIER", Y, U],
     {"move": 2, "focus": "LANPHIER"}),
    ("09:36:40", "09:37:50", "BARBER", 13.8, 55, 100,
     "Behind Barber as he fires into T1-323.", ["BARBER", Y],
     {"move": 1.5, "focus": "BARBER"}),
    ("09:37:50", "09:38:10", CRASH_T1_323, 14.2, 55, 110,
     "T1-323 goes into the jungle inland of Moila Point.", [Y],
     {"move": 1.5, "focus": Y}),
    ("09:38:10", "09:39:20", "HOLMES", 13.4, 55, 80,
     "Holmes and Hine, back in the fight, catch T1-326 low over the water.", ["HOLMES", U],
     {"move": 1.5, "focus": "HOLMES"}),
    ("09:39:20", "09:39:40", DITCH_T1_326, 13.4, 55, 80,
     "T1-326 ditches off Moila Point.", [U], {"move": 1.5, "focus": U}),
    ("09:39:40", "09:40:20", (155.56, -6.82), 10.6, 30, 80,
     "The fight at a glance: top cover overhead, both wrecks, the chase past Kahili.",
     ["HOLMES", "HINE", "LANPHIER", "MITCHELL", Y, U], {"move": 1.5}),
    ("09:40:20", "09:41:10", "HINE", 12.4, 50, 95,
     "Find Hine as the fighters clash again past Ballale.", ["HINE"],
     {"move": 1.5, "focus": "HINE"}),
    ("09:41:10", "09:45:40", "HINE", 11.4, 40, 160,
     "Stay with Hine, his engine smoking, until he is last seen south of Shortland.",
     ["HINE"], {"move": 1.5, "focus": "HINE"}),
    ("09:45:40", "09:52:00", "MITCHELL", 9.5, 35, 150,
     "Mitchell calls the flight home.", ["MITCHELL"], {"move": 2, "focus": "MITCHELL"}),
    ("09:52:00", DURATION, (157.5, -8.0), 1.8, 0, 0,
     "Pull out over the Solomons as they return, while the briefing gives the outcome.", [],
     {"move": 9}),
]


def ms(clock):
    return clock if isinstance(clock, int) else L(clock)


def pacing():
    """The story's pacing in operation ms."""
    return [(L(a), L(b), s) for a, b, s in PACING]


def camera():
    """(camera cues, each shot's intent and the entities it shows, by start_ms)."""
    pace = pacing()
    cues, intents = [], {}
    for start, end, target, zoom, pitch, bearing, intent, shows, opts in SHOTS:
        a, b = ms(start), ms(end)
        aim = ({"kind": "entity", "value": target} if isinstance(target, str)
               else {"kind": "point", "value": {"lon": target[0], "lat": target[1]}})
        move = after_viewing(pace, a, opts.get("move", 1.5)) - a
        c = {"start_ms": a, "end_ms": b, "target": aim, "zoom": zoom, "pitch": pitch,
             "bearing": bearing, "orbit_deg_s": opts.get("orbit", 0.0),
             "transition_ms": min(move, b - a)}
        if "focus" in opts:
            c["focus"] = opts["focus"]
        cues.append(c)
        intents[str(a)] = {"intent": intent, "shows": shows}
    return cues, intents


def document(operation):
    cues, intents = camera()
    return {
        "format": "sokoly-presentation",
        "version": 1,
        "id": "default",
        "name": "Operation Vengeance",
        "operation": operation,
        "chapters": [{"title": t, "at_ms": L(at), "available_ms": L(at)} for t, at in CHAPTERS],
        "camera_track": cues,
        "playback_track": [{"start_ms": a, "end_ms": b, "speed": s} for a, b, s in pacing()],
        "extensions": {INTENTS: intents},
    }
