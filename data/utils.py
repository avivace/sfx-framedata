#!/usr/bin/python
import os
import copy
import json
from bs4 import BeautifulSoup

def preFormat(rawSoup):
    formattedSoup = rawSoup

    moveRows = formattedSoup.select(".frameTbl > tbody > tr")

    with open("./data/data-mapping.json") as json_file:
        mapping = json.load(json_file)

    for moveRow in moveRows:
        if isABodyRow(moveRow):

            # Detect and extract move levels
            extractMoveLevels(formattedSoup, moveRow)

            # Detect and extract "V" symbol
            extractVTrigger(formattedSoup, moveRow)

            # Detect and extract VSkill
            extractVSkill(formattedSoup, moveRow)

            moveNameContent = copy.copy(moveRow.td)
            matchCol = formattedSoup.new_tag("td", class_="custom-col extra-col match-col")
            matchCol.string = ""
            if moveNameContent:
                moveNameContent.find(class_="name").decompose()

                # HTML PHASE
                matchCol.string = str(moveNameContent).lower().replace("<td class=\"name\">", "").replace("</td>", "")

                # Parse images into commands keys
                images = mapping["soup"]["images"]
                parseImages(images, matchCol)
                
                # Parse tags into move levels keys
                tags = mapping["soup"]["tags"]
                parseContent(tags, matchCol)

                # TEXT ONLY PHASE
                # Strip HTML tags away
                matchCol.string = BeautifulSoup(matchCol.string, "lxml").text

                # Reverse move/level order
                reverseMoveAndLevels(matchCol)

                # Parse known strings
                strings = mapping["soup"]["strings"]
                parseContent(strings, matchCol)
                
                # Append match column to soup
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

def parseImages(images, col):
    for image in images:
        col.string = col.string.replace(f"<img class=\"cmd-image-s\" src=\"{image}\"/>", images[image])

def parseContent(elements, col):
    for el in elements:
        col.string = col.string.replace(el, elements[el])

def reverseMoveAndLevels(col):
    invertedMoveCodes = ["pl","pm","ph","kl","km","kh"]
    for invMove in invertedMoveCodes:
        if invMove in col.string:
            col.string = col.string.replace(invMove, invMove[::-1])