import requests
import json
from datetime import datetime

from DB_conect import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()


def fetch_data():
    url = "https://api.tzevaadom.co.il/alerts-history/"
    
    # Set start_date and end_date to the current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    params = {
        'start_date': current_date,
        'end_date': current_date,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        # Return the fetched data
        return json.loads(response.text)
    else:
        # Log details about the error
        print(f"Error {response.status_code}: Unable to fetch data.")
        print(response.text)  # Print the response content for debugging


json_data = fetch_data()


class AlertItem:
    def __init__(self, ID, City, Time):
        self.ID = ID
        self.City = City
        self.Time = Time

    def save(self):
        # Check if the day in alert['time'] is the same as the current date
            # Use a context manager for handling the database connection
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO alerts (ID, City, Time) VALUES (%s, %s, %s)",
                    (self.ID, self.City, self.Time),
                )
                conn.commit()


# Function to format time
def format_time(entry):
    for alert in entry['alerts']:
        # Format time as real date-time
        dt_object = datetime.fromtimestamp(alert['time'])
        alert['time'] = dt_object.strftime("%Y-%m-%d %H:%M:00")

    return entry

# Apply formatting to each entry
formatted_data = [format_time(entry) for entry in json_data]

# Output the formatted data with each city separately
for entry in formatted_data:
    for alert in entry['alerts']:
        for city in alert['cities']:
            if alert['time'][:10] == datetime.now().strftime("%Y-%m-%d"):
                ID = entry['id']
                City = city.split(' -')[0]
                Time = alert['time']
                item = AlertItem(ID, City, Time)
                item.save()

conn.close()