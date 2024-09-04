import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

# function to scrape a website using Selenium and return its HTML content
def scrape_website(website):
    print("Launching chrome browser...")
    
    # set up the Chrome driver path and options
    chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
    try:
        # open the website in Chrome
        driver.get(website)
        print("Page Loaded...")
        
        # get the page's source HTML
        html = driver.page_source
        
        return html
    finally:
        driver.quit() # ensure the browser is closed after scraping
        
# function to extract the body content from the HTML using BeautifulSoup
def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

# function to clean the body content by removing unnecessary elements like scripts and styles
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    
    # remove all script and style elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    
    # extract text and remove extra whitespace
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip
        )
    
    return cleaned_content

# function to split large DOM content into smaller chunks for easier processing   
def split_dom_content(dom_content, max_length=6000):
    # split the content into chunks of a specified maximum length (usual max length is 8000 but made it 6000 to make sure do not hit limit)
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]