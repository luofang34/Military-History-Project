"""Chapters, briefings and pacing for the raid, on the Harpers Ferry clock (sites.L)."""
from composition import INTENTS
from evidence import DISPUTES
from pacing import after_viewing
from sites import DURATION, L

CHAPTERS = [
    ("Sunday at the Kennedy farm", "16 14:30"),
    ("\"Men, get on your arms\"", "16 20:00"),
    ("Wires cut, the bridge and the armory taken", "16 22:18"),
    ("Hostages from the country", "16 23:40"),
    ("The express and Heyward Shepherd", "17 01:20"),
    ("The train goes east with the news", "17 05:50"),
    ("The railroad raises the alarm", "17 07:03"),
    ("The militia take the bridge", "17 10:40"),
    ("The engine house", "17 12:20"),
    ("Beckham, the rifle works, the watch-house", "17 14:35"),
    ("Troops by rail", "17 17:50"),
    ("Lee and the marines", "17 22:40"),
    ("The storming of the engine house", "18 06:56:30"),
]

# (from, until, speed); every still stretch plays at most six seconds.
PACING = [
    ("16 14:30", "16 20:00", 4096),
    ("16 20:00", "16 22:15", 200),
    ("16 22:15", "16 22:50", 45),
    ("16 22:50", "16 23:40", 120),
    ("16 23:40", "17 01:20", 360),
    ("17 01:20", "17 01:34", 25),
    ("17 01:34", "17 02:30", 180),
    ("17 02:30", "17 04:05", 240),
    ("17 04:05", "17 04:55", 900),
    ("17 04:55", "17 05:50", 300),
    ("17 05:50", "17 06:15", 40),
    ("17 06:15", "17 06:55", 150),
    ("17 06:55", "17 07:12", 40),
    ("17 07:12", "17 10:40", 360),
    ("17 10:40", "17 11:50", 200),
    ("17 11:50", "17 13:02", 60),
    ("17 13:02", "17 14:30", 2400),
    ("17 14:30", "17 15:30", 50),
    ("17 15:30", "17 17:20", 300),
    ("17 17:20", "17 17:50", 150),
    ("17 17:50", "17 18:30", 360),
    ("17 18:30", "17 22:40", 720),
    ("17 22:40", "17 23:55", 150),
    ("17 23:55", "18 06:56:30", 4096),
    ("18 06:56:30", "18 07:00:30", 25),
    ("18 07:00:30", "18 07:06", 12),
    ("18 07:06", "18 07:45", 120),
]

PLAQUE = "hmdb-151957"
ANDERSON = "anderson-1861"
MASON = "mason-report"
VILLARD = "villard-1910"
DEWITT = "dewitt-1859"
DOC_Y = "doc-y"
GREENE = "greene-1885"
LEE = "lee-report"

# (entity the note is about, or None for the whole operation; from, until, source, text)
BRIEFINGS = [
    (None, "16 14:30", "16 20:40", PLAQUE,
     "The Kennedy farm, Maryland, Sunday 16 October 1859: headquarters of the Provisional Army "
     "of the United States of America, John Brown and 21 men, five of them "
     "Black, set to seize the armory at Harpers Ferry and free the enslaved."),
    ("KENNEDY FARM", "16 14:30", "16 21:00", ANDERSON,
     "This morning Brown's council met: his Provisional Constitution was read and oaths taken. "
     "This afternoon he gives eleven orders, one for each post."),
    ("BROWN", "16 20:00", "16 21:30", ANDERSON,
     "8 p.m.: \"Men, get on your arms; we will proceed to the Ferry.\" Brown rides the wagon; "
     "the men walk behind in pairs. Owen Brown, Barclay Coppoc and Francis Meriam stay with the "
     "arms."),
    (None, "16 21:00", "16 21:55", VILLARD,
     "Since July Brown had lived here as \"Isaac Smith\"; the rifles and pikes came in crates "
     "of \"Hardware & Castings\". His daughter Annie and Oliver's wife Martha kept house and "
     "watch until late September."),
    (None, "16 21:55", "16 22:30", "douglass-life",
     "In August Frederick Douglass met Brown in a quarry near Chambersburg and would not join: "
     "Brown was \"going into a perfect steel-trap\". Shields Green, who came with Douglass, went "
     "with Brown."),
    ("TIDD", "16 22:20", "16 22:40", ANDERSON,
     "Walking ahead, John Cook and Charles Tidd cut the telegraph on the Maryland side, along "
     "the railroad."),
    ("KAGI", "16 22:29", "16 22:50", VILLARD,
     "About 10:30: Kagi and Aaron Stevens enter the covered bridge and take the watchman, "
     "William Williams. The bridge stood where its piers still stand, below today's."),
    ("BROWN", "16 22:41", "16 23:10", MASON,
     "10:45: at the armory gate the watchman Daniel Whelan will not give up the key; the chain "
     "is twisted off with a crowbar. Brown to Whelan: \"I want to free all the negroes in this "
     "State\"."),
    (None, "16 22:50", "16 23:30", ANDERSON,
     "Without a shot fired the raiders take the arsenal across the street, the Shenandoah "
     "bridge and Hall's rifle works half a mile up the Shenandoah, where Kagi and John Copeland "
     "stay."),
    ("COOK", "16 23:00", "16 23:40", ANDERSON,
     "Cook and Tidd cut the line west, on the Virginia side. Harpers Ferry's telegraph is dead "
     "in both directions."),
    ("STEVENS", "16 23:40", "17 00:30", ANDERSON,
     "Stevens leads five men out the Charlestown pike to seize two slaveholders as hostages and "
     "free their slaves: Col. Lewis W. Washington of Beall-Air and John H. Allstadt."),
    ("WATSON", "17 00:00", "17 01:15", "hinton-1894",
     "Midnight: Patrick Higgins comes to relieve the bridge watchman. Stopped by the guards, he "
     "strikes one and runs; a shot grazes his scalp."),
    ("EXPRESS", "17 01:24", "17 01:31", DEWITT,
     "1:25: the eastbound express from Wheeling reaches the bridge. Conductor A. J. Phelps finds "
     "no watchman and rifles in the bridge, and backs his train."),
    ("STATION", "17 01:30", "17 02:20", MASON,
     "Heyward Shepherd, the free Black baggage master at the station, walks onto the bridge to "
     "look for the watchman and is shot in the back. He dies the next afternoon."),
    ("STEVENS", "17 01:34", "17 02:30", MASON,
     "1:30: Washington is woken by armed men with a torch. As Brown ordered, he must hand his "
     "sword, said to be Frederick the Great's gift to George Washington, to Osborne Anderson, a "
     "free Black man."),
    ("STEVENS", "17 02:58", "17 03:40", MASON,
     "3:00: Allstadt, his son and his slaves are taken. The prisoners ride back in "
     "Washington's carriage and farm wagon."),
    ("BROWN", "17 04:00", "17 05:20", DEWITT,
     "4:00: the hostages reach the armory and are held in the watch-house. Brown sends word that "
     "the express may pass; Phelps will not cross before daylight."),
    ("COOK", "17 05:00", "17 05:55", MASON,
     "5:05: Cook, Tidd and William Leeman drive Washington's four-horse wagon over the bridge to "
     "bring the arms down from the farm."),
    ("BROWN", "17 05:55", "17 06:15", DEWITT,
     "Dawn: Brown walks over the bridge ahead of the train with Phelps: \"You doubtless wonder "
     "that a man of my age should be here with a band of armed men\". The express goes east "
     "with the news."),
    ("EXPRESS", "17 06:15", "17 06:55", "bo-annual-report-1859",
     "The express runs down the Potomac at the railroad's limit of 25 mph, past Sandy Hook, "
     "Berlin and Point of Rocks, to the first telegraph it can use."),
    ("CITIZENS", "17 06:55", "17 07:12", MASON,
     "In the town, armory workmen are taken as they come to work. Townsmen begin to shoot; the "
     "grocer Thomas Boerley is killed at about seven."),
    ("EXPRESS", "17 07:05", "17 08:00", DOC_Y,
     "7:05, Monocacy: Phelps telegraphs Baltimore: \"Express train bound east, under my charge, "
     "was stopped this morning at Harper's Ferry by armed abolitionists.\" He puts them at about "
     "150."),
    ("CAMDEN STATION", "17 09:00", "17 09:45", DOC_Y,
     "9:00, Baltimore: the master of transportation, W. P. Smith, answers: \"Your despatch is "
     "evidently exaggerated and written under excitement.\""),
    ("CAMDEN STATION", "17 10:30", "17 11:00", DOC_Y,
     "10:30: the B&O's president, John W. Garrett, telegraphs President Buchanan, Governor Wise "
     "of Virginia and Maryland's militia: \"You may rely on this.\""),
    ("EXPRESS", "17 11:00", "17 11:30", DOC_Y,
     "11:00, Ellicott's Mills: Phelps to Smith: \"I have not made it half as bad as it is.\""),
    ("JEFFERSON GUARDS", "17 11:00", "17 11:50", VILLARD,
     "Charlestown's Jefferson Guards come by train, cross the Potomac by boat above the town and "
     "march down the Maryland bank, the road the raiders came by."),
    ("JEFFERSON GUARDS", "17 12:00", "17 12:25", VILLARD,
     "Noon: the Guards take the bridge. Oliver Brown, William Thompson and Dangerfield Newby run "
     "for the armory; Newby, 44, is the first of Brown's men killed."),
    ("BROWN", "17 12:05", "17 12:40", MASON,
     "Brown moves into the fire-engine house with nine or ten of his most important hostages. "
     "The others stay in the watch-house next door."),
    ("WATSON", "17 12:30", "17 13:00", VILLARD,
     "Brown sends out flags of truce. William Thompson is seized; Watson Brown and Stevens are "
     "shot under the second. Watson crawls back; Stevens is taken."),
    ("LEEMAN", "17 12:52", "17 13:30", VILLARD,
     "About 1:00: Leeman runs from the upper end of the yard into the Potomac and is shot on a "
     "small island."),
    ("E COPPOC", "17 14:40", "17 15:05", MASON,
     "The mayor, Fontaine Beckham, is shot from the engine house near the railroad's water "
     "station. Townsmen then drag William Thompson onto the bridge and shoot him."),
    ("MARTINSBURG COMPANY", "17 14:58", "17 15:20", VILLARD,
     "3:00: a Martinsburg company of B&O railroad men under Capt. E. G. Alburtis attacks "
     "through the yard and frees the prisoners in the watch-house."),
    ("KAGI", "17 15:00", "17 15:30", MASON,
     "At the rifle works citizens drive out Kagi, Lewis Leary and Copeland. In the Shenandoah "
     "Kagi is killed, Leary mortally wounded, and Copeland taken on a rock."),
    ("BROWN", "17 15:30", "17 17:30", VILLARD,
     "In the engine-house doorway Stewart Taylor is killed and Oliver Brown shot; Oliver will die "
     "in the night. Brown holds out with about ten hostages and five or six men able to fight."),
    ("HAZLETT", "17 17:30", "17 18:30", VILLARD,
     "At dusk Albert Hazlett and Osborne Anderson slip out of the arsenal and get across the "
     "Potomac."),
    ("MARINES", "17 15:30", "17 17:50", GREENE,
     "3:30, Washington: Lt. Israel Greene leaves by train with ninety marines. Bvt. Col. Robert "
     "E. Lee will command, with Lt. J. E. B. Stuart as his aide."),
    ("FREDERICK MILITIA", "17 17:20", "17 19:00", LEE,
     "After sunset three companies from Frederick arrive. Militia and armed townsmen now "
     "surround the armory."),
    ("BALTIMORE MILITIA", "17 20:10", "17 21:30", DOC_Y,
     "8:10 p.m., Monocacy: the troop train from Baltimore, sixteen cars of militia and marines, "
     "\"moving cautiously\"; Lee follows in a special."),
    ("LEE", "17 23:05", "17 23:55", LEE,
     "Soon after eleven Lee reaches Sandy Hook and sends the marines into the armory yard. He "
     "waits for daylight, fearing for the hostages in \"a midnight assault\". By midnight the "
     "telegraph east works again, \"given up to reporters\"."),
    ("BROWN", "17 23:55", "18 06:56:30", VILLARD,
     "In the dark engine house: \"In the quiet of the night … young Oliver Brown died\" (John "
     "Thomas Allstadt, a hostage)."),
    ("STUART", "18 06:56:30", "18 07:00:30", "daingerfield-1885",
     "Daylight: Stuart carries Lee's summons to the door. Brown opens it a few inches and "
     "refuses: \"No! I prefer to die here.\" Stuart steps back and waves his cap."),
    ("STORMING PARTY", "18 07:00:30", "18 07:03", GREENE,
     "Sledge-hammers cannot break the roped doors; the marines batter them with a ladder. "
     "Private Luke Quinn is shot in the gap and dies."),
    ("BROWN", "18 07:02:40", "18 07:20", GREENE,
     "Greene cuts Brown down with his sword. Two raiders are bayoneted; Edwin Coppoc and Shields "
     "Green surrender. \"The whole fight had not lasted over three minutes.\""),
    (None, "18 07:20", "DURATION", PLAQUE,
     "Ten of Brown's men are dead or dying, five escape. Brown and six others are hanged; his "
     "last note: \"the crimes of this guilty land; will never be purged away; but with "
     "blood.\""),
]


READ_CPS = 20.0  # the reading speed tools/composition.py holds briefings to


def annotations(em):
    """Briefings, then each dispute's brief, shown for as long as it takes to read at the
    story's pace there; the records and the basis stay in build/evidence/ and the README."""
    for entity, start, until, source, text in BRIEFINGS:
        end = DURATION + 1 if until == "DURATION" else L(until)
        em.note(source, entity, L(start), end, text, "reported", [])
    for d in DISPUTES.values():
        if d.brief:
            at = max(0, L(d.when()))
            until = after_viewing(pacing(), at, len(d.brief) / READ_CPS + 2)
            em.note("reconstruction-estimate", d.entity, at, until, d.brief, "reconstructed", [])


def pacing():
    return [(L(a), L(b), s) for a, b, s in PACING]


def document(operation, cues, intents):
    return {
        "format": "sokoly-presentation",
        "version": 1,
        "id": "default",
        "name": "John Brown's raid on Harpers Ferry",
        "operation": operation,
        "chapters": [{"title": t, "at_ms": L(at), "available_ms": L(at)} for t, at in CHAPTERS],
        "camera_track": cues,
        "playback_track": [{"start_ms": a, "end_ms": b, "speed": s} for a, b, s in pacing()],
        "extensions": {INTENTS: intents},
    }
