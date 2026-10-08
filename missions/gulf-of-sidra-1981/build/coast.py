"""The Gulf of Sidra's shore from Misrata to the gulf's southern bend, for distance checks.

An ordered extract of the Natural Earth 10 m coastline (public domain), decimated to about
6 km spacing. It is accurate to about a nautical mile, enough to keep reconstructed tracks
outside Libya's 12 nm territorial sea and to check the briefing's distances from land.
"""
import math

SHORE = [
    (18.781, 30.376), (18.719, 30.392), (18.653, 30.422), (18.568, 30.5), (18.324, 30.657),
    (18.236, 30.747), (18.175, 30.786), (18.017, 30.838), (17.927, 30.855), (17.862, 30.914),
    (17.776, 30.935), (17.692, 30.96), (17.614, 30.992), (17.467, 31.03), (17.382, 31.079),
    (17.16, 31.119), (16.942, 31.183), (16.728, 31.224), (16.359, 31.227), (16.045, 31.276),
    (15.761, 31.388), (15.688, 31.438), (15.623, 31.497), (15.514, 31.628), (15.37, 31.929),
    (15.355, 32.039), (15.36, 32.102), (15.37, 32.159), (15.323, 32.224), (15.292, 32.281),
    (15.233, 32.347), (15.182, 32.395), (15.115, 32.413), (14.911, 32.444),
]


def nm_to_shore(p):
    """Nautical miles from (lon, lat) to the nearest point on the shore polyline."""
    k = math.cos(math.radians(p[1]))
    best = math.inf
    for a, b in zip(SHORE, SHORE[1:]):
        ax, ay = (a[0] - p[0]) * 60 * k, (a[1] - p[1]) * 60
        bx, by = (b[0] - p[0]) * 60 * k, (b[1] - p[1]) * 60
        vx, vy = bx - ax, by - ay
        length = vx * vx + vy * vy
        f = 0.0 if length == 0 else max(0.0, min(1.0, -(ax * vx + ay * vy) / length))
        best = min(best, math.hypot(ax + f * vx, ay + f * vy))
    return best
