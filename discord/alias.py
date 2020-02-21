import re

vs1_aliases = ["V-Skill 1", "vs1", "vskill1", "v-skill1"]
# -> [VS1]
vs2_aliases = ["V-Skill 2", "vs2", "vskill2", "v-skill2"]
# -> [VS2]

basedict = {
    # "TABLE NAME" : ["FRIENDLY OFFICIAL NAME", "FRIENDLY ALIAS 1", "FRIENDLY ALIAS 2", [...]]
	# SHARED ALIASES
   	"Standing LP": ["LP", "lp", "jab"],
    "Standing MP": ["MP", "mp", "strong"],
    "Standing HP": ["HP", "hp", "fierce"],
    "Standing LK": ["LK", "lk", "short"],
    "Standing MK": ["MK", "mk", "forward"],
    "Standing HK": ["HK", "hk", "roundhouse"],
    "Crouching LP": ["cr.LP", "cr.lp", "crlp", "cr.jab"],
    "Crouching MP": ["cr.MP", "cr.mp", "crmp", "cr.strong"],
    "Crouching HP": ["cr.HP", "cr.hp", "crhp", "cr.fierce"],
    "Crouching LK": ["cr.LK", "cr.lk", "crlk", "cr.short"],
    "Crouching MK": ["cr.MK", "cr.mk", "crmk", "cr.forward"],
    "Crouching HK": ["cr.HK", "cr.hk", "crhk", "sweep", "spazzata"],
    "Jumping LP": ["j.LP", "j.lp", "jlp", "j.jab"],
    "Jumping MP": ["j.MP", "j.mp", "jmp", "j.strong"],
    "Jumping HP": ["j.HP", "j.hp", "jhp", "j.fierce"],
    "Jumping LK": ["j.LK", "j.lk", "jlk", "j.short"],
    "Jumping MK": ["j.MK", "j.mk", "jmk", "j.forward"],
    "Jumping HK": ["j.HK", "j.hk", "jhk", "j.roundhouse"],
}

userInput = "ryu qcf+lp"

print("userinput is", userInput, "\n")

outer = "(ryu|nash)\s([A-Za-z\+]*)\s*(vt1|vt2){0,1}"
m = re.search(outer, userInput, re.IGNORECASE)
if m:
    char = m.groups(0)[0]
    move = m.groups(0)[1]
    if m.groups(0)[2]:
        vt = m.groups(0)[2].upper()
    else:
        vt = "VT1"

    print("MATCHED outer expression")
    print("char:\t", char)
    print("move:\t", move)
    print("vt:\t",vt)

print("\n")

# Le regex sono il male nocivo te lo giuro
# ricerca con "fireball|hadoken"
hadoken = "([L|M|H]|EX)\s(fireball|hadoken)"

m = re.search(hadoken, move, re.IGNORECASE)
if m:
    # (0) is for the first match
    # [0] is the first group matched
    result = m.groups(0)[0].upper() + " Hadoken"


# ricerca con "qcf"
hadoken2 = "qcf\+([L|M|H|P]{1})p"

m = re.search(hadoken2, move, re.IGNORECASE)
if m:
    # (0) is for the first match
    # [0] is the first group matched
    result = m.groups(0)[0].upper() + " Hadoken"


# ricerca con "shoryuken|dragon punch|dp"
shoryuken = "([L|M|H]|EX)\s(shoryuken|dragon punch|dp)"

m = re.search(shoryuken, move, re.IGNORECASE)
if m:
    # (0) is for the first match
    # [0] is the first group matched
    result = m.groups(0)[0].upper() + " Shoryuken"


# ricerca con "tatsu|tatsumaki"
tatsu = "([L|M|H]|EX)\s(tatsu|tatsumaki)"

m = re.search(tatsu, move, re.IGNORECASE)
if m:
    # (0) is for the first match
    # [0] is the first group matched
    result = m.groups(0)[0].upper() + " Tatsumaki Senpukyaku"


# ricerca con "qcb"
tatsu2 = "qcb\+([L|M|H|K]{1})k"

m = re.search(tatsu2, move, re.IGNORECASE)
if m:
    # (0) is for the first match
    # [0] is the first group matched
    result = m.groups(0)[0].upper() + " Tatsumaki Senpukyaku"


# ricerca con "donkey kick"
donkey = "([L|M|H]|EX)\s(donkey kick)"

m = re.search(donkey, move, re.IGNORECASE)
if m:
    # (0) is for the first match
    # [0] is the first group matched
    result = m.groups(0)[0].upper() + " Jodan Sokutou Geri"


# ricerca con "qcb"
donkey2 = "hcf\+([L|M|H|K]{1})k"

m = re.search(donkey2, move, re.IGNORECASE)
if m:
    # (0) is for the first match
    # [0] is the first group matched
    result = m.groups(0)[0].upper() + " Jodan Sokutou Geri"


print("translated movename:", result)

# TODO
charsolved = char
# TODO: wrap the matchings
movesolved = result
# TODO
vtsolved = vt

finalkey = charsolved +" "+ movesolved +" " +vtsolved
print("\nFinal key:", finalkey)


other = {
	# CHARACTER: RYU
    # V-TRIGGER 1
    "Collarbone Breaker": ["f+MP", "f+mp", "f.mp", "fmp", "overhead"],
    "Solar Plexus Strike": ["f+HP", "f+hp", "f.hp", "fhp"],
    "Axe Kick": ["b+HK", "b+hk", "b.hk", "bhk"],
    "Jodan Nirengeki": ["MP>HP", "mp+hp", "mp hp"],
    "Jodan Sanrengeki": ["MP>HP>HK", "mp+hp+hk", "mp hp hk"],
    "Shoulder Throw": ["throw", "lp+lk", "lplk", "throw"],
    "Somersault Throw": ["b+throw", "b+lp+lk", "blplk", "bthrow", "b+throw", "back throw"],
    "Denjin Renki": ["V-Trigger 1", "vt1", "vtrigger1", "v-trigger1"],
    "Hashogeki": ["V-reversal", "vreversal", "v-reversal"],
 

    "Airborne Tatsumaki Senpukyaku": ["Air Tatsu", "j.qcb+k", "air tatsu"],
    "EX Airborne Tatsumaki Senpukyaku": ["EX Air Tatsu", "j.qcb+kk", "ex air tatsu"],
 

    "Shinku Hadoken": ["CA", "ca", "critical art", "super"],
    "Denjin Hadoken": ["CA VT1", "ca vt1", "critical art vt1", "super vt1"],

	# CHARACTER: RYU
    # V-TRIGGER 2
    "Kakko Fubatsui": ["V-Trigger 2", "vt2", "vtrigger2", "v-trigger2"],
    # da dare come risultato assieme a "Kakko Fubatsui":
	# "Isshin (Stance)"
	# "Isshin (Attack)"


	# CHARACTER: CHUN-LI
    # V-TRIGGER 1
	"Diagonal Jumping HK": ["jf.HK", "jf.hk", "jfhk", "jf.roundhouse", "jb.hk", "jbhk", "jb.roundhouse"],

}

def findAlias(text):
    for move in aliasdict:
        for alias in aliasdict[move]:
            if text == alias:
                return move, aliasdict[move][0]