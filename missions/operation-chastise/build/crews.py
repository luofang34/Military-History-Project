"""Crews as the 617 Squadron ORB lists them, spelling and punctuation as transcribed.

Each list follows the ORB's duty order: captain, flight engineer, navigator, wireless
operator, bomb aimer, front gunner, rear gunner. Fates are from dambustersblog's crew pages
and the ORB editor's notes.
"""
DUTIES = "Captain, F/Eng., Nav., W/Optr., A/B, F/Gunner, R/Gunner"

ORB_CREWS = {
    "AJ-G": ["W/Cmdr. G.P. GIBSON", "Sgt. J. PULFORD", "F/O. H.T. TAERUM",
             "F/Lt. R.E.G.HUTCHISON", "P/O. F.M. SPAFFORD", "F/Sgt.G.A.DEERING",
             "F/Lt. R.D.TREVOR ROPER"],
    "AJ-M": ["F/Lt. J.V. HOPGOOD", "Sgt. C. BRENNAN", "F/O. K. EARNSHAW", "Sgt. J. MINCHIN",
             "F/Sgt. J.W. FRASER", "P/O.G.H. GREGORY", "P/O. A.F. BURCHER"],
    "AJ-P": ["F/L. H.B. MARTIN", "P/O. I. WHITTAKER", "F/Lt. J.F. LEGGO", "F/O. L. CHAMBERS",
             "F/Lt. R.C. HAY", "P/O. B.T. FOXLEE", "F/Sgt. T.D. SIMPSON"],
    "AJ-A": ["S/Ldr. H.M. YOUNG", "Sgt. R. HORSFALL", "Sgt. C.W. ROBERTS", "Sgt. L. NICHOLS",
             "F/O. V.S. MACAUSLAND", "Sgt. A.G. YEO", "Sgt. L. IBBOTSON"],
    "AJ-J": ["F/Lt. D.J.H.MALTBY", "Sgt. J. HATTON", "Sgt. NICHOLSON V.", "Sgt. STONE A.J.",
             "P/O. J. FORT.", "Sgt. HILL E.", "Sgt. SIMMONS D."],
    "AJ-L": ["F/Lt. D.J. SHANNON.", "Sgt. HENDERSON R.", "F/O. F.R. WALKER.", "F/O. B. GOODALE.",
             "F/Sgt. L.J. SUMPTER.", "Sgt. JAGGER B.", "P/O. J. BUCKLEY."],
    "AJ-Z": ["S/Ldr. H.E. MAUDSLAY.", "Sgt. J. MARRIOTT.", "F/O. R.A. URQUHART.",
             "Sgt. R. COTTAM.", "P/O. M.J.D. FULLER.", "F/O. W.J. TYTHERLEIGH.",
             "Sgt. N.C. BURROWS."],
    "AJ-B": ["F/Lt. W. ASTELL.", "Sgt. KINNEAR J.", "P/O. F.A. WILE.", "Sgt. GARSHOWITZ A.",
             "F/O. D. HOPKINSON.", "Sgt. GARBAS F.", "Sgt. BOLITHO R."],
    "AJ-N": ["P/O. L.G. KNIGHT.", "Sgt. GRAYSTON R.", "F/O. H.S. HOBDAY.", "F/Sgt. KELLOW R. G.",
             "F/O. E.C. JOHNSON.", "Sgt. SUTHERLAND R.", "Sgt. O'BRIEN."],
    "AJ-W": ["F/LT. K.L. MUNRO.", "Sgt. APPLEBY F.", "F/O. F.G. RUMBLES.", "Sgt. PIGEON P.E.",
             "Sgt. CLAY J.H.", "Sgt. HOWARTH W.", "F/Sgt. WEEKS H."],
    "AJ-T": ["F/Lt. J.C. MCCARTHY.", "Sgt. RADCLIFFE J.", "F/Sgt. MCLEAN D.A.", "Sgt. EATON R.",
             "Sgt. JOHNSON G.L.", "Sgt. BATSON R.", "F/O. D. RODGER"],
    "AJ-H": ["P/O. G. RICE.", "Sgt. SMITH H.", "F/O. R. MACFARLANE", "Sgt. GOWRIE G.B.",
             "F/Sgt. THRASHER W.", "Sgt. MAYNARD T.", "Sgt. BURNS S."],
    "AJ-K": ["Sgt. BYERS V.W.", "Sgt. TAYLOR A.", "P/O. J.H. WARNER.", "Sgt. WILKINSON R.",
             "Sgt. WHITTAKER A.", "Sgt. JARVIE R.", "Sgt. MCDOWELL H."],
    "AJ-E": ["F/Lt. R.N.G. BARLOW.", "Sgt. WHILLIS S.L.", "F/O. P.S. BURGESS.",
             "F/O. C.R. WILLIAMS.", "Sgt. A. GILLESPIE.", "F/O. H.S. GLINZ.", "Sgt. LIDDELL D."],
    "AJ-C": ["P/O. W.H.T. OTTLEY.", "Sgt. MARSDEN R.", "F/O. J.K. BARRETT.", "Sgt. GUTERMAN J.",
             "F/Sgt. JOHNSTON L.", "Sgt. TEES R.", "Sgt. STRANGE H."],
    "AJ-S": ["P/O. L.J. BURPEE", "Sgt. PEGLOR G.", "Sgt. JAYE T.", "P/O. L.G. WELLER.",
             "Sgt. ARTHUR R.", "Sgt. LONG N.", "F/Sgt. BRADY J.G."],
    "AJ-F": ["F/Sgt. BROWN K.W.", "Sgt. FENERON H.B.", "Sgt. HEAL D.P.", "Sgt. HEWSTONE H.J.",
             "Sgt. OANCIA S.", "Sgt. ALLATSON D.", "F/Sgt. MACDONALD G."],
    "AJ-O": ["F/Sgt. TOWNSEND W.C.", "Sgt. POWELL D.J.", "P/O. C.L. HOWARD.",
             "F/Sgt. CHALMERS G.", "Sgt. FRANKLIN C.E.", "Sgt. WEBB D.E.", "Sgt. WILKINSON J."],
    "AJ-Y": ["F/Sgt. ANDERSON C.T.", "Sgt. PATERSON D.", "Sgt. NUGENT L.", "Sgt. BICKLE D.",
             "Sgt. GREEN S.", "Sgt. EWAN A.", "Sgt. BUCK R."],
}

# Survivors of the lost crews, taken prisoner; everyone else aboard a lost aircraft was killed.
PRISONERS = {"AJ-M": ["F/Sgt. J.W. FRASER", "P/O. A.F. BURCHER"], "AJ-C": ["Sgt. TEES R."]}


def crew_note(code):
    return f"ORB crew ({DUTIES}): " + "; ".join(ORB_CREWS[code])


def fate_note(code):
    taken = PRISONERS.get(code, [])
    killed = [m for m in ORB_CREWS[code] if m not in taken]
    text = "Killed: " + "; ".join(killed)
    if taken:
        text += " — Prisoners of war: " + "; ".join(taken)
    return text
