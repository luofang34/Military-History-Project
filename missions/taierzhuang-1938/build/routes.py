"""The Tianjin–Pukou railway of 1938, and a way of moving units along roads on the clock.

The line between Yanzhou and Hanzhuang still runs on its 1912 alignment (station sites and the
1912 kilometre posts in the county gazetteers agree with today's line), so its points are today's
京沪线, taken a point every 0.04° of latitude, good to about a kilometre; the stations are their
OSM nodes, Lincheng's moved 500 m north to its 1938 site.
"""
from track import Track, distance_m

from sites import JIEHE_STATION, L, LINCHENG, NANSHAHE, STATION, YANZHOU, ZOUXIAN, GUANQIAO

RAILWAY = [
    YANZHOU, (116.8600, 35.52), (116.8862, 35.48), (116.9104, 35.44), ZOUXIAN,
    (116.9692, 35.36), (116.9886, 35.32), (117.0132, 35.28), (117.0472, 35.24), JIEHE_STATION,
    (117.0977, 35.16), (117.1271, 35.12), STATION, (117.1579, 35.04), NANSHAHE,
    (117.1848, 34.96), GUANQIAO, (117.2131, 34.88), (117.2223, 34.84), LINCHENG,
]


def length_m(points):
    return sum(distance_m(a, b) for a, b in zip(points, points[1:]))


class Mover:
    """A track built leg by leg from where and when the last leg ended."""

    def __init__(self, point, at):
        self.track = Track().add(L(at), point, 0.0)

    @property
    def point(self):
        return self.track.waypoints[-1].point

    @property
    def at(self):
        return self.track.waypoints[-1].at_ms

    def hold(self, until):
        """Stays here until `until`; holding until now is a no-op."""
        if L(until) != self.at:
            self.track.add(L(until), self.point, 0.0)
        return self

    def along(self, points, until):
        """Along `points`, from here, arriving at `until` at an even pace."""
        points = [self.point] + [p for p in points if p != self.point]
        start, end = self.at, L(until)
        total = length_m(points)
        done = 0.0
        for a, b in zip(points, points[1:]):
            done += distance_m(a, b)
            self.track.add(start + (end - start) * done / total, b, 0.0)
        return self

    def to(self, point, until):
        return self.along([point], until)


def railway_between(a, b):
    """The railway's points from station `a` to station `b`, in either direction."""
    i, j = RAILWAY.index(a), RAILWAY.index(b)
    return RAILWAY[i:j + 1] if i <= j else list(reversed(RAILWAY[j:i + 1]))
