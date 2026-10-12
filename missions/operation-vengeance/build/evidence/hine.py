"""Hine's loss on the way home."""
from ledger import Dispute, Record

from .names import AMES, GRANT, HN, LEHR, PW_HINE, REPORT, SCAN, SHEET, SUGITA, WP, YANAGIYA

MOMENTS = {
}

DISPUTES = {
    "hine-last-seen": Dispute(
        "Where Hine was last seen", "HINE",
        (Record(REPORT, "During these minutes, Hines' left engine started to smoke and he was "
                "last seen losing altitude south of Shortland Island.", quote=True,
                label=SCAN),
         Record(PW_HINE, "MACR 599 states Hine was last seen by Major Mitchell four miles north "
                "of Shortland just above the sea with one engine smoking and three Zeros making "
                "firing passes.", quote=True),
         Record(PW_HINE, "MACR 609 states Hine was last seen south of Shortland at 9:40am by Lt. "
                "Besby T. Holmes, seen trailing smoke or vapor from the left engine and headed "
                "in the direction of Wilson Strait to the southwest of Shortland.", "09:40",
                quote=True),
         Record(PW_HINE, "No trace of his plane was ever found and he was never seen to crash.",
                quote=True),
         Record(LEHR, "I could see nothing, no splash or anything, and planes falling always "
                "left a big circle of bubbles and the like in the water.", quote=True,
                label="Barber"),
         Record(GRANT, "Mitchell had seen a Lightning trailing oily smoke, being chased by a "
                "Zero.", quote=True)),
        "Hit four miles north of Shortland at 09:41:36; last seen south of it at 09:45:40",
        "The same-day report and Holmes, Hine's element leader (MACR 609), last see him south "
        "of Shortland; Mitchell, from top cover, sees him smoking north of it with Zeros making "
        "passes, which the replay takes as the moment he is hit. Wilson Strait, between Vella "
        "Lavella and Ranongga (OpenStreetMap), lies south-east, on the way home, not south-west "
        "as Pacific Wrecks has it. South of Shortland lies about 40 km from the fight off "
        "Moila Point, a few minutes beyond MACR 609's 9:40. He keeps his height over the "
        "island's hills and loses it beyond.", at="09:45:40", outside=True),
    "zero-claims": Dispute(
        "Whether the Zeros claimed Hine", "HINE",
        (Record(WP, "although neither he nor any of the other Zero pilots had claimed a P-38 "
                "that day.", quote=True),
         Record(SHEET, "撃墜3 同上(不確)3", quote=True,
                label="results: three shot down, three uncertain; per pilot, Tsujinoue two (one "
                "uncertain), Sugita two, Hidaka one uncertain, Yanagiya one; read from the "
                "scan, no places given"),
         Record(SUGITA, "空中戦闘では、杉田の射撃で敵1機がエンジンから煙を噴き、他の敵1機が杉田機に来襲"
                "して交戦、逃げる敵機の翼根を撃って撃墜した", quote=True,
                label="Sugita's fire set one enemy smoking from an engine; he shot down another"),
         Record(GRANT, "reported severely damaging a P-38 that was flying next to another P-38 "
                "struggling to drop its tanks. It was Hine.", quote=True,
                label="of Sugita's claim; the identification is Grant's"),
         Record(YANAGIYA, "約30分追ってゆきましたらね、コロンバーラ島附近を、P38が単機で悠々と飛んでるんですよ。",
                quote=True, label="Yanagiya: after a 30-minute chase, a lone P-38 near "
                "Kolombangara, which he hit; it streamed fuel toward the sea, not seen to "
                "crash")),
        "Not attributed", "The escort did claim P-38s, against Wikipedia, but its sheet gives no "
        "places, and no US aircraft but Hine was lost. The replay shows only the passes Mitchell "
        "saw; Yanagiya's P-38 near Kolombangara, if it was Hine, lies beyond the record's end.",
        shown="09:41:40"),
    "hine-engine": Dispute(
        "Hine's smoking engine", "HINE",
        (Record(REPORT, "Hines' left engine started to smoke", quote=True, label=SCAN),
         Record(PW_HINE, "trailing smoke or vapor from the left engine", quote=True,
                label="MACR 609"),
         Record(LEHR, "Other pilots reported seeing Hine's left engine smoking, but no one saw "
                "him go down.", quote=True),
         Record(HN, "Last seen trailing vapor from his right engine, Ray Hine never returned.",
                quote=True),
         Record(AMES, "but Hine was seen heading out to sea smoking from his right engine.",
                quote=True)),
        "The left engine", "The report and MACR 609, the records made at the time.",
        shown="09:40:30"),
}
