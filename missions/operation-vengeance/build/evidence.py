"""Operation Vengeance's disputed facts, in the form tools/ledger.py describes: each source's
record, compared with the cited pages and, for the 13th Fighter Command report, with its
scanned typescript, and the replay's estimate. Record times are Henderson Field time (UTC+11);
Japanese records keep Tokyo time (UTC+9) in their own words.
"""
from ledger import Dispute, Record
from sites import YAMAMOTO

REPORT = "13th-fighter-command-report"
WP = "wikipedia-operation-vengeance"
HN = "historynet-death-by-p38"
AMES = "warfare-history-network-ames"
GRANT = "afm-grant"
HAULMAN = "afm-haulman"
COURT = "barber-v-widnall"
JA = "ja-wikipedia-kaigun-ko-jiken"
SUGITA = "ja-wikipedia-sugita"
PW_2656 = "pacific-wrecks-2656"
PW_326 = "pacific-wrecks-t1-326"
PW_HINE = "pacific-wrecks-hine"
CONDON = "condon-usni-1990"
LEHR = "historynet-lehr-hine"
SHEET = "jacar-204-kokutai-18-april"
YANAGIYA = "yanagiya-yoshimura"
SCAN = "typescript, read from the scan"

DISPUTES = {
    "sighting": Dispute(
        "The sighting", "CANNING",
        (Record(REPORT, "to the Southwestern coast of Bougainville at the designated time of "
                "0935. As this point was reach the enemy was sighted.", "09:35", quote=True,
                label=SCAN),
         Record(WP, "Mitchell and his force arrived at the intercept point one minute early, at "
                "09:34, just as Yamamoto's aircraft descended into view in a light haze.",
                "09:34", quote=True),
         Record(HN, "Mitchell checked his watch: 0934. They were a minute ahead of schedule.",
                "09:34", quote=True),
         Record(AMES, "It was 9:35 am.", "09:35", quote=True),
         Record(JA, "7時33分　P-38戦闘機16機（出撃後2機故障帰還）、V字編隊の一式陸上攻撃機2機、"
                "零式艦上戦闘機６機をブーゲンビル島上空で発見、攻撃開始。", "09:33", quote=True,
                label="07:33 Tokyo, 09:33 here")),
        "09:34", "Two accounts give 09:34, a minute before the 09:35 the report sets; the "
        "Japanese record's 07:33 Tokyo agrees within two minutes.", at="09:34"),
    "bettys-down": Dispute(
        "The Bettys shot down", YAMAMOTO,
        (Record(JA, "7時50分頃　山本長官搭乗の1番機被弾、モイラ岬のジャングルに墜落。宇垣纏参謀長"
                "搭乗の2番機も被弾炎上し海上に不時着。", "09:50", quote=True,
                label="about 07:50 Tokyo, 09:50 here"),
         Record(SUGITA, "しかし、午前7時45-50分（日本時間）、一式陸攻2機は敵の攻撃で撃墜され、"
                "山本長官は死亡した", "09:45", "09:50", quote=True,
                label="07:45–07:50 Tokyo, 09:45–09:50 here"),
         Record(PW_2656, "Crashed April 18, 1943 at 8:00am", quote=True,
                label="no clock is named")),
        "09:38 and 09:39:20", "T1-323 crashes at 09:38 and T1-326 ditches at 09:39:20, a few "
        "minutes after the 09:34 sighting, as US accounts fly the attack; the same Japanese "
        "accounts put the sighting at 07:33–07:35 Tokyo, so their 07:45–07:50 leaves 10–17 "
        "minutes that no account of the fight fills.", at="09:38", outside=True),
    "credit": Dispute(
        "Who shot down T1-323", YAMAMOTO,
        (Record(REPORT, "He came into it broadside - fired his bursts - a wing flew off and the "
                "plane went flaming to the earth.", quote=True, label=f"Lanphier, {SCAN}"),
         Record(REPORT, "When he fired, the tail section flew off, the bomber turned over on its "
                "back and plummeted to the earth.", quote=True, label=f"Barber, {SCAN}"),
         Record(COURT, "The 1985 Board thus concluded that credit was properly shared, as both "
                "Barber's and Lanphier's fire had contributed to the destruction of Yamamoto's "
                "bomber.", quote=True),
         Record(COURT, "We do not express an opinion as to which pilot, if indeed only one "
                "pilot, was responsible for shooting down Yamamoto.", quote=True),
         Record(PW_2656, "Postwar research has definitively proven Lanphier's victory claim was "
                "incorrect and this bomber was shoot down solely by Barber.", quote=True),
         Record(HAULMAN, "credit for shooting down Yamamoto's plane really should go to Rex "
                "Barber.", quote=True)),
        "Barber's run from astern brings T1-323 down; official credit stays shared",
        "Both attacks are flown as reported; the bomber falls after Barber's run, as Pacific "
        "Wrecks and Haulman conclude, while the Air Force's shared credit stands.",
        shown="09:38"),
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
    "ballale-arrival": Dispute(
        "When the Bettys were due at Ballale", YAMAMOTO,
        (Record(WP, "to depart Rabaul at 06:00 and arrive at Balalae at 08:00, Tokyo time.",
                "10:00", quote=True, label="08:00 Tokyo, 10:00 here"),
         Record(PW_2656, "scheduled to land at 9:45am (7:45am Tokyo time)", "09:45",
                quote=True)),
        "Not shown", "The Bettys never arrive; the plan the report gives, to meet them at "
        "09:35, is what the replay flies.", shown="08:52"),
    "take-off": Dispute(
        "Take-off", "MITCHELL",
        (Record(REPORT, "Time: Take-off 0725 - Return 1140.", "07:25", quote=True, label=SCAN),
         Record(WP, "The specially fitted P-38s took off from Kukum Field on Guadalcanal "
                "beginning at 07:25 on 18 April.", "07:25", quote=True),
         Record(JA, "5時25分　P-38戦闘機18機、ガダルカナル島ヘンダーソン基地出撃。", "07:25",
                quote=True, label="05:25 Tokyo, 07:25 here"),
         Record(HN, "At 0710 hours Mitchell led the cover flight takeoff in Mitch's Squitch.",
                "07:10", quote=True),
         Record(AMES, "we took off at 7:15 am, joined in formation, and left the island at 7:30 "
                "am", "07:15", quote=True)),
        "07:25", "The report's own take-off time, which Wikipedia and the Japanese record share.",
        at="07:25"),
    "p38-count": Dispute(
        "How many P-38s flew", "MITCHELL",
        (Record(REPORT, "Our Forces: 16 P-38's.", quote=True, label=SCAN),
         Record(WP, "10 of the 18 pilots were drawn from the other two squadrons of the 347th "
                "Group, (8 from the 12th FS and 2 from the 70th FS)", quote=True),
         Record(COURT, "sending fifteen P-38's from Guadalcanal", quote=True),
         Record(JA, "P-38戦闘機18機", quote=True, label="eighteen P-38s")),
        "Eighteen take off; sixteen reach Bougainville", "McLanahan's tyre and Moore's tanks "
        "(Wikipedia, Grant) account for the two the report does not count.", shown="07:25:30"),
    "lakunai": Dispute(
        "Departure from Lakunai", YAMAMOTO,
        (Record(JA, "6時05分　一番機に山本長官と幕僚、二番機には…宇垣纏中将ほか幕僚が乗った一式陸上"
                "攻撃機2機、および護衛の零式艦上戦闘機9機、ニューブリテン島ラバウル東飛行場を離陸。",
                "08:05", quote=True, label="06:05 Tokyo, 08:05 here"),
         Record(PW_2656, "At 7:10am local time (6:10am Tokyo time) both bombers took off from "
                "Lakunai Airfield", "08:10", quote=True),
         Record(HN, "Taking off on schedule at 0600 Tokyo time", "08:00", quote=True)),
        "08:06:35", "Between the Japanese record's 06:05 and Pacific Wrecks' 06:10 Tokyo.",
        at="08:06:35"),
    "escort": Dispute(
        "The escort's strength", "ESCORT",
        (Record(REPORT, "Enemy Forces: 3 Type 1 M/B \"Betty\" and 6 Type 0 SSF \"Zeke\".",
                quote=True, label=SCAN),
         Record(JA, "零式艦上戦闘機9機（内3機戦闘前に引きかえす。零戦隊第二小隊の三番機を務めた柳谷"
                "飛行兵長は元々6機だったと主張している。）", quote=True,
                label="nine Zeros, three turning back; Yanagiya says six from the start"),
         Record(SUGITA, "全戦闘機6機の内の第一小隊三番機として杉田も参加", quote=True,
                label="six fighters in all")),
        "Six Zeros in two sections of three", "Six at the fight in every account, including "
        "Yanagiya's own.", shown="08:08:30"),
    "betty-height": Dispute(
        "The Bettys' height", "BETTYS",
        (Record(WP, "They climbed to 6,500 feet (2,000 m), with their fighter escort at their 4 "
                "o'clock position and 1,500 feet (460 m) higher", quote=True),
         Record(REPORT, "The Two bombers were together, flying at 4500 feet, with two sections - "
                "3 Zeros each - 1500 feet above them and slightly to the rear.", "09:34",
                quote=True, label=SCAN),
         Record(AMES, "Two Betty bombers were at 4,000 feet with six Zeros at about 1,500 feet "
                "higher", "09:34", quote=True)),
        "6,500 ft in cruise, 4,500 ft at the sighting", "Wikipedia's cruise height and the "
        "report's height when sighted, the escort 1,500 ft above in both.", shown="08:10"),
    "route-length": Dispute(
        "Length of the P-38 route", "MITCHELL",
        (Record(REPORT, "the flight went 410 miles over the circuitous all-water route",
                quote=True, label=SCAN),
         Record(REPORT, "a 435 mile interception by land planes largely over water", quote=True,
                label=SCAN),
         Record(AMES, "the longest combat mission yet flown (420 miles)", quote=True),
         Record(GRANT, "Two-and-half-hours later, the Lightnings had flown for 494 miles.",
                quote=True),
         Record(WP, "This roundabout approach was plotted and measured to be about 600 miles "
                "(970 km).", quote=True)),
        "About 435 mi", "The report's summary figure, which Pacific Wrecks repeats.",
        shown="08:20"),
    "final-turn": Dispute(
        "The final turn", "MITCHELL",
        (Record(HN, "At 0925, less than 20 miles off Bougainville, they made their final turn "
                "to the northeast", "09:25", quote=True),),
        "09:18, 56 mi out", "At the route's 215 mph a turn at 09:25 lies about 32 mi from the "
        "09:34 interception, not under 20; the replay keeps the stated speed and sighting time.",
        at="09:18", outside=True),
}
