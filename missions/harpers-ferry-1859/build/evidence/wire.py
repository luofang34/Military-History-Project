"""Monday morning: the express released, Phelps's telegrams and the railroad's alarm, and the
troops it carried by night."""
from ledger import Dispute, Moment, Record

from .names import (ANDERSON, BO_1859, DOC_Y, DREW, GREENE, HUNGERFORD, MASON, NPS, SHEP_REG,
                    VILLARD, WP, DEWITT)

MOMENTS = {
    "phelps-telegraphs-from-monocacy": Moment(
        "Phelps telegraphs from Monocacy", "EXPRESS", "17 07:05",
        (Record(DOC_Y, "Express train bound east, under my charge, was stopped this morning at "
                "Harper's Ferry by armed abolitionists. They have possession of the bridge and "
                "the arms and armory of the United States.", "17 07:05", quote=True,
                label="Phelps to W. P. Smith, \"Monocacy, 7.05 A. M., October 17, 1859\""),
         Record(VILLARD, "At 7.05 A. M., Phelps arrived at Monocacy and telegraphed", "17 07:05",
                quote=True))),
    "smith-doubts-the-news": Moment(
        "The master of transportation doubts the news", "CAMDEN STATION", "17 09:00",
        (Record(DOC_Y, "Your despatch is evidently exaggerated and written under excitement. Why "
                "should our trains be stopped by Abolitionists, and how do you know they are "
                "such and that they number one hundred or more? What is their object? Let me "
                "know at once before we proceed to extremities.", "17 09:00", quote=True,
                label="W. P. Smith to Phelps, 9 a.m."),)),
    "garrett-alerts-the-president": Moment(
        "The B&O's president telegraphs President Buchanan", "CAMDEN STATION", "17 10:30",
        (Record(DOC_Y, "The United States Armory at Harper's Ferry is in the possession of "
                "rioters. The wires are cut west of Frederick. The officers of the mail train "
                "have been fired on and one man fatally wounded. You may rely on this.",
                "17 10:30", quote=True,
                label="John W. Garrett to Buchanan, \"Baltimore, Oct. 17th—10.30 A. M.\""),
         Record(VILLARD, "At half-past ten he had telegraphed to the President of the United "
                "States, to Governor Wise, of Virginia, and to Major-General George H. Stewart",
                "17 10:30", quote=True))),
    "phelps-insists": Moment(
        "Phelps answers from Ellicott's Mills", "EXPRESS", "17 11:00",
        (Record(DOC_Y, "My dispatch was not exaggerated, neither was it written under "
                "excitement as you suppose. I have not made it half as bad as it is.",
                "17 11:00", quote=True, label="Phelps, Ellicott's Mills, 11 a.m."),)),
    "buchanan-answers": Moment(
        "President Buchanan answers the railroad", None, "17 13:30",
        (Record(DOC_Y, "Your dispatch has been received, and it shall be promptly attended to.",
                "17 13:30", quote=True,
                label="Buchanan to Garrett, \"Washington, Oct. 17th, 1859—1.30 P. M.\""),)),
    "marines-leave-washington": Moment(
        "The marines leave Washington by train", "MARINES", "17 15:30",
        (Record(GREENE, "With a detachment of ninety marines, I started for Harper's Ferry that "
                "afternoon on the 3:30 train, taking with me two howitzers.", "17 15:30",
                quote=True),
         Record(WP, "The Marines left for Harper's Ferry on the regular 3:30 train, arriving "
                "about 10 PM.", "17 15:30", quote=True))),
    "troop-train-at-monocacy": Moment(
        "The troop train from Baltimore reaches Monocacy", "BALTIMORE MILITIA", "17 20:10",
        (Record(DOC_Y, "Arrived here 8.10, moving cautiously with sixteen cars.", "17 20:10",
                quote=True, label="W. P. Smith, \"Monocacy, 9.15 P. M., October 17, 1859\""),)),
}

DISPUTES = {
    "express-released": Dispute(
        "When the express was let go", "EXPRESS",
        (Record(DOC_Y, "When daylight appeared we were finally permitted to pass, after being "
                "detained from half-past one o'clock to half-past six.", "17 06:30",
                quote=True, label="Phelps, from Monocacy at 7.05 a.m."),
         Record(SHEP_REG, "The train was delayed by the proceedings until half-past six o'clock",
                "17 06:30", quote=True, label="the Baltimore American"),
         Record(DREW, "Capt. P.'s train left at six, having been detained five hours at the "
                "Ferry.", "17 06:00", quote=True, label="the Baltimore Patriot, 17 October"),
         Record(DREW, "About five or half-past five o'clock this morning the deputation of armed "
                "insurgents approached the conductor and gave him five minutes to start his "
                "train and cross the bridge.", "17 05:00", "17 05:30", quote=True,
                label="a passenger"),
         Record(HUNGERFORD, "At five in the morning, dawn faintly began to show. Phelps then "
                "decided to go forward.", "17 05:00", quote=True),
         Record(ANDERSON, "directly after sunrise, the detained train was permitted to start "
                "for the eastward.", quote=True),
         Record(BO_1859, "of passenger trains to twenty and twenty-five miles per hour",
                quote=True, label="the speed limit introduced in the year to September 1859")),
        "Six o'clock", "Phelps telegraphed from Monocacy, 23 miles east, at 7.05. Leaving at "
        "half past six the train would have had to run at 41 mph; leaving at six it runs at 23, "
        "within the railroad's own limit, as the Patriot's six has it. The build fails if the "
        "express runs faster than 25 mph.", at="17 06:00",
        brief="The conductor wrote that he was held until half past six. The replay lets the "
              "train go at six: leaving later, it could not have reached Monocacy by 7.05 "
              "within the railroad's 25 mph limit."),
    "lee-arrives": Dispute(
        "When Colonel Lee arrived", "LEE",
        (Record(GREENE, "At ten o'clock in the evening he came upon a special train from "
                "Washington.", "17 22:00", quote=True),
         Record(DOC_Y, "Arrived at Sandy Hook before 11, and car with Col. Lee arrived soon "
                "after.", "17 23:00", quote=True,
                label="W. P. Smith, \"Harper's Ferry, October 18, 1859 ... 12 midnight\""),
         Record(NPS, "11:00 pm Colonel Robert E. Lee and 90 U.S. Marines arrive by train from "
                "Washington.", "17 23:00", quote=True),
         Record(DEWITT, "About twelve o'clock, Colonel Lee arrived, having under his command "
                "eighty-five marines", "18 00:00", quote=True, label="Col. R. W. Baylor"),
         Record(MASON, "I did not reach the Ferry until about eleven or twelve o'clock on Monday "
                "night", "17 23:00", "18 00:00", quote=True, label="Lee")),
        "Sandy Hook soon after eleven; the marines in the armory yard before midnight",
        "Smith's telegram of that midnight, written where Lee arrived. Greene's times on that "
        "night run an hour ahead of every other record.", at="17 23:05"),
    "marine-strength": Dispute(
        "How many marines came", "MARINES",
        (Record(GREENE, "I instantly replied to Mr. Walsh that we had ninety men available",
                quote=True),
         Record(DEWITT, "eighty-five marines", quote=True, label="Col. R. W. Baylor"),
         Record(WP, "81 privates, 11 sergeants, 13 corporals, and 1 bugler", quote=True),
         Record(NPS, "90 U.S. Marines", quote=True)),
        "Ninety", "Greene commanded them.", shown="17 23:50"),
}
