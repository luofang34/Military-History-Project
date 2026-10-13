"""The roads and the railroad of 1859, and a way of walking them on the clock.

The road from the Kennedy farm is today's Chestnut Grove and Harpers Ferry roads down the
Maryland bank, the road Villard says the Jefferson Guards marched down to the bridge "over the same
road over which the raiders had come". The railroad east of the bridge follows the river round the
foot of Maryland Heights and round Point of Rocks, as it did before the tunnels of 1894 and the
1860s; beyond Point of Rocks it is today's Old Main Line. West of the Point it ran on the trestle
along the armory yard.
"""
from track import Track, distance_m

from sites import (ALLSTADT_HOUSE, ARMORY_GATE, BEALL_AIR, BOLIVAR, BRIDGE_MD, CAMDEN_STATION,
                   ELLICOTTS_MILLS, KENNEDY_FARM, L, MONOCACY, RELAY, STATION, WASHINGTON_DEPOT,
                   WATER_STATION)

# OSRM over OpenStreetMap, farm lane to the Maryland end of the bridge: 7.65 km.
ROAD = [
    KENNEDY_FARM, (-77.71567, 39.37983), (-77.71785, 39.37759), (-77.72087, 39.37261),
    (-77.72406, 39.36871), (-77.72856, 39.36296), (-77.73256, 39.36025), (-77.73470, 39.35455),
    (-77.73728, 39.35137), (-77.73737, 39.34700), (-77.73730, 39.34167), (-77.73843, 39.33768),
    (-77.73914, 39.33521), (-77.73733, 39.33289), (-77.73367, 39.33025), (-77.72726, 39.32594),
    (-77.72602, 39.32428), BRIDGE_MD,
]
LOCK_34 = (-77.73855, 39.33315)  # "the lock kept by George Hardy, about a mile above the bridge"
# Byrne's, "not quite a mile and a half" from the farm; where the road passes the schoolhouse's
# estimated site; and the road at Lock 34. All three are points of ROAD.
BYRNE_ROAD = (-77.72406, 39.36871)
SCHOOLHOUSE_ROAD = (-77.73730, 39.34167)
LOCK_34_ROAD = (-77.73914, 39.33521)

# Through Bolivar and out the Charlestown pike to Halltown; Allstadt's house stands on the pike.
PIKE = [
    ARMORY_GATE, (-77.7310, 39.3236), (-77.7355, 39.3240), BOLIVAR, (-77.7490, 39.3205),
    ALLSTADT_HOUSE, (-77.7700, 39.3140), (-77.7900, 39.3120), (-77.8050, 39.3130), BEALL_AIR,
]

# The B&O from the west along the Virginia bank to the station at the bridge's town end.
FROM_WEST = [(-77.7600, 39.3360), (-77.7480, 39.3310), (-77.7380, 39.3272), (-77.7330, 39.3256),
             WATER_STATION, STATION]

# The B&O east of the bridge: OSM's track, about one point a mile, to Frederick Junction.
EAST = [
    BRIDGE_MD, (-77.72511, 39.32425), (-77.70950, 39.32597), (-77.69137, 39.32420),
    (-77.67497, 39.32994), (-77.66055, 39.32204), (-77.64391, 39.31497), (-77.62619, 39.31102),
    (-77.60148, 39.30554), (-77.58787, 39.30721), (-77.57147, 39.31119), (-77.55689, 39.30510),
    (-77.55578, 39.29138), (-77.54542, 39.27748), (-77.53495, 39.27369), (-77.51872, 39.28411),
    (-77.50878, 39.29504), (-77.49165, 39.30060), (-77.47538, 39.31157), (-77.45701, 39.32558),
    (-77.44977, 39.33108), (-77.43411, 39.34545), (-77.42390, 39.35269), (-77.41310, 39.36241),
    (-77.39694, 39.37007), (-77.39223, 39.37111), MONOCACY,
]
SANDY_HOOK_TRACK = 2  # EAST[2] is the track at Sandy Hook
# Monocacy to Baltimore by the Old Main Line, through Mount Airy, Sykesville and the Patapsco.
TO_BALTIMORE = [MONOCACY, (-77.2500, 39.3740), (-77.1550, 39.3760), (-76.9680, 39.3730),
                (-76.8970, 39.3540), ELLICOTTS_MILLS, RELAY, CAMDEN_STATION]
# The Washington Branch, from the depot to the main stem at Relay.
WASHINGTON_BRANCH = [WASHINGTON_DEPOT, (-76.9200, 38.9800), (-76.8000, 39.1000), RELAY]


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
        """Stays here until `until`; holding until now is a no-op, so legs that end on the
        hour can be followed by a hold to it."""
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


def reverse(points):
    return list(reversed(points))
