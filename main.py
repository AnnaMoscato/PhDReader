# ## HOW - TO - USE

# def uni_button_search(c, b):
#     return

# uni = UniversityScraper(
#     url=,
#     input_field_id=,
#     submit_button_id=,
#     input_search_text=,
#     button_search_function=,
#     buttons_id=,
#     researchers_id=
# )

# uni.run()

from university_parser import UniversityScraper
from selenium.webdriver.common.by import By
from util import button_search_helper

# ===== UNSW ===== 

def UNSW_button_search(c, b):
    return b.accessible_name == "0"+str(c) or b.accessible_name == "next" or b.accessible_name == str(c)

unsw = UniversityScraper(
    url="https://www.unsw.edu.au/research/hdr/find-a-supervisor#search=&sort=relevance&startRank=1&numRanks=12&componentId=36c3802e-58bd-404b-90f6-07d44daf6b35", 
    input_field_id=(By.NAME,"9b55bf87-4f96-4bd5-ac5a-77540c6557f8-search"), 
    submit_button_id=(By.ID, "search-page-submit"), 
    input_search_text="Artificial intelligence", 
    button_search_function=UNSW_button_search, 
    buttons_id=(By.ID,"pagination-"), 
    buttons_fn = button_search_helper,
    researchers_id= (By.CLASS_NAME, "card-profile__container")
)

unsw.run()

print("UNSW Done")
# ===== USYD ===== 

# def USYD_button_search(c,b):
#     return b.text == str(c)

# usyd = UniversityScraper(
#     url="https://www.sydney.edu.au/research/our-research/find-a-researcher.html?",
#     input_field_id=(By.ID,"searchTermsFARTextInput"), 
#     submit_button_id=(By.ID, "btnAdvSearch"), 
#     input_search_text="Artificial intelligence", 
#     button_search_function=USYD_button_search, 
#     buttons_id=(By.CLASS_NAME, "pagination__item"), 
#     researchers_id= (By.CLASS_NAME, "grid")

# )

# usyd.run()

# # ===== MONASH ===== 

# def MONASH_button_search(c,b):
#     return b.text == str(c)

# monash = UniversityScraper(
#     url="https://www.monash.edu/research/find?faculties=%255B%255D&phdCandidate=true&selectedLevels=%255B%255B%255B%255D%252C%255B%255D%255D%255D&queryText=%21padrenull",
#     input_field_id=(By.ID,"querySubmitForm"), 
#     submit_button_id=None, 
#     input_search_text="Artificial intelligence", 
#     button_search_function=MONASH_button_search, 
#     buttons_id=(By.TAG_NAME, "button"), 
#     researchers_id= (By.CLASS_NAME, "find-a-researcher__results--card")
# )

# monash.run()


def melb_button_search(c, b):
    return b.text == str(c)

melb = UniversityScraper(
    url="""https://findanexpert.unimelb.edu.au/searchresults?q=artificial%20intelligence&category=profile&pageNumber=1&pageSize=20&sorting=relevance""",
    input_field_id=(By.ID, "searchBoxInputField"),
    submit_button_id=(By.CLASS_NAME, "btn searchBoxSubmitButton btn-primary searchresults"),
    input_search_text="Artificial Intelligence",
    button_search_function=melb_button_search,
    buttons_id=(By.TAG_NAME, "button"),
    researchers_id=(By.CLASS_NAME, "container-fluid")
)

melb.run()


def uts_button_search(c, b):
    return b.text == str(c)

uts = UniversityScraper(
    url="https://profiles.uts.edu.au/search?by=text&type=user&v=Artificial%20intelligence",
    input_field_id=(By.TAG_NAME, "search"),
    submit_button_id=(By.CLASS_NAME, "L0Z8AZZ29UmIjsYkYdWw L4uI_mPDvzr2NwjpP5Dm"),
    input_search_text="Aritifical Intelligence",
    button_search_function=uts_button_search,
    buttons_id=(By.TAG_NAME, "button"),
    researchers_id=(By.CLASS_NAME, "DI9L8IZwubrRMuNHqPkr")
)

uts.run()