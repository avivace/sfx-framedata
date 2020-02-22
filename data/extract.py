#!/usr/bin/python
import os
import re
import codecs
import json
from bs4 import BeautifulSoup

SOUP_INGREDIENTS = "../pup/test.html"

def main():
    # Check if HTML target file exits
    if (os.path.exists(SOUP_INGREDIENTS)):
        try:
            # Read HTML file
            html_content = codecs.open(SOUP_INGREDIENTS, "r", "utf-8")
            if (html_content):
                # Extract data
                cookAnHotSoup(html_content)
                print("Soup is hot and ready to be tasted!")
        except Exception as err:
            print("ERROR: An errore occured while trying to extract the data:")
            print(err)
    else:
        print("\nERROR: Sorry, you don't have all the ingredients you need to cook your soup :(\n(No data source file present)")


def cookAnHotSoup(html):
    soup = BeautifulSoup(html, "lxml")

    # Get character name
    character = soup.select(".titleName")[0].get_text(
        strip=True).replace("Frame List|", "").lower()
    
    # Get main tables (V-Trigger tables)
    vTriggerTables = soup.find_all("table", {"class": "frameTbl"})

    # Extract all table body rows (our actual data)
    absoluteMess = []
    for triggerTable in vTriggerTables:
        rows = triggerTable.find_all("tr")
        for row in rows:
            cols = row.find_all('td')
            row = []
            for col in cols:
                colContent = col.text.strip()
                colContent = colContent.replace("\n|\r", "")
                re.sub(r"\s\s", " ", colContent)
                row.append(colContent)
            absoluteMess.append(row)

    # Build our data dictionary
    data = {}
    data['character'] = character
    data['data'] = absoluteMess

    # Present our delicious soup
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)


if __name__ == "__main__":
    main()
