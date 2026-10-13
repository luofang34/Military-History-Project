# Battle of Taierzhuang, 14 March – 1 April 1938

The Battle of Taierzhuang, from the fall of Tengxian to the artillery battle at the Grand Canal.
The Japanese Seya Detachment breaks the line north of Tengxian, swings round the east and takes
the walled city from the Sichuan troops of the 22nd Group Army, whose 122nd Division commander,
Wang Mingzhang, is killed at the west gate. It goes on down the railway to Lincheng and along the
branch line by Zaozhuang and Yixian to Taierzhuang, where its 63rd Infantry fights its way into
the walled town on the canal's north bank. From the hills south of the canal Chinese guns answer
the Japanese batteries, and from 31 March the Chinese 10th Artillery Regiment's two German 15 cm
sFH 18/32L howitzers, which outrange every Japanese gun there, fire on them from beyond their
reach. The Chinese side is the friendly force. The replay ends on the evening of 1 April.

This folder is the package (`operation.json`, `events.jsonl`, `presentations/default.json`) and
its generator, `build/`. Regenerate with `python3 build/taierzhuang.py`, then run
`python3 ../../verify.py`. The story's parts are packages of the generator: `build/tengxian/`
for the defence of Tengxian, `build/siege/` for the road south and the battle at the canal.

## Method

- **Clock.** UTC+8, China's coastal standard time. Chinese records are read on it as written.
  The Japanese reports are read on it too, not on Tokyo time: the 10th Infantry's report at
  Taierzhuang says so (「時刻ハ西部標準時トス」), its sunrise for 16 March (06:20) is the sun's at
  UTC+8, its dusk assault at 18:40 only fits local time, and the 63rd Infantry's daily sunrise
  and sunset fit it to within three minutes (the japanese-clock dispute). Operation zero is
  04:00 on 14 March, when the 10th set out from Tangcun.
- **At Tengxian** the main record is the 10th Infantry Regiment's 「滕縣附近戦闘詳報 第十一號」 (JACAR
  C11111170200), read page by page from the archive's images, with its sketch maps and the
  Seya Detachment's orders (C11111170300, C11111170400). Chinese accounts come from the county
  gazetteer, the 22nd Group Army's and the brigades' reports as Chinese Wikipedia, 人民政协网
  and 杨津涛 quote them, and the memoirs gathered in 《悲壮之役》 (1992). Where the two sides
  disagree on a time or a place, each version is in the ledger below.
- **At Taierzhuang** the main records are Japanese too, read the same way: the 63rd Infantry's
  battle report for Taierzhuang, the 10th Infantry's report No. 13 and the battle report of the
  China Garrison's Type 96 15 cm company (臨SAS戦詳第一號), with their sketch maps; the postwar
  manuscript of 大橋武夫, a China Garrison artillery officer, gives the Japanese gunners' verdict
  on the duel. No battle report of the Chinese 7th or 10th Artillery was found; the Chinese side
  comes from 萨沙's account of the sFH 18 in China, Jiang 2017 and Wikipedia.
- **The city of 1938, not today's.** Tengxian's walls and moat were pulled down from 1952 to
  1984 and new streets laid on their line (the gazetteer's 城市街道 chapter): 新兴路 on the west
  wall, 荆河中路 on the south, 善国中路 on the east. The corners, the four gates and the two
  breaches of 17 March (40 m south of the east gate, 20 m west of the south-east corner) are
  placed on those streets, within about 50 m. The east suburb's earth wall stood about 150 m
  west of the Longquan pagoda (龍泉塔), which the Japanese report puts 150 m from its north-east
  corner. The 1938 station stood west of the walls, outside the west suburb, within today's
  滕州站 platforms; the west suburb's power plant (電燈廠), where the 122nd Division had its
  headquarters, is placed between the west gate and the station, within about 150 m.
- **The railway.** The Tianjin–Pukou line between Yanzhou and Lincheng runs on its 1912
  alignment (station sites and the 1912 kilometre posts in the county gazetteers agree with
  today's line), so it is drawn on today's 京沪线; Lincheng's station of 1938 stood 500 m north
  of today's 枣庄西.
- **The moves.** The Japanese columns follow the times and places of the 10th and 63rd
  Infantry's reports (through 抗日战争纪念网's series and Jiang 2015) and Seya's orders: the
  10th from Tangcun by Shiqiang and Chitouji to Jiehe; Seya's swing round the east by Dongguo
  and Wangmiao; the 10th's 1st Battalion from the east at the east suburb, its 3rd Battalion
  round by Wangzhuang and the railway to the south suburb. The Chinese units hold the positions
  the gazetteer and the reports give them. Away from the walls the moves are reconstructed
  within 2 km; at the walls within 100 m.
- **The guns.** Each Japanese battery's reach is a MIL-STD-2525D sector range fan, drawn while
  the battery stands in position and facing the city: the field guns at Xiacun and then
  Shanjiazhuang (improved Type 38, 11,600 m), the heavy battalion's Type 4 15 cm howitzers
  (8,800 m), the China Garrison's Type 96 15 cm howitzers on the 17th (11,900 m). Positions are
  those Jiang gives from the report; Xiacun is not on today's map and is placed 2 km south-east
  of the walls, within 700 m. The defenders had no gun larger than a mortar in the city; the
  Chinese 10th Artillery's German 15 cm sFH 18/32L reached the front with Tang Enbo's corps and
  first fired at Taierzhuang.
- **The road south.** From Lincheng the detachment followed the branch railway by Zaozhuang,
  Yixian and Nigou to Taierzhuang (台棗支線), taken up in 1945; it is drawn through its stations
  as the county gazetteers place them, within about a kilometre, and round the town on the
  63rd's sketch maps' line, within about 300 m. The town of 1938 stood on the canal's north
  bank; the reach through it was straightened in 1959 and the old channel is today's 月河,
  drawn by the basemap. Taierzhuang station's site is the Li Zongren museum, rebuilt there in
  1995. Villages carry today's names on OpenStreetMap where they match the Japanese sketches;
  the south-bank hills the Japanese called 寨山, 韓山 and 雄山 are hilltops on an elevation model at
  the bearings and distances the reports give.
- **The guns at Taierzhuang.** Each battery's reach is a sector range fan opening 90° towards
  the other side's guns: the sFH 18/32L's 15,000 m, the Type 96's 11,900 m, the Type 4's
  8,800 m, the Type 38 field gun's 11,600 m. No range is recorded for the Chinese field guns,
  so they have none. Fire missions are drawn as rounds flying from a battery to its target at
  the times the reports give, at a notional 280 m/s; their tracks show who fired on whom, not
  ballistics.
- **The first 15 cm rounds.** Chinese accounts have the 15 cm guns duelling from 27 March. The
  Japanese reports describe the first duel on 28 March with guns they took for field guns, and
  first record rounds of the 15 cm class at 15:46 on 31 March; the replay follows them
  (duel-on-27-march, first-15cm-fire).
- **Where the 15 cm guns stood** is not in any record. The Japanese saw the rounds come from
  the Xiongshan direction and never found the guns. The replay puts them about 13 km south of
  the Japanese gun line, beyond the reach of every Japanese gun and within their own of
  Liujiahu, with a 3 km bound (sfh-position).
- **On screen** names and quotations are given in English and pinyin; the viewer cannot yet
  draw Chinese or Japanese characters. The ledger keeps the originals.
- **Build checks.** `build/taierzhuang.py` fails if infantry marches faster than 7 km/h or
  armour, lorries, trains and the armoured trains pass 25 km/h; if a battery is not standing
  where its range fan is drawn; if a round flies further than its gun's reach, or the 15 cm
  position lies within a Japanese fan or beyond its own reach of Liujiahu and Sanlizhuang; if
  Wang Mingzhang does not fall at the west moat, or the Japanese battalions are not at the
  outer east gate at 14:15 on the 16th and on the south breach at 16:05 on the 17th; if a
  unit's track at Taierzhuang does not take up where its track at Tengxian leaves it; or if an
  estimate in `build/evidence/` lies outside its records without saying why.

## Conflicts carried

The sources' accounts are kept in `build/evidence/`, one module per part of the story; the
replay's estimates are the dispute entries' "Replay estimate" column.

<!-- evidence ledger: generated by build/taierzhuang.py from build/evidence/ -->
| Dispute | Records (source: what it says) | Replay estimate and basis |
| --- | --- | --- |
| Which clock the Japanese regiment's report keeps (`japanese-clock`) | 歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200): the report's table for 16 March (sunrise 06:20, sunset 17:50); at Tengxian the sun rose at about 06:23 UTC+8, 07:23 Tokyo time: “日出 午前六時二十分 日没 午後五時五十分”<br>「滕县作战之界河附近的战斗 3月14-15日」, 抗日战争纪念网 (2018): the 3rd Battalion's dusk assault, 16 March; sunset at 18:19 UTC+8: “1840趁薄暮一气突入” | **Local time, UTC+8**. Japanese army records are usually read as Tokyo time. The report's sunrise falls within two minutes of the sun's at UTC+8 and an hour from Tokyo time's, and its 18:40 dusk only fits local time; the times the two sides both record (the east gate at about 14:00, the west gate at 17:00) agree on it. |
| When the line at 界河 broke (`jiehe-line-broken`) | 「滕县作战之界河附近的战斗 3月14-15日」, 抗日战争纪念网 (2018): the 63rd Regiment, 14 March: “1810进入界河”<br>滕县保卫战 (zh.wikipedia): 15 March: “13时，界河正面阵地被日军突破” | **The village entered on the 14th; the line round it given up at 13:00 on the 15th**. The 63rd's record is of the village; the Chinese one of the whole line from 界河 to 龍山, which Seya's order of 10:30 on the 15th, issued at 界河, shows was still held east of it. |
| Which way the Japanese swung round the city (`eastern-swing`) | 瀬谷支隊命令, 別紙 (JACAR C11111170300): 瀬支作命第九号 (the advance guard leaves 龍山店 at noon along the 龍山店–東郭–王廟 road): “前衛ハ正午龍山店附近出発 龍山店―東郭 王廟道ニ沿フ地区ヲ王廟ニ向ヒ前進スヘシ”<br>《滕县志》 (中华书局, 1990): 《滕县志》 (over ten thousand round the east of 龍山; by 17:00 the van was at 龍陽店 and 馮河, north-east of the city): “以万余兵力由龙山东侧向滕县城迂回…下午5时许，其先头部队已达滕县城东北的龙阳店、冯河一带” | **By 東郭 and 王廟, east and south-east of the city**. The Japanese orders and the 10th Regiment's report give the route; 龍陽店 appears in no Japanese record and may have been a flank screen. |
| What the heavy battalion fired (`heavy-battalion-guns`) | 「滕县作战之界河附近的战斗 3月14-15日」, 抗日战争纪念网 (2018): “野战重炮兵第二联队一大队(4年式15榴12门)”<br>姜克實「日本軍の史料から見る滕県作戦の実記録」, 文化共生学研究 14 (2015): Jiang's narrative of 16 March: “野戦重砲兵第二聯隊の第Ⅰ大隊（91式105mm榴弾砲12門）も到着し、東関の寨門に向け試射開始”<br>姜克實「日本軍の史料から見る滕県作戦の実記録」, 文化共生学研究 14 (2015): Jiang's own table of the guns: 4年式15糎榴弾砲 1 battalion × 12<br>滕县保卫战 (zh.wikipedia): “野战重炮兵第2联队第1大队（150毫米榴弹炮12门）” | **Twelve Type 4 15 cm howitzers, range 8.8 km**. Three of the four records, Jiang's own table among them, give 15 cm; the range is the Type 4's with its charge increased, as Jiang gives it. |
| Which Type 38 field gun the field battalion had, and its reach (`field-guns-range`) | 姜克實「坂本、瀬谷支隊の台児庄撤退の経緯 ─1938年4月」, 岡山大学文学部紀要 64: at Taierzhuang ten days later: “野砲兵第十聯隊第一大隊の改造38式野砲（7.5糎）8門”<br>姜克實「日本軍の史料から見る滕県作戦の実記録」, 文化共生学研究 14 (2015): at Tengxian: “38式野砲：…有効射撃距離約8,000ｍ” | **The improved Type 38, drawn to its maximum range of 11,600 m**. The same battalion is recorded with the improved gun at Taierzhuang; the range fan shows the furthest a shell could reach, not the effective range. |
| When the guns began to breach the inner wall (`breaching-fire`) | 歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200): “午前八時三十分駐屯軍重砲ハ東門南方四十米ノ城壁ニ對シ野重ハ東南角西方二十米ノ城壁ニ對シ破壊射撃ヲ開始ス”<br>姜克實「日本軍の史料から見る滕県作戦の実記録」, 文化共生学研究 14 (2015): 07:30 ranging; about 1 hour of harassing fire; 09:00 wall-breaching fire begins<br>歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200): the east-gate breach nearly made in fifty rounds: “東門附近ノ如キハ僅カ五十發ニシテ殆ト完成ス” | **08:30**. The report's narrative of the day; its plan had set breaching for 08:00. |
| Where the armoured train was taken (`armoured-train-captured`) | 瀬谷支隊命令, 別紙 (JACAR C11111170300): 瀬支作命第十三號, from an aircraft's report: “飛行機ヨリノ通報ニ依レハ歩六三ハ午後十二時三十分王家樓ニ達シ敵装甲列車一、機関車一輛ヲ鹵獲シアリ”<br>姜克實「日本軍の史料から見る滕県作戦の実記録」, 文化共生学研究 14 (2015): “この列車はのち、南沙河で城外作戦を担当する第六十三聯隊によって拿捕” | **Near 南沙河, at about 12:30**. 王家樓 is not located; 南沙河 is the station south of the city on the 63rd's line of advance. |
| Whether any Chinese 15 cm howitzer fired at Tengxian (`chinese-heavy-guns`) | SFH 18榴彈砲 (zh.wikipedia): the 10th Artillery's battalion of sFH 18/32L, the 32-calibre export model: “拥有7门炮的一营最先被配给汤恩伯第20军团，1938年3月中旬驰援第五战区。”<br>萨沙「国军的雷神之锤——抗战中的sFH18 150毫米榴弹炮」, 抗日战争纪念网 (2018): at Taierzhuang, 27 March: “27日刚刚到阵地，双方猛烈炮战，激战2个多小时”<br>戦史叢書 89 『支那事変陸軍作戦〈2〉』 (1976): the first Japanese note of strong Chinese artillery, at Taierzhuang on 28 March: “有力な敵砲兵（二四～二五門）”<br>姜克實「日本軍の史料から見る滕県作戦の実記録」, 文化共生学研究 14 (2015): the 10th Regiment's captures at Tengxian: three mortars: “敵側も迫撃砲3門しかなかった” | **None: the defenders had mortars, the armoured train and, south of the city, a few mountain guns**. No record puts the 15 cm battalion with the division Tang Enbo sent toward Tengxian; its first recorded fire is at Taierzhuang. |
| What happened at the east suburb on 16 March (`east-suburb-sixteenth`) | 滕县保卫战 (zh.wikipedia): “3月16日10时半，日军炮火猛烈轰击东关，东关城墙被炸开了一二十米的缺口”<br>滕县保卫战 (zh.wikipedia): “下午5时，日军发动第六次攻势，突入城内40余人”<br>滕县保卫战 (zh.wikipedia): “下午6时后，严营长组织2个连发起反击，把突入的日军消灭”<br>姜克實「日本軍の史料から見る滕県作戦の実記録」, 文化共生学研究 14 (2015): from the 10th Regiment's report: “第二回目の集中砲撃により、城（寨）門は完全に破壊され”<br>歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200): after the 14:15 lodgement: “敵ノ抵抗頗ル執拗ニシテ著シク進展セス” | **The gate breached by 14:00; the 3rd Company holds its corner of the suburb from 14:15, and the defenders the rest into the night**. The Japanese report records the lodgement and no ejection; the Chinese counter-attack may have recovered ground within the suburb. |
| When the Japanese held the south wall (`south-wall-taken`) | 滕县保卫战 (zh.wikipedia): “15时日军巩固占领了南城墙”<br>歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200): “午後四時五分第三大隊城壁ニ突入シ西側城壁上ニ向ヒ戦果ヲ擴張ス” | **16:05**. The report of the battalion that climbed the wall; its assault at 14:30 had been thrown back. |
| How and when Wang Mingzhang was killed (`wang-mingzhang-killed`) | 滕县保卫战 (zh.wikipedia): let down from the north-west corner, making for the station, machine-gunned from the west gate tower in a ditch near the power plant: “从城墙西北角缒城后奔西关外火车站，在西关电灯厂附近壕沟内被西城门楼上的日军发现遭密集扫射”<br>蔡永飞「滕县保卫战中的张宣武」, 人民政协网 (2025): “王铭章是在3月17日下午5时左右牺牲的”<br>郑学富, 人民政协网 (2020): at 15:00: “王铭章率部拼死抵抗，不幸身中数弹，壮烈殉国”<br>王銘章 (zh.wikipedia): shot at the central crossroads: “在城中心十字街口指揮作戰時，不幸中彈殉職”<br>國民政府 褒揚令, 6 April 1938: the posthumous decree of 6 April 1938: “以率部奮力巷戰，竟爾殉職”<br>姜克實「日本軍の史料から見る滕県作戦の実記録」, 文化共生学研究 14 (2015): his adjutant 李少坤's memoir, as Jiang gives it: “日が暮れる前、王は「西門外の濠の近くで、城壁上からの射撃」を受け死亡した”<br>歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200): the Japanese learned of his death only from Chinese announcements: “其後軍情報ニ依レハ左記ノ如ク師長王銘章モ戦死セルコト敵ノ發表ニテ明白ナルニ至レリ” | **About 17:30, in the moat outside the west gate, shot from the gate tower with his staff**. Most accounts put it in the west suburb after the west gate fell, at about 17:00 on both sides' records, and before dark; the Japanese found his chief of staff's body outside the west gate. Jiang's estimate of 17:30. |
| The death of Zou Shaomeng, the 124th Division's chief of staff (`zou-shaomeng-killed`) | 歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200): a mounted officer with some fifty guards, shot leaving by the north gate on the evening of the 17th and identified from his papers: “百二十四師参謀長鄒紹孟”<br>滕县保卫战 (zh.wikipedia): the Chinese accounts: killed near the north gate on 17 March | **Shot outside the north gate at about 18:30 on the 17th**. Both sides put it at the north gate; the report places it after the 3rd Battalion reached the north-west corner at 18:30 and gives no time of its own. |
| What became of Wang Lin, the 740th Regiment's commander (`wang-lin-fate`) | 滕县保卫战 (zh.wikipedia): “日军突入东关，守备东关的第124师第370旅第740团团长王麟、团政训员胡清溪阵亡”<br>歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200): among the prisoners of 18 March: “團長代理王麟、第百二十四師参謀張重以下十数名” | **Not resolved**. The Japanese name may be another man or a misidentification; the replay shows the regiment destroyed and no fate for him. |
| The losses at Tengxian (`losses`) | 歩兵第十聯隊死傷表, 3月15日–18日 (JACAR C11111170700): the 10th Regiment's casualty table, 15–18 March: 16 killed (1 officer), 129 wounded, 3 missing of 2,654 engaged<br>歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200): Chinese dead left on the field: “遺棄死体ノミニシテモ其数三千百ヲ算スル”<br>滕县保卫战 (zh.wikipedia): Sun Zhen's report: “我阵亡官兵3000余人，负伤官兵4000余人”<br>滕县保卫战 (zh.wikipedia): Sun Zhen's claim of Japanese losses: “毙伤敌军官佐320余员，击毙士兵1500余名，击伤士兵5700余名” | **Each side's own count is given; no single figure**. Each side's figures for the other's losses are many times the other's own count. |
| When Lincheng fell (`lincheng-fall`) | 滕县保卫战 (zh.wikipedia): “3月17日夕攻占第22集团军总司令部与第41军军部驻地临城”<br>滕县保卫战 (zh.wikipedia): “3月17日晨，临城失守”<br>《薛城区志》: of the station: “1938年5月19日，该站沦入日军手中” | **The evening of 17 March**. The 63rd Regiment's pursuit reached 官橋 at dawn; the May date is the station's, or a confusion. |
| When Yixian fell (`yixian-fell`) | 台兒莊戰役 (zh.wikipedia): “3月18日…第4師在嶧縣附近與日軍機械化部隊激戰，嶧縣當日晚間失陷”<br>歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): the left pursuit force: “日没後人梯ヲ作リ城門上部ノ破壊孔ヨリ突入城門ヲ開キテ城内ニ進入掃蕩シ…二十日午前零時三十分掃蕩ヲ完了シ縣城ヲ確保ス” | **00:30 on 20 March**. The left pursuit force's own account: it attacked on the 19th, climbed in over the south gate after dark and finished clearing the town at 00:30. |
| When the Japanese took Zaozhuang (`zaozhuang-fell`) | 《中共枣庄地方史》 第一卷: “1938年3月18日，枣庄失陷”<br>歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): after 00:30 on 20 March: “同追撃隊ハ嶧縣占領後第八中隊（機關銃一小隊ヲ屬ス）ヲ棗莊占領ノ為派遣ス” | **20 March, by a company of the left pursuit force; not shown**. The Japanese report sends the company after Yixian fell; parties along the Lincheng–Zaozhuang branch may have been there from the 18th. |
| When the Chinese 31st Division took over Taierzhuang (`31st-division-arrival`) | 台兒莊戰役 (zh.wikipedia): “3月22日，第二集團軍第31師到達台兒莊暫歸第二十集團軍指揮”<br>《黄埔》 2018年第3期: “3月22日，王冠五奉命率部进入台儿庄布防，担任守城总指挥” | **08:00 on 22 March**. The day both give; the hour is the replay's. |
| When the Japanese took the town's north-west corner (`north-west-corner-time`) | 戦史叢書 89 『支那事変陸軍作戦〈2〉』 (1976): “二十八日〇七三〇ころ、台児庄の北西角の一部も占領”<br>歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): the first breaching shoot: “支那駐屯重砲中隊午前七時五十分頃破壞射擊ヲ實施シテ概ネ之ヲ破壞シ”<br>歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): the 11th Company's assault: “豫定時刻ニ先ツコト五分午後七時二十五分一擧ニ城内ニ突入シ突擊成功ノ信號白吊星ヲ揚ク” | **19:25**. The regiment's own report breaches the corner at 07:50 and again at 15:30 and storms it at 19:25; the official history's 07:30 is nearest the first breaching shoot. |
| Who held the north-west corner on the night of 28 March (`wenchang-pavilion`) | 《黄埔》 2018年第3期: “3月27日晚，日军100余人窜入城西北角，占领文昌阁…11时，突击队攻克文昌阁”<br>「1938年台儿庄抗战生死三日全纪实」, 抗日战争纪念网: “3月28日，晚8时，日军百余窜入台儿庄西北角…晚11时，攻克文昌阁”<br>歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): “豫定時刻ニ先ツコト五分午後七時二十五分一擧ニ城内ニ突入シ” | **The Japanese foothold kept from 19:25 on the 28th until the 31st**. The 11th Company stays at the corner in the Japanese reports until it is withdrawn at 20:00 on 31 March; the Chinese special company's retaking of the Wenchang pavilion, the corner's highest point, is told but not shown. |
| When the guns opened on 27 March (`type-96-opening-27-march`) | 歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): the assault plan's sketch: “火砲ノ射撃開始午前六時”<br>臨SAS戦詳第一號 臺兒庄附近ノ戰鬪詳報, 第二軍臨時野戰重砲兵中隊 (JACAR C11111730100–C11111731000): “午前五時五十分中隊長ハ…觀測所ニ到リ先ツ側防機關銃ヲ制壓シ引續キ城內右半分ニ對シ擾亂射擊”<br>姜克實「台児庄作戦の概観」, 岡山大学大学院社会文化科学研究科紀要 43 (2017): “05：50砲撃が始まり” | **06:00**. The hour the assault plan set for all the guns; the Type 96 company's commander began on the flanking machine guns ten minutes before. |
| Whether the guns duelled on 27 March (`duel-on-27-march`) | 萨沙「国军的雷神之锤——抗战中的sFH18 150毫米榴弹炮」, 抗日战争纪念网 (2018): the Chinese 7th and 10th Artillery; no clock time: “27日刚刚到阵地，双方猛烈炮战，激战2个多小时”<br>歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): “午後五時三十分頃以來臺兒庄西方地區方向ヨリ野山砲級榴彈劉家湖部落内外至ル所ニ落下シ”<br>歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): “午後七時十五分再ヒ臺兒庄停車場方向及停車場西側附近ヨリ野山砲級榴彈約二十發劉家湖ニ落下ス” | **Chinese field-gun fire on Liujiahu at 17:30 and 19:15; no duel**. The Japanese report on 27 March records Chinese shells on Liujiahu but no counter-battery fire, which is first ordered for the 28th; the Chinese account gives no hour. |
| How many guns the Chinese had round the town (`chinese-gun-count`) | 歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): “敵ハ運河南側高地脚ニ十數門ノ砲ヲ有シ”<br>歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): “敵ハ野砲五－六門列車砲及迫擊砲ヲ有スル”<br>歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): “敵砲兵數少クモ二十四－五門ヲ算シ”<br>歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): from prisoners: “運河ノ線ニハ二營ノ督戰隊及砲四十門アリト” | **Four batteries south of the canal and the station, from 25 March**. The places the Japanese gave for the guns they saw or heard: Zhaishan, Hanshan, Xiongshan and the south bank by the station; their count grew as more were found. |
| Where the Chinese 15 cm howitzers stood (`sfh-position`) | 歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): 1 April: the heavy guns seemed to be towards Xiongshan, south of the town, but deeply hidden; never found: “其重砲ハ臺兒庄南方雄山方向ニアルモノヽ如キモ遮蔽深ク…遂ニ發見スルヲ得ス”<br>大橋武夫「支那事変初期 北支における十五榴部隊を中心とする砲兵戦史資料」 (JACAR C11111729600, C11111729700): even the Type 96, pushed up to the canal, could not reach them; the author calls his sketch exaggerated: “我砲兵中最大射程をもつ九六式十五榴が敵前ギリギリ（運河より前えは出られない）まで陣地を推進しても、敵の砲兵陣地まではとどかない”<br>萨沙「国军的雷神之锤——抗战中的sFH18 150毫米榴弹炮」, 抗日战争纪念网 (2018): on the canal's south bank: “炮10团1营一个连2门sFH18 150毫米榴弹炮赶赴到台儿庄运河南岸”<br>臨SAS戦詳第一號 臺兒庄附近ノ戰鬪詳報, 第二軍臨時野戰重砲兵中隊 (JACAR C11111730100–C11111731000): the Type 96 company's lessons: enemy batteries of two or three guns, often changing position: “砲數ハ二門或ハ三門ノ事多シ…陣地ハ屢々變換スル事多シ” | **South of Xiongshan, about 13 km from the Japanese guns at Sanlizhuang, within 5 km**. In the direction the Japanese saw the rounds come from, and beyond the reach of every Japanese gun from its position, as Ohashi remembered; within the 15 km that reaches Liujiahu and Sanlizhuang, where the rounds fell. |
| How many 15 cm howitzers the Chinese had at Taierzhuang (`sfh-count`) | 大橋武夫「支那事変初期 北支における十五榴部隊を中心とする砲兵戦史資料」 (JACAR C11111729600, C11111729700): “僅か二門のラインメタルに我が全砲兵（野砲一大隊、四年式十五榴一大隊、九六式十五榴一中隊）が完全に制圧される”<br>萨沙「国军的雷神之锤——抗战中的sFH18 150毫米榴弹炮」, 抗日战争纪念网 (2018): “炮10团1营一个连2门”<br>SFH 18榴彈砲 (zh.wikipedia): “拥有7门炮的一营最先被配给汤恩伯第20军团” | **Two**. The Japanese artillery officer and the Chinese account agree on two at the canal; the battalion's seven were split between the canal and Tang Enbo's corps. |
| What the Japanese took the 15 cm guns for (`what-the-japanese-saw`) | 歩兵第十聯隊 臺兒庄附近戦闘詳報 第十三號 (JACAR C11111171800–C11111172200): 15 cm cannon and a good observation zone on the south bank: “十五加ヲ有シ且良好ナル台児庄南岸ノ観測地帯ヲ有スル”<br>歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): 1 April: “十五糎加農級ノ砲彈”<br>大橋武夫「支那事変初期 北支における十五榴部隊を中心とする砲兵戦史資料」 (JACAR C11111729600, C11111729700): “ラインメタル式十五榴” | **The Rheinmetall 15 cm howitzer, sFH 18/32L**. Its 32-calibre barrel and 15 km reach, longer than any Japanese howitzer's, made it look like a cannon to those it fired on. |
| When the Chinese 15 cm howitzers first fired (`first-15cm-fire`) | 萨沙「国军的雷神之锤——抗战中的sFH18 150毫米榴弹炮」, 抗日战争纪念网 (2018): 27 March: “27日刚刚到阵地，双方猛烈炮战，激战2个多小时”<br>Battle of Taierzhuang (en.wikipedia): “On March 28, Chinese artillery support arrived in the form of two 155mm and ten 75mm pieces.”<br>戦史叢書 89 『支那事変陸軍作戦〈2〉』 (1976): 28 March, judged field guns in the 63rd Infantry's report: “有力な敵砲兵（二四～二五門）”<br>歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): “十五糎級火砲ノ射撃ヲ受ケタルハ本戰鬪間ヲ以テ最初トシ”<br>台児荘の戦い (ja.wikipedia): placed in early April: “湯恩伯の部隊に配備されたドイツ製15cm榴弾砲が初めて使用され” | **Their first fire the Japanese recorded: 15:46 on 31 March**. The Chinese account's duel of the 27th has no counterpart in the 63rd Infantry's or the Type 96 company's reports, which describe the guns of the 28th as field guns. Both sides' times are on local time, so the days cannot be a clock's error. |
| When the four concentrations of 31 March fell (`concentration-times`) | 歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): four concentrations between 11:14 and 14:40: “殆ント全砲兵(十五門)” | **11:14, 12:20, 13:30 and 14:40**. The report gives the first and the last; the two between are spaced evenly. |
| When the 15 cm rounds fell on 1 April (`afternoon-bombardments`) | 歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): from the morning, then at fixed intervals in the afternoon: five bombardments by day: “朝來野山砲彈ト共ニ十五糎加農級ノ砲彈落下シ午後ニ至リテハ一定ノ時間々隔ヲ置キテ射撃ヲ集中シ…敵ノ砲撃晝間五回ニ及フ”<br>臨SAS戦詳第一號 臺兒庄附近ノ戰鬪詳報, 第二軍臨時野戰重砲兵中隊 (JACAR C11111730100–C11111731000): “敵砲彈ハ三里庄陣地及劉家湖附近ニ落下ス” | **One in the morning, four in the afternoon at 13:00, 14:30, 16:00 and 17:30**. No times are given; the afternoon's are spaced at the fixed interval the report describes. |

Key moments, on which the sources agree:

| Moment | Records (source: what it says) | Time |
| --- | --- | --- |
| Seya orders the swing round the east of Tengxian (`seya-order-nine`) | 瀬谷支隊命令, 別紙 (JACAR C11111170300): 瀬支作命第九号, "三月十五日午前十時三十分於界河" (the detachment advances by 界河, 東郭 and 王廟 to prepare the attack on Tengxian): “支隊ハ界河、東郭、王廟方面ヨリ王廟附近ニ向ヒ前進シ滕県敵陣地ニ対スル攻撃ヲ準備セントス”<br>歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200): the 10th Regiment, on receiving it (its main body of five companies follows the 63rd and attacks from the weakly held east): “主力（歩兵五中隊）ヲ以テ歩六三ノ後方ニ續行シ敵ノ備ヘ薄キ東方地區ヨリ滕縣附近ノ敵ヲ攻撃スルコトヽナル” | 15 10:30 |
| Yan Yi's battalion reaches the city (`yan-yi-enters-the-city`) | 滕县保卫战 (zh.wikipedia): of the 731st Regiment only Yan Yi's 1st Battalion reached the city: “3月15日17时” | 15 17:00 |
| The Japanese field guns duel with a Chinese armoured train (`armoured-train-duel`) | 歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200): the train has guns and fires on us; it withdraws south after about ten minutes: “該列車ハ砲ヲ有シ我ニ向ヒ射撃ヲ行フ”<br>姜克實「日本軍の史料から見る滕県作戦の実記録」, 文化共生学研究 14 (2015): “11:00、75mm列車砲を装備した南進装甲列車の編隊も発見し、砲撃を交わした” | 16 11:00 |
| A Japanese artillery observer takes the pagoda (`pagoda-observer`) | 姜克實「日本軍の史料から見る滕県作戦の実記録」, 文化共生学研究 14 (2015): from the 10th Regiment's report: 10:00 observer 家形中尉 takes the 龍泉塔 (30 m) and corrects fire<br>歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200): the observer bayonets the Chinese holding the pagoda: “金塔ニ據ル敵ヲ刺殺” | 17 10:00 |
| The Japanese break into the east suburb (`outer-east-gate-breached`) | 歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200): the 3rd Company through the breach of the outer east gate holds a corner: “第三中隊ハ東門ノ破壊口ヨリ突入シ該一角ヲ確保セリ 時正ニ午後二時十五分トス”<br>瀬谷支隊命令, 別紙 (JACAR C11111170300): 瀬支作命第十三號, 18:00 on 16 March: “歩兵第十聯隊ハ滕縣ノ敵ヲ攻撃中ニシテ午後二時十五分同地外壁東門ニ突入セリ” | 16 14:15 |
| The 3rd Battalion enters the south suburb (`outer-south-gate-taken`) | 歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200): “午後六時四十分遂ニ外城南門ニ突入” | 16 18:40 |
| Wang Mingzhang's last telegram (`wang-mingzhang-last-telegram`) | 滕县保卫战 (zh.wikipedia): to Sun Zhen, noon on 17 March (the enemy's heavy guns and aircraft have pounded us since dawn; the wall is breached in many places; I am resolved to fight to the death): “目前敌用重炮、飞机从晨至午不断猛轰，城墙缺口多处，敌步兵屡次登城，屡被击退。职意委座成仁之训，及开封面谕嘉慰之词，决以死拼，以报国家，以报知遇。” | 17 12:00 |
| Colonel Akashiba grazed by a sniper (`akashiba-wounded`) | 歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200): he stayed in command: “午後一時過側方百米ノ距離ヨリ敵小銃弾ノ狙撃ヲ受ケ左背部ニ擦過傷ヲ被リ外城東門内旧大隊本部ノ位置ニ後退ス” | 17 13:00 |
| The 1st Battalion over the east wall, the north gate taken (`east-wall-and-north-gate-taken`) | 歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200): “午後九時四十分遂ニ城壁ニ突入シ北方ニ戦果ヲ擴張シ續イテ午後十一時迄ニハ北門ヲ占領ス” | 17 21:40 |
| The city cleared (`mopping-up-complete`) | 歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200): “午後二時頃ニ至リ概ネ掃蕩完了”<br>歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200): 18 March (the body of 趙渭賓, the 122nd Division's chief of staff, found outside the west gate): “此際西門外ニ第百二十二師参謀長少将趙渭賓ノ屍体ヲ發見セリ” | 18 14:00 |
| The right pursuit force takes Hanzhuang north of the canal (`hanzhuang-taken`) | 歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): “右追撃隊ハ十九日正午頃ヨリ韓莊附近ノ敵ヲ攻撃シ午後一時北部韓莊ヲ占領ス同方面ノ敵ハ増援中ニシテ運河附近ニ約一萬ノ敵アリ” | 19 13:00 |
| The Japanese meet the 31st Division's cavalry at Kangzhuang (`first-contact-at-kangzhuang`) | 《第三十一师台儿庄战役战斗详报》, as quoted in 「台儿庄战役中的中共地下党员」, 宁夏回族自治区交通运输厅 (2017): “9时顷，敌步骑兵约300余，战车一辆，由峄县向东南行进，与师骑兵于康庄遭遇接触，我骑兵稍退” | 23 09:00 |
| The II Battalion's first assault, at the north gate (`first-assault-on-taierzhuang`) | 歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): the battalion's telegram, received 16:30: “午後四時十五分城門ヲ破壞シ突撃開始”<br>歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): received 21:00: “部隊ノ一部突入シタルモ成功セス 目下内外ノ連絡絶エ死傷續出ス敵ハ益々増加シ我ヲ完全ニ包圍セリ彈藥到着セス 大隊ハ北門外ニ在リ” | 24 16:15 |
| A Chinese armoured train fires from the railway (`armoured-train-from-the-station`) | 歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): the 5th Company, about 08:00: “臺兒庄停車場ヨリ敵裝甲列車近ク前進シ來リ中隊ノ集結地ニ對シ機關銃及列車砲ヲ以テ射撃シ” | 25 08:00 |
| The Japanese first report Chinese guns south of the canal (`guns-south-of-the-canal`) | 歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): the 10th Company's commander, received 16:35: “午後四時第二大隊主力ト連絡ヲ確保ス 敵ハ運河南側高地脚ニ十數門ノ砲ヲ有シ盛ニ我ヲ砲撃シアリテ晝間ノ行動甚シク困難ナリ” | 25 16:00 |
| The Type 96 15 cm howitzers arrive and open fire (`type-96-arrives`) | 歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): “支那駐屯砲兵聯隊混成第六中隊(九六式重砲一小隊)…午後五時頃劉家湖ニ到着シ”<br>歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): its first fire at Taierzhuang, 17:30: “劉家湖北側ニ到着陣地ヲ占領シ午後五時三十分三里庄附近ノ陣地ニ據ル敵ヲ制壓シテ之ヲ動搖セシメ” | 25 17:00 |
| The II Battalion breaks into the north-east corner (`north-east-corner-entered`) | 歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): the battalion's telegram, received 08:30: “午前七時五十分突入一角ヲ占領掃蕩中” | 27 07:50 |
| The first artillery duel the Japanese describe (`first-artillery-duel`) | 歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): “午前六時四十分頃三里庄東北部落ノ野戰重砲兵第三中隊臺兒庄西北角附近ニ向ヒ試射ヲ始ムルヤ敵砲兵之ニ對シ射擊ヲ開始シ其射彈右砲兵陣地ノ後方約百米附近ニ落達シ”<br>歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): where the Chinese guns seemed to be: “運河南岸地區寨山(臺兒庄西南約七、五粁)韓山(臺兒庄南々西約五・五粁)及雄山ノ北側附近ニ位置シアルモノヽ如シ” | 28 06:40 |
| Chinese shells burn the Type 96 company's vehicles (`vehicles-burned`) | 臨SAS戦詳第一號 臺兒庄附近ノ戰鬪詳報, 第二軍臨時野戰重砲兵中隊 (JACAR C11111730100–C11111731000): the company's report, under 11:10: “後方ニ集結中ナリシ車輛ハ敵砲彈ノ集中火ヲ受ケガソリンニ命中火災ヲ起シ燒失ス”<br>歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): “敵砲火支那駐屯重砲中隊ノ車輛ニ命中シ輕油發火シ車輛ヲ多數失ヒ下士官以下十三名ノ戰死傷者ヲ生シ” | 29 11:10 |
| About a thousand Chinese attack from the station (`night-attack-from-the-station`) | 歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): “午前三時頃停車場方向ヨリ一部ヲ以テ鐵道線路東側ヲ主力ヲ以テ鐵道線路ニ沿ヒ北進シ來レル約一千ノ敵ノ襲撃ヲ受ケタルモ各隊ノ準備火力ニ依リ之ヲ西方ニ撃退シ” | 30 03:00 |
| The 2nd Heavy Company raided at its guns (`heavy-battery-raided`) | 歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): “午前三時三十分三里庄北側ノ野戰重砲兵第二中隊放列陣地ハ鐵道線路方面ヨリ敵ノ襲撃ヲ受ケ敵兵肉薄シ來リタルモ數發ノ零距離射撃ニ依リ之ヲ撃退シ” | 30 03:30 |
| Chinese guns from Zhaocun on the field-gun position (`zhaocun-duel`) | 歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): “野砲陣地ハ午前六時頃趙村方向ヨリ敵砲兵ノ集中射撃ヲ受ケ不尠損傷ヲ受ケタルモ直ニ其二門ヲ破壊シ他ノ二門ヲ敗退セシメ” | 30 06:00 |
| The first dare-to-die squad attacks the north-west corner (`dare-to-die-squad`) | 「台儿庄战役期间究竟派出了多少支敢死队？」, 澎湃 (2018), from the Chinese units' battle reports: from the 31st Division's battle report: “当圈定57名，各悬奖洋30元，由时营长(时尚彬)率领。当天晚上8点，57名敢死队员佩带日军钢盔“潜形挺进”、“以炸弹手枪纵火冲杀”对西北角的日军发起进攻”<br>「台儿庄战役期间究竟派出了多少支敢死队？」, 澎湃 (2018), from the Chinese units' battle reports: what it took: “夺取敌掩蔽部五，房舍数幢” | 30 20:00 |
| The guns fire on a Chinese train in the station (`train-in-the-station`) | 歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): “先ツ午前六時二十分砲兵隊ヲシテ臺兒庄停車場ニ現出セシ敵列車ニ對スル砲撃ヲ命シ” | 31 06:20 |
| Japanese concentrations on the town, and the Chinese reply (`concentrations-and-the-reply`) | 歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): four concentrations on the town, 11:14–14:40: “殆ント全砲兵(十五門)”<br>歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): “敵ハ我ノ砲撃ヲ受クルヤ砲十數門ヲ以テ劉家湖及三里庄附近ノ我砲兵陣地ニ向ヒ報復的集中射撃ヲ實施シタルモ甚シキ損害ナシ” | 31 11:14 |
| The first 15 cm-class rounds the Japanese record (`first-15cm-class-rounds`) | 歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): “午後三時四十六分野戰重砲兵第三中隊放列陣地ハ十五糎級砲彈ヲ受ケ同中隊火砲一門使用ニ堪ヘサルニ至ル 十五糎級火砲ノ射撃ヲ受ケタルハ本戰鬪間ヲ以テ最初トシ” | 31 15:46 |
| The 11th Company withdraws from the north-west corner (`eleventh-company-withdraws`) | 歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100): the heavy battalion's concentration covering the withdrawal: “午後八時ヲ期シ臺兒庄西側部落ニ集中射撃ヲ指向シ” | 31 20:00 |
| The Japanese field artillery will not attack under the Chinese guns (`superior-enemy-artillery`) | 歩兵第十聯隊 臺兒庄附近戦闘詳報 第十三號 (JACAR C11111171800–C11111172200): the 10th Field Artillery's Lt-Col Taniguchi: a superior enemy artillery that has completed its preparations: “優勢ニシテ而モ諸準備ヲ完了セル敵砲兵” | 1 01:00 |
<!-- end of evidence ledger -->

## Sources

- 歩兵第十聯隊 滕縣附近戦闘詳報 第十一號, 死傷表 and 附図; 瀬谷支隊命令 (防衛省防衛研究所, via JACAR) — https://www.jacar.archives.go.jp/das/meta/C11111170200, https://www.jacar.archives.go.jp/das/meta/C11111170300, https://www.jacar.archives.go.jp/das/meta/C11111170400, https://www.jacar.archives.go.jp/das/meta/C11111170700
- 歩兵第六十三聯隊 台児庄攻略戦闘詳報 — https://www.jacar.archives.go.jp/das/meta/C11111252700 to C11111254100
- 歩兵第十聯隊 臺兒庄附近戦闘詳報 第十三號 — https://www.jacar.archives.go.jp/das/meta/C11111171800, C11111171900, C11111172200
- 臨SAS戦詳第一號 臺兒庄附近ノ戰鬪詳報, 第二軍臨時野戰重砲兵中隊 — https://www.jacar.archives.go.jp/das/meta/C11111730100 to C11111731000
- 大橋武夫「支那事変初期 北支における十五榴部隊を中心とする砲兵戦史資料」 — https://www.jacar.archives.go.jp/das/meta/C11111729600, https://www.jacar.archives.go.jp/das/meta/C11111729700
- 姜克實「台児庄作戦の概観」『岡山大学大学院社会文化科学研究科紀要』43 (2017) — https://ousar.lib.okayama-u.ac.jp/files/public/5/54962/20170412104822203232/hss_043_001_020.pdf
- 姜克實「日本軍の史料から見る滕県作戦の実記録―1938年3月16日〜18日、中国・山東―」『文化共生学研究』14 (岡山大学, 2015) — https://ousar.lib.okayama-u.ac.jp/en/journal/scs/14/--/article/53301
- 戦史叢書 89『支那事変陸軍作戦〈2〉』(朝雲新聞社, 1976), read from the NIDS page images — https://www.nids.mod.go.jp/military_history_search/SoshoView?kanno=089
- 《滕县志》(中华书局, 1990), and the 薛城区志 — https://shandong-chorography.org/database/c46/section/3/toc.md
- 抗日战争纪念网: 「滕县作战之界河附近的战斗 3月14-15日」 and 萨沙「国军的雷神之锤——抗战中的sFH18 150毫米榴弹炮」 — https://www.krzzjn.com/show-355-73636.html, https://www.krzzjn.com/show-1188-88677.html
- 人民政协网: 郑学富 (2020), 蔡永飞「滕县保卫战中的张宣武」 (2025) — https://www.rmzxw.com.cn/c/2020-09-29/2679676.shtml, https://www.rmzxw.com.cn/c/2025-12-01/3827583.shtml
- 杨津涛「中、日战报为何差距四十倍？」, 腾讯 (archived) — https://web.archive.org/web/20190522180020/https://view.news.qq.com/original/legacyintouch/d326.html
- Wikipedia: 滕县保卫战, 王銘章, SFH 18榴彈砲, 台儿庄大战旧址, Battle of Taierzhuang, 台児荘の戦い — https://zh.wikipedia.org/wiki/滕县保卫战, https://zh.wikipedia.org/wiki/台儿庄大战旧址
- 《台儿庄区志》, for the branch railway and its stations — https://shandong-chorography.org/database/c44/section/1/article/164/index.txt
- Sites, streets and the railway: © OpenStreetMap contributors (ODbL), read through Overpass and Nominatim. No map data is bundled.

