"""Chapters, briefings and pacing for the defence of Tengxian, on the UTC+8 clock (sites.L)."""
from composition import INTENTS
from evidence import DISPUTES
from pacing import after_viewing
from sites import DURATION, L

CHAPTERS = [
    ("The Seya Detachment moves south", "14 04:00"),
    ("Jiehe, and the swing round the east", "15 08:00"),
    ("Hold Tengxian for three days", "15 16:30"),
    ("The east suburb", "16 06:00"),
    ("Breaching the walls", "17 07:00"),
    ("Wang Mingzhang", "17 16:30"),
    ("The fall of Tengxian", "17 18:40"),
]

# (from, until, speed)
PACING = [
    ("14 04:00", "14 07:00", 600),
    ("14 07:00", "15 00:00", 2400),
    ("15 00:00", "15 10:00", 2400),
    ("15 10:00", "15 15:00", 1200),
    ("15 15:00", "15 21:30", 600),
    ("15 21:30", "16 06:00", 3000),
    ("16 06:00", "16 10:15", 900),
    ("16 10:15", "16 12:30", 200),
    ("16 12:30", "16 15:00", 300),
    ("16 15:00", "16 19:30", 600),
    ("16 19:30", "17 07:00", 3000),
    ("17 07:00", "17 13:30", 600),
    ("17 13:30", "17 16:00", 400),
    ("17 16:00", "17 18:40", 150),
    ("17 18:40", "17 23:30", 900),
    ("17 23:30", "18 14:30", 3000),
]

REPORT = "jacar-10i-report-11"
ORDERS = "jacar-seya-orders"
JIANG = "jiang-2015"
KRZ = "krzzjn-jiehe"
ZHWIKI = "zhwiki-tengxian"

# (entity the note is about, or None for the whole operation; from, until, source, text)
BRIEFINGS = [
    (None, "14 04:00", "14 07:00", JIANG,
     "March 1938. Japan's armies drive down the Tianjin–Pukou railway toward Xuzhou. In the "
     "way, round Tengxian, stand the Sichuan troops of Sun Zhen's 22nd Group Army: tired men, "
     "a third of them with no rifle, only grenades."),
    ("10 REGT I", "14 04:00", "14 09:00", KRZ,
     "04:00, 14 March: the Seya Detachment, a brigade of Isogai's 10th Division, attacks in "
     "three columns: the 10th Infantry on the right, the guns down the railway, the 63rd "
     "Infantry on the left."),
    ("63 REGT", "14 10:30", "14 14:00", KRZ,
     "11:00: the 63rd takes Xiangcheng, headquarters of the 125th Division."),
    ("370 BDE", "14 12:00", "14 19:30", ZHWIKI,
     "On the right the 10th breaks the 370th Brigade at Shiqiang. At 19:00 the brigade falls back "
     "on Dawu, west of Tengxian."),
    ("63 REGT", "14 17:30", "14 23:00", KRZ,
     "18:10: the 63rd enters Jiehe village, astride the railway. The Chinese line from Jiehe "
     "to Longshan holds on into the next day."),
    ("SEYA", "15 10:30", "15 14:00", ORDERS,
     "10:30, 15 March, at Jiehe: Seya does not go straight down the railway. He sends the "
     "detachment round the east of Tengxian, by Dongguo and Wangmiao, to attack the city from the "
     "east."),
    ("ARMOUR", "15 15:30", "15 17:30", KRZ,
     "At Chengtou the Japanese light armour scatters Wang Wenzhen's 731st Regiment."),
    ("WANG", "15 16:30", "15 18:45", ZHWIKI,
     "Wang Mingzhang is ordered to hold Tengxian three days for Tang Enbo's corps. He has "
     "one regiment and no heavy weapons. Sun Zhen: \"That is my order; if it is not held, "
     "that is on "
     "you.\""),
    ("YAN BN", "15 17:00", "15 19:45", "rmzxw-2025",
     "Yan Yi's battalion reaches the city at 17:00 and takes the east suburb; Zhang Xuanwu's "
     "727th Regiment comes in at dusk, and Zhang takes command of the walls."),
    ("SPECIAL BN", "15 19:30", "15 21:30", "qq-yang-jintao",
     "The 41st Army's Special Service Battalion arrives by train from Lincheng and holds the "
     "south wall. About 2,500 men are in the city; fewer than 2,000 are fighting troops."),
    ("10 REGT I", "16 06:00", "16 08:30", REPORT,
     "Dawn, 16 March. Patrols report the city lightly held, so the 10th Regiment attacks with "
     "just five companies. From Xiacun its commander sees a Nazi flag over the German mission "
     "inside the walls."),
    ("FIELD ARTY", "16 10:20", "16 11:00", JIANG,
     "10:20: eight field guns go into position at Xiacun, 2 km south-east of the walls. Their "
     "reach covers the city many times over."),
    ("ARMOURED TRAIN", "16 10:55", "16 11:45", REPORT,
     "11:00: a Chinese armoured train with 75 mm guns runs south from the station, firing; "
     "the field guns duel with it for ten minutes."),
    ("HEAVY ARTY", "16 11:15", "16 12:20", JIANG,
     "11:15: the heavy battalion ranges on the east suburb's gate. Its first round hits."),
    ("10 REGT I", "16 12:00", "16 13:30", REPORT,
     "Noon: the 3rd Company's assault stops 50 m short of the suburb wall. The guns are told "
     "to make a breach first."),
    ("10 REGT I", "16 14:10", "16 15:25", REPORT,
     "14:15: through the breach the 3rd Company takes a corner of the east suburb. Grenades "
     "keep it there."),
    ("10 REGT III", "16 18:30", "16 19:30", REPORT,
     "18:40, under a full moon: the 3rd Battalion breaks into the south suburb."),
    ("WANG", "16 21:00", "17 03:00", ZHWIKI,
     "21:00: Wang gives up the outer positions. At midnight the remnants of the 370th and "
     "372nd Brigades come in by the west gate."),
    ("GARRISON ARTY", "17 07:30", "17 09:05", REPORT,
     "07:30, 17 March: the guns open again, now with the China Garrison's modern Type 96 15 cm "
     "howitzers. At 08:30 breaching fire begins: 40 m south of the east gate, and 20 m west "
     "of the south-east corner."),
    ("GARRISON ARTY", "17 09:05", "17 10:00", REPORT,
     "Fifty rounds nearly make the east breach. The city burns, and a south wind blows the "
     "smoke north over the defenders."),
    ("PAGODA", "17 10:00", "17 11:00", JIANG,
     "10:00: a Japanese observer fights his way up the Longquan pagoda, 30 m above the city, and "
     "directs the guns."),
    ("WANG", "17 12:00", "17 13:00", ZHWIKI,
     "Noon: Wang's last telegram to Sun Zhen: resolved \"to fight to the death, to repay the "
     "nation and your trust\"."),
    ("10 REGT I", "17 13:00", "17 13:40", REPORT,
     "13:00: Colonel Akashiba is grazed by a sniper. He stays in command."),
    ("10 REGT II", "17 14:30", "17 15:20", REPORT,
     "14:30: the 10th's 2nd Battalion arrives and is sent to the station, to shut the way "
     "out west."),
    ("10 REGT III", "17 14:40", "17 16:10", REPORT,
     "The 3rd Battalion's assault on the south breach is thrown back by grenades. At 16:05 it "
     "is on the wall, and fights west along it."),
    ("WANG", "17 16:50", "17 17:20", ZHWIKI,
     "The west gate falls at about 17:00. Wang and his staff are let down from the north-west "
     "corner, to reach the troops at the station."),
    ("WANG", "17 17:30", "17 18:20", ZHWIKI,
     "In the moat outside the west gate, machine guns on the gate tower cut down Wang "
     "Mingzhang, his chief of staff Zhao Weibin and some ten others."),
    ("372 BDE", "17 18:00", "17 19:30", REPORT,
     "Five or six hundred men who get out westward are caught at the station by the 2nd "
     "Battalion. Outside the north gate the 124th Division's chief of staff, Zou Shaomeng, is "
     "shot."),
    ("727 REGT", "17 20:50", "17 22:00", ZHWIKI,
     "21:00: some two hundred men of the 727th open the walled-up north gate and break out."),
    ("10 REGT I", "17 21:40", "17 23:30", REPORT,
     "21:40: the 1st Battalion is over the east wall. By 23:00 it holds the north gate."),
    (None, "18 06:00", "DURATION", ZHWIKI,
     "18 March: the city is cleared house by house; by 14:00 it is over. Li Zongren later: "
     "without Tengxian's hard defence there would have been no victory at Taierzhuang."),
]

READ_CPS = 20.0  # the reading speed tools/composition.py holds briefings to


def pacing():
    return [(L(a), L(b), s) for a, b, s in PACING]


def annotations(em):
    """Briefings, then each dispute's brief, shown for as long as it takes to read at the
    story's pace there."""
    for entity, start, until, source, text in BRIEFINGS:
        end = DURATION + 1 if until == "DURATION" else L(until)
        em.note(source, entity, L(start), end, text, "reported", [])
    for d in DISPUTES.values():
        if d.brief:
            at = max(0, L(d.when()))
            until = after_viewing(pacing(), at, len(d.brief) / READ_CPS + 2)
            em.note("reconstruction-estimate", d.entity, at, until, d.brief, "reconstructed", [])


def document(operation, cues, intents):
    return {
        "format": "sokoly-presentation",
        "version": 1,
        "id": "default",
        "name": "Battle of Taierzhuang, I: Tengxian",
        "operation": operation,
        "chapters": [{"title": t, "at_ms": L(at), "available_ms": L(at)} for t, at in CHAPTERS],
        "camera_track": cues,
        "playback_track": [{"start_ms": a, "end_ms": b, "speed": s} for a, b, s in pacing()],
        "extensions": {INTENTS: intents},
    }
