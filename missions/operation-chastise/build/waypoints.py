"""Turning points of the planned routes, in flying order.

The order of points and their names follow the "Operation Chastise: planned routes" map
(IBCC 33688, redrawn from Appendix A of 5 Group Operation Order B.976) and Maltby's
navigation log as rebuilt on dambustersblog. Only ZERO and NORTH_ZERO are the order's own
coordinates; the others are geocoded turning-point names, ±1–3 km. Points are (lon, lat).
"""
from sites import SCAMPTON

# England.
WEST_RAYNHAM = (0.785, 52.790)
SOUTHWOLD = (1.679, 52.326)
WAINFLEET = (0.237, 53.107)
# Mablethorpe: the coast the AJ-T log names, on the planned 090° leg from Scampton.
NORTH_COAST_OUT = (0.26, 53.34)

# Southern route (waves 1 and 3).
ZERO = (3.0000, 51.8667)  # B.976: 51°52'N 03°00'E, the first section's Zero Hour position
SCHELDT = (3.70, 51.60)  # "between Walcheren and Schouwen"; no fix published
ROOSENDAAL = (4.456, 51.533)
GILZE_SOUTH = (4.93, 51.53)  # on the Wilhelmina canal south of Gilze-Rijen
BEEK = (5.647, 51.520)  # Wilhelmina canal meets the Zuid-Willemsvaart near Beek en Donk
GOCH = (6.159, 51.676)
REES = (6.396, 51.758)
HALTERN_LAKES = (7.22, 51.74)  # flak and searchlights met by Gibson's section
AHSEN = (7.309, 51.700)
AHLEN = (7.891, 51.763)
SOEST_WEST = (8.02, 51.58)  # between Hamm and Soest, heading south for the lake

SOUTH_OUT = [SOUTHWOLD, ZERO, SCHELDT, ROOSENDAAL, GILZE_SOUTH, BEEK, GOCH, REES,
             HALTERN_LAKES, AHSEN, AHLEN, SOEST_WEST]

# Northern route (wave 2).
NORTH_ZERO = (4.0000, 53.3167)  # B.976: 53°19'N 04°00'E, the second wave at Zero Hour
VLIELAND_GAP = (4.95, 53.22)  # between Vlieland and Texel
STAVOREN = (5.360, 52.883)
HARDERWIJK = (5.619, 52.349)
DOESBURG = (6.153, 52.012)
NORTH_OUT = [NORTH_COAST_OUT, NORTH_ZERO, VLIELAND_GAP, STAVOREN, HARDERWIJK, DOESBURG, REES,
             HALTERN_LAKES, AHSEN, AHLEN]
# Target X on the AJ-T log, where it turned for the Sorpe; placed 2 km short of the Möhne dam.
MOHNE_TURN = (8.0385, 51.5026)
AFSLUITDIJK = (5.20, 53.02)  # "Wall" on the AJ-T log, the IJsselmeer dam
VLIELAND = (5.05, 53.27)  # "Island Vlieland" on the AJ-T log

# Return routes, numbered as on the planned-routes map.
DULMEN = (7.279, 51.828)
NORDHORN_NNW = (7.07, 52.44)
HARDENBERG = (6.619, 52.575)
ZWARTE_WATER = (6.09, 52.59)
DEN_HELDER_SOUTH = (4.760, 52.958)
NORTH_SEA_EXIT = (4.30, 52.98)
RETURN_1 = [AHLEN, DULMEN, NORDHORN_NNW, HARDENBERG, ZWARTE_WATER, DEN_HELDER_SOUTH,
            NORTH_SEA_EXIT, WAINFLEET, SCAMPTON]

ZUTPHEN = (6.195, 52.140)
LEMMER = (5.710, 52.844)
RETURN_2 = [ZUTPHEN, LEMMER, STAVOREN, DEN_HELDER_SOUTH, NORTH_SEA_EXIT, WAINFLEET, SCAMPTON]

EGMOND_SOUTH = (4.626, 52.618)
RETURN_3 = [REES, HARDERWIJK, EGMOND_SOUTH, WAINFLEET, SCAMPTON]

# Reconstructed points the flight plans need; none is sourced to better than its bound.
MARBECK_ABEAM = (6.87, 51.755)  # Maudslay's section abeam Marbeck when Astell went down
TEXEL_NORTH = (4.86, 53.15)  # Byers, off track over Texel
RICE_SEA = (5.05, 53.14)  # Rice strikes the water east of Vlieland
SORPE_NORTH = (7.96, 51.42)  # approach to the Sorpe from the Möhne side
ENNEPE_SEARCH = (7.47, 51.30)  # Townsend's search of the misty valleys
ANDERSON_TURN = (7.62, 51.60)  # where Anderson turned back in mist, 03:10; ±20 km
HAMM = (7.82, 51.68)
OSTONNEN_CLIMB = (8.030, 51.512)  # Hopgood's burning climb, between the dam and Ostönnen
