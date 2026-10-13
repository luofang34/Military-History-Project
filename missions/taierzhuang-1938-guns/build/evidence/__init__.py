"""The artillery evidence, in the form tools/ledger.py describes. Record times are as each source
gives them, on the UTC+8 clock both the Japanese reports keep; quotations are in the sources'
languages, with the label giving the sense in English.
"""
import ledger

from . import fire, positions

PARTS = (positions, fire)
MOMENTS = ledger.merge(part.MOMENTS for part in PARTS)
DISPUTES = ledger.merge(part.DISPUTES for part in PARTS)
if set(MOMENTS) & set(DISPUTES):
    raise ValueError(f"evidence keys {sorted(set(MOMENTS) & set(DISPUTES))} are both a moment "
                     f"and a dispute")
