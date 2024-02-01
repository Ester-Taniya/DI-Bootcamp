from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pprint
import pandas as pd

# Initialize the WebDriver
driver = webdriver.Chrome()
url = "https://www.inmotionhosting.com"
driver.get(url)

# Wait for plan elements to be present
wait = WebDriverWait(driver, 30)
plan_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'compare-1')))

child_values = []

# Loop through parent elements to extract child elements
for parent_element in plan_elements:
    child_elements = parent_element.find_elements(By.CLASS_NAME, 'imh-rostrum-card')
    child_values.extend([c.text for c in child_elements])

# Initialize lists to store plan information
plan_names, descriptions, prices = [], [], []

# Loop through child values to extract plan information
for p in child_values:
    p = p.split('\n')
    if p[0] == 'NEW':
        plan_names.append(p[1])
        descriptions.append(p[2])
        prices.append(p[4])
    else:
        plan_names.append(p[0])
        descriptions.append(p[1])
        prices.append(p[3])

# Create a dictionary from the lists
plan_dict = {'plan_name': plan_names, 'description': descriptions, 'price': prices}

# Create a Pandas DataFrame from the dictionary
df = pd.DataFrame(plan_dict)

# Print the DataFrame
print(df)

# Close the WebDriver
driver.quit()
