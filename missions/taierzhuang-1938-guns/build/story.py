"""Chapters, briefings and pacing for the artillery battle, on the UTC+8 clock (sites.L).

The story runs fast between fire missions and slows through each, so the rounds can be seen in
flight (fire.beats), and through each briefing, so it can be read.
"""
from composition import INTENTS
from evidence import DISPUTES
from fire import FLIGHT_VIEWING_S, beats, flight_windows
from pacing import with_beats
from sites import DURATION, L

CHAPTERS = [
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

# (entity or None, from, until, source, text)
BRIEFINGS = [
    (None, "30 01:30", "30 01:50", KRZ,
     "Taierzhuang, on the Grand Canal, 30 March 1938. For a week the Japanese have fought into "
     "the town. South of the canal the Chinese 10th Artillery has brought two German 15 cm "
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
    (None, "1 18:59:45", "DURATION", OHASHI,
     "\"Throughout the campaign our artillery hunted the Rheinmetall as its sworn enemy but "
     "never caught it\" (Ohashi): on retreat the Chinese always got these guns away first."),
]


# Each dispute's one-line brief, on screen from its record's time until the next note.
DISPUTE_NOTES = {"sfh-position": ("30 01:50", "30 02:10"),
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
    out = [(e, L(a), DURATION + 1 if b == "DURATION" else L(b), s, text)
           for e, a, b, s, text in BRIEFINGS]
    for key, d in DISPUTES.items():
        if d.brief:
            a, b = DISPUTE_NOTES[key]
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
    base = [(0, DURATION, BASE_SPEED)]
    return with_beats(base, [(max(0, a), min(DURATION, b), s) for a, b, s in beats()]
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
