"""The whole story: each part's chapters, briefings and pacing, in the order they happen."""
from composition import INTENTS

from siege import story as siege
from tengxian import story as tengxian

PARTS = (tengxian, siege)
NAME = "Battle of Taierzhuang"


def chapters():
    return [c for part in PARTS for c in part.CHAPTERS]


def pacing():
    """(from ms, until ms, speed), covering the operation end to end."""
    return [segment for part in PARTS for segment in part.pacing()]


def annotations(em):
    for part in PARTS:
        part.annotations(em)


def document(operation, cues, intents, L):
    return {
        "format": "sokoly-presentation",
        "version": 1,
        "id": "default",
        "name": NAME,
        "operation": operation,
        "chapters": [{"title": t, "at_ms": L(at), "available_ms": L(at)} for t, at in chapters()],
        "camera_track": cues,
        "playback_track": [{"start_ms": a, "end_ms": b, "speed": s} for a, b, s in pacing()],
        "extensions": {INTENTS: intents},
    }
