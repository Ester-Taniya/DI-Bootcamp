import requests
import json
import schedule
import time
from datetime import datetime

def fetch_data():
    url = "https://api.tzevaadom.co.il/alerts-history/"
    
    # Replace 'YYYY-MM-DD' with actual start and end dates
    params = {
        'start_date': '2023-01-01',
        'end_date': '2023-12-31',
        # Other parameters as needed
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        # Parse the JSON response
        data = json.loads(response.text)
        
        # Process the data as needed
        print("Data fetched successfully.")
        print(data)
    else:
        # Log details about the error
        print(f"Error {response.status_code}: Unable to fetch data.")
        print(response.text)  # Print the response content for debugging

# Schedule to run at 23:59 every day
schedule.every().day.at("22:34").do(fetch_data)

# Unending cycle
while True:
    schedule.run_pending()
    time.sleep(1)