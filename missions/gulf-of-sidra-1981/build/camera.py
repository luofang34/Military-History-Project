"""Camera shots for the Gulf of Sidra story, framed from the tracks and checked for coverage.

Over open sea there is no ground reference, so every shot is north-up and never orbits. Moving
subjects are followed, and each shot is zoomed to keep every subject on screen for its whole
span, sampled every second. Framing works in screen space: with the camera pitched, a subject
at altitude h is drawn about h·tan(pitch) above its ground point, so that offset counts too.
The build fails if any subject would leave the frame.

The viewer's scale and projection come from tools/framing.py. Each shot states what it is
for; tools/composition.py prints that beside what the viewer's frame report shows.
"""
import framing
from framing import ASPECT, screen_km, width_km
from geometry import (AA2, AIM_102, AIM_107, FE102, FE107, HIT_LEAD_S, HIT_WING_S, LOD_W, LOD_E,
                      MISSILES, NIMITZ, REJOIN_S, S3A, SU_LEAD, SU_WING, s_ms)
from pacing import after_viewing
from story import DURATION, PACING, t

FILL = 0.30  # a subject may sit at most this fraction of the frame size from the centre
MIN_ZOOM, MAX_ZOOM = 5.0, 12.0


def zoom_for(width):
    return framing.zoom_for(width, MIN_ZOOM, MAX_ZOOM, 2.0)


class Framer:
    """Positions of every subject (tracks and fixed points), the shot list being built and
    each shot's intent by its start_ms."""

    def __init__(self, tracks, fixed):
        self.tracks, self.fixed, self.shots, self.intents = tracks, fixed, [], {}

    def alive(self, name, at):
        if name in self.fixed:
            return True
        tr = self.tracks[name]
        return tr.start <= at <= tr.end if name in MISSILES else at >= tr.start

    def where(self, name, at):
        return (self.fixed[name], 0.0) if name in self.fixed else self.tracks[name].at(at)

    def shot(self, start, end, subjects, intent, follow=None, pitch=0, pad_km=0.0, move=1.5):
        """A north-up shot following `follow` (or fixed on the subjects' mean ground position),
        zoomed so every living subject stays within FILL of the frame from its centre, that
        arrives in `move` seconds of viewing (0 cuts) and is for `intent`."""
        times = list(range(start, end, 1000)) + [end - 1]
        if follow is None:
            pts = [self.where(n, at)[0] for at in times for n in subjects if self.alive(n, at)]
            fixed_centre = (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))
            centre_at = lambda _at: fixed_centre  # noqa: E731
            target = {"kind": "point", "value": {"lon": fixed_centre[0], "lat": fixed_centre[1]}}
        else:
            centre_at = lambda at: self.where(follow, at)[0]  # noqa: E731
            target = {"kind": "entity", "value": follow}
        need = 2 * pad_km / (2 * FILL)
        for at in times:
            living = [n for n in subjects if self.alive(n, at)]
            if not living:
                raise ValueError(f"shot at {start} ms has no subject alive at {at} ms")
            for n in living:
                point, alt = self.where(n, at)
                x, y = screen_km(centre_at(at), point, alt, pitch)
                need = max(need, abs(x) / FILL, abs(y) / (FILL * ASPECT))
        zoom = zoom_for(need)
        if need > width_km(zoom) + 1e-6:
            raise ValueError(f"shot at {start} ms cannot frame {subjects} at pitch {pitch}")
        cue = {"start_ms": start, "end_ms": end, "target": target, "zoom": round(zoom, 2),
               "pitch": pitch, "bearing": 0.0, "orbit_deg_s": 0.0,
               "transition_ms": min(after_viewing(PACING, start, move) - start,
                                    (end - start) // 2)}
        if follow:
            cue["focus"] = follow
        self.shots.append(cue)
        self.intents[str(start)] = {"intent": intent, "shows": list(subjects)}


F14S, ALL4 = [FE102, FE107], [FE102, FE107, SU_LEAD, SU_WING]
GULF = [NIMITZ, LOD_W, LOD_E, SU_LEAD]

# (from ms, until ms, subjects, intent, framing): moves take 1.5 s of viewing unless `move`.
SHOTS = [
    (0, t("00:20"), GULF,
     "Where: the carrier, the claimed line across the gulf, and Ghurdabiya on the coast.",
     {"move": 0}),
    (t("00:20"), t("01:00"), [SU_LEAD, SU_WING],
     "Down to the two Fitters leaving Ghurdabiya: the threat, from the Libyan side.",
     {"follow": SU_LEAD, "pitch": 30, "pad_km": 8}),
    (t("01:00"), t("02:30"), [S3A, SU_LEAD],
     "Cross to the S-3A off the coast as Nimitz calls \"Buster North\": the first American "
     "to run.", {"follow": S3A, "pitch": 20, "move": 2.5}),
    (t("02:30"), t("06:00"), [SU_LEAD, SU_WING],
     "Back with the Fitters climbing out over the gulf: who is coming, and how fast.",
     {"follow": SU_LEAD, "pitch": 30, "pad_km": 25, "move": 2}),
    (t("06:00"), t("11:00"), [FE102, FE107, SU_LEAD],
     "The Fast Eagles on their racetrack, with the Fitters on their way in: hunter and "
     "hunted in one frame.", {"follow": FE102, "pitch": 20, "move": 2.5}),
    (t("11:00"), t("14:30"), [FE102, SU_LEAD],
     "Venlet's radar contact: the E-2C turns the section south and the gap starts to close.",
     {"follow": FE102, "pitch": 20, "move": 2}),
    (t("14:30"), s_ms(54), ALL4,
     "The Biddle tape's range calls, twenty miles down to eight: the frame tightens as the "
     "pairs close head-on at a thousand knots.", {"follow": FE102, "pitch": 25, "move": 2}),
    (s_ms(54), s_ms(83), ALL4,
     "Tally-ho: the Fitters in welded wing, and Kleemann holding his nose on their leader.",
     {"follow": FE102, "pitch": 20, "move": 2}),
    (s_ms(83), s_ms(87), [AA2, SU_LEAD, FE102, FE107],
     "Ride the Atoll: fired head-on, it passes under 102.",
     {"follow": AA2, "pitch": 8, "pad_km": 2, "move": 1}),
    (s_ms(87), s_ms(110), ALL4,
     "Pull back to the four as they pass and the Libyans break apart.",
     {"follow": FE102, "pitch": 20}),
    (s_ms(110), s_ms(HIT_WING_S - 3), [FE102, SU_WING],
     "Kleemann turns hard after the wingman and waits for him to clear the sun.",
     {"follow": FE102, "pitch": 15, "pad_km": 5}),
    (s_ms(HIT_WING_S - 3), s_ms(HIT_WING_S), [AIM_102, FE102, SU_WING],
     "Ride Kleemann's Sidewinder to the wingman's tailpipe.",
     {"follow": AIM_102, "pitch": 8, "pad_km": 3, "move": 1}),
    (s_ms(HIT_WING_S), s_ms(150), [SU_WING, FE102],
     "Stay on the wingman as he goes down: the first kill.",
     {"follow": SU_WING, "pitch": 15, "pad_km": 4, "move": 1}),
    (s_ms(150), s_ms(HIT_LEAD_S - 3), [FE107, SU_LEAD],
     "Cross to Muczynski behind the leader: \"Want me shoot my guy down?\"",
     {"follow": FE107, "pitch": 15, "pad_km": 5}),
    (s_ms(HIT_LEAD_S - 3), s_ms(HIT_LEAD_S), [AIM_107, FE107, SU_LEAD],
     "Ride Muczynski's one good Sidewinder to the leader.",
     {"follow": AIM_107, "pitch": 8, "pad_km": 3, "move": 1}),
    (s_ms(HIT_LEAD_S), s_ms(186), [SU_LEAD, FE107],
     "Stay on the leader as his tail comes off, and the parachute that may not open.",
     {"follow": SU_LEAD, "pitch": 15, "pad_km": 4, "move": 1}),
    (s_ms(186), s_ms(REJOIN_S), ALL4,
     "Pull back to the whole scene: two falling Fitters, two F-14s, and permission to "
     "defend themselves arriving after the kills.", {"pitch": 20, "move": 2}),
    (s_ms(REJOIN_S), t("21:00"), F14S,
     "The section rejoins and turns north for Nimitz.",
     {"follow": FE102, "pitch": 20, "pad_km": 20, "move": 2}),
    (t("21:00"), DURATION, GULF + F14S,
     "Pull out to the whole gulf and the line again, as Libya searches for its pilots.",
     {"move": 3}),
]


def shots(tracks, fixed):
    """(the shot list, contiguous from 0 to DURATION; intents by start_ms)."""
    f = Framer(tracks, fixed)
    for start, end, subjects, intent, framing_ in SHOTS:
        f.shot(start, end, subjects, intent, **framing_)
    return f.shots, f.intents
