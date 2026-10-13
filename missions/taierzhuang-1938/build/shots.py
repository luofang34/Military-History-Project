"""The whole camera: each part's shots, in the order they happen."""
from siege import shots as siege
from tengxian import shots as tengxian

PARTS = (tengxian, siege)


def camera():
    cues, intents = [], {}
    for part in PARTS:
        c, i = part.camera()
        cues += c
        intents.update(i)
    return cues, intents
