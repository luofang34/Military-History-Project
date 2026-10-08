"""Camera shots for the Gulf of Sidra story, framed from the tracks and checked for coverage.

Over open sea there is no ground reference, so every shot is north-up and never orbits. Moving
subjects are followed, and each shot is zoomed to keep every subject on screen for its whole
span, sampled every second. Framing works in screen space: with the camera pitched, a subject
at altitude h is drawn about h·tan(pitch) above its ground point, so that offset counts too.
The build fails if any subject would leave the frame.

Scale is calibrated from the viewer: at zoom 12.5 the map is about 8 km wide, and the map area
is about 0.8 as tall as it is wide.
"""
import math

from geometry import (AA2, AIM_102, AIM_107, FE102, FE107, LOD_W, LOD_E, MISSILES, NIMITZ, S3A,
                      SU_LEAD, SU_WING, s_ms)

WIDTH_KM_AT_12_5 = 8.0
ASPECT = 0.8  # map height over width
FILL = 0.30  # a subject may sit at most this fraction of the frame size from the centre
MIN_ZOOM, MAX_ZOOM = 5.0, 12.0


def width_km(zoom):
    return WIDTH_KM_AT_12_5 * 2 ** (12.5 - zoom)


def zoom_for(width):
    z = 12.5 - math.log2(max(width, 2.0) / WIDTH_KM_AT_12_5)
    return max(MIN_ZOOM, min(MAX_ZOOM, z))


def screen_km(centre, point, alt_m, pitch):
    """Where `point` at `alt_m` lands relative to a north-up frame centred on `centre`:
    (km right, km up), counting the upward shift a pitched camera gives anything above ground."""
    lat = (centre[1] + point[1]) / 2
    x = (point[0] - centre[0]) * 111.2 * math.cos(math.radians(lat))
    y = (point[1] - centre[1]) * 111.2 + alt_m / 1000 * math.tan(math.radians(pitch))
    return x, y


class Framer:
    """Positions of every subject (tracks and fixed points) and the shot list being built."""

    def __init__(self, tracks, fixed):
        self.tracks, self.fixed, self.shots = tracks, fixed, []

    def alive(self, name, at):
        if name in self.fixed:
            return True
        tr = self.tracks[name]
        return tr.start <= at <= tr.end if name in MISSILES else at >= tr.start

    def where(self, name, at):
        return (self.fixed[name], 0.0) if name in self.fixed else self.tracks[name].at(at)

    def shot(self, start, end, subjects, follow=None, pitch=0, pad_km=0.0, transition=3000):
        """A north-up shot following `follow` (or fixed on the subjects' mean ground position),
        zoomed so every living subject stays within FILL of the frame from its centre."""
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
               "transition_ms": min(transition, (end - start) // 2)}
        if follow:
            cue["focus"] = follow
        self.shots.append(cue)


def shots(tracks, fixed, t, duration):
    """The shot list, contiguous from 0 to `duration`."""
    f = Framer(tracks, fixed)
    F14S, ALL4 = [FE102, FE107], [FE102, FE107, SU_LEAD, SU_WING]
    gulf = [NIMITZ, LOD_W, LOD_E, SU_LEAD]
    f.shot(0, t("00:20"), gulf, transition=0)
    f.shot(t("00:20"), t("01:00"), [SU_LEAD, SU_WING], SU_LEAD, 30, pad_km=8)
    f.shot(t("01:00"), t("02:30"), [S3A, SU_LEAD], S3A, 20, transition=6000)
    f.shot(t("02:30"), t("06:00"), [SU_LEAD, SU_WING], SU_LEAD, 30, pad_km=25,
           transition=8000)
    f.shot(t("06:00"), t("11:00"), [FE102, FE107, SU_LEAD], FE102, 20, transition=15_000)
    f.shot(t("11:00"), t("13:00"), [FE102, SU_LEAD], FE102, 20, transition=10_000)
    f.shot(t("13:00"), t("14:30"), ALL4, FE102, 25, transition=10_000)
    f.shot(t("14:30"), s_ms(15), ALL4, FE102, 25, transition=6000)
    f.shot(s_ms(15), s_ms(54), ALL4, FE102, 25, transition=5000)
    f.shot(s_ms(54), s_ms(83), ALL4, FE102, 20, transition=4000)
    f.shot(s_ms(83), s_ms(87), [AA2, SU_LEAD, FE102, FE107], AA2, 15, pad_km=2,
           transition=1000)
    f.shot(s_ms(87), s_ms(110), ALL4, FE102, 20, transition=2000)
    f.shot(s_ms(110), s_ms(138), [FE102, SU_WING], FE102, 15, pad_km=5, transition=3000)
    f.shot(s_ms(138), s_ms(141), [AIM_102, FE102, SU_WING], AIM_102, 15, pad_km=3,
           transition=800)
    f.shot(s_ms(141), s_ms(150), [SU_WING, FE102], SU_WING, 15, pad_km=4, transition=1500)
    f.shot(s_ms(150), s_ms(170), [FE107, SU_LEAD], FE107, 15, pad_km=5, transition=3000)
    f.shot(s_ms(170), s_ms(173), [AIM_107, FE107, SU_LEAD], AIM_107, 15, pad_km=3,
           transition=800)
    f.shot(s_ms(173), s_ms(186), [SU_LEAD, FE107], SU_LEAD, 15, pad_km=4, transition=1500)
    f.shot(s_ms(186), s_ms(240), ALL4, None, 20, transition=6000)
    f.shot(s_ms(240), t("21:00"), [FE102, FE107], FE102, 20, pad_km=20, transition=8000)
    f.shot(t("21:00"), duration, gulf + F14S, transition=30_000)
    return f.shots
