import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Edge()
# Look through UNSW
driver.get("https://www.unsw.edu.au/research/hdr/find-a-supervisor#search=&sort=relevance&startRank=1&numRanks=12&componentId=36c3802e-58bd-404b-90f6-07d44daf6b35")
dataUNSW = []
UNSWPageCount = 2

while True:
    try:
        buttons = driver.find_elements(By.ID, str("pagination-"+str(UNSWPageCount)))
        nextPageButton = None

        for b in buttons:
            if UNSWPageCount < 10:
                if b.accessible_name == "0"+str(UNSWPageCount) or b.accessible_name == "next":
                    print("Got button")
                    nextPageButton = b

                    break

            else:
                if b.accessible_name == str(UNSWPageCount) or b.accessible_name == "next":
                    print("Got button")
                    nextPageButton = b

                    break

        print("Searching through page")
        researcher = driver.find_elements(By.CLASS_NAME, "card-profile__container")
        for e in researcher:
            row = e.text.split('\n')
            dataUNSW.append(row)
        nextPageButton.click()
        UNSWPageCount +=1

    except:
         print("error found")
         print("Page count: " + str(UNSWPageCount))
         break

 

print("All researchers saved")   

UnswDF = pd.DataFrame(dataUNSW)

print(UnswDF)
 
# Look through UniSyd

driver.get("https://www.sydney.edu.au/research/our-research/find-a-researcher.html?")

UniSydData = []

UniSydPageCount = 2

time.sleep(2) # Click privacy thing

search = driver.find_element(By.ID, "btnAdvSearch")

search.click()

while True:
    try:
        buttons = driver.find_elements(By.CSS_SELECTOR, "a[class='pagination__item']")
        next_page_button = None

        for b in buttons:
            if b.text == str(UniSydPageCount):
                next_page_button = b

        print("Searching through page number " + str(UniSydPageCount))
        researcher = driver.find_elements(By.CLASS_NAME, "grid")
        for e in researcher:
            row = e.text.split('\n')
            UniSydData.append(row)
    except:
        break

driver.quit()

UniSydDF = pd.DataFrame(UniSydData).dropna()

print(UniSydDF)
 
 
# Look through Monash

driver.get("https://www.monash.edu/research/find?faculties=%255B%255D&phdCandidate=true&selectedLevels=%255B%255B%255B%255D%252C%255B%255D%255D%255D&queryText=%21padrenull")

MonashData = []

MonashPageCount = 2

time.sleep(3)
# Have to click the privacy thing

while True:
    try:
        buttons = driver.find_elements(By.TAG_NAME, "button") # initialise all buttons on screen

        print("Collected researchers")
        next_page_button = None

        for b in buttons:
            if b.text == str(MonashPageCount):
                next_page_button = b

                print("got it")
        researcher = driver.find_elements(By.CLASS_NAME, "find-a-researcher__results--card")
        for e in researcher:
            row = e.text.split('\n')
            MonashData.append(row)
        next_page_button.click()
        MonashPageCount+=1

        print("On page " + str(MonashPageCount))
    except:
        break

driver.quit()

MonashDF = pd.DataFrame(MonashData).dropna()

print(MonashDF)
 
# Look through UniMelb

# I'm getting blocked on the UniMelb site

 
# Look through RMIT

 
# Look through UTS

 