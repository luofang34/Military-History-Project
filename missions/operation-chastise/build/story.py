"""Chapters, briefing notes, disputed times and pacing for the Chastise reconstruction.

Clock times are BDST (UTC+2), which German summer time matched that night. Briefings quote or
paraphrase the sources named on each note; the README lists them.
"""
from composition import INTENTS
from crews import fate_note
import ledger
from pacing import with_beats
from evidence import DISPUTES
from flights import LOSS
from sites import DURATION, L

CHAPTERS = [
    ("Operation Chastise", "21:25"),
    ("Second wave airborne", "21:28"),
    ("First wave airborne", "21:39"),
    ("Vlieland", "22:50"),
    ("Barlow at Haldern", "23:46"),
    ("Astell at Marbeck", "00:12"),
    ("Holding over the Möhne", "00:17"),
    ("Gibson's attack", "00:27"),
    ("Hopgood", "00:31"),
    ("Martin and Young", "00:35"),
    ("McCarthy at the Sorpe", "00:44"),
    ("Maltby breaches the Möhne", "00:47"),
    ("The flood", "00:50"),
    ("To the Eder", "00:56:30"),
    ("Shannon and Maudslay", "01:18"),
    ("Knight breaches the Eder", "01:47"),
    ("The reserve is sent in", "02:24"),
    ("Young off Castricum", "02:38"),
    ("Brown at the Sorpe", "03:00"),
    ("Townsend at the Ennepe", "03:16"),
    ("Home in daylight", "03:39"),
]

# (from, until, speed). A still map plays fast; its briefing stays up into the action that
# follows. Repeated take-offs and long transits play fast, and the attacks play at ATTACK
# except through each run, which `pacing` slows to RUN.
BASE_PACING = [
    ("21:25", "21:27:55", 36), ("21:27:55", "21:32", 10), ("21:32", "21:38", 60),
    ("21:38", "21:41", 10), ("21:41", "21:46", 60), ("21:46", "21:49", 24),
    ("21:49", "21:58", 60), ("21:58", "22:02", 16), ("22:02", "22:50", 120),
    ("22:50", "23:03", 20), ("23:03", "23:46", 180), ("23:46", "23:52", 16),
    ("23:52", "00:12", 120), ("00:12", "00:17", 20), ("00:17", "00:27", 30),
    ("00:27", "00:50", 24), ("00:50", "00:56:30", 12), ("00:56:30", "01:18", 60),
    ("01:18", "01:37", 40), ("01:37", "01:54", 60), ("01:54", "02:24", 60),
    ("02:24", "02:38", 20), ("02:38", "02:56", 60), ("02:56", "03:00", 12),
    ("03:00", "03:08", 60), ("03:08", "03:16", 30), ("03:16", "03:25", 60),
    ("03:25", "03:39", 30), ("03:39", "06:12", 240), ("06:12", "06:15:40", 20),
    ("06:15:40", "06:20", 240),
]

# Each run plays from its lead-in to the mine's burst, and the mine's bounces slower still;
# Young's loss off Castricum likewise.
RUN, MINE = 4, 1.5
RUN_BEFORE_MS, RUN_AFTER_MS = 30_000, 20_000
MINE_BEFORE_MS, MINE_AFTER_MS = 3_000, 10_000


def pacing(releases):
    """The story's pacing in operation ms, slowed through each attack run in `releases`."""
    base = [(L(a), L(b), speed) for a, b, speed in BASE_PACING]
    beats = [(r.at_ms - RUN_BEFORE_MS, r.at_ms + RUN_AFTER_MS, RUN) for r in releases]
    beats += [(r.at_ms - MINE_BEFORE_MS, r.at_ms + MINE_AFTER_MS, MINE) for r in releases]
    young = L(LOSS["AJ-A"])
    beats.append((young - 20_000, young + 20_000, RUN))
    return with_beats(base, beats)


ORB = "orb-617"
DB = "dambustersblog"
ECA = "gibson-eca"
B976 = "order-b976"
ESTIMATE = "reconstruction-estimate"

# (entity or None, from, until, source, text)
BRIEFINGS = [
    (None, "21:25", "21:31", B976,
     "Night of 16/17 May 1943. Nineteen Lancaster B.III (Type 464 Provisioning) of 617 "
     "Squadron, each carrying one 9,250 lb Upkeep mine, are to breach the Ruhr dams: Möhne "
     "(X), Eder (Y) and Sorpe (Z), with Lister, Ennepe and Diemel as last resorts. Upkeep is "
     "spun backwards at 500 rpm and dropped at 60 ft and 220 mph, 400–450 yards short of the "
     "wall. Clock: British Double Summer Time, UTC+2, as was German summer time."),
    (None, "21:28", "21:39", ORB,
     "21:28–21:31: the second wave — Barlow, Munro, Byers, Rice — leaves Scampton singly for "
     "the Sorpe by the northern route over Vlieland and the IJsselmeer, timed to cross the "
     "enemy coast with the first wave. McCarthy, the fifth, is delayed changing to the spare "
     "aircraft AJ-T."),
    ("AJ-G", "21:39", "21:58", ORB,
     "21:39: Gibson, Hopgood and Martin take off in a vic; Young, Maltby and Shannon follow "
     "at 21:47. Under 1,500 ft over England, then 60 ft on the spotlight altimeter over the "
     "sea. Take-off direction and slots on the grass field are reconstructed."),
    ("AJ-T", "21:58", "22:50", ORB,
     "21:59: Maudslay, Astell and Knight. 22:01: McCarthy, who \"took off 20 mins. late\", "
     "his own AJ-Q unserviceable and the spare's compass deviation card missing."),
    ("AJ-W", "22:50", "22:57", ORB,
     "About 22:54: light flak at Vlieland hits Munro's AJ-W and knocks out the intercom. "
     "Unable to direct his crew, he turns for home with his mine."),
    ("AJ-K", "22:57", "23:03", DB,
     "22:57: Byers, off track over Texel and climbing to about 300 ft, is shot down by flak "
     "and falls into the Waddenzee west of Harlingen. All seven are killed; six have no known "
     "grave."),
    ("AJ-H", "22:59", "23:46", ORB,
     "Rice crosses Vlieland at 22:59, then strikes the water of the Waddenzee; the Upkeep is "
     "torn away and the rear turret floods. He turns back. Of the second wave, only Barlow "
     "and McCarthy are still heading for the Sorpe."),
    ("AJ-E", "23:46", "23:52", DB,
     "23:50: Barlow's AJ-E hits high-tension cables at Haldern, east of Rees, and crashes; "
     "all seven are killed. The mine does not explode, and German engineers examine it the "
     "next day."),
    ("AJ-G", "23:52", "00:13", ORB,
     "North-east of Haltern the leading section meets about twelve searchlights and light "
     "flak; Gibson reports it by W/T and Group relays the warning. Hopgood is hit about 20 "
     "minutes from the target, he and his front gunner wounded."),
    ("AJ-B", "00:12", "00:17", DB,
     "00:15: Astell, lagging half a mile behind since the canal turn at Roosendaal, flies "
     "into high-tension cables near Marbeck. Knight's wireless operator logs him going down; "
     "his mine explodes about 90 seconds after the crash. All seven are killed."),
    ("AJ-G", "00:17", "00:27", ECA,
     "Gibson reaches the Möhne about 00:15 and goes over to R/T control ten miles out. The "
     "others wait in left-hand circuits over the hills south of the lake. Six 2 cm guns of "
     "3./leichte Flak-Abteilung 840 defend the dam, two on its towers."),
    ("UPKEEP AJ-G", "00:27", "00:31", ORB,
     "00:28: Gibson, after a dummy run through the flak, attacks first at 60 ft. The mine "
     "bounces three times and explodes short of the wall. B.976 requires three minutes "
     "between attacks for the water to settle."),
    ("AJ-M", "00:31", "00:35", ORB,
     "Hopgood is hit on the run-in and an engine catches fire. He releases late; the mine "
     "bounces over the parapet and destroys the power station below. AJ-M climbs to about "
     "500 ft, a wing comes off, and it crashes near Ostönnen at 00:34. Fraser and Burcher "
     "survive as prisoners; five are killed."),
    ("AJ-P", "00:35", "00:41", ORB,
     "00:38: Martin attacks with Gibson flying alongside to draw the flak. The mine bursts "
     "about 20 yards short; 20 mm fire from the dam holes AJ-P's starboard "
     "outer tank and ailerons."),
    ("AJ-A", "00:41", "00:44", ORB,
     "00:43: Young attacks, Gibson and Martin flanking him firing on the towers. The ORB "
     "records an accurate attack; the mine explodes against the wall."),
    ("AJ-T", "00:44", "00:47", ORB,
     "00:46, at the Sorpe: McCarthy, alone of his wave, attacks along the crest of the earth "
     "dam after nine dummy runs in mist, dropping from 30 ft without spin. The mine explodes "
     "in contact and part of the crest crumbles; the dam holds."),
    ("AJ-J", "00:47", "00:50", DB,
     "00:49: Maltby attacks with Gibson to starboard and Martin to port. Seeing a crumbling "
     "breach at the crown, he swings slightly to port; his mine bounces four times and "
     "explodes against the wall. 00:50: AJ-J signals Goner 78A."),
    ("MÖHNE", "00:50", "00:56:30", "dewiki-moehne",
     "The Möhne breaks: a gap about 30 m wide that widens to 76 m. About 116 million m³ pour into "
     "the valley within twelve hours (1949 US Military Hydrology study), a wave some 10 m "
     "high. 00:56: Gibson signals \"Nigger\", the Möhne breach codeword and the name of "
     "his dog; the word is a racial slur. Martin and Maltby are sent home."),
    ("MÖHNE FLOOD", "00:56:30", "01:18", "dewiki-moehne",
     "The flood reaches Neheim at 01:20. Its Möhnewiesen camp holds between 1,200 and 1,500 "
     "forced labourers, mostly women from Eastern Europe. In Neheim 859 die, 147 Germans and "
     "712 foreigners. The wave passes Wickede about 02:00, Fröndenberg about 03:00 and "
     "Schwerte, some fifty kilometres from the dam, about 05:15."),
    ("AJ-L", "01:18", "01:37", ECA,
     "Gibson leads Shannon, Maudslay and Knight, with Young, to the Eder. It is undefended "
     "but deep in fog-filled hills: each run dives over Waldeck castle from 1,000 ft, drops to "
     "60 ft past the Hammerberg spit, turns hard left onto the wall, and climbs steeply to "
     "starboard to clear the hill beyond. Shannon makes repeated dummy runs."),
    ("AJ-Z", "01:37", "01:47", ORB,
     "01:39: Shannon attacks; the mine bounces twice and explodes, with no visible result. "
     "Maudslay, something hanging beneath his aircraft, releases too late: the Upkeep hits "
     "the parapet and explodes beneath AJ-Z. Asked if he is all right, he answers faintly, "
     "\"I think so\"."),
    ("AJ-N", "01:47", "01:54", DB,
     "01:52: Knight, the last mine in the first wave, makes one dummy run and attacks on the "
     "second. It bounces three times and breaches the Eder about 30 ft below the crest. "
     "01:54: Gibson signals \"Dinghy\"."),
    ("5 GROUP HQ", "01:54", "02:24", DB,
     "Grantham logs Goner 28B from Maudslay at 01:57 and Goner 710B from Knight about 02:00. "
     "About 160 million m³ leave the Eder; the flood runs down the valley past Fritzlar into "
     "the Fulda towards Kassel. Between 47 and 68 die in the Eder valley (de.wikipedia)."),
    ("5 GROUP HQ", "02:24", "02:38", DB,
     "Group sends the reserve: 02:26 Townsend to the Ennepe; 02:28 Anderson to the Sorpe; "
     "02:31 Ottley to the Lister, acknowledged. Burpee was lost at Gilze-Rijen about 02:00. "
     "02:35: Ottley is shot down near Hamm; rear gunner Fred Tees survives as a prisoner. "
     "02:36: Maudslay is shot down by flak at Klein-Netterden, near Emmerich; all killed."),
    ("AJ-A", "02:38", "03:00", ORB,
     "02:58: Young, almost clear of Holland, is shot down by flak and comes down in the sea "
     "off Castricum aan Zee. All seven are killed and lie in Bergen General Cemetery."),
    ("AJ-F", "03:00", "03:16", ORB,
     "03:10: Anderson, his rear turret unserviceable and the valleys filling with mist, "
     "turns back with his mine. 03:14: Brown attacks the Sorpe from 60 ft after marking the "
     "mist with incendiaries in the trees; the mine explodes on the crest, which holds."),
    ("AJ-O", "03:16", "03:39", ORB,
     "03:37: Townsend drops on his third run in mist; the mine bounces twice and explodes "
     "short. He reported the Ennepe; the ORB editor, Sweetman and others argue he attacked "
     "the Bever, about 11 km to the south."),
    (None, "03:39", "06:20", "wikipedia-chastise",
     "Gibson lands at 04:15. Townsend, the last back, crosses Holland in daylight and lands "
     "at 06:15. Of 133 aircrew, 53 are killed and three captured; eight Lancasters are lost. "
     "The floods kill at least 1,650 people, more than 1,000 of them forced labourers and "
     "prisoners of war. Gibson is awarded the Victoria Cross."),
]


def until(clock):
    return DURATION + 1 if clock == "06:20" else L(clock)


def annotations(em):
    """Briefings and the crews lost, then each disputed fact's note for viewers. The ORB's
    crew lists stay in build/crews.py; each aircraft's name already gives its captain."""
    for entity, start, end, source, text in BRIEFINGS:
        em.note(source, entity, L(start), until(end), text, "reported", [])
    for code, at in LOSS.items():
        em.note(DB, code, L(at), L(at) + 600_000, fate_note(code), "reported", [])
    ledger.emit(em, DISPUTES, L, ESTIMATE)


def document(operation, camera_track, intents, pace):
    return {
        "format": "sokoly-presentation",
        "version": 1,
        "id": "default",
        "name": "Operation Chastise",
        "operation": operation,
        "chapters": [{"title": t, "at_ms": L(at), "available_ms": L(at)} for t, at in CHAPTERS],
        "camera_track": camera_track,
        "playback_track": [{"start_ms": a, "end_ms": b, "speed": s} for a, b, s in pace],
        "extensions": {INTENTS: intents},
    }
