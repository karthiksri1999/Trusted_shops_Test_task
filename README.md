# Trusted_shops_Test_task 

### To perform the end-to-end test on the Trusted Shops profile page, I am using Selenium WebDriver in Python. 
### Here's a step-by-step guide on how to execute the test:

# Step 1: Install Selenium WebDriver
### Install the Selenium WebDriver package for Python using pip: pip install selenium

# Step 2: Set up the test environment
### Import the necessary modules and set up the WebDriver to use a browser for automation. For this test, I am using Google Chrome:

import time <br />
from selenium import webdriver <br />
from selenium.webdriver.common.by import By <br />
from selenium.webdriver.chrome.service import Service <br />
from selenium.webdriver.chrome.options import Options <br />
from selenium.webdriver.support.ui import WebDriverWait <br />
from selenium.webdriver.support import expected_conditions as EC <br />
### Set up Selenium options
options = Options() <br />
options.add_argument("--disable-logging") <br />
### Set up Chrome driver service
service = Service("C:\Karthik\Code\chromedriver_win32\chromedriver.exe") <br />
### Choose Chrome browser
driver = webdriver.Chrome(service=service, options=options) <br />
### Set the maximum time to wait for the page to load
timeout = 10 <br />

# Step 3: Navigating to the profile page
driver.get("https://www.trustedshops.de/bewertung/info_X77B11C1B8A5ABA16DDEC0C30E7996C21.html") <br />

# Step 4: Check if the page title exists
### Wait for the page title to load
wait = WebDriverWait(driver, timeout) <br />
page_title = wait.until(EC.presence_of_element_located((By.XPATH, "//title"))) <br />
### Get the text of the page title
title_text = page_title.get_attribute("text") <br />
### Check if the page title exists and print it
if title_text: <br />
print("Page title exists:", title_text) <br />
else: <br />
print("Page title does not exist.") <br />

# Step 5: Check if the grade is visible and above zero
### Find the grade element
div_element = driver.find_element(By.XPATH, "//div[@class='sc-3a77ab16-8 hA-dRdV']") <br />
span_element = div_element.find_element(By.XPATH, ".//span[@class='sc-3a77ab16-6 kohtTt']") <br />
grade_text = span_element.text.strip() <br />
### Replace comma with dot in grade_text
grade_text = grade_text.replace(',', '.') <br />
if grade_text != "" and float(grade_text.split("/")[0]) > 0: <br />
print("Grade is visible and above zero:", grade_text) <br />
print("\n") <br />
else: <br />
print("Grade is not visible or not above zero.") <br />
print("\n") <br />

# Step 6: Check if the "Wie berechnet sich die Note?" link opens the window with additional information and verify the provided information
### Find and click on the "Wie berechnet sich die Note?" link
url="https://www.trustedshops.de/bewertung/info_X77B11C1B8A5ABA16DDEC0C30E7996C21.html" <br />
driver.get(url) <br />
wie_berechnet_link = WebDriverWait(driver, 10).until( <br />
EC.element_to_be_clickable((By.LINK_TEXT, "Wie berechnet sich die Note?")) <br />
) <br />
wie_berechnet_link.click() <br />
### Wait for the modal window to appear
modal_window = WebDriverWait(driver, 10).until( <br />
EC.visibility_of_element_located((By.XPATH, "//div[@class='Modalstyles__Modal-sc-10yc67r-0 gSuQkh']")) <br />
) <br />
### Check if the provided information is relevant
info_text = modal_window.text <br />
if "Lesen Sie die Bewertungen anderer Kundinnen und Kunden von Jalousiescout.de als Orientierungshilfe!" in info_text: <br />
print("Relevant information found: \n", info_text) <br />
print("\n") <br />
else: <br />
print("Relevant information not found.") <br />

# Step 7: Click on "2 Stars" to filter all "two stars" reviews and verify the filter
### Click on the filter button
driver = webdriver.Chrome() driver.get("https://www.trustedshops.de/bewertung/info_X77B11C1B8A5ABA16DDEC0C30E7996C21.html") <br />
filter_button = driver.find_element(By.XPATH, "//div[@class='sc-35f7948-0 giiFno']") <br />
filter_button.click() <br />
### Filter reviews based on the CSS code
reviews = driver.find_elements(By.XPATH, "//div[contains(@class, 'csnystk c1-2ljs')]") <br />
### Check if every review has the first two stars with a different color and the remaining three stars unfilled
all_correct_stars = True <br />
for review in reviews: <br />
star_elements = review.find_elements(By.XPATH, ".//span[contains(@class, 'c1-2ljs csnystk c1-2ljs-0')]") <br />
if len(star_elements) != 5: <br />
all_correct_stars = False <br />
break <br />
for i, star in enumerate(star_elements): <br />
if i < 2: <br />
if star.get_attribute("style") != "display: inline; color: rgb(255, 220, 15);": <br />
all_correct_stars = False <br />
break <br />
else: <br />
if star.get_attribute("style") != "display: inline; color: rgb(204, 204, 204);": <br />
all_correct_stars = False <br />
break <br />
### Print the result
if all_correct_stars: <br />
print("The entire list consists of two stars") <br />
else: <br />
print("The list contains more than two stars or is invalid") <br />

# Step 8: Create the sum of all star percentage values and verify that the sum is equal to or below 100
### Find and click on the "2 Stars" filter button
filter_button = driver.find_element(By.XPATH, "//span[@class='Iconstyles__Icon-sc-hltmf-0 bZPqEd sc-fe1e7ad3-0 jgEUUL hls hls-icon-arrow-chevron-down']") <br />
filter_button.click() <br />
### Wait for the filtered reviews to load
wait = WebDriverWait(driver, 10) <br />
wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'sc-ccb4adb3-0')]"))) <br />
### Find all the filtered review elements 
review_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'sc-ccb4adb3-0')]") <br />
### Check if every review has only two stars
all_two_stars = True <br />
for review_element in review_elements: <br />
filled_star_elements = review_element.find_elements(By.XPATH, ".//span[@style='display: inline; color: rgb(255, 220, 15);']") <br />
unfilled_star_elements = review_element.find_elements(By.XPATH, ".//span[@style='display: inline; color: rgb(204, 204, 204);']") <br />
### Assuming each filled star represents 100%, so 2 stars represent 40%
sum_star_percentages = len(review_elements) * 40 <br />
print("Sum of star percentage values:", sum_star_percentages) <br />

# Step 9: Clean up and close the WebDriver
driver.quit() 
