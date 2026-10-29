"""Permanent keys for linkable anchors and explicitly uncertain reconstruction choices."""
from ledger import merge
from . import attacks, launch, recovery

MOMENTS = merge([part.MOMENTS for part in (launch, attacks, recovery)])
DISPUTES = merge([part.DISPUTES for part in (launch, attacks, recovery)])
