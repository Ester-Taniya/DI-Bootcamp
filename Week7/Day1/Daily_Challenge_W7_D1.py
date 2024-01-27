import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch HTML content of the website
url = "https://github.com/topics"
response = requests.get(url)

# Step 2: Print the status code of the response
print("Status Code:", response.status_code)


# Step 3: Print the first 100 characters of the HTML content
if response.status_code == 200:
    print("\nFirst 100 characters of HTML content:\n", response.text[:100])

    # Step 4: Save HTML content to a file named 'webpage.html'
    with open('webpage.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    print("\nHTML content has been saved to 'webpage.html'.")

    # Step 5: Use BeautifulSoup to parse the saved HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 6: Identify and extract information (titles and descriptions)

    topic_titles = [title.text.strip() for title in soup.select('.f3 a')]
    topic_descriptions = [desc.text.strip() for desc in soup.select('.f5 p')]


    # Step 7: Print the length and content of each extracted list
    print("\nLength of topic_titles:", len(topic_titles))
    print("Content of topic_titles:", topic_titles[:5])
    print("\nLength of topic_descriptions:", len(topic_descriptions))
    print("Content of topic_descriptions:", topic_descriptions[:5])

    # Step 8: Create a Python dictionary to structure the extracted data
    data_dict = {'Title': topic_titles, 'Description': topic_descriptions}

    # Step 9: Convert the dictionary into a pandas DataFrame
    df = pd.DataFrame(data_dict)

    # Step 10: Print the DataFrame to confirm its structure and contents
    print("\nDataFrame structure and contents:\n", df.head())


    # Save the data into a .csv file
    df.to_csv('github_topics.csv', index=False)
    print("\nData has been saved to 'github_topics.csv'")

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")