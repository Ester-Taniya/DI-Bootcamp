import requests
import json
import schedule
import time
from datetime import datetime

def fetch_and_save_data():
    url = "https://api.tzevaadom.co.il/alerts-history/"
    params = {
        'start_date': 'YYYY-MM-DD',
        'end_date': 'YYYY-MM-DD',
        # Other parameters as needed
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        filename = "data_.json"

        #  new file saver
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"Data saved to {filename}")
    else:
        print(f"Error {response.status_code}: Unable to fetch data.")




# run function in  23:59
schedule.every().day.at("21:17").do(fetch_and_save_data)

# unending  cycle:
while True:
    schedule.run_pending()
    time.sleep(1)

