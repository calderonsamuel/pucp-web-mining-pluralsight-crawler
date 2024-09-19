from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the URL
url = "https://www.pluralsight.com/browse"
driver.get(url)

# click the "menuPsnavSkillsCourses" button
menu_button = driver.find_element(By.ID, "menuPsnavSkillsCourses")
menu_button.click()

# Wait for the dropdown to be visible
driver.implicitly_wait(3)

# Find the section containing the links
section = driver.find_element(By.CSS_SELECTOR, "section.ps-nav-courses.ps-nav-dropdown")

# Get all the <a> elements with href attribute inside the section
links = section.find_elements(By.CSS_SELECTOR, "a[href]")

# Extract the href attributes
hrefs = [link.get_attribute("href") for link in links]

# Print the hrefs
for href in hrefs:
    print(href)

# Initialize a dictionary to store the children of each href
href_children = {}

# For each href, get all the children of the ".browse-search-results-list" element
for href in hrefs:
    driver.get(href)
    driver.implicitly_wait(3)
    
    # Find the .browse-search-results-list element
    results_list = driver.find_element(By.CSS_SELECTOR, ".browse-search-results-list")
    
    # Get all the children of the results list
    children = results_list.find_elements(By.XPATH, "./*")
    
    # Store the text of each child element in the dictionary
    href_children[href] = [child.text for child in children]


# Close the driver
driver.quit()