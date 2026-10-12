"""The story camera: one shot per beat, contiguous from the start to the end of the record.

Every shot is fitted to its subjects by `framing.Framer`; subjects are Lancasters, mines, the
flood front, fixed sites, or the run-in points that frame an attack. Each shot states what it
is for; tools/composition.py prints that beside what the viewer's frame report shows.
"""
from drops import chase_ms, releases, sequence
from framer import Framer
from sites import CRASH, DURATION, FIXED, HAMMERBERG, L, NEHEIM_CAMP, WALDECK
from targets import ENNEPE_START, MOHNE_START, SORPE_START, STEEPLE_START

POINTS = {
    "MÖHNE RUN-IN": MOHNE_START, "SORPE RUN-IN": SORPE_START, "ENNEPE RUN-IN": ENNEPE_START,
    "LANGSCHEID RUN-IN": STEEPLE_START,
    "WALDECK": WALDECK, "HAMMERBERG": HAMMERBERG, "NEHEIM": NEHEIM_CAMP,
    "OSTÖNNEN": CRASH["AJ-M"][0], "CASTRICUM": CRASH["AJ-A"][0], "HALDERN": CRASH["AJ-E"][0],
}


# (from, until, subjects, intent, framing): moves last 1.5 s of viewing unless `move` says.
SHOTS = [
    (0, "21:27:30", ["SCAMPTON", "MÖHNE", "EDER", "SORPE"],
     "Where and why: the base and the three target dams on one map while the briefing sets "
     "out the night's task.", {"move": 0}),
    ("21:27:30", "21:32", ["SCAMPTON", "AJ-E", "AJ-W", "AJ-K", "AJ-H"],
     "Fly in from the map to Scampton as the second wave leaves singly for the northern "
     "route.", {"pitch": 40, "move": 2.5}),
    ("21:32", "21:38", ["AJ-E", "AJ-W", "AJ-K", "AJ-H"],
     "Ride out with Barlow, leading the second wave toward the coast.",
     {"follow": "AJ-E", "pitch": 20, "pad_km": 4}),
    ("21:38", "21:41", ["SCAMPTON", "AJ-G", "AJ-M", "AJ-P"],
     "Gibson's vic takes off together: the leader whose calls will run the attack.",
     {"pitch": 40, "pad_km": 1.5}),
    ("21:41", "21:46", ["AJ-G", "AJ-M", "AJ-P"],
     "Gibson's vic forms up and turns away: the formation the story follows to the Möhne.",
     {"follow": "AJ-G", "pitch": 30, "pad_km": 2}),
    ("21:46", "21:49", ["SCAMPTON", "AJ-A", "AJ-J", "AJ-L"],
     "Young's vic leaves eight minutes behind, briefly: the same field and the same drill.",
     {"pitch": 40, "pad_km": 1.5}),
    ("21:49", "21:58", ["AJ-A", "AJ-J", "AJ-L"],
     "Young's vic sets course after Gibson's.",
     {"follow": "AJ-A", "pitch": 30, "pad_km": 2}),
    ("21:58", "22:02", ["SCAMPTON", "AJ-Z", "AJ-B", "AJ-N", "AJ-T"],
     "The last vic leaves, and McCarthy sets off twenty minutes late in the spare aircraft.",
     {"pitch": 40, "pad_km": 1.5}),
    ("22:02", "22:50", ["AJ-G", "AJ-E", "SCAMPTON"],
     "Pull out to both routes over the North Sea, timed to cross the enemy coast together: "
     "the second wave north for Vlieland, the first south for the Scheldt.", {"move": 3}),
    ("22:50", "23:03", ["AJ-W", "AJ-K", "AJ-H", "AJ-E"],
     "The second wave at Vlieland: within ten minutes three of its five are lost or turned "
     "back.", {"pitch": 25, "move": 2}),
    ("23:03", "23:46", ["AJ-G", "AJ-A", "AJ-Z"],
     "Back to the first wave, low across Holland toward the Rhine.",
     {"follow": "AJ-G", "pitch": 20, "pad_km": 10, "move": 2}),
    ("23:46", "23:52", ["AJ-E", "HALDERN"],
     "Barlow's last minutes: the cables at Haldern.", {"pitch": 40, "pad_km": 3, "move": 2}),
    ("23:52", "00:12", ["AJ-G", "AJ-A"],
     "The leading section through the searchlights and flak past Haltern, where Hopgood is "
     "hit.", {"follow": "AJ-G", "pitch": 25, "pad_km": 8, "move": 2}),
    ("00:12", "00:17", ["AJ-B", "AJ-Z", "AJ-N"],
     "Astell, lagging behind Maudslay's section, strikes cables near Marbeck.",
     {"pitch": 35, "pad_km": 2}),
    ("00:17", "00:27", ["MÖHNE", "AJ-G", "AJ-M", "AJ-P", "AJ-A", "AJ-J", "AJ-L"],
     "The first wave reaches the Möhne and settles into its circuits over the hills: the "
     "stage for the attacks.", {"pitch": 35, "move": 2.5}),
    ("00:27", "00:31", ["MÖHNE", "MÖHNE RUN-IN", "UPKEEP AJ-G"],
     "Down onto the run-in from the lake: Gibson's attack, and his mine bursting short.",
     {"pitch": 50, "pad_km": 0.8, "move": 2}),
    ("00:31", "00:35", ["MÖHNE", "MÖHNE RUN-IN", "OSTÖNNEN", "UPKEEP AJ-M"],
     "Widen to take in Ostönnen: Hopgood hit on the run, his mine over the parapet, his "
     "crash.", {"pitch": 45}),
    ("00:35", "00:41", ["MÖHNE", "MÖHNE RUN-IN", "UPKEEP AJ-P"],
     "Back on the run-in: Martin attacks with Gibson alongside drawing the flak, and his mine "
     "bursts short.", {"pitch": 50, "pad_km": 0.8}),
    ("00:41", "00:44", ["MÖHNE", "UPKEEP AJ-A"],
     "Closer on the wall for Young: his mine meets it, and the dam still stands.",
     {"pitch": 55, "pad_km": 1.5}),
    ("00:44", "00:47", ["SORPE", "LANGSCHEID RUN-IN", "UPKEEP AJ-T"],
     "Cut away to the Sorpe: McCarthy, alone of his wave, comes in over Langscheid's steeple "
     "and drops along the crest of the earth dam, and it holds.",
     {"pitch": 50, "pad_km": 1.0, "move": 0}),
    ("00:47", "00:50", ["MÖHNE", "MÖHNE RUN-IN", "UPKEEP AJ-J"],
     "Cut back to the Möhne for Maltby's attack, the one that breaks it.",
     {"pitch": 50, "pad_km": 0.8, "move": 0}),
    ("00:50", "00:50:09", ["MÖHNE"],
     "The breach as Fray photographed it from the air the next morning, shown from his "
     "camera.", {"focus": "MÖHNE", "pitch": 50, "pad_km": 0.8, "move": 0}),
    ("00:50:09", "00:50:18", ["MÖHNE"],
     "The breach from below the wall, as photographed later that month.",
     {"focus": "MÖHNE", "pitch": 50, "pad_km": 0.8, "move": 0}),
    ("00:50:18", "00:56:30", ["MÖHNE", "MÖHNE FLOOD", "NEHEIM"],
     "Pull back from the breach as the flood runs down the valley toward Neheim and its "
     "labour camp.", {"pitch": 40, "pad_km": 1.0, "move": 2.5}),
    ("00:56:30", "01:18", ["AJ-G", "AJ-L", "AJ-Z", "AJ-N", "AJ-A"],
     "Gibson leads the rest east to the Eder while the flood keeps running.",
     {"follow": "AJ-G", "pitch": 25, "pad_km": 4, "move": 2}),
    ("01:18", "01:37", ["EDER", "WALDECK", "AJ-L"],
     "The Eder: castle, spit and hills that make its approach so hard, and Shannon's dummy "
     "runs.", {"pitch": 45, "pad_km": 0.8, "move": 2}),
    ("01:37", "01:47", ["EDER", "WALDECK", "HAMMERBERG", "UPKEEP AJ-L", "UPKEEP AJ-Z"],
     "The whole approach, castle to dam, for Shannon's release and Maudslay's late one.",
     {"pitch": 50, "pad_km": 1.2}),
    ("01:47", "01:54", ["EDER", "HAMMERBERG", "UPKEEP AJ-N"],
     "Tighter for Knight, the last mine: the dive past the spit, the turn onto the dam, the "
     "breach.", {"pitch": 55, "pad_km": 0.8}),
    ("01:54", "01:54:09", ["EDER"],
     "The Eder's breach as photographed later that month, shown from the camera.",
     {"focus": "EDER", "pitch": 50, "pad_km": 0.8, "move": 0}),
    ("01:54:09", "02:24", ["AJ-G", "AJ-A", "AJ-Z", "AJ-N", "AJ-L", "MÖHNE FLOOD", "EDER FLOOD"],
     "Pull out over Germany: both floods running, the survivors turning for home.",
     {"move": 3}),
    ("02:24", "02:38", ["AJ-C", "AJ-Z", "AJ-O", "AJ-Y", "AJ-F"],
     "The reserve is sent to the dams still standing, and more crews are lost on the way.",
     {"pitch": 20, "move": 2}),
    ("02:38", "02:56", ["AJ-A"],
     "Young, nearly clear of Holland.", {"follow": "AJ-A", "pitch": 30, "pad_km": 8}),
    ("02:56", "03:00", ["AJ-A", "CASTRICUM"],
     "Young's end off Castricum.", {"pitch": 35, "pad_km": 2}),
    ("03:00", "03:08", ["AJ-F", "SORPE", "AJ-Y"],
     "Brown heads for the Sorpe as the valleys fill with mist; Anderson turns back.",
     {"follow": "AJ-F", "pitch": 20, "move": 2}),
    ("03:08", "03:16", ["SORPE", "SORPE RUN-IN", "UPKEEP AJ-F"],
     "Brown's attack on the Sorpe: incendiaries in the trees, the mine on the crest; the "
     "dam holds.", {"pitch": 50, "pad_km": 1.0}),
    ("03:16", "03:25", ["AJ-O", "ENNEPE"],
     "Townsend searches for his dam in the mist.",
     {"follow": "AJ-O", "pitch": 30, "pad_km": 2}),
    ("03:25", "03:39", ["ENNEPE", "ENNEPE RUN-IN", "UPKEEP AJ-O"],
     "Townsend's runs and the mine that falls short.", {"pitch": 50, "pad_km": 1.0}),
    ("03:39", "05:25", ["AJ-O", "AJ-F", "AJ-Y", "SCAMPTON"],
     "Pull out: the survivors cross the North Sea home into daylight, Townsend last.",
     {"move": 3}),
    ("05:25", "06:12", ["AJ-O"],
     "Townsend alone over the sea in daylight.",
     {"follow": "AJ-O", "pitch": 25, "pad_km": 15, "move": 2}),
    ("06:12", DURATION, ["SCAMPTON", "AJ-O"],
     "Townsend lands, the last one back, while the briefing gives the night's toll.",
     {"pitch": 40, "pad_km": 2}),
]


def lifetimes(plan):
    out = {}
    for code, track in plan.tracks.items():
        out[code] = (track.start, track.end if code in plan.lost else DURATION)
    for mine, track in plan.mines.items():
        out[mine] = (track.start, track.end)
    out["MÖHNE FLOOD"] = (plan.flood.start, DURATION)
    out["EDER FLOOD"] = (plan.eder_flood.start, DURATION)
    return out


def shots(plan, pacing):
    """(camera cues, intents by start_ms) for SHOTS, fitted under the story's `pacing`."""
    fixed = {id_: point for id_, _, _, _, point, _, _ in FIXED}
    fixed.update(POINTS)
    tracks = {**plan.tracks, **plan.mines, "MÖHNE FLOOD": plan.flood,
              "EDER FLOOD": plan.eder_flood}
    f = Framer(tracks, fixed, lifetimes(plan), pacing)
    drops = releases(plan)
    for start, end, subjects, intent, framing in SHOTS:
        a = start if isinstance(start, int) else L(start)
        b = end if isinstance(end, int) else L(end)
        code = next((c for c, (r, _) in drops.items() if a < r - chase_ms(c) and r < b), None)
        # A drop's own sequence shows its mine; the wide shot around it does not.
        shows = [n for n in subjects if n not in POINTS and n != f"UPKEEP {code}"]

        def base(s, e, purpose, move=framing.get("move", 1.5)):
            f.shot(s, e, subjects, {"intent": purpose, "shows": shows},
                   **{**framing, "move": move})
        if code is None:
            base(a, b, intent)
            continue
        base(a, drops[code][0] - chase_ms(code), intent)
        sequence(f, plan, code, b, lambda s, e, purpose: base(s, e, purpose, move=2))
    return f.shots, f.intents
