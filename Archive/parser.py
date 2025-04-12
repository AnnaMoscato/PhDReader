import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

class UniversityScraper():
    def __init__(self, url : str, input_field_id : tuple[By, str], submit_button_id : tuple[By, str],
                  input_search_text : str, button_search_function, buttons_id : tuple[By, str], researchers_id : tuple[By, str]) -> None:
        print("Initialising webdriver")
        self.driver = webdriver.Edge()
        self.driver.get(url)

        print("Initialising variables")
        self.data = []
        self.button_search_function = button_search_function
        self.buttons_by, self.buttons_id = buttons_id
        self.researchers_by, self.researchers_id = researchers_id 
        self.page_count = 2

        try:
            input_field = self.driver.find_element(input_field_id[0], input_field_id[1])
            input_field.clear()
            input_field.send_keys(input_search_text)
        except Exception as e:
            print(f"Error found when inputting search text: {e}")

        try:
            submit_button = self.driver.find_element(submit_button_id[0], submit_button_id[1])
            submit_button.click()
        except Exception as e:
            print(f"Error found when clicking submit button: {e}")

        print("Sleeping for 3 seconds so page can reload")
        time.sleep(3)

    def find_button(self):
        try: 
            buttons = self.driver.find_elements(self.buttons_by, self.buttons_id+str(self.page_count))
            next_page_button = None
            for b in buttons: 
                print(f"accessible name: {b.accessible_name} of button {b}")
                if self.button_search_function(self.page_count, b):
                    next_page_button = b
            if next_page_button is None:
                print("No button was found")
            self.button = next_page_button
        except Exception as e:
            print(f"Error found while looking for button: {e}")
    
    def get_researchers(self):
        try:
            self.reserachers = self.driver.find_elements(self.researchers_by, self.researchers_id)
        except Exception as e:
            print(f"Error found while extracting researchers: {e}")

    def extract_researchers(self):
        try:
            for e in self.reserachers:
                row = e.text.split('\n')
                self.data.append(row)
        except Exception as e:
            print(f"Error found while extracting researchers: {e}")

    def go_to_next_page(self):
        try:
            self.page_count += 1
            self.button.click()
            print("Waiting 3 seconds for page to load")
            time.sleep(3)
        except Exception as e:
            print(f"Error found while trying to navigatet to next page: {e}")

    def run(self):
        while True:
            try: 
                # print("Finding button")
                self.find_button()
                # print("Getting researcher")
                self.get_researchers()
                # print("Extracting researcher")
                self.extract_researchers()
                # print("Going to next page")
                if self.button is not None:
                    self.go_to_next_page()
                else:
                    break
            except Exception as e:
                print(f"Error found when running: {e}")

        print(f"""
            === Searching completed ===
            === Length of researchers: {len(self.data)} ===
            === Converting to Pandas ===
              """)
        df = pd.DataFrame(self.data)
        print(df.head(5))
        

## HOW - TO - USE

def UNSW_button_search(c, b):
    return b.accessible_name == "0"+str(c) or b.accessible_name == "next" or b.accessible_name == str(c)

unsw = UniversityScraper(
    url="https://www.unsw.edu.au/research/hdr/find-a-supervisor#search=&sort=relevance&startRank=1&numRanks=12&componentId=36c3802e-58bd-404b-90f6-07d44daf6b35", 
    input_field_id=(By.NAME,"9b55bf87-4f96-4bd5-ac5a-77540c6557f8-search"), 
    submit_button_id=(By.ID, "search-page-submit"), 
    input_search_text="Artificial intelligence", 
    button_search_function=UNSW_button_search, 
    buttons_id=(By.ID,"pagination-"), 
    researchers_id= (By.CLASS_NAME, "card-profile__container")
)

unsw.run()