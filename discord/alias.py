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

    "Shoulder Throw": ["lp+lk", "lplk", "throw"],
    "Somersault Throw": ["b+lp+lk", "blplk", "bthrow", "b+throw", "back throw"],
    "[VS1] Mind's Eye": ["vs1","vskill1","v-skill1"],   
    "[VS2] Thust Strike": ["vs2","vskill2","v-skill2"],
    "[VS2] Thust Strike (upon successful parry)": ["vs2 parry","vskill2 parry","v-skill2 parry"],
    "Denjin Renki": ["vt1", "vtrigger1", "v-trigger1"],
    "Hashogeki": ["vreversal", "v-reversal","vrev"],
    "Shinku Hadoken": ["ca", "critical art", "super"],
    "Denjin Hadoken" : ["ca vt1", "critical art vt1", "super vt1"],
 
    # V-TRIGGER 2
    "Kakko Fubatsui": ["vt2", "vtrigger2", "v-trigger2"],
    "Isshin (Stance)": ["vt2 parry","vtrigger2 parry", "v-trigger2 parry"]
    # "Isshin (Attack)":

}

chunliexact = {
    # CHARACTER: CHUN-LI
    # V-TRIGGER 1
       
    "Koshuto": ["lp+lk", "lplk", "throw"],
    "Tenshin Shushu": ["b+lp+lk", "blplk", "bthrow", "b+throw", "back throw"],
    "Ryuseiraku": ["j.lp+lk", "jlplk", "jthrow", "j.throw", "air throw"],
    "[VS1] Rankyaku": ["vs1","vskill1","v-skill1"],
    "[VS1] Souseikyaku": ["vs1>vs1","vskill1>vskill1","v-skill1>v-skill1"],
    "[VS2] Hazansyu": ["vs2","vskill2","v-skill2"],
    "Renkiko": ["vt1", "vtrigger1", "v-trigger1"],
    "Sohakkei": ["vreversal", "v-reversal","vrev"],
    "Hoyokusen": ["ca", "critical art", "super"],
    
    # V-TRIGGER 2
    "Kikosho": ["vt2", "vtrigger2", "v-trigger2"],
    "Kikosho (Charge)": ["vt2 hold", "vtrigger2 hold", "v-trigger2 hold"]
    # ANOTHER "Kikosho" IS PRESENT
}

nashexact = {
    # CHARACTER: NASH
    # V-TRIGGER 1
    
    "Bullet Combination (3)": ["mk>hk>vs1","mk>hk>mp+mk"],
    "Dragon Suplex": ["lp+lk", "lplk", "throw"],
    "Target Down": ["b+lp+lk", "blplk", "bthrow", "b+throw", "back throw"],
    "Air Jack": ["j.lp+lk", "jlplk", "jthrow", "j.throw", "air throw"],
    "[VS1] Bullet Clear": ["vs1","vskill1","v-skill1"],
    "[VS2] Silent Sharpness": ["vs2","vskill2","v-skill2"],   
    "Sonic Move - Hide": ["vt1", "vtrigger1", "v-trigger1"],
    "Sonic Move - Blitz Air": ["b+vt1", "b.vt1", "b+vtrigger1", "b+v-trigger1"],
    "Sonic Move - Steel Air": ["f+vt1", "f.vt1", "f+vtrigger1", "f+v-trigger1"],
    "Sonic Move - Avoid": ["vreversal", "v-reversal","vrev"],   
    "Judgement Saber": ["ca", "critical art", "super"],
    "L Sonic Scythe (VS2 Ver.)": ["qcb+lk vs2"],
    "M Sonic Scythe (VS2 Ver.)": ["qcb+mk vs2"],
    "H Sonic Scythe (VS2 Ver.)": ["qcb+hk vs2"],
    "EX Sonic Scythe (VS2 Ver.)": ["qcb+kk vs2"],

    # V-TRIGGER 2

    "Stealth Dash": ["vt2", "vtrigger2", "v-trigger2"],
    "Stealth Dash (Stop)": ["vt2+b", "vtrigger2+b", "v-trigger2+b"],
    "Justice Corridor": ["vt2+p", "vtrigger2+p", "v-trigger2+p"],
    "Justice Shell": ["vt2+k", "vtrigger2+k", "v-trigger2+k"]
}

mbisonexact = {
    # CHARACTER: M. BISON
    # V-TRIGGER 1   
     
    "Psycho Impact": ["lp+lk", "lplk", "throw"],
    "Psycho Fall": ["b+lp+lk", "blplk", "bthrow", "b+throw", "back throw"],
    "[VS1] Psycho Reflect": ["vs1","vskill1","v-skill1"],
    "[VS1] Psycho Reflect (Shoot Projectile)": ["vs1 fb","vskill1 fb","v-skill1 fb"],
    # "[VS1] Psycho Reflect (Attack)"
    "[VS2] Hell's Warp": ["vs2","vskill2","v-skill2"],
    "Psycho Power": ["vt1", "vtrigger1", "v-trigger1"],
    "Psycho Burst": ["vreversal", "v-reversal","vrev"],
    "Ultimate Psycho Crusher": ["ca", "critical art", "super"],
    "Ultimate Psycho Crusher (Airborne)": ["j.ca", "j.critical art", "j.super"],
    "EX Psycho Inferno (Cancel)": ['qcb+pp cancel'],
    "EX Double Knee Press (Cancel)": ['bf+kk cancel'],
    "EX Head Press (Cancel)": ['du+kk cancel'],

    # V-TRIGGER 2

    "Psycho Nightmare": ["vt2", "vtrigger2", "v-trigger2"],
    # "Psycho Crusher"
    "Psycho Judgement": ['hcb+k>hcb+k']
}

cammyexact = {
    # CHARACTER: CAMMY
    # V-TRIGGER 1   
     
    "Gyro Clipper": ["lp+lk", "lplk", "throw"],
    "Delta Through": ["b+lp+lk", "blplk", "bthrow", "b+throw", "back throw"],
    "Neck Spiral": ["j.lp+lk", "jlplk", "jthrow", "j.throw", "air throw"],
    "[VS1] Axel Spin Knuckle": ["vs1","vskill1","v-skill1"],
    "[VS2] Spinning Attack": ["vs2","vskill2","v-skill2"],
    "Delta Drive": ["vt1", "vtrigger1", "v-trigger1"],
    "Strike Back": ["vreversal", "v-reversal","vrev"],
    "Cross Scissors Pressure": ["hcf+p>j.throw","hcf+p>j.lp+lk","hcf+p>jthrow","hcf+p>jlp+lk","hcf+p>air throw"],
    "Cross Stinger Assault": ["ca", "critical art", "super"],

    # V-TRIGGER 2

    "Delta Ambush": ["vt2", "vtrigger2", "v-trigger2"],
    "Delta Step": ["f+vt2", "f.vt2", "f+vtrigger2", "f+v-trigger2"],
    "Delta Twist": ["vt2+p","vtrigger2+p","v-trigger2+p"],
    "Reverse Edge": ["vt2+k","vtrigger2+k","v-trigger2+k"]
}

birdieexact = {
    # CHARACTER: BIRDIE
    # V-TRIGGER 1   
     
    "Bad Skull": ["lp+lk", "lplk", "throw"],
    "Bad Chain": ["b+lp+lk", "blplk", "bthrow", "b+throw", "back throw"],
    "Break Time": ["vs1","vskill1","v-skill1"],
    "Banana Time": ["b+vs1","b+vskill1","b+v-skill1"],
    "Drink Time": ["d+vs1","d+vskill1","d+v-skill1"],
    "[VS2] Chewing Time": ["vs2","vskill2","v-skill2"],
    "[VS2] Chewing Time (Hold Button)": ["vs2 hold","vskill2 hold","v-skill2 hold"],
    "Enjoy Time": ["vt1", "vtrigger1", "v-trigger1"],
    "Pepper Pot": ["vreversal", "v-reversal","vrev"],
    "Skip To My Chain": ["ca", "critical art", "super"],

    # V-TRIGGER 2

    "Birdie Time": ["vt2", "vtrigger2", "v-trigger2"],
    # "Bull Swing"
    "Bull Capture": ["d+vt2", "d+vtrigger2", "d+v-trigger2"]
}


## Regex matching

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
    elif char == "bison":
        char = "mbison"
    
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
        elif char == "cammy":
            result = matchExact(move, cammyexact) 
        elif char == "mbison":
            result = matchExact(move, mbisonexact)
        elif char == "birdie":
            result = matchExact(move, birdieexact)

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
