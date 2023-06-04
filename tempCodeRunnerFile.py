import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the browser and navigate to the website
driver = webdriver.Chrome()
driver.get("https://www.trustedshops.de/bewertung/info_X77B11C1B8A5ABA16DDEC0C30E7996C21.html")

# Find and click on the "2 Stars" filter button
filter_button = driver.find_element(By.XPATH, "//div[@class='sc-35f7948-0 giiFno']")
filter_button.click()

# Wait for the filtered reviews to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'sc-de43f235-0')]")))

# Find all the filtered review elements
review_elements = driver.find_elements(By.XPATH, "//div[@class='sc-2e7612c5-0 sc-f836bc46-0 kyZgbN chcERM']")

# Check if every review has only two stars
all_two_stars = True
for review_element in review_elements:
    filled_star_elements = review_element.find_elements(By.XPATH, ".//span[contains(@style, 'color: rgb(255, 220, 15)')]")
    unfilled_star_elements = review_element.find_elements(By.XPATH, ".//span[contains(@style, 'color: rgb(204, 204, 204)')]")
    
    if len(filled_star_elements) != 2 or len(unfilled_star_elements) != 3:
        all_two_stars = False
        break

# Calculate the sum of star percentage values
sum_star_percentages = 0
for review_element in review_elements:
    filled_star_elements = review_element.find_elements(By.XPATH, ".//span[contains(@style, 'color: rgb(255, 220, 15)')]")
    star_percentage = len(filled_star_elements) * 20
    sum_star_percentages += star_percentage

# Print the intermediate information for debugging
print("Review Elements Count:", len(review_elements))
print("All Two Stars:", all_two_stars)
print("Sum of Star Percentage Values:", sum_star_percentages)

# Close the browser
driver.quit()
