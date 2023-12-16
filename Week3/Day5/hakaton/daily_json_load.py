import requests
import json
import schedule
import time
from datetime import datetime

def fetch_and_save_data():
    url = "https://api.tzevaadom.co.il/alerts-history/"
    
    # Replace 'YYYY-MM-DD' with actual start and end dates
    params = {
        'start_date': '2023-01-01',
        'end_date': '2023-12-31',
        # Other parameters as needed
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        # Generate a filename with the current date
        current_date = datetime.now().strftime("%Y-%m-%d")
        filename = f"data_{current_date}.json"

        # Save the data to a JSON file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"Data saved to {filename}")
    else:
        # Log details about the error
        print(f"Error {response.status_code}: Unable to fetch data.")
        print(response.text)  # Print the response content for debugging

# Schedule to run at 23:59 every day
schedule.every().day.at("23:59").do(fetch_and_save_data)

# Unending cycle
while True:
    schedule.run_pending()
    time.sleep(1)
