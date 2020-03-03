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
    "Stealth Dash (Stop)": ["vt2>b", "vtrigger2>b"],
    "Justice Corridor": ["vt2>p", "vtrigger2>p"],
    "Justice Shell": ["vt2>k", "vtrigger2>k"]
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
    "Psycho Crusher": ["psycho crusher"],
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
    "Delta Twist": ["vt2>p","vtrigger2>p"],
    "Reverse Edge": ["vt2>k","vtrigger2>k"]
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
    "Bull Swing": ["bull swing","vt2 chain","chain vt2"],
    "Bull Capture": ["d+vt2", "d+vtrigger2","vt2 low chain","low chain vt2"]
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
    "Clouded Mirror": ["clouded mirror","vt1 leap","leap vt1"],
    "Clouded Mirror (HOLD BUTTON)": ["vt1 hold", "vtrigger1 hold"],
    "Ceremony of Honor": ["ca", "critical art", "super"],
    "Soul Offering": ["ca vt1", "critical art vt1", "super vt1"],

    # V-TRIGGER 2

    "Eruption of Power": ["vt2", "vtrigger2"],
    "Heart Of Gold": ["fb vt2","vt2 fb","heart of gold"]
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
    "Flash Arch - Rossa (Attack)": ["vt2 parry"],
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

zangiefexact = {
    # CHARACTER: ZANGIEF
    # V-TRIGGER 1   

    "Atomic Drop": ["throw"],
    "Captured": ["bthrow", "b+throw", "back throw"],
    "Horosho Chokeslam": ["throw cr"],
    "[VS1] Iron Muscle": ["vs1","vskill1"],
    "[VS1] Iron Muscle (Attack)": ["vs1 hold","vskill1 hold"],
    "[VS1] Iron Muscle (Attack after forward walk)": ["vs1 release","vskill1 release"],
    "[VS2] Super Russian Kick": ["vs2","vskill2"],
    "[VS2] Super Russian Kick (Hold Button)": ["vs2 hold","vskill2 hold"],
    "Cyclone Lariat": ["vt1", "vtrigger1"],
    "Activation Cyclone Lariat": ["vt1 hold", "vtrigger1 hold"],
    "Post-activation Cyclone Lariat": ["vt1 max hold", "vtrigger1 max hold"],
    "Muscle Explosion": ["vreversal","vrev"],
    "Double Lariat": ["ppp"],
    "Bolshoi Russian Suplex": ["ca", "critical art", "super"],

    # V-TRIGGER 2

    "Cossacck Muscle": ["vt2", "vtrigger2"]
}

lauraexact = {
    # CHARACTER: LAURA
    # V-TRIGGER 1   

    "Seoi Throw": ["throw"],
    "Pullback Hold": ["bthrow", "b+throw", "back throw"],
    "[VS1] Volty Line": ["vs1","vskill1"],
    "[VS1] Linear Movement - Avante (Movement)": ["f+vs1","f+vskill1"],
    "[VS1] Linear Movement - Avante (Attack)": ["f+vs1 hold","f+vskill1 hold"],
    "[VS1] Linear Movement - Esquiva (Movement)": ["b+vs1","b+vskill1"],
    "[VS1] Linear Movement - Esquiva (Attack)": ["b+vs1 hold","b+vskill1 hold"],
    "[VS1] Linear Movement - Finta (Movement)": ["b+vs1>vs1"],
    "[VS1] Linear Movement - Finta (Attack)": ["b+vs1>vs1 hold"],
    "[VS2] Volty Sprink": ["vs2","vskill2"],
    "[VS2] Thunder Spike": ["vs2>p"],
    "[VS2] Heavy Heel": ["vs2>k"],
    "[VS2] Thunder Spike Lv.1": ["vs2>p vt1"],
    "[VS2] Thunder Spike Lv.2": ["vs2>p hold vt1"],
    "Spark Show": ["vt1", "vtrigger1"],
    "Double Slap": ["vreversal","vrev"],
    "Inazuma Spin Hold": ["ca", "critical art", "super"],

    # V-TRIGGER 2

    "Shock Stance": ["vt2", "vtrigger2"],
    "Shock Choke": ["vt2>vt2"],
    "Linear Movement - Avante (Movement)": ["vt2>vs1"],
    "Linear Movement - Avante (Attack)": ["vt2>vs1 hold"],
    "Volty Sprink": ["vt2>vs2"],
    "Thunder Spike": ["vt2>vs2>p"],
    "Heavy Heel": ["vt2>vs2>k"]
}

dhalsimexact = {
    # CHARACTER: DHALSIM
    # V-TRIGGER 1   

    "Yoga Rocket": ["throw"],
    "Yoga Hoop": ["bthrow", "b+throw", "back throw"],
    "[VS1] Yoga Float": ["vs1","vskill1"],
    "[VS1] Yoga Float (Airborne)": ["j.vs1","j.vskill1"],
    "[VS2] Yoga Deep Breath": ["vs2","vskill2"],
    "[VS2] Yoga Deep Breath(Airborne)": ["j.vs2","j.vskill2"],
    "Yoga Burner": ["vt1", "vtrigger1"],
    "Yoga Mala": ["vreversal","vrev"],
    "Yoga Fire (VS2 Ver.)": ["qcf+p vs2"],
    "EX Yoga Fire (VS2 Ver.)": ["qcf+pp vs2"],
    "Yoga Teleport": ["dp+ppp","dp+kkk"],
    "Airborne Yoga Teleport": ["j.dp+ppp","j.dp+kkk"],
    "Yoga Sunburst (Lv1)": ["ca", "critical art", "super"],
    "Yoga Sunburst (Lv2)": ["ca hold", "critical art hold", "super hold"],
    "Yoga Sunburst (Lv3)": ["ca max hold", "critical art max hold", "super max hold"],
    "Airborne Yoga Sunburst (Lv1)": ["j.ca", "j.critical art", "j.super"],
    "Airborne Yoga Sunburst (Lv2)": ["j.ca hold", "j.critical art hold", "j.super hold"],
    "Airborne Yoga Sunburst (Lv3)": ["j.ca max hold", "j.critical art max hold", "j.super max hold"],

    # V-TRIGGER 2

    "Yoga Sansara": ["vt2", "vtrigger2"],
    "Airborne Yoga Sansara": ["j.vt2", "j.vtrigger2"]
}

fangexact = {
    # CHARACTER: F.A.N.G
    # V-TRIGGER 1   

    "Senpukuga (Prone)": ["d+ppp"],
    "Senpukuga (Attack)": ["d+ppp>k"],
    "Shimonshu": ["throw"],
    "Kyoshitsugeki": ["bthrow", "b+throw", "back throw"],
    "[VS1] Nishodoku": ["vs1","vskill1"],
    "[VS2] Sodokubu": ["vs2","vskill2"],
    "[VS2] Sodokubu (upon successful parry)": ["vs2 parry","vskill2 parry"],
    "Dokunomu": ["vt1", "vtrigger1"],
    "Nikaiho": ["vreversal","vrev"],
    "EX Ryobenda (Placed Poison)": ["bf+kk poison"],
    "Nikyoushu": ["j.ppp"],
    "Shishiruirui": ["ca", "critical art", "super"],

    # V-TRIGGER 2

    "Koryo Dokuda": ["vt2", "vtrigger2"]
}

alexexact = {
    # CHARACTER: ALEX
    # V-TRIGGER 1   

    "Face-Crush Chop": ["throw"],
    "Leg Tomahawk": ["bthrow", "b+throw", "back throw"],
    "[VS1] Overhaul": ["vs1","vskill1"],
    "[VS2] Overchain": ["vs2","vskill2"],
    "Rage Shift": ["vt1", "vtrigger1"],
    "Big Boot": ["vreversal","vrev"],
    "L Flash Chop (VS2 Ver.)": ["qcf+lp vs2"],
    "M Flash Chop (VS2 Ver.)": ["qcf+mp vs2"],
    "H Flash Chop (VS2 Ver.)": ["qcf+hp vs2"],
    "EX Flash Chop (VS2 Ver.)": ["qcf+pp vs2"],
    "L Slash Elbow (VS2 Ver.)": ["bf+lk vs2"],
    "M Slash Elbow (VS2 Ver.)": ["bf+mk vs2"],
    "H Slash Elbow (VS2 Ver.)": ["bf+hk vs2"],
    "EX Slash Elbow (VS2 Ver.)": ["bf+kk vs2"],
    "L Air Knee Smash (VS2 Ver.)": ["dp+lk vs2"],
    "M Air Knee Smash (VS2 Ver.)": ["dp+mk vs2"],
    "H Air Knee Smash (VS2 Ver.)": ["dp+hk vs2"],
    "EX Air Knee Smash (VS2 Ver.)": ["dp+kk vs2"],
    "L Air Stampede (VS2 Ver.)": ["du+lk vs2"],
    "M Air Stampede (VS2 Ver.)": ["du+mk vs2"],
    "H Air Stampede (VS2 Ver.)": ["du+hk vs2"],
    "EX Air Stampede (VS2 Ver.)": ["du+kk vs2"],
    "Power Drop": ["hcb+p"],
    "EX Power Drop": ["hcb+pp"],
    # "Sledge Hammer (Parry)"
    "Sledge Hammer (Attack)": ["vt1 parry"],
    "Sledge Hammer (Charge Attack)": ["vt1 hold"],
    "Power Drop (Sledge Hammer Version)": ["hcb+p vt1"],
    "EX Power Drop (Sledge Hammer Version)": ["hcb+pp vt1"],
    "Heavy Hammer": ["ca", "critical art", "super"],
    "Heavy Hammer (1st Hit Blocked or Miss)": ["ca miss"],

    # V-TRIGGER 2

    "Rage Boost": ["vt2", "vtrigger2"],
    "Flyng DDT": ["ddt"],
    "Choke Sleeper": ["qcf+p>vt2"]
}

guileexact = {
    # CHARACTER: GUILE
    # V-TRIGGER 1   

    "Knee Bazooka": ["b+lk","f+lk"],
    "Rolling Sobat": ["b+mk","f+mk"],
    "Dragon Suplex": ["throw"],
    "Judo Throw": ["bthrow", "b+throw", "back throw"],
    "Flying Mare": ["jthrow", "j.throw", "air throw"],
    "Flying Buster Chop": ["jbthrow", "j.bthrow", "back air throw","j.b+throw"],
    "[VS1] Sonic Blade": ["vs1","vskill1"],
    "[VS2] Dive Sonic": ["vs2","vskill2"],
    "Solid Puncher": ["vt1", "vtrigger1"],
    "Reverse Back Knuckle": ["vreversal","vrev"],
    "Sonic Break (1st Projectile)":["mini boom","b+vt1","f+vt1"],
    "Sonic Break (additional projectiles)":["vt1>p","bf+p>p"],
    "EX Sonic Break":["bf+pp>p"],
    "Sonic Cross":["vs1>bf+p"],
    "EX Sonic Cross":["vs1>bf+pp"],
    "Sonic Hurricane": ["ca", "critical art", "super"],
    "Sonic Tempest": ["ca vt1", "critical art vt1", "super vt1"],

    # V-TRIGGER 2

    "Knife Edge": ["vt2", "vtrigger2"]
}

ibukiexact = {
    # CHARACTER: IBUKI
    # V-TRIGGER 1   

    # Jumping LP (from H Kasumigake)
    # Jumping HP (from H Kasumigake)
    "Yamikazura": ["throw"],
    "Kubiori": ["bthrow", "b+throw", "back throw"],
    "Tobizaru": ["jthrow", "j.throw", "air throw"],
    "[VS1] Tenrai": ["vs1","vskill1"],
    "[VS1] Tenrai (Hold Button)": ["vs1 hold","vskill1 hold"],
    "[VS2] Makibishi": ["vs2","vskill2"],
    # "[VS2] Makibishi": ["vs2>p"],
    "Rokushaku Horokudama (Akebono)": ["vt1", "d+vt1", "vtrigger1"],
    "Rokushaku Horokudama (Hizakari)": ["b+vt1"],
    "Rokushaku Horokudama (Tasogare)": ["f+vt1"],
    "Hanagasumi": ["vreversal","vrev"],
    "EX L Kunai": ["qcf+lp+mp","qcf+lpmp"],
    "EX M Kunai": ["qcf+lp+hp","qcf+lphp"],
    "EX H Kunai": ["qcf+mp+hp","qcf+mphp"],
    "Kachofugetsu": ["ca", "critical art", "super"],

    # V-TRIGGER 2

    "Fuma Shuriken (Haku)": ["vt2", "vtrigger2"],
    "Fuma Shuriken (Kokufu)": ["b+vt2", "b+vtrigger2"]

}

balrogexact = {
    # CHARACTER: BALROG
    # V-TRIGGER 1   

    "Hard Smasher (3)": ["mk>mp>vs1"],
    "Hard Smasher (4)": ["mk>mp>vs1>p"],
    # "Hard Smasher (4)": ["mk>mp>vs1>k"],
    "OTB": ["mk>mp>vs2"],
    "Stomping Combo (2)": ["d+mk>d+mk"],
    "Dirty Bomber": ["throw"],
    "Dirty Shot": ["bthrow", "b+throw", "back throw"],
    "[VS1] KKB": ["vs1","vskill1"],
    "[VS1] KKB (Cancel)": ["vs1 cancel","vskill1 cancel"],
    "[VS1] Buffalo Swing": ["vs1>p"],
    "[VS1] Buffalo Pressure": ["vs1>k"],
    "[VS2] FFB": ["vs2","vskill2"],
    "Crazy Rush": ["vt1", "vtrigger1"],
    "Buffalo Headbutt": ["vreversal","vrev"],
    "L Dash Straight (VS2 Ver.)": ["bf+lp vs2"],
    "M Dash Straight (VS2 Ver.)": ["bf+mp vs2"],
    "H Dash Straight (VS2 Ver.)": ["bf+hp vs2"],
    "EX Dash Straight (VS2 Ver.)": ["bf+pp vs2"],
    "Charging Buffalo (1)": ["f+p 1 vt1"],
    "Charging Buffalo (2)": ["f+p 2 vt1"],
    "Charging Buffalo (3)": ["f+p 3 vt1"],
    "Charging Buffalo (4)": ["f+p 4 vt1"],
    "EX Charging Buffalo": ["f+pp vt1"],
    "Charging Buffalo (VS2 Ver.) (1)": ["f+p 1 vs2 vt1","f+p 1 vt1 vs2"],
    "Charging Buffalo (VS2 Ver.) (2)": ["f+p 2 vs2 vt1","f+p 2 vt1 vs2"],
    "Charging Buffalo (VS2 Ver.) (3)": ["f+p 3 vs2 vt1","f+p 3 vt1 vs2"],
    "Charging Buffalo (VS2 Ver.) (4)": ["f+p 4 vs2 vt1","f+p 4 vt1 vs2"],
    "EX Charging Buffalo (VS2 Ver.) (1)": ["f+pp 1 vs2 vt1","f+pp 1 vt1 vs2"],
    "EX Charging Buffalo (VS2 Ver.) (2)": ["f+pp 2 vs2 vt1","f+pp 2 vt1 vs2"],
    "Bursting Buffalo (1)": ["f+k 1 vt1"],
    "Bursting Buffalo (2)": ["f+k 2 vt1"],
    "Bursting Buffalo (3)": ["f+k 3 vt1"],
    "Bursting Buffalo (4)": ["f+k 4 vt1"],
    "EX Bursting Buffalo": ["f+kk vt1"],
    "Turn Punch (Lv1)": ["tap lv1"],
    "Turn Punch (Lv2)": ["tap lv2"],
    "Turn Punch (Lv3)": ["tap lv3"],
    "Turn Punch (Lv4)": ["tap lv4"],
    "Turn Punch (Lv5)": ["tap lv5"],
    "Turn Punch (Lv6)": ["tap lv6"],
    "Turn Punch (Lv7)": ["tap lv7"],
    "Turn Punch (Lv8)": ["tap lv8"],
    "Turn Punch (Lv9)": ["tap lv9"],
    "Turn Punch (FINAL)": ["tap lv10"],
    "Gigaton Blow": ["ca", "critical art", "super"],

    # V-TRIGGER 2

    "No Mercy": ["vt2", "vtrigger2"],
    "B3": ["vt2 command grab","vt2 grab"]

}

juriexact = {
    # CHARACTER: JURI
    # V-TRIGGER 1   

    "Standing LP (Chain Combo)": ["lp chain"],
    "Standing MP (Chain Combo)": ["mp chain"],
    "Standing HP (Chain Combo)": ["hp chain"],
    "Standing LK (Chain Combo)": ["lk chain"],
    "Standing MK (Chain Combo)": ["mk chain"],
    "Standing HK (Chain Combo)": ["hk chain"],
    "Crouching LP (Chain Combo)": ["cr.lp chain"],
    "Crouching MP (Chain Combo)": ["cr.mp chain"],
    "Crouching HP (Chain Combo)": ["cr.hp chain"],
    "Crouching LK (Chain Combo)": ["cr.lk chain"],
    "Crouching MK (Chain Combo)": ["cr.mk chain"],
    "Crouching HK (Chain Combo)": ["cr.hk chain"],
    "Jumping MP (Chain Combo)": ["j.mp chain"],
    "Jumping HP (Chain Combo)": ["j.hp chain"],
    "Jumping MK (Chain Combo)": ["j.mk chain"],
    "Jumping HK (Chain Combo)": ["j.hk chain"],
    "Kyoretsushu": ["mp>f+hp","mp>b+hp"],
    "Chisenkyaku": ["throw"],
    "Kaeikyaku": ["bthrow", "b+throw", "back throw"],
    "Zankasen": ["jthrow", "j.throw", "air throw"],
    "[VS1] Kasatushu (Whiff)": ["vs1","vskill1"],
    "[VS1] Kasatushu Lv.1": ["vs1 lv1","vskill1 lv1"],
    "[VS1] Kasatushu Lv.2": ["vs1 lv2","vskill1 lv2"],
    "[VS1] Kasatushu Lv.2 (Instant Activation Version)": ["vs1 lv2 instant"],
    "[VS2] Fuha Enzan (Charge)": ["vs2 store","vskill2 store"],
    "[VS2] Fuha Enzan (Attack)": ["vs2","vskill2"],
    "Feng Shui Enngine Type Alpha": ["vt1", "vtrigger1"],
    "Kaisenrenkyaku": ["vreversal","vrev"],
    "Fuharenkyaku (Charge Kick)": ["store"],
    "Sakkai Fuhazan": ["ca", "critical art", "super"],

    # V-TRIGGER 2

    "Feng Shui Enngine beta": ["vt2", "vtrigger2"]

}

urienexact = {
    # CHARACTER: URIEN
    # V-TRIGGER 1   

    "Spartan Bomb (Forward)": ["throw"],
    "Spartan Bomb (Back)": ["bthrow", "b+throw", "back throw"],
    "[VS1] Metallic Aura": ["vs1","vskill1"],
    "[VS2] Indignant Thunder": ["vs2","vskill2"],
    "Aegis Reflector (Forward)": ["b+vt1", "b+vtrigger1"],
    "Aegis Reflector (Back)": ["vt1", "vtrigger1", "f+vt1", "f+vtrigger1"],
    "Aegis Reflector (Up)": ["d+vt1", "d+vtrigger1"],
    "Anger Snap Fist": ["vreversal","vrev"],
    "EX L Metallic Sphere": ["qcf+lp+mp","qcf+lpmp"],
    "EX M Metallic Sphere": ["qcf+lp+hp","qcf+lphp"],
    "EX H Metallic Sphere": ["qcf+mp+hp","qcf+mphp"],
    "EX L Metallic Sphere (Hold Button)": ["qcf+lp+mp hold","qcf+lpmp hold"],
    "EX M Metallic Sphere (Hold Button)": ["qcf+lp+hp hold","qcf+lphp hold"],
    "EX H Metallic Sphere (Hold Button)": ["qcf+mp+hp hold","qcf+mphp hold"],
    "L Metallic Sphere (VS2 Ver.)": ["qcf+lp vs2"],
    "M Metallic Sphere (VS2 Ver.)": ["qcf+mp vs2"],
    "H Metallic Sphere (VS2 Ver.)": ["qcf+hp vs2"],
    "EX Metallic Sphere L (VS2 Ver.)": ["qcf+lp+mp vs2", "qcf+lpmp vs2"],
    "EX Metallic Sphere M (VS2 Ver.)": ["qcf+lp+hp vs2", "qcf+lphp vs2"],
    "EX Metallic Sphere H (VS2 Ver.)": ["qcf+mp+hp vs2", "qcf+mphp vs2"],
    "2nd Aegis Reflector (Forward)": ["b+aegis"],
    "2nd Aegis Reflector (Back)": ["aegis", "f+aegis"],
    "2nd Aegis Reflector (Up)": ["d+aegis"],
    "Dominant Crush": ["ca", "critical art", "super"],

    # V-TRIGGER 2

    "Tyrant Pressure": ["vt2", "vtrigger2"],
    "Tyrant Blaze": ["vt2 tackle", "tackle vt2"],
    "Tyrant Blaze (Charge Attack)": ["vt2 tackle hold", "tackle vt2 hold"]
}

akumaexact = {
    # CHARACTER: AKUMA
    # V-TRIGGER 1   

    "Goshoha": ["throw", "lp+lk"],
    "Shuretsuzan": ["bthrow", "b+throw", "back throw"],
    "[VS1] Rakan": ["vs1","vskill1"],
    "[VS1] Rakan Gosho": ["vs1>p"],
    "[VS1] Rakan Gokyaku": ["vs1>k"],
    "[VS2] Kiai": ["vs2","vskill2"],
    "[VS2] Sekia Goshoha": ["vs2>hcb+p"],
    "[VS2] EX Sekia Goshoha": ["vs2>hcb+pp"],
    "Dohatsu Shoten": ["vt1", "vtrigger1"],
    "Gosenkyaku": ["vreversal","vrev"],
    "Ashura Senku (Forward)": ["dp+kkk"],
    "Ashura Senku (Back)": ["r.dp+kkk"],
    "Hyakki Gozan": ["hcf+k>"],
    "Hyakki Gosho": ["hcf+k>p"],
    "Hyakki Gojin": ["hcf+k>k"],
    "Hyakki Gosai": ["hcf+k>lp+lk", "hcf+k>lplk", "hcf+k>throw"],
    "EX Hyakki Gozan": ["hcf+kk>"],
    "EX Hyakki Gosho": ["hcf+kk>p"],
    "EX Hyakki Gojin": ["hcf+kk>k"],
    "EX Hyakki Gosai": ["hcf+kk>lp+lk", "hcf+kk>lplk", "hcf+kk>throw"],
    "Hyakki Gozanku (On startup hit)": ["hcf+kk>qcf+p"],
    "Hyakki Gorasen": ["hcf+kk>qcb+k"],
    "Gohadoken": ["qcf+p vt1"],
    "Zanku Hadoken": ["j.qcf+p vt1"],
    "Sekia Kuretsuha": ["ca", "critical art", "super"],
    "Shun Goku Satsu": ["demon"],

    # V-TRIGGER 2

    "Shiretsu Hasshi": ["vt2", "vtrigger2"],
    "Gohadoken": ["qcf+pp vt2"],
    "Sekia Goshoha": ["hcb+pp vt2"],
    "EX Zanku Hadoken (On release hit)": ["j.qcf+pp vt2"],
    "Goshoryuken": ["dp+pp vt2"],
    "Tatsumaki Zankukyaku": ["qcb+kk vt2"],
    "Airborne Tatsumaki Zankukyaku": ["j.qcb+kk vt2"],
    "Hyakkishu": ["hcf+kk vt2"]

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
    elif char == "mika":
        char = "rmika"
    elif char == "sim":
        char = "dhalsim"
    elif char == "claw":
        char = "vega"
    elif char == "dictator":
        char = "mbison"
    elif char == "boxer":
        char = "balrog"
    elif char == "rog":
        char = "balrog"
    elif char == "honda":
        char = "ehonda"
    
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
        elif char == "zangief":
            result = matchExact(move, zangiefexact)
        elif char == "laura":
            result = matchExact(move, lauraexact)
        elif char == "dhalsim":
            result = matchExact(move, dhalsimexact)
        elif char == "fang":
            result = matchExact(move, fangexact)
        elif char == "alex":
            result = matchExact(move, alexexact)
        elif char == "guile":
            result = matchExact(move, guileexact)
        elif char == "ibuki":
            result = matchExact(move, ibukiexact)
        elif char == "balrog":
            result = matchExact(move, balrogexact)
        elif char == "juri":
            result = matchExact(move, juriexact)
        elif char == "urien":
            result = matchExact(move, urienexact)
        elif char == "akuma":
            result = matchExact(move, akumaexact)
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
