import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

class UniversityParser():
    def __init__(self, webpage : str, button_name : str, researcher_str : str, page_num : int = 2):
        self.webpage = webpage
        self.page_num = page_num
        self.button_name = button_name
        self.researcher_str = researcher_str

        # Initialisation
        self.driver = webdriver.Edge()
        self.driver.get(webpage)
        self.academics = []

    def get_html_soup(self):
        html = self.driver.page_source
        self.soup = BeautifulSoup(html, "html.parser")

    def parse_academics(self, html):
        all_supervisors = html.find_all("a", class_="card-profile__container")
        return all_supervisors
    
    def run(self):
        print("=== Beginning of Parser ===")
        try:
            while True:
                print(f"=== Extracting HTML of page {self.page_num} ===")
                soup = self.get_html_soup()
                print(f"=== Extracting academics ===")
                academic_list = self.parse_academics(soup)
                print(f"=== Saving academics ===")
                self.academics.append(academic_list)
                print(f"=== Finding next page button ===")
                self.page_num += 1
                button = self.find_button(soup)
                print(f"=== Going to page {self.page_num} ===")
                self.go_to_next_page()
                time.sleep(1)
        except Exception as e:
            print("=== Pagination Loop Broken ===")
            print(e)
        print(len(self.academics))
    
    def find_button(self, soup):
        self.button = self.driver.find_element(By.ID, self.button_name)

    def go_to_next_page(self):
        self.button.click()

