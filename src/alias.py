
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
	"cr.LP" : ["cr.lp", "cr.jab"],
	"cr.MP" : ["cr.mp", "cr.strong"],
	"cr.HP" : ["cr.hp", "cr.fierce"],
	"cr.LK" : ["cr.lk", "cr.short"],
	"cr.MK" : ["cr.mk", "cr.forward"],
	"cr.HK" : ["cr.hk", "sweep", "spazzata"],
	"j.LP" : ["j.lp", "j.jab"],
	"j.MP" : ["j.mp", "j.strong"],
	"j.HP" : ["j.hp", "j.fierce"],
	"j.LK" : ["j.lk", "j.short"],
	"j.MK" : ["j.mk", "j.forward"],
	"j.HK" : ["j.hk", "j.roundhouse"],
	"f+MP" : ["f+mp"],
	"f+HP" : ["f+hp"],
	"b+HK" : ["b+hk"],
	"MP>HP" : ["mp+hp"],
	"MP>HP>HK" : ["mp+hp+hk"],
	"throw" : ["lp+lk", "throw"],
	"b+throw" : ["b+lp+lk", "b+throw"]
}

def findAlias(text):
	for move in aliasdict:
		for alias in aliasdict[move]:
			if text == alias:
				return move
