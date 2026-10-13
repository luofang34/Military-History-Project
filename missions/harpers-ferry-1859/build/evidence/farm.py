"""Sunday at the Kennedy farm, the march down the Maryland road and the bridge."""
from ledger import Dispute, Moment, Record

from .names import ANDERSON, DEWITT, DOC_Y, HINTON, LEE, MASON, NPS, NPS_HS, VILLARD, WP

MOMENTS = {
    "kennedy-farm-council": Moment(
        "The council at the Kennedy farm", None, "16 10:00",
        (Record(ANDERSON, "At 10 o'clock, the council was assembled. I was appointed to the "
                "Chair", "16 10:00", quote=True),
         Record(ANDERSON, "After the council adjourned, the Constitution was read for the "
                "benefit of the few who had not before heard it, and the necessary oaths taken.",
                quote=True))),
    "armory-watchman-taken": Moment(
        "Daniel Whelan, the armory watchman, taken at the gate", "BROWN", "16 22:45",
        (Record(MASON, "To the best of my knowledge it was a quarter before eleven o'clock on "
                "Sunday night, the 16th of October.", "16 22:45", quote=True,
                label="Daniel Whelan"),
         Record(MASON, "I came here from Kansas, and this is a slave State; I want to free all "
                "the negroes in this State; I have possession now of the United States armory, "
                "and if the citizens interfere with me, I must only burn the town and have "
                "blood.", quote=True, label="Whelan, quoting Brown"))),
}

DISPUTES = {
    "march-from-the-farm": Dispute(
        "When the march left the Kennedy farm", "BROWN",
        (Record(ANDERSON, "At eight o'clock on Sunday evening, Captain Brown said: \"Men, get on "
                "your arms; we will proceed to the Ferry.\"", "16 20:00", quote=True),
         Record(NPS, "8:00 pm Brown and 18 of his men advance towards Harpers Ferry.",
                "16 20:00", quote=True),
         Record(WP, "On Sunday night, October 16, 1859, at about 11 PM, Brown left three of his "
                "men behind as a rear-guard", "16 23:00", quote=True)),
        "Eight o'clock", "Anderson marched with Brown. Wikipedia's eleven is the time Lee and "
        "the Mason Report give for the seizure of the bridge, after a walk of more than two "
        "hours (National Park Service).", at="16 20:00"),
    "bridge-taken": Dispute(
        "When the raiders took the Potomac bridge", "KAGI",
        (Record(VILLARD, "It was half-past ten when Kagi and Stevens, as advance guard, entered "
                "the Maryland bridge and made William Williams, the watchman, their prisoner.",
                "16 22:30", quote=True),
         Record(NPS_HS, "About 10:30 p.m.", "16 22:30", quote=True,
                label="the march reaches the B&O bridge"),
         Record(DEWITT, "The first active movement in the insurrection was made about a half "
                "past ten o'clock on Sunday night.", "16 22:30", quote=True),
         Record(HINTON, "The capture of the place was effected before eleven on the 16th.",
                quote=True),
         Record(LEE, "a party of insurgents, about 11 p.m. on the 16th, had seized the watchmen "
                "stationed at the armory, rifle factory, and bridge across the Potomac",
                "16 23:00", quote=True),
         Record(MASON, "between 11 and 12 o'clock at night", "16 23:00", "17 00:00",
                quote=True, label="the Report, of the crossing")),
        "Half past ten", "Three accounts agree on half past ten, and Whelan, at the armory gate "
        "beyond the bridge, swore to a quarter to eleven; Lee was not there.", at="16 22:30"),
    "potomac-bridge-guard": Dispute(
        "Who held the Potomac bridge", "WATSON",
        (Record(ANDERSON, "Captain Watson Brown and Stewart Taylor were to take positions at the "
                "Potomac bridge, and hold it till morning.", quote=True, label="order sixth"),
         Record(ANDERSON, "Captains Oliver Brown and William Thompson were to execute a similar "
                "order at the Shenandoah bridge, until morning.", quote=True,
                label="order seventh"),
         Record(HINTON, "he was seized by one (Oliver Brown, he afterwards learned)", quote=True,
                label="the relief watchman Patrick Higgins, at midnight"),
         Record(NPS_HS, "answered quietly by Taylor and Watson Brown", quote=True,
                label="of Higgins at the bridge"),
         Record(VILLARD, "They quickly drove from it Oliver Brown and the rest of the guard",
                quote=True, label="the Jefferson Guards at the bridge, about noon"),
         Record(MASON, "I passed two armed men on the bridge -- a white man and a colored man. I "
                "think the white man was a son of Brown", quote=True,
                label="Terence Byrne, between nine and ten on Monday")),
        "Watson Brown and Stewart Taylor by night, as ordered; Oliver Brown, William Thompson "
        "and Dangerfield Newby by Monday morning", "Anderson gives Brown's orders as written; "
        "Byrne and Villard find Oliver Brown and a Black man, Newby, on the bridge on Monday. "
        "Higgins's memory of striking Oliver Brown at midnight is the one record that does not "
        "fit, and the replay does not follow it.", shown="16 22:33",
        brief="Who guarded the Potomac bridge is disputed: Brown's orders put Watson Brown and "
              "Stewart Taylor there for the night, but by Monday Oliver Brown held it."),
    "telegraph-cut": Dispute(
        "Where and when the telegraph was cut", "WIRE EAST",
        (Record(ANDERSON, "That Captains Charles P. Tidd and John E. Cook walk ahead of the "
                "wagon in which Captain Brown rode to the Ferry, to tear down the telegraph "
                "wires on the Maryland side along the railroad; and to do the same on the "
                "Virginia side, after the town should be captured.", quote=True,
                label="order fourth"),
         Record(HINTON, "Cook and Tidd were so busily engaged in cutting the telegraph wires "
                "along the road that they had no time to think.", quote=True),
         Record(DOC_Y, "The telegraph wires are cut East and West of Harper's Ferry, and this is "
                "the first station that I could send a despatch from.", quote=True,
                label="Phelps, from Monocacy at 7.05 a.m."),
         Record(DOC_Y, "The wires are cut between Frederick and Harper's Ferry.", quote=True,
                label="Garrett to Governor Wise, 10½ a.m."),
         Record(DOC_Y, "the telegraph wires are cut, no communication east.", quote=True,
                label="A. Diffey, from Martinsburg via Wheeling"),
         Record(WP, "They cut the telegraph line twice, to prevent communication in either "
                "direction: first on the Maryland side of the bridge; slightly later on the far "
                "side of the station, preventing communication with Virginia.", quote=True)),
        "The line east cut by Cook and Tidd on the Maryland bank beside the bridge, at about "
        "22:24; the line west on the Virginia bank above the armory, at about 23:05",
        "No source gives a time or a distance from town. The line ran along the railroad "
        "(Anderson), which on the Maryland side leaves the bridge downstream; the road the "
        "march came by meets it only at the bridge, so the east cut is placed there as the "
        "column arrives, and the west cut once the armory is taken.", at="16 22:24",
        outside=True,
        brief="No source says where Cook and Tidd cut the wires, or when; the replay cuts the "
              "line east as the column reaches the bridge, and the line west once the town is "
              "taken."),
}
