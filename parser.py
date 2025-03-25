import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd


class UNSW_Reader:
    def __init__(self):

        # Configure Chrome options for headless environment
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.page_num = 1

        self.academics = [] 

    def get_html(self, url):
        if self.page_num == 1:
            self.driver.get(url)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    
    # Takes in a soup and using beautiful soup parses all the academics on the page - only works for UNSW currently
    def parse_academics(self, html):
        all_supervisors = html.find_all("a", class_="card-profile__container")
        return all_supervisors

    def parse_one_academic(self, academic_list):
        pass

    def run(self, url):
        print("=== Beginning UNSW Parser ===")
        try:
            while True:
                print(f"=== Extracting HTML of page {self.page_num} ===")
                soup = self.get_html("https://www.unsw.edu.au/research/hdr/find-a-supervisor#search=&sort=relevance&startRank=1&numRanks=12&componentId=9b55bf87-4f96-4bd5-ac5a-77540c6557f8")
                print("=== Exracting academics ===")
                academic_list = self.parse_academics(soup)
                print("=== Saving academics ===")
                self.academics.append(academic_list) 
                print("=== Finding next page button ===")
                self.page_num += 1
                button = self.find_button(soup)
                print(f"=== Going to page {self.page_num}===")
                self.go_to_next_page(button)
                time.sleep(1)
        except Exception as e:
            print("=== Pagination Loop Broken ===")
            print(e)
        print(len(self.academics))
    # Get Search terms and use them to search for relevant academics
    def relevant_search(self, search_terms):
        pass

    
    def find_button(self, soup):
        # button = soup.find_all("a", id = "pagination-2")
        print(f"button: {self.driver.find_element(By.ID, "pagination-3")}")
        print("pagination-"+str(self.page_num))
        return self.driver.find_element(By.ID, "pagination-"+str(self.page_num))

    def go_to_next_page(self, button):
        print(button)
        print(button.id)
        print(button.tag_name)
        print(button.is_displayed())
        print(button.is_enabled())
        print(button.text)
        button.click()
    
if __name__ == "__main__":
    reader = UNSW_Reader()
    reader.run("https://www.unsw.edu.au/research/hdr/find-a-supervisor#search=&sort=relevance&startRank=1&numRanks=12&componentId=36c3802e-58bd-404b-90f6-07d44daf6b35")