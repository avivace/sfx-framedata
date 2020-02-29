#!/usr/bin/python
import os
import copy
import json
from bs4 import BeautifulSoup

def preFormat(rawSoup):
    formattedSoup = rawSoup

    moveRows = formattedSoup.select(".frameTbl > tbody > tr")

    for moveRow in moveRows:
        if isABodyRow(moveRow):

            # Detect and extract move levels
            extractMoveLevels(formattedSoup, moveRow)

            # Detect and extrac "V" symbol
            extractVTrigger(formattedSoup, moveRow)

            # Detect and extrac VSkill
            extractVSkill(formattedSoup, moveRow)

            moveNameContent = copy.copy(moveRow.td)
            matchCol = formattedSoup.new_tag("td", class_="custom-col extra-col match-col")
            matchCol.string = ""
            if moveNameContent:
                moveNameContent.find(class_="name").decompose()
                matchCol.string = str(moveNameContent).lower().replace("<td class=\"name\">", "").replace("</td>", "")
                matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/1.gif?h=6ecbbeac560a29ef09988f3102c8be9f\"/>", "db")
                matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/2.gif?h=146d9a7c6b006b57d999d5633df090f0\"/>", "d")
                matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/3.gif?h=705de611ba081ecabe11861b0c4047f3\"/>", "df")
                matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/4.gif?h=30f455943bd68bafe11e9359b871465d\"/>", "b")
                matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/6.gif?h=24d3886f118640b674eae14fabd0e016\"/>", "f")
                matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/8.gif?h=9247962a975feda8fd5e99965f18f774\"/>", "u")
                matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/9.gif?h=41302981c9b1fd5c57eb7c11d8980de9\"/>", "uf")
                matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/214.gif?h=b1e91134cef6d20e99b404fae2437195\"/>", "qcb")
                matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/236.gif?h=81e527af198d2e5ddacf0aed44f61cdb\"/>", "qcf")
                matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/421.gif?h=59e10a581b753ed56f0ec4c84b6171de\"/>", "r.dp")
                matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/41236.gif?h=787788efb7ec868b50e3ba62dbc35a31\"/>", "hcf")
                matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/623.gif?h=91ce5a17eb810540f177449f580dc244\"/>", "dp")
                matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/63214.gif?h=94b63ab09919622f1e451e21ffa32412\"/>", "hcb")
                matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/63214789.gif?h=ea94c393814d70e1aedca75b3fc57311\"/>", "360")
                matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/c2.gif?h=7658c782425aef8b1eb937fcc509e195\"/>", "d")
                matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/c4.gif?h=2a138cf782017000f8c40c9f6013b2e3\"/>", "b")
                matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/btn/kick.gif?h=782ca1c7f3e42332887e30ab0a5d37df\"/>", "k")
                matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/next.gif?h=124a6dc32d24b2472cf317a685310f07\"/>", ">")
                matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/btn/punch.gif?h=cdde7fc8901adab4686621a896922c1a\"/>", "p")
                # matchCol.string = re.sub(r"<img.*src=.*1.gif[^<]*\/>", "db", matchCol.string)
                # matchCol.string = re.sub(r"<img.*src=.*2.gif[^<]*\/>", "d", matchCol.string)
                # matchCol.string = re.sub(r"<img.*src=.*3.gif[^<]*\/>", "df", matchCol.string)
                # matchCol.string = re.sub(r"<img.*src=.*4.gif[^<]*\/>", "b", matchCol.string)
                # matchCol.string = re.sub(r"<img.*src=.*6.gif[^<]*\/>", "f", matchCol.string)
                # matchCol.string = re.sub(r"<img.*src=.*8.gif[^<]*\/>", "u", matchCol.string)
                # matchCol.string = re.sub(r"<img.*src=.*9.gif[^<]*\/>", "uf", matchCol.string)
                # matchCol.string = re.sub(r"<img.*src=.*214.gif[^<]*\/>", "qcb", matchCol.string)
                # matchCol.string = re.sub(r"<img.*src=.*236.gif[^<]*\/>", "qcf", matchCol.string)
                # matchCol.string = re.sub(r"<img.*src=.*421.gif[^<]*\/>", "r.dp", matchCol.string)
                # matchCol.string = re.sub(r"<img.*src=.*41236.gif[^<]*\/>", "hcf", matchCol.string)
                # matchCol.string = re.sub(r"<img.*src=.*623.gif[^<]*\/>", "dp", matchCol.string)
                # matchCol.string = re.sub(r"<img.*src=.*63214.gif[^<]*\/>", "hcb", matchCol.string)
                # matchCol.string = re.sub(r"<img.*src=.*63214789.gif[^<]*\/>", "360", matchCol.string)
                # matchCol.string = re.sub(r"<img.*src=.*c2.gif[^<]*\/>", "d", matchCol.string)
                # matchCol.string = re.sub(r"<img.*src=.*c4.gif[^<]*\/>", "b", matchCol.string)
                # matchCol.string = re.sub(r"<img.*src=.*kick.gif[^<]*\/>", "k", matchCol.string)
                # matchCol.string = re.sub(r"<img.*src=.*next.gif[^<]*\/>", ">", matchCol.string)
                # matchCol.string = re.sub(r"<img.*src=.*punch.gif[^<]*\/>", "p", matchCol.string)
                matchCol.string = matchCol.string.replace("<span class=\"key-hkfrm\">h</span>", "h")
                matchCol.string = matchCol.string.replace("<span class=\"key-hpfrm\">h</span>", "h")
                matchCol.string = matchCol.string.replace("<span class=\"key-mpfrm\">m</span>", "m")
                matchCol.string = matchCol.string.replace("<span class=\"key-mkfrm\">m</span>", "m")
                matchCol.string = matchCol.string.replace("<span class=\"key-lpfrm\">l</span>", "l")
                matchCol.string = matchCol.string.replace("<span class=\"key-lkfrm\">l</span>", "l")

                matchCol.string = BeautifulSoup(matchCol.string, "lxml").text
                invertedMoveCodes = ["pl","pm","ph","kl","km","kh"]
                for invMove in invertedMoveCodes:
                    if invMove in matchCol.string:
                        matchCol.string = matchCol.string.replace(invMove, invMove[::-1])
                matchCol.string = matchCol.string.replace("mpmk", "mp+mk")
                matchCol.string = matchCol.string.replace("hphk", "hp+hk")
                matchCol.string = matchCol.string.replace("(during jump)", "j.")
                matchCol.string = matchCol.string.replace("(during forward or back jump)", "j.")
                matchCol.string = matchCol.string.replace("(during vertical jump)", "u")
                matchCol.string = matchCol.string.replace("(during v-trigger ii)", "")
                matchCol.string = matchCol.string.replace("(while crouching)", "cr.")
                matchCol.string = matchCol.string.replace("(hold buttons)", " hold")
                matchCol.string = matchCol.string.replace("(max hold button)", " max hold")
                matchCol.string = matchCol.string.replace("(after holding the button)", "")
                matchCol.string = matchCol.string.replace("(when selecting vskill i)", "")
                matchCol.string = matchCol.string.replace("(when selecting vskill ii)", "")
                
                moveRow.append(matchCol)

    return formattedSoup

def preClean(dirtySoup):
    cleanedSoup = dirtySoup

    # Remove move level symbol in moves name
    removeJunkByClass(cleanedSoup, "p", "keyBlockFrm")

    # Remove additional move info (text between parenthesis)
    removeJunkByClass(cleanedSoup, "span", "cmdPartsText")

    # Remove duplicates for Damage values
    removeJunkByClass(cleanedSoup, "span", "damageTotalOnly")

    # Remove duplicates for Stun values
    removeJunkByClass(cleanedSoup, "span", "stunTotalOnly")

    return cleanedSoup

def getMoveStructure(path):
    with open(path) as json_file:
        structure = json.load(json_file)
        return structure


def getSoupIngredients():
    soupIngredients = []
    for file in os.listdir("pup/htmldumps/"):
        if (file.endswith(".html")):
            soupIngredients.append(file.replace(".html", ""))
    return soupIngredients


def bringSoupToTheTable(outputDir, soupData):
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    with open(f'{outputDir}data.json', 'w') as outfile:
        json.dump(soupData, outfile, indent=4)

def removeJunkByClass(soup, tag, className):
    selectedJunk = soup.find_all(tag, {"class": className})
    for pieceOfJunk in selectedJunk:
        pieceOfJunk.decompose()

def isABodyRow(row):
    headers = row.find_all("th")
    return len(headers) == 0

def extractMoveLevels(soup, moveRow):
    moveLevelFrames = moveRow.find_all(class_=["key-LPFrm","key-MPFrm","key-HPFrm", "key-LKFrm","key-MKFrm","key-HKFrm"])

    foundLevels = []
    moveLevelsCol = soup.new_tag("td", class_="custom-col extra-col move-levels-col")

    for level in moveLevelFrames:
        if level.string not in foundLevels:
            foundLevels.append(level.string)
    
    moveLevelsCol.string = "|".join(foundLevels)
    moveRow.append(moveLevelsCol)

def extractVTrigger(soup, moveRow):
    vTriggerCol = soup.new_tag("td", class_="custom-col extra-col vTrigger-col")
    vTriggerCol.string = ""
    vSymbol = moveRow.find(class_="vt")
    if vSymbol:
        vSymbol.decompose()
        vTriggerCol.string = "Yes"
    moveRow.append(vTriggerCol)

def extractVSkill(soup, moveRow):
    vSkillOne = moveRow.find(text="(WHEN SELECTING VSKILL I)")
    vSkillTWo = moveRow.find(text="(WHEN SELECTING VSKILL II)")
    vSkillCol = soup.new_tag("td", class_="custom-col extra-col vSkill-col")
    vSkillCol.string = ""

    if vSkillOne:
        vSkillCol.string = "1"
    elif vSkillTWo:
        vSkillCol.string = "2"
    
    moveRow.append(vSkillCol)