from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

url = "https://www.inmotionhosting.com/"
driver.get(url)

wait = WebDriverWait(driver, 10)

page_source = driver.page_source



soup = BeautifulSoup(driver.page_source, 'html.parser')
plans = soup.find_all('div', class_='plan-details')


data = []
for plan in plans:
    plan_name = plan.find('h2').text.strip() 
    features = plan.find('ul').text.strip()  
    price = plan.find('span', class_='price').text.strip()  

    data.append({
        'Plan Name': plan_name,
        'Features': features,
        'Price': price
    })

df = pd.DataFrame(data)
df.to_csv('hosting_plans.csv', index=False)
driver.quit()

print('Data scraping completed and saved to hosting_plans.csv')
