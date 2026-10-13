"""Sunday night: Stevens's party in the country, the express held at the bridge and Heyward
Shepherd."""
from ledger import Dispute, Moment, Record

from .names import ANDERSON, DEWITT, DREW, HINTON, LEE, MASON, NPS, SHEP_REG, VILLARD, WP

MOMENTS = {
    "allstadt-taken": Moment(
        "John H. Allstadt and his slaves seized", "STEVENS", "17 03:00",
        (Record(MASON, "There was a party of men came there on the 17th of October, at three "
                "o'clock in the morning.", "17 03:00", quote=True, label="John H. Allstadt"),
         Record(LEE, "Mr. J.H. Allstadt and six of his servants were in the same manner seized "
                "about 3 a.m.", "17 03:00", quote=True))),
}

DISPUTES = {
    "hostage-party": Dispute(
        "Who went with Stevens to take hostages", "STEVENS",
        (Record(ANDERSON, "The men selected by Col. Stevens to act under his orders during the "
                "night were Charles P. Tidd, Osborne P. Anderson, Shields Green, John E. Cook, "
                "and Sherrard Lewis Leary.", quote=True),
         Record(HINTON, "Charles P. Tidd, John E. Cook, Osborne P. Anderson, Lewis Sherrard "
                "Leary, and John A. Copeland", quote=True, label="p. 283"),
         Record(MASON, "The party consisted of Stevens, Cook, Tidd, Taylor, and the negro man "
                "Shields Green. There was a sixth man whom I did not see; but Cook afterwards "
                "told me his name was Meriam.", quote=True, label="Lewis W. Washington"),
         Record(LEE, "They then dispatched six men, under one of their party, called Captain "
                "Aaron C. Stevens", quote=True),
         Record(WP, "Brown detached a party under John Cook, Jr., to capture Colonel Lewis "
                "Washington", quote=True)),
        "Stevens with Tidd, Cook, Osborne Anderson, Shields Green and Leary", "Anderson was one "
        "of them. Washington learned the names afterwards, and his Taylor and Meriam were at the "
        "bridge and the farm in Anderson's account.", shown="16 23:40"),
    "washington-taken": Dispute(
        "When Lewis W. Washington was seized at Beall-Air", "STEVENS",
        (Record(MASON, "They appeared at my chamber door about half past one o'clock in the "
                "morning.", "17 01:30", quote=True, label="Lewis W. Washington"),
         Record(LEE, "The party took Colonel L.W. Washington from his bed about 1 a.m. on the "
                "17th", "17 01:00", quote=True),
         Record(VILLARD, "It was at midnight that Colonel Washington was awakened by four armed "
                "men", "17 00:00", quote=True),
         Record(NPS, "12:00 am Enslavers Lewis Washington and John Allstadt are taken hostage",
                "17 00:00", quote=True)),
        "Half past one", "Washington's own testimony. The party left the armory once the town "
        "was taken, and Beall-Air is five miles out by the pike: a walk that ends nearer half "
        "past one than midnight.", at="17 01:30"),
    "hostages-reach-the-armory": Dispute(
        "When the hostages reached the armory", "STEVENS",
        (Record(MASON, "I suppose about half past three; some time before daylight on Monday "
                "morning.", "17 03:30", quote=True, label="Lewis W. Washington"),
         Record(VILLARD, "We arrived at the Armory just about daybreak.", quote=True,
                label="John Thomas Allstadt"),
         Record(MASON, "About four o'clock I heard a wagon coming down the street", "17 04:00",
                quote=True, label="Dr. John D. Starry"),
         Record(DEWITT, "at about 4 o'clock saw a wagon driven in the yard", "17 04:00",
                quote=True, label="conductor Phelps at Brown's trial")),
        "Four o'clock", "Starry and Phelps, who were awake in the town, both heard or saw the "
        "wagon at about four.", at="17 04:00"),
    "express-arrives": Dispute(
        "When the eastbound express reached the bridge", "EXPRESS",
        (Record(DEWITT, "my train arrived at 1.25, bound east; saw no watchman at the bridge",
                "17 01:25", quote=True, label="Phelps at Brown's trial"),
         Record(MASON, "arrived at Harper's Ferry at its usual hour, about half past one o'clock "
                "in the morning.", "17 01:30", quote=True, label="the Report"),
         Record(SHEP_REG, "reached a point near the bridge at Harper's Ferry at 20 minutes of one "
                "o'clock this morning, when it was stopped.", "17 00:40", quote=True,
                label="the Baltimore American"),
         Record(DREW, "The express train, in which our informant was passenger, reached Harper's "
                "Ferry about 1 o'clock this morning.", "17 01:00", quote=True),
         Record(WP, "About 1:15 AM the eastbound Baltimore & Ohio express train from Wheeling",
                "17 01:15", quote=True)),
        "1:25", "The conductor's sworn time, which the Park Service also gives.",
        at="17 01:25"),
    "shepherd-shot": Dispute(
        "When Heyward Shepherd was shot", "STATION",
        (Record(MASON, "about half past one o'clock, I heard a shot fired in the direction of "
                "the Baltimore and Ohio railroad bridge, the iron span of the bridge, and "
                "immediately afterwards a cry of distress", "17 01:30", quote=True,
                label="Dr. John D. Starry"),
         Record(DEWITT, "as I got on the tresseling, I heard the report of a gun, and Hayward, "
                "the colored man, came running to me, and said, 'Captain, I am shot;'",
                quote=True, label="Phelps at Brown's trial"),
         Record(ANDERSON, "He was ordered to stop by the sentinels stationed at the bridge, "
                "which he refused to do, but turned to go in an opposite direction, when he was "
                "fired upon, and received a mortal wound.", quote=True),
         Record(HINTON, "Just as the train was leaving, Cook recrossed the bridge ... Heyward "
                "Shepherd, the Hotel porter, was shot soon after.", quote=True)),
        "About half past one, while the train was held", "Starry heard the shot and treated "
        "Shepherd; the conductor, Anderson and Starry all put it before the train left. Hinton, "
        "writing in 1894, alone puts it after.", at="17 01:30"),
}
