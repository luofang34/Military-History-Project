"""The reserve wave sent in after the breaches."""
from ledger import Dispute, Moment, Record

from .names import DB, EDITOR, LOG, ORB, WP  # noqa: F401

MOMENTS = {
    "anderson-turns-back": Moment(
        "Anderson turns back", "AJ-Y", "03:10",
        (Record(ORB, "Anderson, his rear turret unserviceable and the valleys filling with mist, "
                "turns back with his mine at 0310.", "03:10"),)),
    "townsend-release": Moment(
        "Townsend's attack", "AJ-O", "03:37",
        (Record(ORB, "Townsend drops on his third run at 0337; the mine bounces twice and "
                "explodes short.", "03:37"),)),
}

DISPUTES = {
    "burpee-loss": Dispute(
        "Burpee's loss", "AJ-S",
        (Record("asn", "01:53", "01:53", quote=True, label="Time"),
         Record(ORB, "Shot down at 0200 immediately south of Gilze-Rijen (Netherlands) on way "
                "to target.", "02:00", quote=True, label=EDITOR)),
        "02:00", "The ORB editor's note; the two differ by seven minutes.", at="02:00"),
    "ottley-loss": Dispute(
        "Ottley's loss", "AJ-C",
        (Record(DB, "At 0231, Group sent the code word “Gilbert” to AJ-C, and the signal was "
                "acknowledged.", "02:31", quote=True),
         Record(DB, "The second signal was not acknowledged, indicating that AJ-C had met its "
                "fate at about 0231.", "02:31", quote=True),
         Record(DB, "Ken Brown, flying AJ-F a few minutes behind, reported seeing him hit the "
                "ground at 0235.", "02:35", quote=True)),
        "02:35", "Brown's sighting, the one direct observation.", at="02:35"),
    "townsend-target": Dispute(
        "Townsend's target", "AJ-O",
        (Record(ORB, "ENNEPE DAM. 1 Mine. 60ft. 0337 hrs.", "03:37", quote=True),
         Record(ORB, "Post war research proves that Townsend attacked not the Ennerpe Dam but the "
                "Bever Dam nearby to the North West instead.", quote=True, label=EDITOR),
         Record("hinks-2010", "Sweetman (2002) makes a strong case that the fourth dam attacked "
                "was the Bever Dam", quote=True)),
        "The Ennepe, as reported", "Townsend's own report; the dams' coordinates put the Bever "
        "11 km south of the Ennepe, not north-west.", shown="03:37",
        brief="Townsend reported attacking the Ennepe dam; post-war research suggests it was "
        "the Bever dam nearby."),
}
