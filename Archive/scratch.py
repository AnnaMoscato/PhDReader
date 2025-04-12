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

input_field = driver.find_element(By.NAME, "9b55bf87-4f96-4bd5-ac5a-77540c6557f8-search")
input_field.send_keys("Artificial intelligence")

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