import json
import os
from datetime import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))

# Укажите путь к вашему файлу JSON
file_path = os.path.join(dir_path, 'data_2023-12-16.json')

# Откройте файл и загрузите данные с помощью модуля json
with open(file_path, 'r') as file:
    json_data = json.load(file)

# Вывод данных
for entry in json_data:
    print(f"ID: {entry['id']}")
    print(f"Description: {entry['description']}")
    for alert in entry['alerts']:
        print(f"  Time: {alert['time']}")
        print(f"  Cities: {', '.join(alert['cities'])}")
        print(f"  Threat: {alert['threat']}")
        print("---")


