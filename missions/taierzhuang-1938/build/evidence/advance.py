"""14–15 March: the Seya Detachment breaks the line north of Tengxian and swings round the east;
and the clock its records keep."""
from ledger import Dispute, Moment, Record

from .names import GAZETTEER, KRZ_JIEHE, ORDERS, REPORT, ZHWIKI

MOMENTS = {
    "seya-order-nine": Moment(
        "Seya orders the swing round the east of Tengxian", "SEYA", "15 10:30",
        (Record(ORDERS, "支隊ハ界河、東郭、王廟方面ヨリ王廟附近ニ向ヒ前進シ滕県敵陣地ニ対スル攻撃ヲ準備セン"
                "トス", "15 10:30", quote=True,
                label="瀬支作命第九号, \"三月十五日午前十時三十分於界河\" (the detachment advances "
                      "by 界河, 東郭 and 王廟 to prepare the attack on Tengxian)"),
         Record(REPORT, "主力（歩兵五中隊）ヲ以テ歩六三ノ後方ニ續行シ敵ノ備ヘ薄キ東方地區ヨリ滕縣附近ノ敵ヲ"
                "攻撃スルコトヽナル", quote=True,
                label="the 10th Regiment, on receiving it (its main body of five companies "
                      "follows the 63rd and attacks from the weakly held east)"))),
    "yan-yi-enters-the-city": Moment(
        "Yan Yi's battalion reaches the city", "YAN BN", "15 17:00",
        (Record(ZHWIKI, "3月15日17时", "15 17:00", quote=True,
                label="of the 731st Regiment only Yan Yi's 1st Battalion reached the city"),)),
}

DISPUTES = {
    "japanese-clock": Dispute(
        "Which clock the Japanese regiment's report keeps", None,
        (Record(REPORT, "日出 午前六時二十分 日没 午後五時五十分", quote=True,
                label="the report's table for 16 March (sunrise 06:20, sunset 17:50); at "
                      "Tengxian the sun rose at about 06:23 UTC+8, 07:23 Tokyo time"),
         Record(KRZ_JIEHE, "1840趁薄暮一气突入", quote=True,
                label="the 3rd Battalion's dusk assault, 16 March; sunset at 18:19 UTC+8")),
        "Local time, UTC+8", "Japanese army records are usually read as Tokyo time. The report's "
        "sunrise falls within two minutes of the sun's at UTC+8 "
        "and an hour from Tokyo time's, and its 18:40 dusk only fits local time; the times the "
        "two sides both record (the east gate at about 14:00, the west gate at 17:00) agree on "
        "it.", shown="16 08:00",
        brief="Japanese records are usually in Tokyo time, but this regiment's sunrise and dusk "
              "fit local time; the replay reads its times as local."),
    "jiehe-line-broken": Dispute(
        "When the line at 界河 broke", "379 BDE",
        (Record(KRZ_JIEHE, "1810进入界河", "14 18:10", quote=True,
                label="the 63rd Regiment, 14 March"),
         Record(ZHWIKI, "13时，界河正面阵地被日军突破", "15 13:00", quote=True,
                label="15 March")),
        "The village entered on the 14th; the line round it given up at 13:00 on the 15th",
        "The 63rd's record is of the village; the Chinese one of the whole line from 界河 to "
        "龍山, which Seya's order of 10:30 on the 15th, issued at 界河, shows was still held "
        "east of it.", at="15 13:00"),
    "eastern-swing": Dispute(
        "Which way the Japanese swung round the city", "63 REGT",
        (Record(ORDERS, "前衛ハ正午龍山店附近出発 龍山店―東郭 王廟道ニ沿フ地区ヲ王廟ニ向ヒ前進スヘシ",
                quote=True, label="瀬支作命第九号 (the advance guard leaves 龍山店 at noon along "
                                  "the 龍山店–東郭–王廟 road)"),
         Record(GAZETTEER, "以万余兵力由龙山东侧向滕县城迂回…下午5时许，其先头部队已达滕县城东北的龙阳店、"
                "冯河一带", quote=True,
                label="《滕县志》 (over ten thousand round the east of 龍山; by 17:00 the van "
                      "was at 龍陽店 and 馮河, north-east of the city)")),
        "By 東郭 and 王廟, east and south-east of the city",
        "The Japanese orders and the 10th Regiment's report give the route; 龍陽店 appears in "
        "no Japanese record and may have been a flank screen.", shown="15 14:00",
        brief="The Japanese records route the swing far to the east, by Dongguo and Wangmiao; "
              "Chinese accounts have its van at Longyangdian, north-east of the city."),
}
