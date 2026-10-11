"""Shot framing for the Chastise story: each shot is zoomed from the tracks it must show.

Shots are north-up. A shot either follows one aircraft or holds a fixed point (the mean ground
position of its subjects), and is zoomed so every subject that exists during the shot stays
within FILL of the frame from its centre, sampled every two seconds. With the camera pitched, a
subject at height h is drawn about h·tan(pitch) above its ground point, so that offset counts.
The build fails if a shot cannot frame its subjects or if a followed aircraft has no fix.

The viewer's scale and projection come from tools/framing.py.
"""
import framing as scale
from framing import ASPECT, screen_km, width_km
from pacing import after_viewing

FILL = 0.32
MIN_ZOOM, MAX_ZOOM = 3.5, 14.5


def zoom_for(width):
    return scale.zoom_for(width, MIN_ZOOM, MAX_ZOOM, 0.5)


class Framer:
    """Subjects are track names or fixed sites; `lifetimes` gives each track's (first, last)
    fixed instant, so lost aircraft drop out of the frame once their wreck is reported. Moves
    between shots last a given viewing time under `pacing`, whatever the playback speed."""

    def __init__(self, tracks, fixed, lifetimes, pacing):
        self.tracks, self.fixed, self.lifetimes, self.pacing = tracks, fixed, lifetimes, pacing
        self.shots, self.intents = [], {}

    def alive(self, name, at):
        if name in self.fixed:
            return True
        first, last = self.lifetimes[name]
        return first <= at <= last

    def where(self, name, at):
        return (self.fixed[name], 0.0) if name in self.fixed else self.tracks[name].at(at)

    def shot(self, start, end, subjects, intent, follow=None, pitch=0, pad_km=0.0, move=1.5):
        """A shot from `start` to `end` ms, arriving from the previous shot in `move` seconds of
        viewing (0 cuts); `intent` is its {"intent", "shows"} promise for the frame report."""
        if end <= start:
            raise ValueError(f"shot {start}–{end} ms is empty")
        if self.shots and self.shots[-1]["end_ms"] != start:
            raise ValueError(f"shot at {start} ms does not follow the previous one")
        times = list(range(start, end, 2000)) + [end - 1]
        if follow is not None:
            missing = [at for at in times if not self.alive(follow, at)]
            if missing:
                raise ValueError(f"shot at {start} ms follows {follow}, untracked at {missing[0]}")
            centre_at = lambda at: self.where(follow, at)[0]  # noqa: E731
            target = {"kind": "entity", "value": follow}
        else:
            pts = [self.where(n, at)[0] for at in times for n in subjects if self.alive(n, at)]
            if not pts:
                raise ValueError(f"shot at {start} ms has no subject")
            centre = (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))
            centre_at = lambda _at: centre  # noqa: E731
            target = {"kind": "point", "value": {"lon": round(centre[0], 5),
                                                 "lat": round(centre[1], 5)}}
        need = pad_km / FILL
        for at in times:
            for n in subjects:
                if self.alive(n, at):
                    x, y = screen_km(centre_at(at), *self.where(n, at), pitch)
                    need = max(need, abs(x) / FILL, abs(y) / (FILL * ASPECT))
        zoom = zoom_for(need)
        if need > width_km(zoom) + 1e-6:
            raise ValueError(f"shot at {start} ms cannot frame {subjects} at pitch {pitch}")
        cue = {"start_ms": start, "end_ms": end, "target": target, "zoom": round(zoom, 2),
               "pitch": pitch, "bearing": 0.0, "orbit_deg_s": 0.0,
               "transition_ms": min(after_viewing(self.pacing, start, move) - start,
                                    (end - start) // 2)}
        if follow:
            cue["focus"] = follow
        self.shots.append(cue)
        self.intents[str(start)] = intent
        return cue
