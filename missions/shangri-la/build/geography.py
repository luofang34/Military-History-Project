"""Approximate geographic anchors; paths between them are explicitly reconstructed."""
from datetime import datetime, timezone

OP = 'shangri-la'


def clock(value):
    """Ship clock (UTC+10) on 18 April, relative to 07:30; display uses Japan UTC+9."""
    h, m, s = (int(x) for x in (value.split(':') + ['0'])[:3])
    return ((h * 60 + m - 450) * 60 + s) * 1000


DURATION = clock('23:10')
ANCHOR = int(datetime(1942, 4, 17, 21, 30, tzinfo=timezone.utc).timestamp() * 1000)
JAPAN = {'kind': 'fixed', 'seconds': 32400,
         'source': 'Japan standard time, UTC+9; naval zone minus ten is UTC+10'}
SHIP = {'kind': 'fixed', 'seconds': 36000,
        'source': 'Enterprise action report: zone minus ten, UTC+10'}
# Hornet's 0800 position; Doolittle's navigator places launch 17 nautical miles north.
LAUNCH = (153.45, 35.433333)
TOKYO = (139.77, 35.70)
YOKOHAMA = (139.65, 35.46)
YOKOSUKA = (139.66, 35.29)
NAGOYA = (136.90, 35.16)
KOBE = (135.18, 34.68)
QUZHOU = (118.87, 28.97)
SHANGRAO = (117.97, 28.45)
NINGBO = (121.55, 29.87)
SHIPU = (121.93, 29.20)
WENZHOU = (120.80, 27.90)
VLADIVOSTOK = (132.15, 43.38)
YAKUSHIMA = (130.00, 30.50)
SITES = {'TOKYO': TOKYO, 'YOKOHAMA': YOKOHAMA, 'YOKOSUKA': YOKOSUKA,
         'NAGOYA': NAGOYA, 'KOBE': KOBE, 'QUZHOU': QUZHOU,
         'NINGBO': NINGBO, 'SHANGRAO': SHANGRAO, 'SOVIET AIRFIELD': VLADIVOSTOK}
