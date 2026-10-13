"""A way of moving units and rounds on the clock."""
from track import Track, distance_m

from sites import L


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
