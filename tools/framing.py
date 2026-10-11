"""The viewer's map scale and the screen projection that camera framing is fitted with.

Calibrated from the viewer: at zoom 12.5 the map is about 8 km wide, and the map area is about
0.8 as tall as it is wide. With the camera pitched, a subject at height h is drawn about
h·tan(pitch) above its ground point.
"""
import math

WIDTH_KM_AT_12_5 = 8.0
ASPECT = 0.8  # map height over width


def width_km(zoom):
    """Map width in kilometres at `zoom`."""
    return WIDTH_KM_AT_12_5 * 2 ** (12.5 - zoom)


def zoom_for(width, lowest, highest, narrowest_km):
    """The zoom that shows `width` km, no narrower than `narrowest_km`, within the range."""
    z = 12.5 - math.log2(max(width, narrowest_km) / WIDTH_KM_AT_12_5)
    return max(lowest, min(highest, z))


def screen_km(centre, point, alt_m, pitch):
    """Where `point` at `alt_m` lands relative to a north-up frame centred on `centre`:
    (km right, km up), counting the upward shift a pitched camera gives anything above ground."""
    lat = (centre[1] + point[1]) / 2
    x = (point[0] - centre[0]) * 111.2 * math.cos(math.radians(lat))
    y = (point[1] - centre[1]) * 111.2 + alt_m / 1000 * math.tan(math.radians(pitch))
    return x, y
