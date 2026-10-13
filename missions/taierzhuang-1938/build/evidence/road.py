"""The road south, 18–23 March: the pursuit from Lincheng to Hanzhuang and Yixian, and the
Chinese 31st Division into Taierzhuang."""
from ledger import Dispute, Moment, Record

from .names import HUANGPU, J63, NX_31DIV, ZAOZHUANG_HISTORY, ZHWIKI_TZZ

MOMENTS = {
    "hanzhuang-taken": Moment(
        "The right pursuit force takes Hanzhuang north of the canal", "63 REGT I", "19 13:00",
        (Record(J63, "右追撃隊ハ十九日正午頃ヨリ韓莊附近ノ敵ヲ攻撃シ午後一時北部韓莊ヲ占領ス同方面ノ敵ハ増援中"
                "ニシテ運河附近ニ約一萬ノ敵アリ", "19 13:00", quote=True),)),
    "first-contact-at-kangzhuang": Moment(
        "The Japanese meet the 31st Division's cavalry at Kangzhuang", "63 REGT II", "23 09:00",
        (Record(NX_31DIV, "9时顷，敌步骑兵约300余，战车一辆，由峄县向东南行进，与师骑兵于康庄遭遇接触，我骑兵"
                "稍退", "23 09:00", quote=True),)),
}

DISPUTES = {
    "yixian-fell": Dispute(
        "When Yixian fell", "63 REGT II",
        (Record(ZHWIKI_TZZ, "3月18日…第4師在嶧縣附近與日軍機械化部隊激戰，嶧縣當日晚間失陷", "18 18:00",
                "18 23:59", quote=True),
         Record(J63, "日没後人梯ヲ作リ城門上部ノ破壊孔ヨリ突入城門ヲ開キテ城内ニ進入掃蕩シ…二十日午前零時三十分"
                "掃蕩ヲ完了シ縣城ヲ確保ス", "20 00:30", quote=True, label="the left pursuit force")),
        "00:30 on 20 March", "The left pursuit force's own account: it attacked on the 19th, "
        "climbed in over the south gate after dark and finished clearing the town at 00:30.",
        at="20 00:30",
        brief="Chinese accounts have Yixian fall on the evening of 18 March; the Japanese "
              "report has it taken after dark on the 19th."),
    "zaozhuang-fell": Dispute(
        "When the Japanese took Zaozhuang", "SEYA",
        (Record(ZAOZHUANG_HISTORY, "1938年3月18日，枣庄失陷", quote=True),
         Record(J63, "同追撃隊ハ嶧縣占領後第八中隊（機關銃一小隊ヲ屬ス）ヲ棗莊占領ノ為派遣ス", quote=True,
                label="after 00:30 on 20 March")),
        "20 March, by a company of the left pursuit force; not shown",
        "The Japanese report sends the company after Yixian fell; parties along the "
        "Lincheng–Zaozhuang branch may have been there from the 18th.", shown="20 06:00"),
    "31st-division-arrival": Dispute(
        "When the Chinese 31st Division took over Taierzhuang", "31 DIV",
        (Record(ZHWIKI_TZZ, "3月22日，第二集團軍第31師到達台兒莊暫歸第二十集團軍指揮", "22 00:00", "22 23:59",
                quote=True),
         Record(HUANGPU, "3月22日，王冠五奉命率部进入台儿庄布防，担任守城总指挥", "22 00:00", "22 23:59",
                quote=True)),
        "08:00 on 22 March", "The day both give; the hour is the replay's.", at="22 08:00"),
}
