"""Viewing time under a story's pacing, and pacing built around the moments that matter.

A pacing is a contiguous list of (from ms, until ms, speed) in operation time; a viewer spends
(until - from) / speed of real time on each stretch.
"""


def viewing_between(pacing, a, b):
    """Viewing seconds the story spends between operation times `a` and `b`."""
    return sum(max(0, min(b, until) - max(a, start)) / speed
               for start, until, speed in pacing) / 1000


def after_viewing(pacing, start, seconds):
    """The operation time reached `seconds` of viewing after `start`."""
    left = seconds * 1000
    for a, b, speed in pacing:
        if b <= start:
            continue
        a = max(a, start)
        if (b - a) / speed >= left:
            return int(a + left * speed)
        left -= (b - a) / speed
    return pacing[-1][1]


def with_beats(base, beats):
    """`base` with each beat's (from, until, speed) laid over it, slowing the story through
    the moment a beat covers; where beats overlap, the slowest wins."""
    cuts = sorted({t for a, b, _ in base for t in (a, b)}
                  | {t for a, b, _ in beats for t in (a, b) if base[0][0] < t < base[-1][1]})
    out = []
    for a, b in zip(cuts, cuts[1:]):
        speed = next(s for c, d, s in base if c <= a < d)
        speed = min([speed] + [s for c, d, s in beats if c <= a and b <= d])
        if out and out[-1][2] == speed:
            out[-1] = (out[-1][0], b, speed)
        else:
            out.append((a, b, speed))
    return out
