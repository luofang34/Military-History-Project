"""The take-offs from Guadalcanal and Rabaul, and the forces that flew."""
from ledger import Dispute, Moment, Record
from sites import YAMAMOTO

from .names import AMES, COURT, HN, JA, PW_2656, REPORT, SCAN, SUGITA, WP

MOMENTS = {
    "mclanahan-tyre": Moment(
        "McLanahan's burst tyre", "MCLANAHAN", "07:27:20",
        (Record(WP, "Lt James McLanahan blows a tyre on the take-off roll; Holmes takes his place "
                "in Lanphier's attack section.", None),)),
    "moore-turns-back": Moment(
        "Moore turns back", "MOORE", "07:36",
        (Record(WP, "Lt Joseph Moore's drop tanks will not feed and he turns back; Hine fills the "
                "fourth attack slot.", None),)),
}

DISPUTES = {
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
    "ballale-arrival": Dispute(
        "When the Bettys were due at Ballale", YAMAMOTO,
        (Record(WP, "to depart Rabaul at 06:00 and arrive at Balalae at 08:00, Tokyo time.",
                "10:00", quote=True, label="08:00 Tokyo, 10:00 here"),
         Record(PW_2656, "scheduled to land at 9:45am (7:45am Tokyo time)", "09:45",
                quote=True)),
        "Not shown", "The Bettys never arrive; the plan the report gives, to meet them at "
        "09:35, is what the replay flies.", shown="08:52"),
}
