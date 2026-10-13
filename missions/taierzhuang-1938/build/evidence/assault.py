"""The first battle for the town, 24–29 March: the assaults, the guns that came up behind them and
the Chinese guns that answered."""
from ledger import Dispute, Moment, Record

from .names import HUANGPU, J63, JIANG_17, KRZ_SFH, KRZ_TZZ, SAS, SOSHO

MOMENTS = {
    "first-assault-on-taierzhuang": Moment(
        "The II Battalion's first assault, at the north gate", "63 REGT II", "24 16:15",
        (Record(J63, "午後四時十五分城門ヲ破壞シ突撃開始", "24 16:15", quote=True,
                label="the battalion's telegram, received 16:30"),
         Record(J63, "部隊ノ一部突入シタルモ成功セス 目下内外ノ連絡絶エ死傷續出ス敵ハ益々増加シ我ヲ完全ニ包圍セリ"
                "彈藥到着セス 大隊ハ北門外ニ在リ", quote=True, label="received 21:00"))),
    "armoured-train-from-the-station": Moment(
        "A Chinese armoured train fires from the railway", "TRAIN", "25 08:00",
        (Record(J63, "臺兒庄停車場ヨリ敵裝甲列車近ク前進シ來リ中隊ノ集結地ニ對シ機關銃及列車砲ヲ以テ射撃シ",
                "25 08:00", quote=True, label="the 5th Company, about 08:00"),)),
    "guns-south-of-the-canal": Moment(
        "The Japanese first report Chinese guns south of the canal", "XIONGSHAN GUNS",
        "25 16:00",
        (Record(J63, "午後四時第二大隊主力ト連絡ヲ確保ス 敵ハ運河南側高地脚ニ十數門ノ砲ヲ有シ盛ニ我ヲ砲撃シ"
                "アリテ晝間ノ行動甚シク困難ナリ", "25 16:00", quote=True,
                label="the 10th Company's commander, received 16:35"),)),
    "type-96-arrives": Moment(
        "The Type 96 15 cm howitzers arrive and open fire", "TYPE 96", "25 17:00",
        (Record(J63, "支那駐屯砲兵聯隊混成第六中隊(九六式重砲一小隊)…午後五時頃劉家湖ニ到着シ", "25 17:00",
                quote=True),
         Record(J63, "劉家湖北側ニ到着陣地ヲ占領シ午後五時三十分三里庄附近ノ陣地ニ據ル敵ヲ制壓シテ之ヲ動搖セシメ",
                quote=True, label="its first fire at Taierzhuang, 17:30"))),
    "north-east-corner-entered": Moment(
        "The II Battalion breaks into the north-east corner", "63 REGT II", "27 07:50",
        (Record(J63, "午前七時五十分突入一角ヲ占領掃蕩中", "27 07:50", quote=True,
                label="the battalion's telegram, received 08:30"),)),
    "first-artillery-duel": Moment(
        "The first artillery duel the Japanese describe", "HEAVY 3", "28 06:40",
        (Record(J63, "午前六時四十分頃三里庄東北部落ノ野戰重砲兵第三中隊臺兒庄西北角附近ニ向ヒ試射ヲ始ムルヤ敵砲兵"
                "之ニ對シ射擊ヲ開始シ其射彈右砲兵陣地ノ後方約百米附近ニ落達シ", "28 06:40", quote=True),
         Record(J63, "運河南岸地區寨山(臺兒庄西南約七、五粁)韓山(臺兒庄南々西約五・五粁)及雄山ノ北側附近ニ位置"
                "シアルモノヽ如シ", quote=True, label="where the Chinese guns seemed to be"))),
    "vehicles-burned": Moment(
        "Chinese shells burn the Type 96 company's vehicles", "TYPE 96", "29 11:10",
        (Record(SAS, "後方ニ集結中ナリシ車輛ハ敵砲彈ノ集中火ヲ受ケガソリンニ命中火災ヲ起シ燒失ス", "29 11:10",
                quote=True, label="the company's report, under 11:10"),
         Record(J63, "敵砲火支那駐屯重砲中隊ノ車輛ニ命中シ輕油發火シ車輛ヲ多數失ヒ下士官以下十三名ノ戰死傷者ヲ"
                "生シ", quote=True))),
}

DISPUTES = {
    "north-west-corner-time": Dispute(
        "When the Japanese took the town's north-west corner", "11 COY",
        (Record(SOSHO, "二十八日〇七三〇ころ、台児庄の北西角の一部も占領", "28 07:30", quote=True),
         Record(J63, "支那駐屯重砲中隊午前七時五十分頃破壞射擊ヲ實施シテ概ネ之ヲ破壞シ", "28 07:50",
                quote=True, label="the first breaching shoot"),
         Record(J63, "豫定時刻ニ先ツコト五分午後七時二十五分一擧ニ城内ニ突入シ突擊成功ノ信號白吊星ヲ揚ク",
                "28 19:25", quote=True, label="the 11th Company's assault")),
        "19:25", "The regiment's own report breaches the corner at 07:50 and again at 15:30 and "
        "storms it at 19:25; the official history's 07:30 is nearest the first breaching shoot.",
        at="28 19:25"),
    "wenchang-pavilion": Dispute(
        "Who held the north-west corner on the night of 28 March", "11 COY",
        (Record(HUANGPU, "3月27日晚，日军100余人窜入城西北角，占领文昌阁…11时，突击队攻克文昌阁", "27 18:00",
                "27 23:00", quote=True),
         Record(KRZ_TZZ, "3月28日，晚8时，日军百余窜入台儿庄西北角…晚11时，攻克文昌阁", "28 20:00",
                "28 23:00", quote=True),
         Record(J63, "豫定時刻ニ先ツコト五分午後七時二十五分一擧ニ城内ニ突入シ", "28 19:25", quote=True)),
        "The Japanese foothold kept from 19:25 on the 28th until the 31st",
        "The 11th Company stays at the corner in the Japanese reports until it is withdrawn at "
        "20:00 on 31 March; the Chinese special company's retaking of the Wenchang pavilion, "
        "the corner's highest point, is told but not shown.", at="28 19:25",
        brief="Chinese accounts say a special company of 72 men retook the Wenchang pavilion "
              "that night; the Japanese report keeps a foothold in the corner until 31 March."),
    "type-96-opening-27-march": Dispute(
        "When the guns opened on 27 March", "TYPE 96",
        (Record(J63, "火砲ノ射撃開始午前六時", "27 06:00", quote=True, label="the assault plan's sketch"),
         Record(SAS, "午前五時五十分中隊長ハ…觀測所ニ到リ先ツ側防機關銃ヲ制壓シ引續キ城內右半分ニ對シ擾亂射擊",
                "27 05:50", quote=True),
         Record(JIANG_17, "05：50砲撃が始まり", "27 05:50", quote=True)),
        "06:00", "The hour the assault plan set for all the guns; the Type 96 company's commander "
        "began on the flanking machine guns ten minutes before.", at="27 06:00"),
    "duel-on-27-march": Dispute(
        "Whether the guns duelled on 27 March", "STATION GUNS",
        (Record(KRZ_SFH, "27日刚刚到阵地，双方猛烈炮战，激战2个多小时", quote=True,
                label="the Chinese 7th and 10th Artillery; no clock time"),
         Record(J63, "午後五時三十分頃以來臺兒庄西方地區方向ヨリ野山砲級榴彈劉家湖部落内外至ル所ニ落下シ",
                "27 17:30", quote=True),
         Record(J63, "午後七時十五分再ヒ臺兒庄停車場方向及停車場西側附近ヨリ野山砲級榴彈約二十發劉家湖ニ落下ス",
                "27 19:15", quote=True)),
        "Chinese field-gun fire on Liujiahu at 17:30 and 19:15; no duel",
        "The Japanese report on 27 March records Chinese shells on Liujiahu but no counter-battery "
        "fire, which is first ordered for the 28th; the Chinese account gives no hour.",
        shown="27 17:30",
        brief="Chinese accounts tell of a two-hour artillery duel on 27 March; the Japanese "
              "report records only Chinese shells on Liujiahu that evening."),
    "chinese-gun-count": Dispute(
        "How many guns the Chinese had round the town", "XIONGSHAN GUNS",
        (Record(J63, "敵ハ運河南側高地脚ニ十數門ノ砲ヲ有シ", "25 16:00", quote=True),
         Record(J63, "敵ハ野砲五－六門列車砲及迫擊砲ヲ有スル", "27 13:45", quote=True),
         Record(J63, "敵砲兵數少クモ二十四－五門ヲ算シ", "28 09:00", quote=True),
         Record(J63, "運河ノ線ニハ二營ノ督戰隊及砲四十門アリト", "29 21:30", quote=True,
                label="from prisoners")),
        "Four batteries south of the canal and the station, from 25 March",
        "The places the Japanese gave for the guns they saw or heard: Zhaishan, Hanshan, "
        "Xiongshan and the south bank by the station; their count grew as more were found.",
        shown="28 08:00"),
}
