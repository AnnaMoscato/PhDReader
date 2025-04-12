from typing import Optional
from selenium.webdriver.common.by import By

def button_search_helper(button_id: By, button_name: str, page_count: Optional[int]=None) -> tuple[By, str]:
    if page_count: return (button_id, str(button_name + str(page_count)))
    else: return (button_id, button_name)