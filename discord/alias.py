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

textinput = "qcf+lp"

# Le regex sono il male nocivo te lo giuro
# ricerca con "fireball|hadoken"
hadoken = "([L|M|H]|EX)\s(fireball|hadoken)"

m = re.search(hadoken, textinput, re.IGNORECASE)
if m:
    # (0) is for the first match
    # [0] is the first group matched
    result = m.groups(0)[0].upper() + " Hadoken"
    print(result)


# ricerca con "qcf"
hadoken2 = "qcf\+([L|M|H|P]{1})p"

m = re.search(hadoken2, textinput, re.IGNORECASE)
if m:
    # (0) is for the first match
    # [0] is the first group matched
    result = m.groups(0)[0].upper() + " Hadoken"
    print(result)


# ricerca con "shoryuken|dragon punch|dp"
shoryuken = "([L|M|H]|EX)\s(shoryuken|dragon punch|dp)"

m = re.search(shoryuken, textinput, re.IGNORECASE)
if m:
    # (0) is for the first match
    # [0] is the first group matched
    result = m.groups(0)[0].upper() + " Shoryuken"
    print(result)


# ricerca con "tatsu|tatsumaki"
tatsu = "([L|M|H]|EX)\s(tatsu|tatsumaki)"

m = re.search(tatsu, textinput, re.IGNORECASE)
if m:
    # (0) is for the first match
    # [0] is the first group matched
    result = m.groups(0)[0].upper() + " Tatsumaki Senpukyaku"
    print(result)


# ricerca con "qcb"
tatsu2 = "qcb\+([L|M|H|K]{1})k"

m = re.search(tatsu2, textinput, re.IGNORECASE)
if m:
    # (0) is for the first match
    # [0] is the first group matched
    result = m.groups(0)[0].upper() + " Tatsumaki Senpukyaku"
    print(result)


# ricerca con "donkey kick"
donkey = "([L|M|H]|EX)\s(donkey kick)"

m = re.search(donkey, textinput, re.IGNORECASE)
if m:
    # (0) is for the first match
    # [0] is the first group matched
    result = m.groups(0)[0].upper() + " Jodan Sokutou Geri"
    print(result)


# ricerca con "qcb"
donkey2 = "hcf\+([L|M|H|K]{1})k"

m = re.search(donkey2, textinput, re.IGNORECASE)
if m:
    # (0) is for the first match
    # [0] is the first group matched
    result = m.groups(0)[0].upper() + " Jodan Sokutou Geri"
    print(result)





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