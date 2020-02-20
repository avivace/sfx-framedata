# Move name solver

prefixdict = {
	"Crouching" : ["cb"]
}

aliasdict = {

	# "TABLE NAME" : ["FRIENDLY OFFICIAL NAME", "FRIENDLY ALIAS 1", "FRIENDLY ALIAS 2", [...]]
	"TODO" : ["LP","lp", "jab"],
	"TODO" : ["MP","mp", "strong"],
	"TODO" : ["HP","hp", "fierce"],
	"TODO" : ["LK","lk", "short"],
	"TODO" : ["MK","mk", "forward"],
	"TODO" : ["HK","hk", "roundhouse"],
	"TODO" : ["cr.LP","cr.lp", "crlp", "cr.jab"],
	"TODO" : ["cr.MP","cr.mp", "crmp", "cr.strong"],
	"TODO" : ["cr.HP","cr.hp", "crhp", "cr.fierce"],
	"TODO" : ["cr.LK","cr.lk", "crlk", "cr.short"],
	"TODO" : ["cr.MK","cr.mk", "crmk", "cr.forward"],
	"TODO" : ["cr.HK","cr.hk", "crhk", "sweep", "spazzata"],
	"TODO" : ["j.LP","j.lp", "jlp", "j.jab"],
	"TODO" : ["j.MP","j.mp", "jmp", "j.strong"],
	"TODO" : ["j.HP","j.hp", "jhp", "j.fierce"],
	"TODO" : ["j.LK","j.lk", "jlk", "j.short"],
	"TODO" : ["j.MK","j.mk", "jmk", "j.forward"],
	"TODO" : ["j.HK","j.hk", "jhk", "j.roundhouse"],
	"TODO" : ["f+MP","f+mp", "f.mp", "fmp", "overhead"],
	"TODO" : ["f+HP","f+hp", "f.hp", "fhp"],
	"TODO" : ["b+HK","b+hk", "b.hk", "bhk"],
	"TODO" : ["MP>HP","mp+hp", "mphp"],
	"TODO" : ["MP>HP>HK","mp+hp+hk", "mphphk"],
	"TODO" : ["throw","lp+lk", "lplk", "throw"],
	"TODO" : ["b+throw","b+lp+lk", "blplk", "bthrow", "b+throw", "back throw"],
	"TODO" : ["VS1","vs1", "vskill1", "v-skill1"],
	"TODO" : ["VS2","vs2", "vskill2", "v-skill2"],
	"TODO" : ["VT1","vt1", "vtrigger1", "v-trigger1"],
	"TODO" : ["V-reversal","vreversal", "v-reversal"],
	"TODO" : ["L Hadoken","qcf+lp", "l hadoken"],
	"TODO" : ["M Hadoken","qcf+mp", "m hadoken"],
	"TODO" : ["H Hadoken","qcf+hp", "h hadoken"],
	"TODO" : ["EX Hadoken","qcf+pp", "ex hadoken"],
	"TODO" : ["L Shoryuken","l dp", "l shoryuken"],
	"TODO" : ["M Shoryuken","m dp", "m shoryuken"],
	"TODO" : ["H Shoryuken","h dp", "h shoryuken"],
	"TODO" : ["EX Shoryuken","ex dp", "ex shoryuken", "giallata"],
	"TODO" : ["L Tatsu","qcb+lk", "l tatsu"],
	"TODO" : ["M Tatsu","qcb+mk", "m tatsu"],
	"TODO" : ["H Tatsu","qcb+hk", "h tatsu"],
	"TODO" : ["EX Tatsu","qcb+kk", "ex tatsu"],
	"TODO" : ["L Donkey Kick","hcf+lk", "l donkey"],
	"TODO" : ["M Donkey Kick","hcf+mk", "m donkey"],
	"TODO" : ["H Donkey Kick","hcf+hk", "h donkey"],
	"TODO" : ["EX Donkey Kick","hcf+kk", "ex donkey"],
	"TODO" : ["CA","ca", "critical art", "super"]
}

def findAlias(text):
	for move in aliasdict:
		for alias in aliasdict[move]:
			if text == alias:
				return move, aliasdict[move][0]