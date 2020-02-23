import logging
import re

logging.basicConfig(level=logging.DEBUG)

## Utility
def matchExact(text, data):
    for move in data:
        for alias in data[move]:
            if text == alias:
                return move

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
    
    "Diagonal Jumping HK": ["uf+hk","ufhk","ub+hk","ubhk"],
    # NEED TO TRANSLATE TO:
    # "Jumping HK"

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
        if (move == "Jumping HK" and char == "chun-li"):
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



    # I TRIED

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

def resolveMoveName(userstring):
    logging.info("USERSTRING"+userstring)
    # product of dennitopolino typing blind:
    holyregex = "(\w+\-*\w+)\s(\w+|\w+\.\w+|\w+\s\w+|\w+\+\w+|\w+\s\w+\s\w+|\w+,\w+\+\w+)\s*(vt1|vt2){0,1}$"
    # ye, don't ask
    m = re.search(holyregex, userstring, re.IGNORECASE)
    if m:
        char = m.groups(0)[0]
        move = m.groups(0)[1].lower()
        if m.groups(0)[2]:
            vt = m.groups(0)[2].upper()
        else:
            vt = "VT0"

        logging.info("MATCHED outer expression")
        logging.info("char:\t%s", char)
        logging.info("move:\t%s", move)
        logging.info("vt:\t%s", vt)

    result = None
    print(char)

    ## CHAR MATCHING
    if char == "chunli":
        char = "chun-li"

    ## MOVE MATCHING
    if char == "ryu":
        result = matchExact(move, ryuexact)
    elif char == "chun-li":
        result = matchExact(move, chunliexact)

    if not result:
        if char == "ryu":
            result = ryuRegex(move)
        elif char == "chun-li":
            result = chunliRegex(move)
    if not result:
        result = commonRegex(move, char)
    if not result:
        result = move

    logging.info("translated movename:%s", result)

    charsolved = char

    # TODO: wrap the matchings
    movesolved = result
    # TODO
    vtsolved = vt

    finalkey = charsolved + " " + movesolved + " " + vtsolved
    logging.info("Final key:%s", finalkey)

    resultdict = {
        'character': char,
        'move': movesolved,
        'vt': vtsolved
    }

    return resultdict
