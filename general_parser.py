import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

class UniversityParser():
    def __init__(self, webpage : str, page_num : int = 2, button_name : str, researcher_str : str):
        self.webpage = webpage
        self.driver = webdriver.Edge()
        self.driver.get(webpage)

        self.page_num = page_num
        self.button_name = button_name
        self.researcher_str = researcher_str

    def get_html_soup(self):
        html = self.driver.page_source
        self.soup = BeautifulSoup(html, "html.parser")

    def parse_academics(self, html):
        all_supervisors = html.find_all("a", class_="card-profile__container")
        return all_supervisors
    
    def run(self):
        pass
    
    def find_button(self, soup):
        self.button = self.driver.find_element(By.ID, self.button_name)

    def go_to_next_page(self, button):
        button.click()
