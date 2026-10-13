"""The raid's evidence, in the form tools/ledger.py describes: its key moments and its disputed
facts, one module per part of the story. Record times are as each source gives them, read on the
Harpers Ferry clock (sites.py); sources quoted by a later writer are labelled with whose words
they are.
"""
import ledger

from . import farm, monday, night, tuesday, wire

PARTS = (farm, night, wire, monday, tuesday)
MOMENTS = ledger.merge(part.MOMENTS for part in PARTS)
DISPUTES = ledger.merge(part.DISPUTES for part in PARTS)
if set(MOMENTS) & set(DISPUTES):
    raise ValueError(f"evidence keys {sorted(set(MOMENTS) & set(DISPUTES))} are both a moment "
                     f"and a dispute")
