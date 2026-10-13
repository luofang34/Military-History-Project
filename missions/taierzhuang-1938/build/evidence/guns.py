"""The guns: the Japanese batteries round Tengxian, the Chinese armoured train, and the Chinese
15 cm howitzers that were not there."""
from ledger import Dispute, Moment, Record

from .names import JIANG, JIANG_WD, KRZ_JIEHE, KRZ_SFH, ORDERS, REPORT, SOSHO, ZHWIKI, ZHWIKI_SFH

MOMENTS = {
    "armoured-train-duel": Moment(
        "The Japanese field guns duel with a Chinese armoured train", "ARMOURED TRAIN", "16 11:00",
        (Record(REPORT, "該列車ハ砲ヲ有シ我ニ向ヒ射撃ヲ行フ", "16 11:00", quote=True,
                label="the train has guns and fires on us; it withdraws south after about ten "
                      "minutes"),
         Record(JIANG, "11:00、75mm列車砲を装備した南進装甲列車の編隊も発見し、砲撃を交わした", "16 11:00",
                quote=True))),
    "pagoda-observer": Moment(
        "A Japanese artillery observer takes the pagoda", "PAGODA", "17 10:00",
        (Record(JIANG, "10:00 observer 家形中尉 takes the 龍泉塔 (30 m) and corrects fire",
                "17 10:00", quote=False, label="from the 10th Regiment's report"),
         Record(REPORT, "金塔ニ據ル敵ヲ刺殺", quote=True,
                label="the observer bayonets the Chinese holding the pagoda"))),
}

DISPUTES = {
    "heavy-battalion-guns": Dispute(
        "What the heavy battalion fired", "HEAVY ARTY",
        (Record(KRZ_JIEHE, "野战重炮兵第二联队一大队(4年式15榴12门)", quote=True),
         Record(JIANG, "野戦重砲兵第二聯隊の第Ⅰ大隊（91式105mm榴弾砲12門）も到着し、東関の寨門に向け試射開始",
                "16 11:15", quote=True, label="Jiang's narrative of 16 March"),
         Record(JIANG, "4年式15糎榴弾砲 1 battalion × 12", quote=False,
                label="Jiang's own table of the guns"),
         Record(ZHWIKI, "野战重炮兵第2联队第1大队（150毫米榴弹炮12门）", quote=True)),
        "Twelve Type 4 15 cm howitzers, range 8.8 km",
        "Three of the four records, Jiang's own table among them, give 15 cm; the range is "
        "the Type 4's with its charge increased, as Jiang gives it.", shown="16 11:15",
        brief="Whether the heavy battalion's twelve guns were 15 cm or 10.5 cm howitzers is "
              "disputed; the replay draws the 15 cm Type 4's 8.8 km range."),
    "field-guns-range": Dispute(
        "Which Type 38 field gun the field battalion had, and its reach", "FIELD ARTY",
        (Record(JIANG_WD, "野砲兵第十聯隊第一大隊の改造38式野砲（7.5糎）8門", quote=True,
                label="at Taierzhuang ten days later"),
         Record(JIANG, "38式野砲：…有効射撃距離約8,000ｍ", quote=True,
                label="at Tengxian")),
        "The improved Type 38, drawn to its maximum range of 11,600 m",
        "The same battalion is recorded with the improved gun at Taierzhuang; the range fan "
        "shows the furthest a shell could reach, not the effective range.", shown="16 10:20"),
    "breaching-fire": Dispute(
        "When the guns began to breach the inner wall", "GARRISON ARTY",
        (Record(REPORT, "午前八時三十分駐屯軍重砲ハ東門南方四十米ノ城壁ニ對シ野重ハ東南角西方二十米ノ城壁ニ對シ"
                "破壊射撃ヲ開始ス", "17 08:30", quote=True),
         Record(JIANG, "07:30 ranging; about 1 hour of harassing fire; 09:00 wall-breaching fire "
                "begins", "17 09:00", quote=False),
         Record(REPORT, "東門附近ノ如キハ僅カ五十發ニシテ殆ト完成ス", quote=True,
                label="the east-gate breach nearly made in fifty rounds")),
        "08:30", "The report's narrative of the day; its plan had set breaching for 08:00.",
        at="17 08:30"),
    "armoured-train-captured": Dispute(
        "Where the armoured train was taken", "ARMOURED TRAIN",
        (Record(ORDERS, "飛行機ヨリノ通報ニ依レハ歩六三ハ午後十二時三十分王家樓ニ達シ敵装甲列車一、機関車一輛ヲ"
                "鹵獲シアリ", "16 12:30", quote=True,
                label="瀬支作命第十三號, from an aircraft's report"),
         Record(JIANG, "この列車はのち、南沙河で城外作戦を担当する第六十三聯隊によって拿捕", quote=True)),
        "Near 南沙河, at about 12:30", "王家樓 is not located; 南沙河 is the station south of "
        "the city on the 63rd's line of advance.", at="16 12:30"),
    "chinese-heavy-guns": Dispute(
        "Whether any Chinese 15 cm howitzer fired at Tengxian", None,
        (Record(ZHWIKI_SFH, "拥有7门炮的一营最先被配给汤恩伯第20军团，1938年3月中旬驰援第五战区。", quote=True,
                label="the 10th Artillery's battalion of sFH 18/32L, the 32-calibre export "
                      "model"),
         Record(KRZ_SFH, "27日刚刚到阵地，双方猛烈炮战，激战2个多小时", quote=True,
                label="at Taierzhuang, 27 March"),
         Record(SOSHO, "有力な敵砲兵（二四～二五門）", quote=True,
                label="the first Japanese note of strong Chinese artillery, at Taierzhuang on "
                      "28 March"),
         Record(JIANG, "敵側も迫撃砲3門しかなかった", quote=True,
                label="the 10th Regiment's captures at Tengxian: three mortars")),
        "None: the defenders had mortars, the armoured train and, south of the city, a few "
        "mountain guns", "No record puts the 15 cm battalion with the division Tang Enbo sent "
        "toward Tengxian; its first recorded fire is at Taierzhuang.", shown="16 12:25",
        brief="No Chinese 15 cm howitzer fired at Tengxian: the 10th Artillery's sFH 18/32L "
              "came with Tang Enbo's corps and first fired at Taierzhuang, on 27 or 28 March."),
}
