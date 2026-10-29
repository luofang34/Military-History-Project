"""Sixteen aircraft, identified by serial, with adopted ship-clock anchors.

Launches follow Doolittle's aircraft accounts. Attack/end times without an explicit pilot
clock are editorial estimates, recorded as disputes rather than invented observations.
Coordinates denote districts or broad recovery areas, not surveyed bomb strikes or wrecks.
"""
from dataclasses import dataclass
from geography import (TOKYO, YOKOHAMA, YOKOSUKA, NAGOYA, KOBE,
                       SHIPU, WENZHOU, VLADIVOSTOK)


@dataclass(frozen=True)
class Crew:
    number: int
    serial: str
    pilot: str
    launch: str
    attack: str
    target: tuple
    objective: str
    finish: str
    endpoint: tuple
    outcome: str
    survivors: int = 5
    captured: int = 0

    @property
    def id(self):
        return f'B25-{self.number:02d}'


CREWS = [
    Crew(1, '40-2344', 'James H. Doolittle', '08:20', '13:30', TOKYO,
         'Tokyo industrial districts; four incendiary clusters', '21:20', (119.0, 30.25), 'bailout'),
    Crew(2, '40-2292', 'Travis Hoover', '08:25', '13:35', (139.74, 35.75),
         'Tokyo arsenal district', '21:10', (121.6, 29.8), 'forced landing'),
    Crew(3, '40-2270', 'Robert M. Gray', '08:30', '13:40', (139.80, 35.70),
         'Tokyo gas and chemical works', '22:15', (119.1, 28.7), 'bailout', 4),
    Crew(4, '40-2282', 'Everett W. Holstrom', '08:33', '13:35', (140.10, 34.90),
         'Bombs jettisoned offshore under fighter attack', '22:00', (118.2, 28.3), 'bailout'),
    Crew(5, '40-2283', 'David M. Jones', '08:37', '13:45', (139.78, 35.65),
         'Tokyo oil, power and factory targets', '22:10', (118.6, 28.7), 'bailout'),
    Crew(6, '40-2298', 'Dean E. Hallmark', '08:40', '13:50', TOKYO,
         'Tokyo; detailed attack report unavailable', '22:00', WENZHOU, 'ditching', 3, 3),
    Crew(7, '40-2261', 'Ted W. Lawson', '08:43', '13:45', (139.78, 35.68),
         'Tokyo factories and residential area', '21:00', (121.65, 29.0), 'ditching'),
    Crew(8, '40-2242', 'Edward J. York', '08:46', '13:50', TOKYO,
         'Tokyo; then Soviet diversion', '19:30', VLADIVOSTOK, 'internment'),
    Crew(9, '40-2303', 'Harold F. Watson', '08:50', '14:00', (139.80, 35.65),
         'Tokyo Gas and Electric; identification disputed', '22:30', (116.5, 27.7), 'bailout'),
    Crew(10, '40-2250', 'Richard O. Joyce', '08:53', '14:00', (139.75, 35.62),
         'Japan Special Steel and surrounding Tokyo districts', '22:20', (118.9, 29.4), 'bailout'),
    Crew(11, '40-2249', 'Charles R. Greening', '08:56', '14:10', (140.1, 35.6),
         'Reported refinery near Sakura; identification uncertain', '22:40', (118.1, 29.5), 'bailout'),
    Crew(12, '40-2278', 'William M. Bower', '08:59', '14:15', YOKOHAMA,
         'Yokohama refinery and factories', '22:30', (118.4, 29.4), 'bailout'),
    Crew(13, '40-2247', 'Edgar E. McElroy', '09:01', '14:40', YOKOSUKA,
         'Yokosuka naval yard', '22:45', (116.5, 28.5), 'bailout'),
    Crew(14, '40-2297', 'John A. Hilger', '09:07', '15:20', NAGOYA,
         'Nagoya barracks, oil storage, arsenal and aircraft works', '22:20', (118.2, 28.3), 'bailout'),
    Crew(15, '40-2267', 'Donald G. Smith', '09:15', '15:45', KOBE,
         'Kobe waterfront and aircraft industry', '22:10', (121.7, 29.1), 'ditching'),
    Crew(16, '40-2268', 'William G. Farrow', '09:19', '15:30', NAGOYA,
         'Nagoya; detailed contemporary report unavailable', '23:00', SHIPU, 'bailout', 5, 5),
]
