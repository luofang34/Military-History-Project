"""The fire the reports record, 30 March – 1 April, and when the 15 cm guns first fired."""
from ledger import Dispute, Moment, Record

from .names import ENWIKI, J10, J63, JAWIKI, KRZ_SFH, SAS, SOSHO

MOMENTS = {
    "night-attack-from-the-station": Moment(
        "About a thousand Chinese attack from the station", "NIGHT ATTACK", "30 03:00",
        (Record(J63, "午前三時頃停車場方向ヨリ一部ヲ以テ鐵道線路東側ヲ主力ヲ以テ鐵道線路ニ沿ヒ北進シ來レル約一千"
                "ノ敵ノ襲撃ヲ受ケタルモ各隊ノ準備火力ニ依リ之ヲ西方ニ撃退シ", "30 03:00", quote=True),)),
    "heavy-battery-raided": Moment(
        "The 2nd Heavy Company raided at its guns", "NIGHT ATTACK", "30 03:30",
        (Record(J63, "午前三時三十分三里庄北側ノ野戰重砲兵第二中隊放列陣地ハ鐵道線路方面ヨリ敵ノ襲撃ヲ受ケ敵兵肉薄"
                "シ來リタルモ數發ノ零距離射撃ニ依リ之ヲ撃退シ", "30 03:30", quote=True),)),
    "zhaocun-duel": Moment(
        "Chinese guns from Zhaocun on the field-gun position", "EAST GUNS", "30 06:00",
        (Record(J63, "野砲陣地ハ午前六時頃趙村方向ヨリ敵砲兵ノ集中射撃ヲ受ケ不尠損傷ヲ受ケタルモ直ニ其二門ヲ破壊"
                "シ他ノ二門ヲ敗退セシメ", "30 06:00", quote=True),)),
    "train-in-the-station": Moment(
        "The guns fire on a Chinese train in the station", "TRAIN", "31 06:20",
        (Record(J63, "先ツ午前六時二十分砲兵隊ヲシテ臺兒庄停車場ニ現出セシ敵列車ニ對スル砲撃ヲ命シ", "31 06:20",
                quote=True),)),
    "concentrations-and-the-reply": Moment(
        "Japanese concentrations on the town, and the Chinese reply", "JP 15CM ROUNDS",
        "31 11:14",
        (Record(J63, "殆ント全砲兵(十五門)", "31 11:14", quote=True,
                label="four concentrations on the town, 11:14–14:40"),
         Record(J63, "敵ハ我ノ砲撃ヲ受クルヤ砲十數門ヲ以テ劉家湖及三里庄附近ノ我砲兵陣地ニ向ヒ報復的集中射撃ヲ實施"
                "シタルモ甚シキ損害ナシ", quote=True))),
    "first-15cm-class-rounds": Moment(
        "The first 15 cm-class rounds the Japanese record", "CN 15CM ROUNDS", "31 15:46",
        (Record(J63, "午後三時四十六分野戰重砲兵第三中隊放列陣地ハ十五糎級砲彈ヲ受ケ同中隊火砲一門使用ニ堪ヘサルニ"
                "至ル 十五糎級火砲ノ射撃ヲ受ケタルハ本戰鬪間ヲ以テ最初トシ", "31 15:46", quote=True),)),
    "eleventh-company-withdraws": Moment(
        "The 11th Company withdraws from the north-west corner", "11 COY", "31 20:00",
        (Record(J63, "午後八時ヲ期シ臺兒庄西側部落ニ集中射撃ヲ指向シ", "31 20:00", quote=True,
                label="the heavy battalion's concentration covering the withdrawal"),)),
    "superior-enemy-artillery": Moment(
        "The Japanese field artillery will not attack under the Chinese guns", "FIELD 10I",
        "1 01:00",
        (Record(J10, "優勢ニシテ而モ諸準備ヲ完了セル敵砲兵", "1 01:00", quote=True,
                label="the 10th Field Artillery's Lt-Col Taniguchi: a superior enemy artillery "
                      "that has completed its preparations"),)),
}

DISPUTES = {
    "first-15cm-fire": Dispute(
        "When the Chinese 15 cm howitzers first fired", "CN 15CM ROUNDS",
        (Record(KRZ_SFH, "27日刚刚到阵地，双方猛烈炮战，激战2个多小时", quote=True, label="27 March"),
         Record(ENWIKI, "On March 28, Chinese artillery support arrived in the form of two 155mm "
                "and ten 75mm pieces.", quote=True),
         Record(SOSHO, "有力な敵砲兵（二四～二五門）", quote=True,
                label="28 March, judged field guns in the 63rd Infantry's report"),
         Record(J63, "十五糎級火砲ノ射撃ヲ受ケタルハ本戰鬪間ヲ以テ最初トシ", "31 15:46", quote=True),
         Record(JAWIKI, "湯恩伯の部隊に配備されたドイツ製15cm榴弾砲が初めて使用され", quote=True,
                label="placed in early April")),
        "Their first fire the Japanese recorded: 15:46 on 31 March",
        "The Chinese account's duel of the 27th has no counterpart in the 63rd Infantry's or "
        "the Type 96 company's reports, which describe the guns of the 28th as field guns. "
        "Both sides' times are on local time, so the days cannot be a clock's error.",
        at="31 15:46",
        brief="Chinese accounts have the 15 cm guns duelling from 27 March; the Japanese record "
              "their first 15 cm-class rounds at 15:46 on 31 March."),
    "concentration-times": Dispute(
        "When the four concentrations of 31 March fell", "JP 15CM ROUNDS",
        (Record(J63, "殆ント全砲兵(十五門)", "31 11:14", "31 14:40", quote=True,
                label="four concentrations between 11:14 and 14:40"),),
        "11:14, 12:20, 13:30 and 14:40", "The report gives the first and the last; the two "
        "between are spaced evenly.", at="31 12:20"),
    "afternoon-bombardments": Dispute(
        "When the 15 cm rounds fell on 1 April", "CN 15CM ROUNDS",
        (Record(J63, "朝來野山砲彈ト共ニ十五糎加農級ノ砲彈落下シ午後ニ至リテハ一定ノ時間々隔ヲ置キテ射撃ヲ集中シ"
                "…敵ノ砲撃晝間五回ニ及フ", quote=True,
                label="from the morning, then at fixed intervals in the afternoon: five "
                      "bombardments by day"),
         Record(SAS, "敵砲彈ハ三里庄陣地及劉家湖附近ニ落下ス", "1 19:00", quote=True)),
        "One in the morning, four in the afternoon at 13:00, 14:30, 16:00 and 17:30",
        "No times are given; the afternoon's are spaced at the fixed interval the report "
        "describes.", at="1 09:30", outside=True),
}
