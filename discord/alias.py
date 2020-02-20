# Move name solver

prefixdict = {
    "Crouching": ["cb"]
}

aliasdict = {

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

	# CHARACTER: RYU
    # V-TRIGGER 1
    "Collarbone Breaker": ["f+MP", "f+mp", "f.mp", "fmp", "overhead"],
    "Solar Plexus Strike": ["f+HP", "f+hp", "f.hp", "fhp"],
    "Axe Kick": ["b+HK", "b+hk", "b.hk", "bhk"],
    "Jodan Nirengeki": ["MP>HP", "mp+hp", "mp hp"],
    "Jodan Sanrengeki": ["MP>HP>HK", "mp+hp+hk", "mp hp hk"],
    "Shoulder Throw": ["throw", "lp+lk", "lplk", "throw"],
    "Somersault Throw": ["b+throw", "b+lp+lk", "blplk", "bthrow", "b+throw", "back throw"],
    "[VS1] Mind's Eye": ["V-Skill 1", "vs1", "vskill1", "v-skill1"],
    "[VS2] Thust Strike": ["V-Skill 2", "vs2", "vskill2", "v-skill2"],
    # da dare come risultato assieme a "[VS2] Thust Strike":
	# "[VS2] Thust Strike (upon successful parry)"
	"Denjin Renki": ["V-Trigger 1", "vt1", "vtrigger1", "v-trigger1"],
    "Hashogeki": ["V-reversal", "vreversal", "v-reversal"],
    "L Hadoken": ["L Fireball", "qcf+lp", "l hadoken"],
    "M Hadoken": ["M Fireball", "qcf+mp", "m hadoken"],
    "H Hadoken": ["H Fireball", "qcf+hp", "h hadoken"],
    "EX Hadoken": ["EX Fireball", "qcf+pp", "ex hadoken"],
    "L Shoryuken": ["L Dragon Punch", "l dp", "l shoryuken"],
    "M Shoryuken": ["M Dragon Punch", "m dp", "m shoryuken"],
    "H Shoryuken": ["H Dragon Punch", "h dp", "h shoryuken"],
    "EX Shoryuken": ["EX Dragon Punch", "ex dp", "ex shoryuken", "giallata"],
    "L Tatsumaki Senpukyaku": ["L Tornado Kick", "qcb+lk", "l tatsu"],
    "M Tatsumaki Senpukyaku": ["M Tornado Kick", "qcb+mk", "m tatsu"],
    "H Tatsumaki Senpukyaku": ["H Tornado Kick", "qcb+hk", "h tatsu"],
    "EX Tatsumaki Senpukyaku": ["EX Tornado Kick", "qcb+kk", "ex tatsu"],
    "Airborne Tatsumaki Senpukyaku": ["Air Tatsu", "j.qcb+k", "air tatsu"],
    "EX Airborne Tatsumaki Senpukyaku": ["EX Air Tatsu", "j.qcb+kk", "ex air tatsu"],
    "L Jodan Sokutou Geri": ["L Donkey Kick", "hcf+lk", "l donkey kick"],
    "M Jodan Sokutou Geri": ["M Donkey Kick", "hcf+mk", "m donkey kick"],
    "H Jodan Sokutou Geri": ["H Donkey Kick", "hcf+hk", "h donkey kick"],
    "EX Jodan Sokutou Geri": ["EX Donkey Kick", "hcf+kk", "ex donkey kick"],
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



def findAlias(text):
    for move in aliasdict:
        for alias in aliasdict[move]:
            if text == alias:
                return move, aliasdict[move][0]