"""The dam photographs, each shown from its solved camera once its dam's flood is running.

The photographs were taken after the raid; the story pauses on each while its brief says when
and by whom. Each `media/<key>/replay.json` is the photo-pose pipeline's output: the
photograph, its fitted camera and the drape of the photograph on the terrain. The viewer's
overlay tour flies from the story's view onto the photograph, lays it over the terrain half
transparent, brings it to full opacity and fades it out, over the replay's `duration_s` of
operation time; each window is that long and the story slows to SPEED through it.
"""
import hashlib
import json
from pathlib import Path

from sites import L
from track import bearing_deg

ROOT = Path(__file__).resolve().parents[1]
TOUR = "overlay"

MEDIA = "media"
SPEED = 0.75

# (key, dam, window start, source id, source name, brief). Each dam's photographs follow its
# breach once its flood front is on the map; consecutive windows follow each other.
PHOTOS = [
    ("moehne-fray", "MÖHNE", "00:50", "photo-fray",
     "Jerry Fray, No. 542 Squadron RAF: the Möhne breached, 17 May 1943 (public domain)",
     "Photographed the next morning, 17 May, from Flying Officer Jerry Fray's reconnaissance "
     "Spitfire: the Möhne breached, the lake pouring out through the gap."),
    ("moehne-bundesarchiv", "MÖHNE", "00:50:09", "photo-schalber",
     "Bundesarchiv, Bild 101I-637-4192-20 / Schalber (CC BY-SA 3.0 DE)",
     "Photographed later in May 1943, from below the wall: the breach, and the rubble the "
     "water tore loose."),
    ("eder-bundesarchiv", "EDER", "01:54", "photo-eder",
     "Bundesarchiv, Bild 183-C0212-0043-012 (CC BY-SA 3.0 DE)",
     "Photographed later in May 1943: the Eder's broken wall, water still running through."),
]


def replay(out, key):
    return json.loads((out / MEDIA / key / "replay.json").read_text())


def heading(key, out=ROOT):
    """The photograph's camera heading: from its camera to the middle of its frustum."""
    r = replay(out, key)["reconstruction"]
    eye = (r["view"]["centre"]["lon"], r["view"]["centre"]["lat"])
    far = [sum(c[i] for c in r["frustum"]) / len(r["frustum"]) for i in (0, 1)]
    return bearing_deg(eye, tuple(far))


def windows(out=ROOT):
    """(key, dam, start ms, end ms) for each photograph, its replay's length long."""
    rows = []
    for key, dam, start, *_ in PHOTOS:
        a = L(start)
        rows.append((key, dam, a, a + round(replay(out, key)["duration_s"] * 1000)))
    return rows


def beats(out):
    return [(a, b, SPEED) for _, _, a, b in windows(out)]


def sources():
    return [{"id": sid, "name": name} for _, _, _, sid, name, _ in PHOTOS]


def annotate(em, out):
    """Each photograph's brief on its dam, for as long as it is shown."""
    for (key, dam, a, b), (*_, sid, _, brief) in zip(windows(out), PHOTOS):
        em.note(sid, dam, a, b, brief, "reported", [f"{MEDIA}/{key}/photo.png"])


def attach(op, out):
    """Writes the media archive and declares it, its assets and its windows in `op`."""
    units = {}
    for key, dam, a, _ in windows(out):
        units.setdefault(dam, []).append({"id": key, "label": replay(out, key)["name"],
                                          "replay": f"{key}/replay.json", "start_s": a / 1000,
                                          "tour": TOUR})
    (out / MEDIA / "debrief.json").write_text(json.dumps(
        {"format": "sokoly-debrief", "version": 1, "name": "Chastise dam photographs",
         "units": [{"id": u, "sidc": "SHGPIUED--H----", "media": m} for u, m in units.items()]},
        indent=1, ensure_ascii=False) + "\n")
    types = {".png": "image/png", ".jpg": "image/jpeg", ".json": "application/json"}
    op["media_archive"] = f"{MEDIA}/debrief.json"
    op["assets"] = [
        {"id": str(f.relative_to(out)), "path": str(f.relative_to(out)),
         "media_type": types[f.suffix], "bytes": f.stat().st_size,
         "sha256": hashlib.sha256(f.read_bytes()).hexdigest(),
         "source": "Dam photographs: credit and method in each replay's registration"}
        for f in sorted((out / MEDIA).rglob("*")) if f.is_file() and f.name != "debrief.json"]
    op["availability"] = [{"source": sid, "entity": dam, "spans": [[a, b]]}
                          for (_, dam, a, b), (*_, sid, _, _) in zip(windows(out), PHOTOS)]
    for e in op["entities"]:
        e["camera"] = e["camera"] or e["id"] in units
