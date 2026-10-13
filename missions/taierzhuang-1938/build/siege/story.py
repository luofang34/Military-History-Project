"""Chapters, briefings and pacing for the artillery battle, on the UTC+8 clock (sites.L).

The story runs fast between fire missions and slows through each, so the rounds can be seen in
flight (fire.beats), and through each briefing, so it can be read.
"""
from composition import INTENTS
from evidence import DISPUTES
from .fire import FLIGHT_VIEWING_S, beats, flight_windows
from pacing import with_beats
from .sites import BEGIN, END, L

CHAPTERS = [
    ("The road to the Grand Canal", "18 14:30"),
    ("The first assault on Taierzhuang", "23 07:00"),
    ("Guns on both banks", "25 06:30"),
    ("Into the town", "27 05:30"),
    ("The first duel", "28 06:00"),
    ("Two guns beyond reach", "30 01:30"),
    ("Night attacks on the gun line", "30 02:20"),
    ("Counter-battery, 30 March", "30 06:00"),
    ("The concentrations of 31 March", "31 08:30"),
    ("The first 15 cm rounds", "31 15:30"),
    ("1 April: the guns that could not be found", "1 05:00"),
]

BASE_SPEED = 4096
READ_CPS = 20.0
NOTE_SPEED = 8.0  # round a flight, while a note is read
READ_BY = "1 19:00:45"  # the last note is read by then; it stays to the end

J63 = "jacar-63i-taierzhuang"
J10 = "jacar-10i-report-13"
SAS = "jacar-sas-report"
OHASHI = "jacar-ohashi"
KRZ = "krzzjn-sfh18"
JIANG = "jiang-2017"
ZHWIKI = "zhwiki-taierzhuang"
KRZ_TZZ = "krzzjn-three-days"
NX = "nx-31div"
PAPER = "thepaper-squads"

# (entity or None, from, until, source, text)
BRIEFINGS = [
    (None, "18 14:30", "18 18:30", JIANG,
     "18 March. From Lincheng the Seya Detachment sends two forces on: one south to Hanzhuang "
     "on the Grand Canal, one east along the branch railway to Yixian."),
    ("63 REGT I", "19 12:30", "19 13:30", J63,
     "19 March, 13:00: the right force takes Hanzhuang north of the canal. Across the water "
     "stand about 10,000 Chinese."),
    ("63 REGT II", "19 17:00", "20 00:30", J63,
     "At Yixian the gates will not break. After dark the men climb a human ladder through a "
     "hole above the south gate; by 00:30 the town is theirs."),
    ("20 ARMY CORPS", "20 06:00", "20 20:00", KRZ_TZZ,
     "Tang Enbo's 20th Army Corps gives way before them and draws off into the hills to the "
     "east, to fall on the Japanese flank later."),
    ("31 DIV", "22 02:00", "22 08:00", ZHWIKI,
     "22 March: the 31st Division of Sun Lianzhong's 2nd Group Army takes over Taierzhuang. Chi "
     "Fengcheng puts a regiment in the walled town and another forward at Beiluo."),
    ("63 REGT", "22 12:00", "22 17:30", J63,
     "The 63rd's main body marches from Lincheng to Yixian."),
    ("63 REGT II", "23 07:00", "23 12:00", J63,
     "23 March: from Yixian a battalion of the 63rd Infantry and one field battery set out to "
     "take Taierzhuang and hold the Grand Canal. At 09:00 the 31st Division's cavalry meets them "
     "at Kangzhuang; by dusk they have fought through to Beiluo."),
    ("63 REGT II", "24 08:40", "24 11:30", J63,
     "24 March: the battalion comes down past Liujiahu and by noon is 200 m from the town's "
     "brick wall."),
    ("63 REGT II", "24 16:10", "24 16:30", J63,
     "16:15: its guns open two breaches west of the north gate and the companies charge. About "
     "ten men get in and are cut off."),
    ("63 REGT II", "24 22:30", "25 01:30", J63,
     "By night the battalion is out of ammunition and surrounded outside the north gate. It has "
     "lost about a hundred men."),
    ("TRAIN", "25 07:30", "25 08:10", J63,
     "25 March, 08:00: a Chinese armoured train runs north from the station and fires its gun "
     "on the Japanese."),
    ("TYPE 96", "25 11:00", "25 12:50", SAS,
     "The China Garrison's two Type 96 15 cm howitzers, the most modern Japanese guns here, "
     "come down by lorry from Lincheng."),
    ("XIONGSHAN GUNS", "25 15:50", "25 16:10", J63,
     "16:00: the Japanese report more than ten Chinese guns at the foot of the hills south of "
     "the canal, shelling them so hard they cannot move by day."),
    ("TYPE 96", "25 17:20", "25 17:40", J63,
     "17:30: from Liujiahu the Type 96 howitzers open fire."),
    ("EAST FORCE", "25 20:30", "25 21:30", J63,
     "At night the Chinese attack the Japanese batteries again and again; the gunners fight "
     "them off with rifles and fire at point-blank range."),
    ("HEAVY 3", "26 15:50", "26 22:00", J63,
     "26 March: the first company of the 2nd Field Heavy Artillery's Type 4 15 cm howitzers "
     "reaches Liujiahu after dark."),
    ("63 REGT II", "27 05:50", "27 06:10", J63,
     "27 March, 06:00: every gun opens on the north wall. At 07:50 the battalion breaks into the "
     "north-east corner and raises its flag."),
    ("63 REGT", "27 11:00", "27 13:30", J63,
     "The 63rd's main body comes down from Yixian with the rest of the heavy artillery and a "
     "company of tanks."),
    ("TANKS", "27 14:00", "27 15:30", J63,
     "The tanks charge the north-west corner. Two are destroyed and three break down."),
    ("31 DIV", "27 15:35", "27 16:40", KRZ_TZZ,
     "15:40: inside the town Wang Guanwu leads a counter-attack and sets fire to the temple and "
     "blockhouses where the Japanese hold out."),
    ("HEAVY 3", "28 06:38", "28 06:45", J63,
     "28 March, 06:40: as the heavy guns range on the north-west corner, Chinese guns answer "
     "from the hills south of the canal. Their first rounds fall 100 m behind the battery."),
    ("XIONGSHAN GUNS", "28 08:00", "28 09:30", J63,
     "The Japanese count at least 24 or 25 Chinese guns. They take those in the hills for field "
     "guns, those by the town for mountain guns and mortars."),
    ("63 REGT III", "28 15:00", "28 16:00", J63,
     "Short of shells, and under the Chinese guns themselves, the Japanese batteries cannot "
     "give the infantry enough support."),
    ("11 COY", "28 19:15", "28 19:30", J63,
     "19:25: after two breaching shoots by the Type 96, the 11th Company storms the north-west "
     "corner."),
    ("TYPE 96", "29 11:05", "29 11:15", SAS,
     "29 March, 11:10: Chinese shells set the Type 96 company's lorries on fire. Thirteen men "
     "are killed or wounded, and nearly all its vehicles are lost."),
    ("TYPE 96", "29 12:55", "29 13:05", J63,
     "Moved back to Liujiahu, the Type 96 hunts the Chinese batteries east of the town."),
    (None, "30 01:30", "30 01:50", KRZ,
     "30 March. The Japanese hold the town's north-east and north-west corners and their guns "
     "stand round Liujiahu. South of the canal the Chinese 10th Artillery has brought two "
     "German 15 cm "
     "sFH 18/32L howitzers, whose 15 km outranges every Japanese gun here."),
    (None, "30 02:10", "30 02:35", OHASHI,
     "On the map each battery's reach is drawn as a fan. A Japanese gunner later wrote: "
     "\"a mere two Rheinmetalls completely suppressed our whole artillery\"."),
    ("NIGHT ATTACK", "30 02:35", "30 03:10", J63,
     "03:00: about a thousand Chinese come north from the station along the railway against "
     "the Japanese reserve south of Sanlizhuang."),
    ("NIGHT ATTACK", "30 03:28", "30 04:00", J63,
     "03:30: they reach the 2nd Heavy Company's guns north of Sanlizhuang and are driven off by "
     "fire at point-blank range."),
    ("EAST GUNS", "30 05:58", "30 06:10", J63,
     "06:00: Chinese guns towards Zhaocun shell the Japanese field guns; the field guns hit two "
     "and drive off the other two."),
    ("TYPE 96", "30 10:09:40", "30 10:11", SAS,
     "The Type 96 company's two modern 15 cm howitzers search the villages east of the town."),
    ("EAST FORCE", "30 17:20", "30 17:33", J63,
     "17:30: a Chinese night attack forms east of Mengzhuang; the heavy guns break it up."),
    ("SQUAD", "30 19:30", "30 21:00", PAPER,
     "20:00: 57 volunteers of the 31st Division, wearing Japanese helmets, creep up on the "
     "Japanese in the north-west corner with grenades and pistols. They take five dugouts and "
     "a few houses."),
    ("TRAIN", "31 00:00", "31 00:30", J63,
     "In the night a Chinese armoured train comes into the station from south of the canal."),
    ("TRAIN", "31 06:20", "31 06:40", J63, "06:20: the Japanese guns are ordered onto it."),
    ("TYPE 96", "31 08:49:40", "31 08:50:40", SAS,
     "31 March: the Type 96 company opens on the town's west half."),
    ("JP 15CM ROUNDS", "31 11:13", "31 11:17", J63,
     "11:14: nearly all the Japanese artillery, fifteen guns, concentrates on the town, the "
     "first of four times before 14:40."),
    ("CN ROUNDS", "31 11:17", "31 11:25", J63,
     "At once more than ten Chinese guns answer on the Japanese batteries at Liujiahu and "
     "Sanlizhuang."),
    ("EAST GUNS", "31 15:04", "31 15:08", J63,
     "15:05: a Chinese battery is found at Canglangmiao, east of the town; it moves on."),
    ("CN 15CM ROUNDS", "31 15:45:40", "31 15:46:40", J63,
     "15:46: 15 cm-class rounds land on the 3rd Heavy Company and knock out a Type 4 howitzer: "
     "the first the Japanese have taken in the battle. They cannot find the guns."),
    ("TYPE 96", "31 16:14", "31 16:18", J63,
     "16:15: the Type 96 company fires on a battery it has found at Hanshan."),
    (None, "31 17:49:30", "31 17:51", J63,
     "At 17:12 the China Garrison's independent field-gun company had reported all four of "
     "its guns knocked out by Chinese fire."),
    ("11 COY", "31 19:59", "31 20:03", J63,
     "20:00: under the heavy guns' cover the 11th Company gives up its foothold at the "
     "town's north-west corner."),
    ("FIELD 10I", "1 01:00", "1 02:00", J10,
     "1 April, 01:00: the 10th Field Artillery's commander will not attack under \"a superior "
     "enemy artillery that has completed its preparations\". The attack is put off."),
    ("CN 15CM ROUNDS", "1 09:28", "1 09:34", J63,
     "15 cm rounds now fall on Liujiahu and Sanlizhuang five times through the day. The "
     "Japanese think they come from towards Xiongshan, but never find the guns."),
    ("TYPE 96", "1 17:24", "1 17:28", SAS,
     "17:25: the Type 96 company silences guns south of the station."),
    (None, "1 18:59:45", "END", OHASHI,
     "\"Throughout the campaign our artillery hunted the Rheinmetall as its sworn enemy but "
     "never caught it\" (Ohashi): on retreat the Chinese always got these guns away first."),
]


# Each dispute's one-line brief, on screen from its record's time until the next note.
DISPUTE_NOTES = {"yixian-fell": ("20 00:30", "20 05:00"),
                 "duel-on-27-march": ("27 17:28", "27 17:33"),
                 "wenchang-pavilion": ("28 21:00", "28 22:30"),
                 "sfh-position": ("30 01:50", "30 02:10"),
                 "first-15cm-fire": ("31 15:46:40", "31 15:47:40")}


def slow(a, b, text):
    """(display from, slow from, slow until, speed) for a note on screen from `a` to `b`.

    A note whose window holds a fire mission is read round that flight, two thirds before it
    and a third after, so the story is not still while it is read; any other is read evenly
    through its window. The note appears no later than its reading starts."""
    need = len(text) / READ_CPS + 1.5
    flights = [(m, e) for m, e in flight_windows() if a <= m <= b]
    if not flights:
        b = min(b, L(READ_BY))
        return a, a, b, (b - a) / 1000 / need
    m, e = flights[0]
    spare = max(1.0, need - FLIGHT_VIEWING_S)
    before, after = int(spare * 2 / 3 * NOTE_SPEED * 1000), int(spare / 3 * NOTE_SPEED * 1000)
    return min(a, m - before), m - before, e + after, NOTE_SPEED


def notes():
    """(entity, from ms, until ms, source, text) of every note, briefings and disputes'
    briefs."""
    out = [(e, L(a), END + 1 if b == "END" else L(b), s, text)
           for e, a, b, s, text in BRIEFINGS]
    for key, (a, b) in DISPUTE_NOTES.items():
        d = DISPUTES[key]
        out.append((d.entity, L(a), L(b), "reconstruction-estimate", d.brief))
    return [(e, slow(a, b, text)[0], b, s, text) for e, a, b, s, text in out]


def reading():
    """(from, until, speed) slowing each note's window enough to read it."""
    out = []
    for _, a, b, _, text in notes():
        _, x, y, speed = slow(a, b, text)
        if speed < BASE_SPEED:
            out.append((x, y, speed))
    return out


def pacing():
    base = [(BEGIN, END, BASE_SPEED)]
    return with_beats(base, [(max(BEGIN, a), min(END, b), s) for a, b, s in beats()]
                      + reading())


def annotations(em):
    for entity, a, b, source, text in notes():
        kind = "reconstructed" if source == "reconstruction-estimate" else "reported"
        em.note(source, entity, a, b, text, kind, [])


def document(operation, cues, intents):
    return {
        "format": "sokoly-presentation",
        "version": 1,
        "id": "default",
        "name": "Battle of Taierzhuang, II: the guns at the canal",
        "operation": operation,
        "chapters": [{"title": t, "at_ms": L(at), "available_ms": L(at)} for t, at in CHAPTERS],
        "camera_track": cues,
        "playback_track": [{"start_ms": a, "end_ms": b, "speed": s} for a, b, s in pacing()],
        "extensions": {INTENTS: intents},
    }
