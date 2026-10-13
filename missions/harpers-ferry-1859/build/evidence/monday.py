"""Monday 17 October in the town: the militia take the bridges and the raiders fall back on the
engine house."""
from ledger import Dispute, Moment, Record

from .names import ANDERSON, DEWITT, HINTON, LEE, MASON, NPS, NPS_HS, VILLARD

MOMENTS = {
    "boerley-killed": Moment(
        "Thomas Boerley killed", "CITIZENS", "17 07:00",
        (Record(MASON, "When I got on the hill, I learned that they had shot Boerley. That was "
                "probably about 7 o'clock.", "17 07:00", quote=True, label="Dr. John D. Starry"),
         Record(NPS, "7:00 am Townspeople begin firing on the raiders. Groceryman Thomas Boerly "
                "is killed by return fire.", "17 07:00", quote=True))),
    "leeman-killed": Moment(
        "William Leeman shot in the Potomac", "LEEMAN", "17 13:00",
        (Record(MASON, "I saw a man shot in the Potomac river on Monday, I suppose about one "
                "o'clock.", "17 13:00", quote=True, label="Dr. John D. Starry"),
         Record(VILLARD, "the death, about one o'clock in the afternoon, of William H. Leeman",
                "17 13:00", quote=True),
         Record(NPS, "1:00 pm Raider William Leeman is killed as he attempts to escape across "
                "the Potomac River.", "17 13:00", quote=True))),
    "martinsburg-company-frees-the-prisoners": Moment(
        "The Martinsburg company frees the prisoners in the watch-house", "MARTINSBURG COMPANY",
        "17 15:00",
        (Record(MASON, "About three o'clock on Monday", "17 15:00", quote=True,
                label="Daniel Whelan, of his release"),
         Record(NPS, "3:00 pm At the Armory, militiamen free most of the hostages and force "
                "Brown and his men into the engine house.", "17 15:00", quote=True),
         Record(VILLARD, "we found in the room adjoining the engine-house some thirty or forty "
                "prisoners ... The windows were broken open by our party, and these men "
                "escaped", quote=True, label="Capt. E. G. Alburtis"))),
}

DISPUTES = {
    "jefferson-guards-take-the-bridge": Dispute(
        "When the Jefferson Guards took the Potomac bridge", "JEFFERSON GUARDS",
        (Record(LEE, "About 11 a.m. the volunteer companies from Virginia began to arrive, and "
                "the Jefferson Guards and volunteers from Charlestown, under Captain J.W. Rowen, "
                "I understood, were first on the ground.", "17 11:00", quote=True),
         Record(VILLARD, "It was about noon that the Jefferson Guards reached the Maryland end "
                "of the Potomac bridge.", "17 12:00", quote=True),
         Record(ANDERSON, "It was about twelve o'clock in the day when we were first attacked by "
                "the troops.", "17 12:00", quote=True),
         Record(DEWITT, "At about noon, the Charlestown troops, under command of Colonel Robert "
                "W. Baylor, crossed the Susquehanna River [sic] some distance up, and marched "
                "down the Maryland side to the mouth of the bridge", "17 12:00", quote=True)),
        "Noon at the bridge, after reaching the heights at eleven", "Lee's eleven is their "
        "arrival on the ground, before they crossed the Potomac above the town and marched down "
        "the Maryland bank (Villard).", at="17 12:00"),
    "newby-killed": Dispute(
        "When and where Dangerfield Newby was killed", "NEWBY",
        (Record(VILLARD, "Mr. Washington shot and instantly killed Dangerfield Newby, who, with "
                "William Thompson and Oliver Brown, had been driven off the bridge by the "
                "Jefferson Guards and was fleeing back to the armory. Newby was thus the first "
                "to die of John Brown's men", quote=True),
         Record(ANDERSON, "was shot through the head by a person who took aim at him from a "
                "brick store window, on the opposite side of the street", quote=True),
         Record(DEWITT, "A light mulatto was shot just outside the Armory gate.", quote=True),
         Record(NPS, "10:00 am … Dangerfield Newby is shot", "17 10:00", quote=True)),
        "Just after noon, outside the armory gate", "Villard and Anderson put it after the "
        "Jefferson Guards' attack at noon, Villard as Newby ran back from the bridge; the Park "
        "Service's ten o'clock is earlier than the attack it follows.", at="17 12:06",
        outside=True),
    "flags-of-truce": Dispute(
        "The flags of truce", "WATSON",
        (Record(VILLARD, "at Brown's request, a prisoner named Cross went out with William "
                "Thompson to stop the firing, with the sole result that Thompson fell into the "
                "hands of the enemy.", quote=True),
         Record(VILLARD, "Stevens fell, shot twice by George W. Chambers, a saloon-keeper, from "
                "a window in the Gait House", quote=True),
         Record(ANDERSON, "he was fired upon, and wounded severely. He returned to the engine "
                "house, and fought bravely after that for fully and hour and a half",
                quote=True, label="of Watson Brown"),
         Record(NPS, "10:00 am … William Thompson is captured under a white flag", "17 10:00",
                quote=True),
         Record(NPS, "Noon Raiders Watson Brown and Aaron Stevens are shot while carrying a "
                "second flag of truce.", "17 12:00", quote=True)),
        "Thompson taken at twenty past twelve; Watson Brown and Stevens shot at half past",
        "Villard's order: the flags went out after Brown had withdrawn into the engine house at "
        "noon.", at="17 12:32", outside=True),
    "beckham-killed": Dispute(
        "When the mayor, Fontaine Beckham, was killed", "E COPPOC",
        (Record(MASON, "Beckham was the last shot, about four o'clock in the evening.",
                "17 16:00", quote=True, label="Dr. John D. Starry"),
         Record(MASON, "He was killed on the trusseling just above the hotel and near the water "
                "station; he was shot from the engine-house in the armory-yard.", quote=True,
                label="George W. Chambers"),
         Record(VILLARD, "Coppoc fired, but missed … But Coppoc was already firing again. This "
                "shot killed Beckham.", quote=True, label="John Thomas Allstadt"),
         Record(NPS, "2:00 pm", "17 14:00", quote=True, label="the entry for Beckham's death")),
        "A quarter to three", "Villard puts the Martinsburg company's attack just after "
        "Beckham's death, and Whelan, whom it freed, says about three.", at="17 14:45",
        brief="When the mayor was killed is disputed, between two and four; the replay puts it "
              "just before the Martinsburg company's attack at three, as Villard orders them."),
    "rifle-works-stormed": Dispute(
        "When the rifle works were stormed", "KAGI",
        (Record(MASON, "I organized a party about half past two or three o'clock, and sent them "
                "over there", "17 14:30", "17 15:00", quote=True, label="Dr. John D. Starry"),
         Record(MASON, "I went to put on some dry clothes on at half past three o'clock, and "
                "that fight was then over.", "17 15:30", quote=True,
                label="Dr. John D. Starry"),
         Record(NPS, "2:00 pm Citizens storm the U.S. Rifle Works.", "17 14:00", quote=True)),
        "Three o'clock", "Starry organised the attack.", at="17 15:00"),
    "anderson-and-hazlett-escape": Dispute(
        "When Osborne Anderson and Albert Hazlett left the arsenal", "HAZLETT",
        (Record(ANDERSON, "Captain Hazlett and myself being in the Arsenal opposite, saw the "
                "charge upon the engine house with the ladder", quote=True),
         Record(VILLARD, "In all probability they left their posts in the arsenal about "
                "nightfall on Monday", quote=True),
         Record(NPS, "Raiders Albert Hazlett and Osborne Anderson, overlooked by townspeople, "
                "leave the Arsenal and escape across the Potomac River.", quote=True,
                label="the entry for dark on Monday"),
         Record(ANDERSON, "about two o'clock in the morning", quote=True,
                label="of their arrival at the schoolhouse")),
        "At nightfall on Monday", "Anderson's own account has the marines at the engine house "
        "on Monday; Villard and the Park Service put the escape at dark.", at="17 17:30",
        outside=True,
        brief="Anderson wrote that he and Hazlett watched the marines' charge before slipping "
              "away; Villard thinks they left at nightfall on Monday, as the replay shows."),
    "schoolhouse-site": Dispute(
        "Where the schoolhouse stood", "SCHOOLHOUSE",
        (Record(MASON, "deposited in a school-house about a mile from the village of Harper's "
                "Ferry, on the Maryland side.", quote=True, label="the Report"),
         Record(ANDERSON, "the school-house in the mountains, three-fourths of a mile from the "
                "Ferry.", quote=True),
         Record(NPS_HS, "midway between Harpers Ferry and the Kennedy farm", quote=True),
         Record(HINTON, "I hurried on till I came to the lock kept by George Hardy, about a mile "
                "above the bridge", quote=True,
                label="Cook's confession, going down from the schoolhouse")),
        "On the road above Lock 34, about two kilometres from the bridge, within 1.5 km",
        "Cook passed Hardy's lock, a mile above the bridge, below the schoolhouse; the road "
        "the arms came down from the farm runs past it. No marker stands there.",
        shown="17 09:15"),
}
