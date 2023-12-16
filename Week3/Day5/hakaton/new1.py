import json
import os
from datetime import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'data_2023-12-16.json')

# Откройте файл и загрузите данные с помощью модуля json
with open(file_path, 'r') as file:
    json_data = json.load(file)


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
    print(f"ID: {entry['id']}")
    for alert in entry['alerts']:
        print(f"  Time: {alert['time']}")
        for city in alert['cities']:
            print(f"    City: {city}")
        
        print("---")
