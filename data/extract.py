#!/usr/bin/python
import os
import re
import codecs
import json
from bs4 import BeautifulSoup


def cookAnHotSoup(html, characterName):
    soup = BeautifulSoup(html, "lxml")

    # Build a basic data dictionary
    characterData = {}

    # Prelimary cleaning
    soup = clean(soup)

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
            move = {
                'name': '',
                'frame': {
                    'startup': '',
                    'active': '',
                    'recovery': '',
                },
                'recovery': {},
                'vTriggerCancelRecovery': {},
                'cancelInfo': '',
                'damage': '',
                'stun': '',
                'meterGain': '',
                'properties': '',
                'projectileNullification': '',
                'airborneHurtbox': '',
                'comments': ''
            }
            for j, col in enumerate(cols):
                colContent = col.text.strip()
                colContent = colContent.replace("\n", "")
                colContent = colContent.replace("\r", "")
                re.sub(r"\s\s", " ", colContent)
                row.append(colContent)

                if (j == 0):
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
                    move["projectileNullification"] = colContent
                elif (j == 14):
                    move["airborneHurtbox"] = colContent
                elif (j == 15):
                    move["comments"] = colContent

            if (len(row) > 0):
                characterData["vt" + str(tableIndex + 1)].append(move)

    # Save character data in dictionary
    data[characterName] = characterData


def clean(dirtySoup):
    cleanedSoup = dirtySoup
    keyBlockFrames = cleanedSoup.find_all("p", {"class": "keyBlockFrm"})
    for kbf in keyBlockFrames:
        kbf.decompose()
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
    bringSoupToTheTable()

if __name__ == "__main__":
    data = {}
    SOUP_INGREDIENTS_PATH = "pup/htmldumps/"
    SOUP_INGREDIENTS = getSoupIngredients()
    DATA_OUTPUT_DIR = "data/extracted/"
    main()
