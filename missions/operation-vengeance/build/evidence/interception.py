"""The interception off Bougainville and the Bettys' end."""
from ledger import Dispute, Moment, Record
from sites import YAMAMOTO

from .names import AMES, COURT, HAULMAN, HN, JA, PW_2656, REPORT, SCAN, SUGITA, WP

MOMENTS = {
    "barber-attack": Moment(
        "Barber attacks T1-323", "BARBER", "09:36:40",
        (Record("pacific-wrecks", "Barber fires from directly astern of T1-323 while Zeros make "
                "passes on him; its right engine and tail are hit.", None),)),
    "ugaki-ditching": Moment(
        "Ugaki's Betty ditches", "T1-326 UGAKI", "09:39:20",
        (Record("pacific-wrecks", "T1-326 ditches about 100 m off Moila Point; Ugaki, Hayashi and "
                "Captain Kitamura survive, and 11 of 14 aboard die.", None),)),
}

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
}
