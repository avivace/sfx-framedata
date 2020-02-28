import logging
import re
import json

logging.basicConfig(level=logging.DEBUG)

## Utility
def matchExact(text, data):
    for move in data:
        for alias in data[move]:
            if text == alias:
                return move

with open('../data/extracted/data.json', 'r') as f:
    data = json.load(f)

## Exact matching
ryuexact = {
    # CHARACTER: RYU
    # V-TRIGGER 1
    "Collarbone Breaker": ["f+mp","fmp", "overhead"],
    "Solar Plexus Strike": ["f+hp", "fhp"],
    "Axe Kick": ["b+hk", "bhk"],
    
    "Jodan Nirengeki": ["mp>hp"],
    "Jodan Sanrengeki": ["mp>hp>hk"],
    # IF POSSIBLE GROUP UNDER: 
    # "target combo" (name not in the table)

    "Shoulder Throw": ["lp+lk", "lplk", "throw"],
    "Somersault Throw": ["b+lp+lk", "blplk", "bthrow", "b+throw", "back throw"],
    "[VS1] Mind's Eye": ["vs1","vskill1","v-skill1"],
    
    "[VS2] Thust Strike": ["vs2","vskill2","v-skill2"],
    # GROUP WITH:
    # "[VS2] Thust Strike (upon successful parry)"

    "Denjin Renki": ["vt1", "vtrigger1", "v-trigger1"],
    "Hashogeki": ["vreversal", "v-reversal","vrev"],
    "Airborne Tatsumaki Senpukyaku": ["j.qcb+k", "jqcb+k", "air tatsu"],
    "EX Airborne Tatsumaki Senpukyaku": ["j.qcb+kk",  "jqcb+kk", "ex air tatsu"],
    "Shinku Hadoken": ["ca", "critical art", "super"],
    
    # "Denjin Hadoken" = "Shinku Hadoken" when using "vt1" modificator


    # questa scassa tutto, me lo sento
    "Hadoken (Lv2)": ["qcf+p vt1"],
    # GROUP WITH:
    # "Hadoken (Lv3)"
    
    # "EX Hadoken (Lv1)" = "EX Hadoken" when using "vt1" modificator
    # GROUP WITH:
    # "EX Hadoken (Lv2)"


    
    # V-TRIGGER 2
    "Kakko Fubatsui": ["vt2", "vtrigger2", "v-trigger2"],
    # GROUP WITH:
    # "Isshin (Stance)"
    # "Isshin (Attack)"
}

chunliexact = {
    # CHARACTER: CHUN-LI
    # V-TRIGGER 1
    
    "Vertical Jump HK": ["u+hk","uhk","split kicks","split"],
    "Senenshu": ["df+mk", "dfmk", "overhead"],
    "Tsuitotsuken": ["b+mp","bmp","f+mp","fmp"],
    "Hakkei": ["b+hp","bhp","hey","ey"],
    "Kakurakukyaku": ["df+hk","dfhk"],
    "Tenkukyaku": ["b+hk","bhk"],
    "Yokusenkyaku": ["f+hk","fhk"],
    
    "Yosokyaku": ["j.d+mk","jd+mk","jdmk","air stomp","stomp"],
    # GROUP WITH:
    # Yosokyaku (2)
    # Yosokyaku (3)
    
    "Koshuto": ["lp+lk", "lplk", "throw"],
    "Tenshin Shushu": ["b+lp+lk", "blplk", "bthrow", "b+throw", "back throw"],
    "Ryuseiraku": ["j.lp+lk", "jlplk", "jthrow", "j.throw", "air throw"],

    "[VS1] Rankyaku": ["vs1","vskill1","v-skill1"],
    # GROUP WITH:
    # "[VS1] Souseikyaku"

    "[VS2] Hazansyu": ["vs2","vskill2","v-skill2"],
    "Renkiko": ["vt1", "vtrigger1", "v-trigger1"],
    "Sohakkei": ["vreversal", "v-reversal","vrev"],
    "Hoyokusen": ["ca", "critical art", "super"],
    
    
    # V-TRIGGER 2
    "Kikosho": ["vt2", "vtrigger2", "v-trigger2"]
    # ANOTHER "Kikosho" IS PRESENT
    # GROUP WITH:
    # "Kikosho" (the second one)
    # "Kikosho (Charge)"
}

nashexact = {
    # CHARACTER: NASH
    # V-TRIGGER 1
    
    
    "Vertical Jump HK": ["u+hk","uhk"],
    "Chopping Assault": ["f+mp","fmp", "overhead"],
    "Spinning Back Knuckle": ["f+hp", "fhp"],
    "Knee Bazooka": ["f+lk", "flk"],
    "Jumping Sobat": ["f+mk","fmk"],
    "Side Knee Attack": ["b+mk","bmk"],
    "Step Kick": ["f+hk","fhk"],

    "Rapid Punch": ["lp>mp"],
    "Rapid Kick": ["lk>mk"],
    "Wind Shear (2)": ["mp>lk"],
    "Wind Shear (3)": ["mp>lk>hp"],
    "Down Burst": ["d+mp>f+mp","cr.mp>f+mp","crmp>f+mp","crmp>fmp"],
    "(Raptor/Bullet) Combination (2)": ["mk>hk"],
    "Raptor Combination (3)": ["mk>hk>mk"],
    # "Bullet Combination (3)": ["mk>hk>mp+mk"],
    # (WHEN SELECTING VSKILL I)
    # IF POSSIBLE GROUP UNDER: 
    # "target combo" (name not in the table)

    "Dragon Suplex": ["lp+lk", "lplk", "throw"],
    "Target Down": ["b+lp+lk", "blplk", "bthrow", "b+throw", "back throw"],
    "Air Jack": ["j.lp+lk", "jlplk", "jthrow", "j.throw", "air throw"],
    "[VS1] Bullet Clear": ["vs1","vskill1","v-skill1"],
    "[VS2] Silent Sharpness": ["vs2","vskill2","v-skill2"],
    
    "Sonic Move - Hide": ["hp+hk","d+hp+hk","cr.hp+hk","crhp+hk","crhphk"],
    "Sonic Move - Blitz Air": ["b+hp+hk","bhp+hk","bhphk"],
    "Sonic Move - Steel Air": ["f+hp+hk","fhp+hk","fhphk"],
    "Sonic Move - Avoid": ["vreversal", "v-reversal","vrev"],
    # GROUP UNDER VT1?
    
    "Judgement Saber": ["ca", "critical art", "super"] 
}

## Regex matching
def ryuRegex(movestring):
    # matching with "qcf"
    hadoken2 = "qcf\+([L|M|H|P]{1})p"
    m = re.search(hadoken2, movestring, re.IGNORECASE)
    if m:
        # (0) is for the first match
        # [0] is the first group matched
        if m.groups(0)[0] == "p":
            mod = "EX"
        else:
            mod = m.groups(0)[0]

        return mod.upper() + " Hadoken"

    # matching with "qcb"
    tatsu2 = "qcb\+([L|M|H|K]{1})k"

    m = re.search(tatsu2, movestring, re.IGNORECASE)
    if m:
        # (0) is for the first match
        # [0] is the first group matched
        if m.groups(0)[0] == "k":
            mod = "EX"
        else:
            mod = m.groups(0)[0]

        return mod.upper() + " Tatsumaki Senpukyaku"

    # matching with "hcf"
    donkey2 = "hcf\+([L|M|H|K]{1})k"

    m = re.search(donkey2, movestring, re.IGNORECASE)
    if m:
        # (0) is for the first match
        # [0] is the first group matched
        if m.groups(0)[0] == "k":
            mod = "EX"
        else:
            mod = m.groups(0)[0]

        return mod.upper() + " Jodan Sokutou Geri"

    # matching with "hadoken|hado"
    hadoken = "([L|M|H]|EX)\s(hadoken|hado)"
    m = re.search(hadoken, movestring, re.IGNORECASE)
    if m:
        # (0) is for the first match
        # [0] is the first group matched
        return m.groups(0)[0].upper() + " Hadoken"

    # matching with "shoryu|dragon punch|dp"
    shoryuken = "([L|M|H]|EX)\s(shoryu|dragon punch|dp)"

    m = re.search(shoryuken, movestring, re.IGNORECASE)
    if m:
        # (0) is for the first match
        # [0] is the first group matched
        return m.groups(0)[0].upper() + " Shoryuken"

    # matching with "tatsu|tatsumaki"
    tatsu = "([L|M|H]|EX)\s(tatsu|tatsumaki)"

    m = re.search(tatsu, movestring, re.IGNORECASE)
    if m:
        # (0) is for the first match
        # [0] is the first group matched
        return m.groups(0)[0].upper() + " Tatsumaki Senpukyaku"

    # matching with "donkey kick|donkey"
    donkey = "([L|M|H]|EX)\s(donkey kick|donkey)"

    m = re.search(donkey, movestring, re.IGNORECASE)
    if m:
        # (0) is for the first match
        # [0] is the first group matched
        return m.groups(0)[0].upper() + " Jodan Sokutou Geri"

    return ""

def commonRegex(movestring, char):
    # Le regex sono il male nocivo te lo giuro
    normals = "(cr|j|st){0,1}.{0,1}([L|M|H]{1})(p|k)"
    m = re.search(normals, movestring, re.IGNORECASE)
    if m:
        if m.groups(0)[0] == "cr":
            mod = "Crouching"
        elif m.groups(0)[0] == "j":
            mod = "Jumping"
        elif m.groups(0)[0] == "st":
            mod = "Standing"
        elif not m.groups(0)[0]:
            mod = "Standing"

        move = f'{mod} {m.groups(0)[1].upper()}{m.groups(0)[2].upper()}'
        if (move == "Jumping HK" and (char == "chun-li" or char == "nash")):
            move = "Diagonal Jumping HK"
        return move

def chunliRegex(movestring):
    # matching with "b,f+"
    kikoken2 = "b,f\+([L|M|H|P]{1})p"
    m = re.search(kikoken2, movestring, re.IGNORECASE)
    if m:
        # (0) is for the first match
        # [0] is the first group matched
        if m.groups(0)[0] == "p":
            mod = "EX"
        else:
            mod = m.groups(0)[0]

        return mod.upper() + " Kikoken"


    # matching with "d,u+"
    sbk2 = "d,u\+([L|M|H|k]{1})k"
    m = re.search(sbk2, movestring, re.IGNORECASE)
    if m:
        # (0) is for the first match
        # [0] is the first group matched
        if m.groups(0)[0] == "k":
            mod = "EX"
        else:
            mod = m.groups(0)[0]

        return mod.upper() + " Spinning Bird Kick"


    # matching with "qcf"
    hyaku2 = "(j.|j){0,1}qcf\+([L|M|H|K]{1})k"
    m = re.search(hyaku2, movestring, re.IGNORECASE)
    if m:
        if m.groups(0)[1].lower() == "k":
            mod = "EX"
        else:
            mod = m.groups(0)[1].upper()

        # (0) is for the first match
        # [0] is the first group matched
        if m.groups(0)[0] == "j":
            mod = mod + " Airborne"
        elif m.groups(0)[0] == "j.":
            mod = mod + " Airborne"

        return f'{mod} Hyakuretsukyaku'
        
      
    # matching with "kiko"
    kikoken = "([L|M|H]|EX)\s(kiko)"
    m = re.search(kikoken, movestring, re.IGNORECASE)
    if m:
        # (0) is for the first match
        # [0] is the first group matched
        return m.groups(0)[0].upper() + " Kikoken"


    # matching with "hyaku|legs"
    hyaku = "([L|M|H]|EX)\s(hyaku|legs)"
    m = re.search(hyaku, movestring, re.IGNORECASE)
    if m:
        # (0) is for the first match
        # [0] is the first group matched
        return m.groups(0)[0].upper() + " Hyakuretsukyaku"


    # matching with "sbk|spinning"
    sbk = "([L|M|H]|EX)\s(sbk|spinning)"
    m = re.search(sbk, movestring, re.IGNORECASE)
    if m:
        # (0) is for the first match
        # [0] is the first group matched
        return m.groups(0)[0].upper() + " Spinning Bird Kick"

    return ""

def nashRegex(movestring):
    # matching with "qcf+p"
    sonic2 = "qcf\+([L|M|H|P]{1})p"
    m = re.search(sonic2, movestring, re.IGNORECASE)
    if m:
        # (0) is for the first match
        # [0] is the first group matched
        if m.groups(0)[0] == "p":
            mod = "EX"
        else:
            mod = m.groups(0)[0]

        return mod.upper() + " Sonic Boom"

    # matching with "qcf+k"
    moon2 = "qcf\+([L|M|H|P]{1})k"
    m = re.search(moon2, movestring, re.IGNORECASE)
    if m:
        # (0) is for the first match
        # [0] is the first group matched
        if m.groups(0)[0] == "k":
            mod = "EX"
        else:
            mod = m.groups(0)[0]

        return mod.upper() + " Moonsault Slash"

    # matching with "qcb"
    scythe = "qcb\+([L|M|H|K]{1})k\s*(vs2){0,1}"

    m = re.search(scythe, movestring, re.IGNORECASE)
    if m:
        # (0) is for the first match
        # [0] is the first group matched
        if m.groups(0)[0] == "k":
            mod = "EX"
        else:
            mod = m.groups(0)[0]
    
        if m.groups(0)[1] == "vs2":
            mod2 = " (VS2 Ver.)"
        else:
            mod2 = ""
        return f'{mod.upper()} Sonic Scythe{mod2}'

    # matching with "moonsault|moon"
    moon = "([L|M|H]|EX)\s(moonsault|moon)"
    m = re.search(moon, movestring, re.IGNORECASE)
    if m:
        # (0) is for the first match
        # [0] is the first group matched
        return m.groups(0)[0].upper() + " Moonsault Slash"

    # matching with "dp|tragedy"
    tragedy = "([L|M|H]|EX)\s(dp|tragedy)"
    m = re.search(tragedy, movestring, re.IGNORECASE)
    if m:
        # (0) is for the first match
        # [0] is the first group matched
        return m.groups(0)[0].upper() + " Tragedy Assault"


    return ""

def resolveMoveName(userstring):
    logging.info("USERSTRING "+userstring)
    # product of dennitopolino typing blind:
    holyregex = "^(\S+)\s(\S+|\S+\s\S+|\S+\s\S+\s\S+)\s*(vt1|vt2){0,1}$"
    # ye, don't ask
    m = re.search(holyregex, userstring, re.IGNORECASE)
    if m:
        char = m.groups(0)[0]
        move = m.groups(0)[1].lower()
        if m.groups(0)[2]:
            vt = m.groups(0)[2].upper()
            vtd = vt
        else:
            vt = "vt0"
            vtd = "vt1"
        logging.info("MATCHED outer expression")
        logging.info("char:\t%s", char)
        logging.info("move:\t%s", move)
        logging.info("vt:\t%s", vt)

    result = None
    matchtype = 0

    ## CHAR MATCHING
    if char == "chunli":
        char = "chun-li"
    
    ## direct key matching
    for moveExact in data[char][vtd.lower()]:
        if move.lower() == moveExact["matchCol"].lower():
            result = move

    ## charmove matching
    if not result:
        matchtype = 1
        if char == "ryu":
            result = matchExact(move, ryuexact)
        elif char == "chun-li":
            result = matchExact(move, chunliexact)
        elif char == "nash":
            result = matchExact(move, nashexact)


    charsolved = char
    # TODO: wrap the matchings
    movesolved = result
    # TODO
    vtsolved = vt

    resultdict = {
        'character': char,
        'move': movesolved,
        'vt': vtsolved,
        'type': matchtype
    }

    logging.info("Final match:%s", resultdict)

    return resultdict
