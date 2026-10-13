"""Where the guns stood, how many the Chinese had, and what the Japanese took them for."""
from ledger import Dispute, Record

from .names import J10, J63, KRZ_SFH, OHASHI, SAS, ZHWIKI_SFH

MOMENTS = {}

DISPUTES = {
    "sfh-position": Dispute(
        "Where the Chinese 15 cm howitzers stood", "SFH",
        (Record(J63, "其重砲ハ臺兒庄南方雄山方向ニアルモノヽ如キモ遮蔽深ク…遂ニ發見スルヲ得ス", quote=True,
                label="1 April: the heavy guns seemed to be towards Xiongshan, south of the "
                      "town, but deeply hidden; never found"),
         Record(OHASHI, "我砲兵中最大射程をもつ九六式十五榴が敵前ギリギリ（運河より前えは出られない）まで陣地を"
                "推進しても、敵の砲兵陣地まではとどかない", quote=True,
                label="even the Type 96, pushed up to the canal, could not reach them; the "
                      "author calls his sketch exaggerated"),
         Record(KRZ_SFH, "炮10团1营一个连2门sFH18 150毫米榴弹炮赶赴到台儿庄运河南岸", quote=True,
                label="on the canal's south bank"),
         Record(SAS, "砲數ハ二門或ハ三門ノ事多シ…陣地ハ屢々變換スル事多シ", quote=True,
                label="the Type 96 company's lessons: enemy batteries of two or three guns, "
                      "often changing position")),
        "South of Xiongshan, about 13 km from the Japanese guns at Sanlizhuang, within 5 km",
        "In the direction the Japanese saw the rounds come from, and beyond the reach of "
        "every Japanese gun from its position, as Ohashi remembered; within the 15 km that reaches "
        "Liujiahu and Sanlizhuang, where the rounds fell.", shown="30 01:50",
        brief="No record says where the two Chinese 15 cm howitzers stood. The replay puts "
              "them south of Xiongshan, where the Japanese thought they were, beyond the reach "
              "of every Japanese gun."),
    "sfh-count": Dispute(
        "How many 15 cm howitzers the Chinese had at Taierzhuang", "SFH",
        (Record(OHASHI, "僅か二門のラインメタルに我が全砲兵（野砲一大隊、四年式十五榴一大隊、九六式十五榴一中隊）"
                "が完全に制圧される", quote=True),
         Record(KRZ_SFH, "炮10团1营一个连2门", quote=True),
         Record(ZHWIKI_SFH, "拥有7门炮的一营最先被配给汤恩伯第20军团", quote=True)),
        "Two", "The Japanese artillery officer and the Chinese account agree on two at the "
        "canal; the battalion's seven were split between the canal and Tang Enbo's corps.",
        shown="30 01:45"),
    "what-the-japanese-saw": Dispute(
        "What the Japanese took the 15 cm guns for", "CN 15CM ROUNDS",
        (Record(J10, "十五加ヲ有シ且良好ナル台児庄南岸ノ観測地帯ヲ有スル", quote=True,
                label="15 cm cannon and a good observation zone on the south bank"),
         Record(J63, "十五糎加農級ノ砲彈", quote=True, label="1 April"),
         Record(OHASHI, "ラインメタル式十五榴", quote=True)),
        "The Rheinmetall 15 cm howitzer, sFH 18/32L", "Its 32-calibre barrel and 15 km reach, "
        "longer than any Japanese howitzer's, made it look like a cannon to those it fired "
        "on.", shown="1 09:30"),
}
