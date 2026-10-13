"""The sources the operation cites, as operation.json declares them."""
from clock import CST_S, DURATION

CLOCK = {"kind": "fixed", "seconds": CST_S,
         "source": "China's coastal standard time, UTC+8; the Japanese reports are read on it "
                   "(build/evidence/, japanese-clock)"}
RECONSTRUCTED = {"motion": "great_circle", "max_gap_ms": DURATION, "zone": CLOCK}
SOURCES = [
    {"id": "reconstruction-chinese", "name": "Chinese units' moves, reconstructed",
     **RECONSTRUCTED},
    {"id": "reconstruction-japanese", "name": "Japanese units' moves, reconstructed",
     **RECONSTRUCTED},
    {"id": "reconstruction-guns", "name": "Batteries' range fans, reconstructed",
     "zone": CLOCK},
    {"id": "reconstruction-railway",
     "name": "The Tianjin–Pukou railway and the Taierzhuang branch of 1938",
     "zone": CLOCK},
    {"id": "reconstruction-estimate",
     "name": "Replay estimates where sources disagree (build/evidence/)", "zone": CLOCK},
    {"id": "jacar-10i-report-11", "name": "歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200)",
     "zone": CLOCK},
    {"id": "jacar-seya-orders", "name": "瀬谷支隊命令, 別紙 (JACAR C11111170300)", "zone": CLOCK},
    {"id": "jacar-10i-casualties", "name": "歩兵第十聯隊死傷表, 3月15日–18日 (JACAR C11111170700)"},
    {"id": "jiang-2015", "name": "姜克實「日本軍の史料から見る滕県作戦の実記録」, 文化共生学研究 14 (2015)"},
    {"id": "jiang-withdrawal", "name": "姜克實「坂本、瀬谷支隊の台児庄撤退の経緯 ─1938年4月」, "
     "岡山大学文学部紀要 64"},
    {"id": "senshi-sosho-89", "name": "戦史叢書 89 『支那事変陸軍作戦〈2〉』 (1976)"},
    {"id": "krzzjn-jiehe", "name": "「滕县作战之界河附近的战斗 3月14-15日」, 抗日战争纪念网 (2018)"},
    {"id": "krzzjn-sfh18", "name": "萨沙「国军的雷神之锤——抗战中的sFH18 150毫米榴弹炮」, 抗日战争纪念网 "
     "(2018)"},
    {"id": "zhwiki-tengxian", "name": "滕县保卫战 (zh.wikipedia)"},
    {"id": "zhwiki-wang-mingzhang", "name": "王銘章 (zh.wikipedia)"},
    {"id": "zhwiki-sfh18", "name": "SFH 18榴彈砲 (zh.wikipedia)"},
    {"id": "tengxian-gazetteer", "name": "《滕县志》 (中华书局, 1990)"},
    {"id": "xuecheng-gazetteer", "name": "《薛城区志》"},
    {"id": "rmzxw-2020", "name": "郑学富, 人民政协网 (2020)"},
    {"id": "rmzxw-2025", "name": "蔡永飞「滕县保卫战中的张宣武」, 人民政协网 (2025)"},
    {"id": "qq-yang-jintao", "name": "杨津涛「中、日战报为何差距四十倍？」, 腾讯 (2019)"},
    {"id": "nationalist-decree-1938", "name": "國民政府 褒揚令, 6 April 1938"},
    {"id": "reconstruction-fire", "name": "Fire missions, from the Japanese reports' times",
     **RECONSTRUCTED},
    {"id": "jacar-63i-taierzhuang",
     "name": "歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100)",
     "zone": CLOCK},
    {"id": "jacar-10i-report-13",
     "name": "歩兵第十聯隊 臺兒庄附近戦闘詳報 第十三號 (JACAR C11111171800–C11111172200)",
     "zone": CLOCK},
    {"id": "jacar-sas-report",
     "name": "臨SAS戦詳第一號 臺兒庄附近ノ戰鬪詳報, 第二軍臨時野戰重砲兵中隊 "
             "(JACAR C11111730100–C11111731000)", "zone": CLOCK},
    {"id": "jacar-ohashi",
     "name": "大橋武夫「支那事変初期 北支における十五榴部隊を中心とする砲兵戦史資料」 "
             "(JACAR C11111729600, C11111729700)", "zone": CLOCK},
    {"id": "jiang-2017", "name": "姜克實「台児庄作戦の概観」, 岡山大学大学院社会文化科学研究科紀要 43 "
     "(2017)"},
    {"id": "enwiki-taierzhuang", "name": "Battle of Taierzhuang (en.wikipedia)"},
    {"id": "jawiki-taierzhuang", "name": "台児荘の戦い (ja.wikipedia)"},
    {"id": "zhwiki-taierzhuang-site", "name": "台儿庄大战旧址 (zh.wikipedia)"},
    {"id": "zhwiki-taierzhuang", "name": "台兒莊戰役 (zh.wikipedia)"},
    {"id": "nx-31div", "name": "《第三十一师台儿庄战役战斗详报》, as quoted in 「台儿庄战役中的中共地下党员」, "
     "宁夏回族自治区交通运输厅 (2017)", "zone": CLOCK},
    {"id": "zaozhuang-party-history", "name": "《中共枣庄地方史》 第一卷"},
    {"id": "krzzjn-three-days", "name": "「1938年台儿庄抗战生死三日全纪实」, 抗日战争纪念网",
     "zone": CLOCK},
    {"id": "huangpu-2018", "name": "《黄埔》 2018年第3期", "zone": CLOCK},
    {"id": "thepaper-squads", "name": "「台儿庄战役期间究竟派出了多少支敢死队？」, 澎湃 (2018), from "
     "the Chinese units' battle reports", "zone": CLOCK},
    {"id": "osm", "name": "OpenStreetMap"},
]
