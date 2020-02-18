
prefixdict = {
	"Crouching" : ["cb"]
}

aliasdict = {
	"LP" : ["jab", "lp"],
	"MP" : ["AAAA"],
	"Collarbone Breaker" : ["f+mp"],

}

def findAlias(text):
	for move in aliasdict:
		for alias in aliasdict[move]:
			if text == alias:
				return move
