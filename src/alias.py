
prefixdict = {
	"Crouching" : ["cb"]
}

aliasdict = {
	"LP" : ["lp", "jab"],
	"MP" : ["mp", "strong"],
	"HP" : ["hp", "fierce"],
	"LK" : ["lk", "short"],
	"MK" : ["mk", "forward"],
	"HK" : ["hk", "roundhouse"],
	"cr.LP" : ["cr.lp", "crlp", "cr.jab"],
	"cr.MP" : ["cr.mp", "crmp", "cr.strong"],
	"cr.HP" : ["cr.hp", "crhp", "cr.fierce"],
	"cr.LK" : ["cr.lk", "crlk", "cr.short"],
	"cr.MK" : ["cr.mk", "crmk", "cr.forward"],
	"cr.HK" : ["cr.hk", "crhk", "sweep", "spazzata"],
	"j.LP" : ["j.lp", "jlp", "j.jab"],
	"j.MP" : ["j.mp", "jmp", "j.strong"],
	"j.HP" : ["j.hp", "jhp", "j.fierce"],
	"j.LK" : ["j.lk", "jlk", "j.short"],
	"j.MK" : ["j.mk", "jmk", "j.forward"],
	"j.HK" : ["j.hk", "jhk", "j.roundhouse"],
	"f+MP" : ["f+mp", "f.mp", "fmp", "overhead"],
	"f+HP" : ["f+hp", "f.hp", "fhp"],
	"b+HK" : ["b+hk", "b.hk", "bhk"],
	"MP>HP" : ["mp+hp", "mphp"],
	"MP>HP>HK" : ["mp+hp+hk", "mphphk"],
	"throw" : ["lp+lk", "lplk", "throw"],
	"b+throw" : ["b+lp+lk", "blplk", "bthrow", "b+throw", "back throw"],
	"VS1" : ["vs1", "vskill1", "v-skill1"],
	"VS2" : ["vs2", "vskill2", "v-skill2"],
	"VT1" : ["vt1", "vtrigger1", "v-trigger1"],
	"V-reversal" : ["vreversal", "v-reversal"],
	"L Hadoken" : ["qcf+lp", "l hadoken"],
	"M Hadoken" : ["qcf+mp", "m hadoken"],
	"H Hadoken" : ["qcf+hp", "h hadoken"],
	"EX Hadoken" : ["qcf+pp", "ex hadoken"],
	"L Shoryuken" : ["l dp", "l shoryuken"],
	"M Shoryuken" : ["m dp", "m shoryuken"],
	"H Shoryuken" : ["h dp", "h shoryuken"],
	"EX Shoryuken" : ["ex dp", "ex shoryuken", "giallata"],
	"L Tatsu" : ["qcb+lk", "l tatsu"],
	"M Tatsu" : ["qcb+mk", "m tatsu"],
	"H Tatsu" : ["qcb+hk", "h tatsu"],
	"EX Tatsu" : ["qcb+kk", "ex tatsu"],
	"L Donkey Kick" : ["hcf+lk", "l donkey"],
	"M Donkey Kick" : ["hcf+mk", "m donkey"],
	"H Donkey Kick" : ["hcf+hk", "h donkey"],
	"EX Donkey Kick" : ["hcf+kk", "ex donkey"],
	"CA" : ["ca", "critical art", "super"]
}

def findAlias(text):
	for move in aliasdict:
		for alias in aliasdict[move]:
			if text == alias:
				return move
