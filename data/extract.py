#!/usr/bin/python
import os
import re
import codecs
import json
import copy
from bs4 import BeautifulSoup


def cookAnHotSoup(html, characterName):
    soup = BeautifulSoup(html, "lxml")

    # Build a basic data dictionary
    characterData = {}

    # Prelimary cleaning
    soup = preClean(soup)

    # Get main tables (V-Trigger tables)
    vTriggerTables = soup.find_all("table", {"class": "frameTbl"})

    for i in range(0, len(vTriggerTables)):
        characterData['vt' + str(i + 1)] = []

    # Extract all table body rows (our actual data)
    for tableIndex, triggerTable in enumerate(vTriggerTables):
        rows = triggerTable.find_all("tr")
        for i, row in enumerate(rows):
            cols = row.find_all('td')
            row = []
            move = getMoveStructure(MOVE_STRUCTURE_PATH)
            for j, col in enumerate(cols):
                colContent = col.text.strip()
                colContent = colContent.replace("\n", " ")
                colContent = colContent.replace("\r", " ")
                colContent = re.sub(r"\s+", " ", colContent)
                row.append(colContent)

                if (j == 0):
                    colContent = colContent.replace("+", "")
                    move["name"] = colContent
                elif (j == 1):
                    move["frame"]["startup"] = colContent
                elif (j == 2):
                    move["frame"]["active"] = colContent
                elif (j == 3):
                    move["frame"]["recovery"] = colContent
                elif (j == 4):
                    move["recovery"]["onHit"] = colContent
                elif (j == 5):
                    move["recovery"]["onBlock"] = colContent
                elif (j == 6):
                    move["vTriggerCancelRecovery"]["onHit"] = colContent
                elif (j == 7):
                    move["vTriggerCancelRecovery"]["onBlock"] = colContent
                elif (j == 8):
                    move["cancelInfo"] = colContent
                elif (j == 9):
                    move["damage"] = colContent
                elif (j == 10):
                    move["stun"] = colContent
                elif (j == 11):
                    move["meterGain"] = colContent
                elif (j == 12):
                    move["properties"] = colContent
                elif (j == 13):
                    if (colContent):
                        move["projectileNullification"] = colContent and "Yes"
                elif (j == 14):
                    move["airborneHurtbox"] = colContent
                elif (j == 15):
                    # Remove Japanese characters
                    colContent = colContent.encode('ascii', 'ignore').decode('unicode_escape')
                    move["comments"] = colContent
                elif (j == 16):
                    move["vTrigger"] = colContent
                elif (j == 17):
                    move["matchCol"] = colContent
                elif (j == 18):
                    move["dirtyMatchCol"] = colContent

            if (len(row) > 0):
                characterData["vt" + str(tableIndex + 1)].append(move)

    # Save character data in dictionary
    data[characterName] = characterData


def getMoveStructure(path):
    with open(path) as json_file:
        structure = json.load(json_file)
        return structure


def preClean(dirtySoup):
    cleanedSoup = dirtySoup

    # Colooorssss
    moveRows = cleanedSoup.select(".frameTbl > tbody > tr")

    for moveRow in moveRows:
    #     moveLevelFrame = moveRow.find(class_=["key-LPFrm","key-MPFrm","key-HPFrm"])
    #     moveLevelKey = moveLevelFrame and moveLevelFrame.string
        
    #     if moveLevelKey:
    #         moveLevelCol = cleanedSoup.new_tag("td", class_="custom-col extra-col move-level-col")
    #         moveLevelCol.string = moveLevelKey
    #         moveRow.append(moveLevelCol)

        # Move away "V" symbol
        vTriggerCol = cleanedSoup.new_tag("td", class_="custom-col extra-col vTrigger-col")
        vTriggerCol.string = ""
        vSymbol = moveRow.find(class_="vt")
        if vSymbol:
            vTriggerCol.string = "Yes"
        moveRow.append(vTriggerCol)

        invertedMoveCodes = ["pl","pm","ph","kl","km","kh"]

        moveNameContent = copy.copy(moveRow.td)
        matchCol = cleanedSoup.new_tag("td", class_="custom-col extra-col match-col")
        matchCol.string = ""
        if moveNameContent:
            # moveNameContent.find(class_="name").decompose()
            matchCol.string = str(moveNameContent).lower().replace("<td class=\"name\">", "").replace("</td>", "")
            matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/1.gif?h=6ecbbeac560a29ef09988f3102c8be9f\"/>", "db")
            matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/2.gif?h=146d9a7c6b006b57d999d5633df090f0\"/>", "d")
            matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/3.gif?h=705de611ba081ecabe11861b0c4047f3\"/", "df")
            matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/4.gif?h=30f455943bd68bafe11e9359b871465d\"/>", "b")
            # matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/5.gif?h=5c61278719e2dea3e98b59650f7f9a29\"/>", "")
            matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/6.gif?h=24d3886f118640b674eae14fabd0e016\"/>", "f")
            matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/9.gif?h=41302981c9b1fd5c57eb7c11d8980de9\"/>", "uf")
            matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/214.gif?h=b1e91134cef6d20e99b404fae2437195\"/>", "qcb")
            matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/236.gif?h=81e527af198d2e5ddacf0aed44f61cdb\"/>", "qcf")
            matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/421.gif?h=59e10a581b753ed56f0ec4c84b6171de\"/>", "r.dp")
            matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/41236.gif?h=787788efb7ec868b50e3ba62dbc35a31\"/>", "hcf")
            matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/623.gif?h=91ce5a17eb810540f177449f580dc244\"/>", "dp")
            matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/63214.gif?h=94b63ab09919622f1e451e21ffa32412\"/>", "hcb")
            matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/key/63214789.gif?h=ea94c393814d70e1aedca75b3fc57311\"/>", "360")
            matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/btn/kick.gif?h=782ca1c7f3e42332887e30ab0a5d37df\"/>", "k")
            matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/next.gif?h=124a6dc32d24b2472cf317a685310f07\"/>", ">")
            matchCol.string = matchCol.string.replace("<img class=\"cmd-image-s\" src=\"https://game.capcom.com/cfn/sfv/as/img/cmd/btn/punch.gif?h=cdde7fc8901adab4686621a896922c1a\"/>", "p")
            matchCol.string = matchCol.string.replace("<span class=\"key-hkfrm\">h</span>", "h")
            matchCol.string = matchCol.string.replace("<span class=\"key-hpfrm\">h</span>", "h")
            matchCol.string = matchCol.string.replace("<span class=\"key-mpfrm\">m</span>", "m")
            matchCol.string = matchCol.string.replace("<span class=\"key-mkfrm\">m</span>", "m")
            matchCol.string = matchCol.string.replace("<span class=\"key-lpfrm\">l</span>", "l")
            matchCol.string = matchCol.string.replace("<span class=\"key-lkfrm\">l</span>", "l")
            matchCol.string = matchCol.string.replace("(during jump)", "j.")
            matchCol.string = matchCol.string.replace("(during forward or back jump)", "j.")
            matchCol.string = matchCol.string.replace("(during vertical jump)", "u")
            matchCol.string = matchCol.string.replace("(while crouching)", "cr.")
            # matchCol.string = matchCol.string.replace("or", "")
            dirtyMatchCol =  copy.copy(matchCol)
            matchCol.string = BeautifulSoup(matchCol.string, "lxml").text
            for invMove in invertedMoveCodes:
                if invMove in matchCol.string:
                    matchCol.string = matchCol.string.replace(invMove, invMove[::-1])
            moveRow.append(matchCol)
            moveRow.append(dirtyMatchCol)


    # Remove move level symbol in moves name
    keyBlockFrames = cleanedSoup.find_all("p", {"class": "keyBlockFrm"})
    for kbf in keyBlockFrames:
        kbf.decompose()

    # Remove additional move info (text between parenthesis)
    addInfoTexts = cleanedSoup.find_all("span", { "class": "cmdPartsText"})
    for addInfoText in addInfoTexts:
        addInfoText.decompose()

    # Remove duplicates for Damage values
    duplicateDamages = cleanedSoup.find_all("span", { "class": "damageTotalOnly"})
    for duplicateDamage in duplicateDamages:
        duplicateDamage.decompose()
    
    # Remove duplicates for Stun values
    duplicateStuns = cleanedSoup.find_all("span", { "class": "stunTotalOnly"})
    for duplicateStun in duplicateStuns:
        duplicateStun.decompose()

    return cleanedSoup


def getSoupIngredients():
    soupIngredients = []
    for file in os.listdir("pup/htmldumps/"):
        if (file.endswith(".html")):
            soupIngredients.append(file.replace(".html", ""))
    return soupIngredients


def bringSoupToTheTable():
    # Present our delicious soup
    if not os.path.exists(DATA_OUTPUT_DIR):
        os.makedirs(DATA_OUTPUT_DIR)

    with open(f'{DATA_OUTPUT_DIR}data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)


def main():
    print("\nEXTRACTING DATA\nCooking a delicious soup...")
    for characterName in SOUP_INGREDIENTS:
        INGREDIENT = SOUP_INGREDIENTS_PATH + characterName + ".html"
        # Check if HTML target file exits
        if (os.path.exists(INGREDIENT)):
            try:
                # Read HTML file
                html_content = codecs.open(INGREDIENT, "r", "utf-8")
                if (html_content):
                    # Extract data
                    cookAnHotSoup(html_content, characterName)
            except Exception as err:
                print("ERROR: An error occured while trying to extract the data:")
                print(err)
        else:
            print(
                "\nERROR: Sorry, you don't have all the ingredients you need to cook your soup :(\n(No data source file present)")

    # Save file
    print("\nDONE\nSoup is hot and ready to be tasted!")
    bringSoupToTheTable()


if __name__ == "__main__":
    data = {}
    SOUP_INGREDIENTS_PATH = "pup/htmldumps/"
    SOUP_INGREDIENTS = getSoupIngredients()
    DATA_OUTPUT_DIR = "data/extracted/"
    MOVE_STRUCTURE_PATH = "data/move-structure.json"
    main()
