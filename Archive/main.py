
import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def get_page_html(url, output_html_file="unsw_page.html", output_parsed_file="unsw_parsed.txt"):
    """
    Opens a selenium driver to get HTML from the specified URL and shows how it looks to BeautifulSoup
    
    Args:
        url (str): The URL to scrape
        output_html_file (str): Filename to save the raw HTML
        output_parsed_file (str): Filename to save the BeautifulSoup parsing example
        
    Returns:
        tuple: (raw_html, soup_object)
    """
    print(f"Starting to fetch HTML from {url}")
    
    chromedriver_autoinstaller.install()

    # Configure Chrome options for headless environment
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Initialize the driver
    try:
        print("Attempting to initialize Chrome driver...")
        driver = webdriver.Chrome(options=chrome_options)
        print("Chrome driver initialized successfully")
    except Exception as e:
        print(f"Standard Chrome driver initialization failed: {e}")
        try:
            print("Trying with explicit service path...")
            # Try common paths in Codespaces
            potential_paths = [
                '/usr/bin/chromedriver',
                '/usr/local/bin/chromedriver',
                '/opt/chromedriver/chromedriver',
            ]
            
            for path in potential_paths:
                try:
                    print(f"Trying chromedriver at: {path}")
                    service = Service(executable_path=path)
                    driver = webdriver.Chrome(service=service, options=chrome_options)
                    print(f"Successfully initialized with driver at {path}")
                    break
                except Exception as path_e:
                    print(f"Failed with path {path}: {path_e}")
            else:
                raise Exception("Could not initialize Chrome driver with any known path")
        except Exception as final_e:
            print(f"All Chrome driver initialization attempts failed: {final_e}")
            print("\nTroubleshooting tips:")
            print("1. Install Chromedriver: sudo apt update && sudo apt install -y chromium-chromedriver")
            print("2. Check installation path: which chromedriver")
            print("3. Install Selenium: pip install selenium")
            print("4. Try running with a specific path to chromedriver")
            return None, None
    
    try:
        # Navigate to the page
        print(f"Navigating to {url}")
        driver.get(url)
        
        # Wait for the page to load
        print("Waiting for page to load...")
        try:
            # Wait for some element that indicates the page has loaded
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.coveo-result-list-container"))
            )
            print("Page loaded successfully")
        except Exception as wait_e:
            print(f"Warning: Wait timed out, but continuing: {wait_e}")
        
        # Allow some extra time for JavaScript execution
        print("Waiting additional time for JavaScript...")
        time.sleep(10)
        
        # Get the page source
        print("Retrieving page source...")
        html = driver.page_source
        
        # Save the raw HTML to a file
        print(f"Saving raw HTML to {output_html_file}")
        with open(output_html_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        # Parse with BeautifulSoup
        print("Parsing with BeautifulSoup...")
        soup = BeautifulSoup(html, 'html.parser')
        
        # Save BeautifulSoup parsing example
        print(f"Saving BeautifulSoup parsing example to {output_parsed_file}")
        with open(output_parsed_file, 'w', encoding='utf-8') as f:
            # Write information about the page structure
            f.write("=== Page Title ===\n")
            f.write(soup.title.string + "\n\n")
            
            f.write("=== Supervisors Found ===\n")
            supervisor_items = soup.select("div.coveo-result-list-container div.coveo-list-layout.CoveoResult")
            f.write(f"Number of supervisor items found: {len(supervisor_items)}\n\n")
            
            if supervisor_items:
                # Example of first supervisor
                f.write("=== First Supervisor Example ===\n")
                f.write(supervisor_items[0].prettify() + "\n\n")
                
                # Example of extracting information
                f.write("=== Extracting Information Example ===\n")
                for i, item in enumerate(supervisor_items[:3]):  # First 3 supervisors
                    f.write(f"--- Supervisor {i+1} ---\n")
                    
                    # Name
                    name_element = item.select_one("div.coveo-title a")
                    if name_element:
                        f.write(f"Name: {name_element.text.strip()}\n")
                        f.write(f"Profile URL: {name_element.get('href', 'Not found')}\n")
                    
                    # Paragraphs
                    info_elements = item.select("div.coveo-result-row p")
                    f.write(f"Number of paragraph elements: {len(info_elements)}\n")
                    for j, elem in enumerate(info_elements):
                        f.write(f"Paragraph {j+1}: {elem.text.strip()}\n")
                    
                    # Research Interests
                    research_header = item.select_one("div.coveo-result-row h4")
                    if research_header and "Research Interests" in research_header.text:
                        f.write("Research Interests found\n")
                        research_list = research_header.find_next("ul")
                        if research_list:
                            interests = research_list.select("li")
                            f.write(f"Number of research interests: {len(interests)}\n")
                            for interest in interests:
                                f.write(f"- {interest.text.strip()}\n")
                    
                    # Email
                    email_element = item.select_one("a[href^='mailto:']")
                    if email_element:
                        f.write(f"Email: {email_element['href'].replace('mailto:', '')}\n")
                    
                    f.write("\n")
            
            # Pagination information
            f.write("=== Pagination Information ===\n")
            pagination = soup.select("ul.coveo-pager li")
            f.write(f"Pagination elements found: {len(pagination)}\n")
            for i, page in enumerate(pagination):
                f.write(f"Page element {i+1}: {page.get('class', [])} - {page.text.strip()}\n")
        
        print("HTML retrieval and parsing complete!")
        return html, soup
        
    except Exception as e:
        print(f"Error during HTML retrieval: {e}")
        return None, None
    finally:
        # Close the browser
        print("Closing the browser...")
        driver.quit()

# Example usage
if __name__ == "__main__":
    url = "https://www.unsw.edu.au/research/hdr/find-a-supervisor#search=&sort=relevance&startRank=1&numRanks=12&componentId=36c3802e-58bd-404b-90f6-07d44daf6b35"
    
    html, soup = get_page_html(url)
    
    if html:
        print("\nSuccess! HTML has been saved to 'unsw_page.html'")
        print("BeautifulSoup parsing example saved to 'unsw_parsed.txt'")
        print("\nTo explore the structure in Python, you can use:")
        print("from bs4 import BeautifulSoup")
        print("with open('unsw_page.html', 'r', encoding='utf-8') as f:")
        print("    soup = BeautifulSoup(f.read(), 'html.parser')")
        print("\n# Find all supervisor elements")
        print("supervisors = soup.select('div.coveo-result-list-container div.coveo-list-layout.CoveoResult')")
        print("print(f'Found {len(supervisors)} supervisors')")
    else:
        print("\nFailed to retrieve HTML. See error messages above.")