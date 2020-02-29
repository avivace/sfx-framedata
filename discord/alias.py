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

    "Shoulder Throw": ["throw"],
    "Somersault Throw": ["bthrow", "b+throw", "back throw"],
    "[VS1] Mind's Eye": ["vs1","vskill1"],   
    "[VS2] Thust Strike": ["vs2","vskill2"],
    "[VS2] Thust Strike (upon successful parry)": ["vs2 parry","vskill2 parry"],
    "Denjin Renki": ["vt1", "vtrigger1"],
    "Hashogeki": ["vreversal", "vrev"],
    "Shinku Hadoken": ["ca", "critical art", "super"],
    "Denjin Hadoken" : ["ca vt1", "critical art vt1", "super vt1"],
 
    # V-TRIGGER 2
    "Kakko Fubatsui": ["vt2", "vtrigger2"],
    "Isshin (Stance)": ["vt2 parry","vtrigger2 parry"]
    # "Isshin (Attack)":

}

chunliexact = {
    # CHARACTER: CHUN-LI
    # V-TRIGGER 1
       
    "Koshuto": ["throw"],
    "Tenshin Shushu": ["bthrow", "b+throw", "back throw"],
    "Ryuseiraku": ["jthrow", "j.throw", "air throw"],
    "[VS1] Rankyaku": ["vs1","vskill1"],
    "[VS1] Souseikyaku": ["vs1>vs1","vskill1>vskill1"],
    "[VS2] Hazansyu": ["vs2","vskill2"],
    "Renkiko": ["vt1", "vtrigger1"],
    "Sohakkei": ["vreversal", "vrev"],
    "Hoyokusen": ["ca", "critical art", "super"],
    
    # V-TRIGGER 2
    "Kikosho": ["vt2", "vtrigger2"],
    "Kikosho (Charge)": ["vt2 hold", "vtrigger2 hold"]
    # ANOTHER "Kikosho" IS PRESENT
}

nashexact = {
    # CHARACTER: NASH
    # V-TRIGGER 1
    
    "Bullet Combination (3)": ["mk>hk>vs1"],
    "Dragon Suplex": ["throw"],
    "Target Down": ["bthrow", "b+throw", "back throw"],
    "Air Jack": ["jthrow", "j.throw", "air throw"],
    "[VS1] Bullet Clear": ["vs1","vskill1"],
    "[VS2] Silent Sharpness": ["vs2","vskill2"],   
    "Sonic Move - Hide": ["vt1", "vtrigger1"],
    "Sonic Move - Blitz Air": ["b+vt1", "b+vtrigger1"],
    "Sonic Move - Steel Air": ["f+vt1", "f+vtrigger1"],
    "Sonic Move - Avoid": ["vreversal", "vrev"],   
    "Judgement Saber": ["ca", "critical art", "super"],
    "L Sonic Scythe (VS2 Ver.)": ["qcb+lk vs2"],
    "M Sonic Scythe (VS2 Ver.)": ["qcb+mk vs2"],
    "H Sonic Scythe (VS2 Ver.)": ["qcb+hk vs2"],
    "EX Sonic Scythe (VS2 Ver.)": ["qcb+kk vs2"],

    # V-TRIGGER 2

    "Stealth Dash": ["vt2", "vtrigger2"],
    "Stealth Dash (Stop)": ["vt2+b", "vtrigger2+b"],
    "Justice Corridor": ["vt2+p", "vtrigger2+p"],
    "Justice Shell": ["vt2+k", "vtrigger2+k"]
}

mbisonexact = {
    # CHARACTER: M. BISON
    # V-TRIGGER 1   
     
    "Psycho Impact": ["throw"],
    "Psycho Fall": ["bthrow", "b+throw", "back throw"],
    "[VS1] Psycho Reflect": ["vs1","vskill1"],
    "[VS1] Psycho Reflect (Shoot Projectile)": ["vs1 fb","vskill1 fb"],
    # "[VS1] Psycho Reflect (Attack)"
    "[VS2] Hell's Warp": ["vs2","vskill2"],
    "Psycho Power": ["vt1", "vtrigger1"],
    "Psycho Burst": ["vreversal","vrev"],
    "Ultimate Psycho Crusher": ["ca", "critical art", "super"],
    "Ultimate Psycho Crusher (Airborne)": ["j.ca", "j.critical art", "j.super"],
    "EX Psycho Inferno (Cancel)": ["qcb+pp cancel"],
    "EX Double Knee Press (Cancel)": ["bf+kk cancel"],
    "EX Head Press (Cancel)": ["du+kk cancel"],

    # V-TRIGGER 2

    "Psycho Nightmare": ["vt2", "vtrigger2"],
    # "Psycho Crusher"
    "Psycho Judgement": ["hcb+k>hcb+k"]
}

cammyexact = {
    # CHARACTER: CAMMY
    # V-TRIGGER 1   
     
    "Gyro Clipper": ["throw"],
    "Delta Through": ["bthrow", "b+throw", "back throw"],
    "Neck Spiral": ["jthrow", "j.throw", "air throw"],
    "[VS1] Axel Spin Knuckle": ["vs1","vskill1"],
    "[VS2] Spinning Attack": ["vs2","vskill2"],
    "Delta Drive": ["vt1", "vtrigger1"],
    "Strike Back": ["vreversal", "vrev"],
    "Cross Scissors Pressure": ["hcf+p>j.throw","hcf+p>jthrow","hcf+p>air throw"],
    "Cross Stinger Assault": ["ca", "critical art", "super"],

    # V-TRIGGER 2

    "Delta Ambush": ["vt2", "vtrigger2"],
    "Delta Step": ["f+vt2", "f+vtrigger2"],
    "Delta Twist": ["vt2+p","vtrigger2+p"],
    "Reverse Edge": ["vt2+k","vtrigger2+k"]
}

birdieexact = {
    # CHARACTER: BIRDIE
    # V-TRIGGER 1   
     
    "Bad Skull": ["throw"],
    "Bad Chain": ["bthrow", "b+throw", "back throw"],
    "Break Time": ["vs1","vskill1"],
    "Banana Time": ["b+vs1","b+vskill1"],
    "Drink Time": ["d+vs1","d+vskill1"],
    "[VS2] Chewing Time": ["vs2","vskill2"],
    "[VS2] Chewing Time (Hold Button)": ["vs2 hold","vskill2 hold"],
    "Enjoy Time": ["vt1", "vtrigger1"],
    "Pepper Pot": ["vreversal", "vrev"],
    "Skip To My Chain": ["ca", "critical art", "super"],

    # V-TRIGGER 2

    "Birdie Time": ["vt2", "vtrigger2"],
    # "Bull Swing"
    "Bull Capture": ["d+vt2", "d+vtrigger2"]
}

kenexact = {
    # CHARACTER: KEN
    # V-TRIGGER 1   

    "Knee Bash": ["throw"],
    "Hell Wheel": ["bthrow", "b+throw", "back throw"],
    "[VS1] Quick Step": ["vs1","vskill1"],
    "[VS1] Quick Step (Hold Button)": ["vs1 hold","vskill1 hold"],
    "[VS2] Ryusenkyaku": ["vs2","vskill2"],
    "[VS2] Ryusenkyaku (Hold Button)": ["vs2 hold","vskill2 hold"],
    "Heat Rush": ["vt1", "vtrigger1"],
    "Senpu Nataotoshi": ["vreversal","vrev"],
    "Guren Enjinkyaku": ["ca", "critical art", "super"],

    # V-TRIGGER 2

    "Shinryuken": ["vt2", "vtrigger2"],
    "Shinryuken (Lv2)": ["vt2 lv2", "vtrigger2 lv2"],
    "Shinryuken (Lv3)": ["vt2 lv3", "vtrigger2 lv3"]
}

necalliexact = {
    # CHARACTER: NECALLI
    # V-TRIGGER 1   

    "Soul Sealer": ["throw"],
    "Soul Discriminator": ["bthrow", "b+throw", "back throw"],
    "[VS1] Culminated Power": ["vs1","vskill1"],
    "[VS2] Crawling Beast": ["vs2","vskill2"],
    "Torrent of Power": ["vt1", "vtrigger1"],
    "The Calling": ["vreversal","vrev"],
    # "Clouded Mirror"
    "Clouded Mirror (HOLD BUTTON)": ["vt1 hold", "vtrigger1 hold"],
    "Ceremony of Honor": ["ca", "critical art", "super"],
    "Soul Offering": ["ca vt1", "critical art vt1", "super vt1"],

    # V-TRIGGER 2

    "Eruption of Power": ["vt2", "vtrigger2"]
    # "Heart Of Gold"
}

vegaexact = {
    # CHARACTER: VEGA
    # V-TRIGGER 1   

    "Matador Flash": ["hp>hp>vs1","hp>hp>vskill1"],
    "Matador Flash (Attack)": ["hp>hp>vs1 hold","hp>hp>vskill1 hold"],
    "Rainbow Suplex": ["throw"],
    "Crescent Line": ["bthrow", "b+throw", "back throw"],
    "Stardust Shot": ["jthrow", "j.throw", "air throw"],
    "[VS1] Matador Turn": ["vs1","vskill1"],
    "[VS1] Matador Turn (Hold Button)": ["vs1 hold","vskill1 hold"],
    "[VS2] Matador Flip": ["vs2","vskill2"],
    "[VS2] Cosmic Smart": ["vs2>k","vskill2>k"],
    # "Bloody Kiss - Torero (Projectile)"
    "Bloody Kiss - Torero (Attack)": ["vt1", "vtrigger1"],
    # "Bloody Kiss - Rojo (Projectile)"
    "Bloody Kiss - Rojo (Attack)": ["d+vt1", "d+vtrigger1"],
    # "Bloody Kiss - Azul (Projectile)"
    "Bloody Kiss - Azul (Attack)": ["j.vt1", "j.vtrigger1"],
    "Backslash": ["vreversal+p","vrev+p","vreversal p","vrev p"],
    "Short Backlash": ["vreversal+k","vrev+k","vreversal k","vrev k"],
    "Izuna Drop": ["dp+k>throw"],
    "EX Izuna Drop": ["dp+kk>throw"],
    "Bloody Garden Drop": ["du+kk>throw"],
    "Bloody Rain": ["ca", "critical art", "super"],

    # V-TRIGGER 2

    "Alegrias": ["vt2", "vtrigger2"],
    # "Flash Arch - Rossa (Stance)"
    "Flash Arch - Rossa (Attack)": ["vt2 vt2"],
    "Flash Arch - Granate": ["f+vt2", "f+vtrigger2"]
}

rmikaexact = {
    # CHARACTER: R. MIKA
    # V-TRIGGER 1   

    "Passion Press": ["b+mp","f+mp"],
    "Passion Rope Throw": ["b+mp>b+mp","f+mp>f+mp","b+mp>f+mp","f+mp>b+mp"],
    "Daydream Headlock": ["throw"],
    "Sell Down": ["bthrow", "b+throw", "back throw"],
    "Dream Driver": ["throw cr"],
    "[VS1] Mic Performance": ["vs1","vskill1"],
    "[VS2] Pumped Up!": ["vs2","vskill2"],
    "[VS2] Pumped Up! (upon successful parry)": ["vs2 parry","vskill2 parry"],
    "Nadeshiko (above)": ["vt1", "vtrigger1"], 
    "Nadeshiko (above) (Hold Button)": ["vt1 hold", "vtrigger1 hold"],
    "Nadeshiko (front)": ["b+vt1", "b+vtrigger1"],
    "Nadeshiko (front) (Hold Button)": ["b+vt1 hold", "b+vtrigger1 hold"],
    "Nadeshiko (behind)": ["f+vt1", "f+vtrigger1"],
    "Nadeshiko (behind) (Hold Button)": ["f+vt1 hold", "f+vtrigger1 hold"],
    "Peach Gator": ["vreversal","vrev"],
    "Peach Assault": ["ca", "critical art", "super"],

    # V-TRIGGER 2

    "Steel Chair": ["vt2", "vtrigger2"],
    "Fightin' Dirty": ["vt2 hold", "vtrigger2 hold"]
}

rashidexact = {
    # CHARACTER: RASHID
    # V-TRIGGER 1   

    "Riding Glider": ["throw"],
    "Rising Sun": ["bthrow", "b+throw", "back throw"],
    "[VS1] Front Flip": ["vs1","vskill1"],
    "[VS1] L Airborne Eagle Spike (from V-Skill)": ["vs1>lk"],
    "[VS1] M Airborne Eagle Spike (from V-Skill)": ["vs1>mk"],
    "[VS1] H Airborne Eagle Spike (from V-Skill)": ["vs1>hk"],
    "[VS1] EX Airborne Eagle Spike (from V-Skill)": ["vs1>kk"],
    "[VS1] Rolling Assault": ["d+vs1","d+vskill1"],
    "[VS1] Nail Assault": ["d+vs1>k"],
    "[VS2] Wing Stroke": ["vs2","vskill2"],
    "[VS2] Wing Spike": ["vs2>k"],
    "[VS2]EX Wing Spike": ["vs2>kk"],
    "[VS2] Airborne Wing Stroke": ["j.vs2","jvs2"],
    "Ysaar": ["vt1", "vtrigger1"], 
    "Sliding Roll": ["vreversal","vrev"],
    "L S2pinning Mixer (Rapid Inputs)": ["qcf+lp lv2"],
    "L Spinning Mixer (Additional Rapid Inputs)": ["qcf+lp lv3"],
    "M Spinning Mixer (Rapid Inputs)": ["qcf+mp lv2"],
    "M Spinning Mixer (Additional Rapid Inputs)": ["qcf+mp lv3"],
    "H Spinning Mixer (Rapid Inputs)": ["qcf+hp lv2"],
    "H Spinning Mixer (Additional Rapid Inputs)": ["qcf+hp lv3"],
    "Dash Spinning Mixer (Rapid Inputs)": ["dash f+p lv2"],
    "Dash Spinning Mixer (Additional Rapid Inputs)": ["dash f+p lv3"],
    "Spinning Mixer": ["qcf+p vt1"],
    "EX Spinning Mixer (Rapid Inputs)": ["qcf+pp lv2"],
    "EX Spinning Mixer (Additional Rapid Inputs)": ["qcf+pp lv3"],
    "EX Spinning Mixer": ["qcf+pp vt1"],
    "EX Airborne Eagle Spike": ["qcb+k vt1"],
    "Altair": ["ca", "critical art", "super"],

    # V-TRIGGER 2

    "Easifa": ["vt2", "vtrigger2"]
}

karinexact = {
    # CHARACTER: KARIN
    # V-TRIGGER 1   

    "Hajotsui": ["throw"],
    "Arakuma Inashi": ["bthrow", "b+throw", "back throw"],
    "[VS1] Meioken": ["vs1","vskill1"],
    "[VS1] Meioken (Hold Button)": ["vs1 hold","vskill1 hold"],
    "[VS2] Fudo Sosho": ["vs2","vskill2"],
    "[VS2] Fudo Sosho (Hold Button)": ["vs2 hold","vskill2 hold"],
    "Kanzuki-Ryu Guren No Kata": ["vt1", "vtrigger1"],
    "Ressencho": ["vreversal","vrev"],
    "Tenko": ["qcf+k>p"],
    "Tenko (Fastest)": ["instant tenko"],
    "EX Tenko": ["qcf+kk>p"],
    "Orochi": ["qcf+k>d+p","qcf+k>dp"],
    "EX Orochi": ["qcf+kk>d+p","qcf+kk>dp"],
    "Senha Resshu": ["qcb+p>u+k","qcb+p>uk"],
    "Senha Kusabi": ["qcb+p>d+k","qcb+p>dk"],
    "Guren Hosho": ["qcf+p>p"],
    "Guren Senha": ["qcf+p>u+p","qcf+p>up"],
    "Guren Hochu": ["qcf+p>d+p>d+p","qcf+p>dp>dp"],
    "Guren Resshu": ["qcf+p>u+k","qcf+p>uk"],
    "Guren Kusabi": ["qcf+p>d+k","qcf+p>dk"],
    "Guren Kyoho": ["qcf+p>k"],
    "Kanzuki-Ryu Hadorokushiki Hasha No Kata": ["ca", "critical art", "super"],

    # V-TRIGGER 2

    "Tenha No Kata": ["vt2", "vtrigger2"],
    "Yasha Gaeshi Ten": ["vt2 parry high","vt2 parry mid"],
    "Yasha Gaeshi Chi": ["vt2 parry low"]
}

sethexact = {
    # CHARACTER: SETH
    # V-TRIGGER 1   

    "Tanden Combination": ["mp>hp>vs1","mp>hp>vskill1"],
    "Death Throw": ["throw", "bthrow", "b+throw", "back throw"],
    "[VS1] Tanden Engine": ["vs1","vskill1"],
    "[VS1] Tanden Install": ["vs1>p","vskill1>p"],
    "[VS2] Tanden Booster": ["vs2","vskill2"],
    "[VS2] Tanden Booster (Stop)": ["vs2>vs2"],
    "Tanden Ignition": ["vt1", "vtrigger1"],
    "Calamity Shutter": ["vreversal", "vrev"],
    "Tanden Destruction": ["ca", "critical art", "super"],
    "Tanden Extreme": ["ca vt1", "critical art vt1", "super vt1"],

    # V-TRIGGER 2

    "Tanden Maneuver": ["vt2", "vtrigger2"]
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
        elif char == "ken":
            result = matchExact(move, kenexact)
        elif char == "necalli":
            result = matchExact(move, necalliexact)
        elif char == "vega":
            result = matchExact(move, vegaexact)
        elif char == "rmika":
            result = matchExact(move, rmikaexact)
        elif char == "rashid":
            result = matchExact(move, rashidexact)
        elif char == "karin":
            result = matchExact(move, karinexact)
        elif char == "seth":
            result = matchExact(move, sethexact)

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
