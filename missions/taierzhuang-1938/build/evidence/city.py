"""16–18 March: the suburbs, the walls, Wang Mingzhang's death and the end of resistance."""
from ledger import Dispute, Moment, Record

from .names import (DECREE, JIANG, LOSSES, ORDERS, REPORT, RMZXW_2020, RMZXW_2025,
                    XUECHENG, ZHWIKI, ZHWIKI_WANG)

MOMENTS = {
    "outer-east-gate-breached": Moment(
        "The Japanese break into the east suburb", "10 REGT I", "16 14:15",
        (Record(REPORT, "第三中隊ハ東門ノ破壊口ヨリ突入シ該一角ヲ確保セリ 時正ニ午後二時十五分トス",
                "16 14:15", quote=True,
                label="the 3rd Company through the breach of the outer east gate holds a corner"),
         Record(ORDERS, "歩兵第十聯隊ハ滕縣ノ敵ヲ攻撃中ニシテ午後二時十五分同地外壁東門ニ突入セリ",
                "16 14:15", quote=True, label="瀬支作命第十三號, 18:00 on 16 March"))),
    "outer-south-gate-taken": Moment(
        "The 3rd Battalion enters the south suburb", "10 REGT III", "16 18:40",
        (Record(REPORT, "午後六時四十分遂ニ外城南門ニ突入", "16 18:40", quote=True),)),
    "wang-mingzhang-last-telegram": Moment(
        "Wang Mingzhang's last telegram", "WANG", "17 12:00",
        (Record(ZHWIKI, "目前敌用重炮、飞机从晨至午不断猛轰，城墙缺口多处，敌步兵屡次登城，屡被击退。职意委座成仁"
                "之训，及开封面谕嘉慰之词，决以死拼，以报国家，以报知遇。", "17 12:00", quote=True,
                label="to Sun Zhen, noon on 17 March (the enemy's heavy guns and aircraft have "
                      "pounded us since dawn; the wall is breached in many places; I am "
                      "resolved to fight to the death)"),)),
    "akashiba-wounded": Moment(
        "Colonel Akashiba grazed by a sniper", "10 REGT I", "17 13:00",
        (Record(REPORT, "午後一時過側方百米ノ距離ヨリ敵小銃弾ノ狙撃ヲ受ケ左背部ニ擦過傷ヲ被リ外城東門内旧大隊"
                "本部ノ位置ニ後退ス", "17 13:00", quote=True,
                label="he stayed in command"),)),
    "east-wall-and-north-gate-taken": Moment(
        "The 1st Battalion over the east wall, the north gate taken", "10 REGT I", "17 21:40",
        (Record(REPORT, "午後九時四十分遂ニ城壁ニ突入シ北方ニ戦果ヲ擴張シ續イテ午後十一時迄ニハ北門ヲ占領ス",
                "17 21:40", quote=True),)),
    "mopping-up-complete": Moment(
        "The city cleared", "10 REGT I", "18 14:00",
        (Record(REPORT, "午後二時頃ニ至リ概ネ掃蕩完了", "18 14:00", quote=True),
         Record(REPORT, "此際西門外ニ第百二十二師参謀長少将趙渭賓ノ屍体ヲ發見セリ", quote=True,
                label="18 March (the body of 趙渭賓, the 122nd Division's chief of staff, "
                      "found outside the west gate)"))),
}

DISPUTES = {
    "east-suburb-sixteenth": Dispute(
        "What happened at the east suburb on 16 March", "10 REGT I",
        (Record(ZHWIKI, "3月16日10时半，日军炮火猛烈轰击东关，东关城墙被炸开了一二十米的缺口", "16 10:30",
                quote=True),
         Record(ZHWIKI, "下午5时，日军发动第六次攻势，突入城内40余人", "16 17:00", quote=True),
         Record(ZHWIKI, "下午6时后，严营长组织2个连发起反击，把突入的日军消灭", "16 18:00", quote=True),
         Record(JIANG, "第二回目の集中砲撃により、城（寨）門は完全に破壊され", "16 14:00", quote=True,
                label="from the 10th Regiment's report"),
         Record(REPORT, "敵ノ抵抗頗ル執拗ニシテ著シク進展セス", quote=True,
                label="after the 14:15 lodgement")),
        "The gate breached by 14:00; the 3rd Company holds its corner of the suburb from 14:15, "
        "and the defenders the rest into the night",
        "The Japanese report records the lodgement and no ejection; the Chinese counter-attack "
        "may have recovered ground within the suburb.", at="16 14:15",
        brief="Chinese accounts have the Japanese who broke into the east suburb thrown out at "
              "dusk; the Japanese report has them holding a corner of it all night."),
    "south-wall-taken": Dispute(
        "When the Japanese held the south wall", "10 REGT III",
        (Record(ZHWIKI, "15时日军巩固占领了南城墙", "17 15:00", quote=True),
         Record(REPORT, "午後四時五分第三大隊城壁ニ突入シ西側城壁上ニ向ヒ戦果ヲ擴張ス", "17 16:05",
                quote=True)),
        "16:05", "The report of the battalion that climbed the wall; its assault at 14:30 had "
        "been thrown back.", at="17 16:05"),
    "wang-mingzhang-killed": Dispute(
        "How and when Wang Mingzhang was killed", "WANG",
        (Record(ZHWIKI, "从城墙西北角缒城后奔西关外火车站，在西关电灯厂附近壕沟内被西城门楼上的日军发现遭密集"
                "扫射", quote=True,
                label="let down from the north-west corner, making for the station, machine-"
                      "gunned from the west gate tower in a ditch near the power plant"),
         Record(RMZXW_2025, "王铭章是在3月17日下午5时左右牺牲的", "17 17:00", quote=True),
         Record(RMZXW_2020, "王铭章率部拼死抵抗，不幸身中数弹，壮烈殉国", "17 15:00", quote=True,
                label="at 15:00"),
         Record(ZHWIKI_WANG, "在城中心十字街口指揮作戰時，不幸中彈殉職", quote=True,
                label="shot at the central crossroads"),
         Record(DECREE, "以率部奮力巷戰，竟爾殉職", quote=True,
                label="the posthumous decree of 6 April 1938"),
         Record(JIANG, "日が暮れる前、王は「西門外の濠の近くで、城壁上からの射撃」を受け死亡した", quote=True,
                label="his adjutant 李少坤's memoir, as Jiang gives it"),
         Record(REPORT, "其後軍情報ニ依レハ左記ノ如ク師長王銘章モ戦死セルコト敵ノ發表ニテ明白ナルニ至レリ",
                quote=True, label="the Japanese learned of his death only from Chinese "
                                  "announcements")),
        "About 17:30, in the moat outside the west gate, shot from the gate tower with his staff",
        "Most accounts put it in the west suburb after the west gate fell, at about 17:00 on "
        "both sides' records, and before dark; the Japanese found his chief of staff's body "
        "outside the west gate. Jiang's estimate of 17:30.", at="17 17:30", outside=True,
        brief="Accounts of Wang Mingzhang's death differ in time and place; most put it at dusk "
              "in the moat outside the west gate, under fire from the gate tower."),
    "zou-shaomeng-killed": Dispute(
        "The death of Zou Shaomeng, the 124th Division's chief of staff", "124 DIV",
        (Record(REPORT, "百二十四師参謀長鄒紹孟", quote=True,
                label="a mounted officer with some fifty guards, shot leaving by the north gate "
                      "on the evening of the 17th and identified from his papers"),
         Record(ZHWIKI, "killed near the north gate on 17 March", quote=False,
                label="the Chinese accounts")),
        "Shot outside the north gate at about 18:30 on the 17th",
        "Both sides put it at the north gate; the report places it after the 3rd Battalion "
        "reached the north-west corner at 18:30 and gives no time of its own.", at="17 18:30",
        outside=True),
    "wang-lin-fate": Dispute(
        "What became of Wang Lin, the 740th Regiment's commander", "740 REGT",
        (Record(ZHWIKI, "日军突入东关，守备东关的第124师第370旅第740团团长王麟、团政训员胡清溪阵亡",
                quote=True),
         Record(REPORT, "團長代理王麟、第百二十四師参謀張重以下十数名", quote=True,
                label="among the prisoners of 18 March")),
        "Not resolved", "The Japanese name may be another man or a misidentification; the "
        "replay shows the regiment destroyed and no fate for him.", shown="17 09:00"),
    "losses": Dispute(
        "The losses at Tengxian", "TENGXIAN",
        (Record(LOSSES, "16 killed (1 officer), 129 wounded, 3 missing of 2,654 engaged",
                quote=False,
                label="the 10th Regiment's casualty table, 15–18 March"),
         Record(REPORT, "遺棄死体ノミニシテモ其数三千百ヲ算スル", quote=True,
                label="Chinese dead left on the field"),
         Record(ZHWIKI, "我阵亡官兵3000余人，负伤官兵4000余人", quote=True,
                label="Sun Zhen's report"),
         Record(ZHWIKI, "毙伤敌军官佐320余员，击毙士兵1500余名，击伤士兵5700余名", quote=True,
                label="Sun Zhen's claim of Japanese losses")),
        "Each side's own count is given; no single figure", "Each side's figures for the "
        "other's losses are many times the other's own count.", shown="18 14:00"),
    "lincheng-fall": Dispute(
        "When Lincheng fell", "63 REGT",
        (Record(ZHWIKI, "3月17日夕攻占第22集团军总司令部与第41军军部驻地临城", "17 18:00", quote=True),
         Record(ZHWIKI, "3月17日晨，临城失守", "17 06:00", quote=True),
         Record(XUECHENG, "1938年5月19日，该站沦入日军手中", quote=True,
                label="of the station")),
        "The evening of 17 March", "The 63rd Regiment's pursuit reached 官橋 at dawn; the "
        "May date is the station's, or a confusion.", at="17 17:00"),
}
