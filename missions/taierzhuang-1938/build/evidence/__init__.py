"""The evidence for the Battle of Taierzhuang, in the form tools/ledger.py describes: its key
moments and its disputed facts, one module per part of the story. Record times are as each source
gives them, read on the UTC+8 clock (see the japanese-clock dispute); quotations are in the
sources' own languages, with the label giving the sense in English.
"""
import ledger

from . import advance, assault, city, duel, guns, positions, road

PARTS = (advance, guns, city, road, assault, positions, duel)
MOMENTS = ledger.merge(part.MOMENTS for part in PARTS)
DISPUTES = ledger.merge(part.DISPUTES for part in PARTS)
if set(MOMENTS) & set(DISPUTES):
    raise ValueError(f"evidence keys {sorted(set(MOMENTS) & set(DISPUTES))} are both a moment "
                     f"and a dispute")
