
#______________XP_1_____________________
from bs4 import BeautifulSoup
# HTML content of the page
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sports World</title>
    <style>
        body { font-family: Arial, sans-serif; }
        header, nav, section, article, footer { margin: 20px; padding: 15px; }
        nav { background-color: #333; }
        nav a { color: white; padding: 14px 20px; text-decoration: none; display: inline-block; }
        nav a:hover { background-color: #ddd; color: black; }
        .video { text-align: center; margin: 20px 0; }
    </style>
</head>
<body>

    <header>
        <h1>Welcome to Sports World</h1>
        <p>Your one-stop destination for the latest sports news and videos.</p>
    </header>

    <nav>
        <a href="#football">Football</a>
        <a href="#basketball">Basketball</a>
        <a href="#tennis">Tennis</a>
    </nav>

    <section id="football">
        <h2>Football</h2>
        <article>
            <h3>Latest Football News</h3>
            <p>Read about the latest football matches and player news.</p>
            <div class="video">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/football-video-id" frameborder="0" allowfullscreen>
                </iframe>
            </div>
        </article>
    </section>

    <section id="basketball">
        <h2>Basketball</h2>
        <article>
            <h3>NBA Highlights</h3>
            <p>Watch highlights from the latest NBA games.</p>
            <div class="video">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/basketball-video-id" frameborder="0" allowfullscreen>
                </iframe>
            </div>
        </article>
    </section>

    <section id="tennis">
        <h2>Tennis</h2>
        <article>
            <h3>Grand Slam Updates</h3>
            <p>Get the latest updates from the world of Grand Slam tennis.</p>
            <div class="video">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/tennis-video-id" frameborder="0" allowfullscreen></iframe>
            </div>
        </article>
    </section>

    <footer>
        <form action="mailto:contact@sportsworld.com" method="post" enctype="text/plain">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name"><br>
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email"><br>
            <label for="message">Message:</label><br>
            <textarea id="message" name="message" rows="4" cols="50"></textarea><br><br>
            <input type="submit" value="Send">
        </form>
    </footer>

</body>
</html>
"""

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find the title of the webpage
title = soup.title.text
print(f'Title of the webpage: {title}')

# Extract all paragraphs from the page
paragraphs = soup.find_all('p')
for i, paragraph in enumerate(paragraphs, start=1):
    print(f'Paragraph {i}: {paragraph.text}')

# Retrieve all links on the page
links = soup.find_all('a', href=True)
for i, link in enumerate(links, start=1):
    print(f'Link {i}: {link["href"]}')
#_______________________________________________________________________________________________________
    


#________________XP_2_______________________
import requests

# Specify the URL for which you want to fetch the robots.txt
website_url = "https://en.wikipedia.org"

# Construct the robots.txt URL
robots_txt_url = f"{website_url}/robots.txt"

# Make a GET request to fetch the content
response = requests.get(robots_txt_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Display the content of robots.txt
    print(response.text)
else:
    print(f"Failed to fetch robots.txt. Status code: {response.status_code}")


#_______________________________________________________________________________________________________
    


#________________XP_3_______________________
import requests
from bs4 import BeautifulSoup

# Specify the URL of the Wikipedia main page
url = "https://en.wikipedia.org/wiki/Main_Page"

# Make a GET request to fetch the HTML content
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract and display all header tags
    header_tags = soup.find_all(re.compile('^h\d$'))  # give all varibles in tags
    for header_tag in header_tags:
        print(header_tag.text.strip())

    

else:
    print(f"Failed to fetch the main page. Status code: {response.status_code}")

#_______________________________________________________________________________________________________
    


#________________XP_4_______________________
import requests
from bs4 import BeautifulSoup

# Specify the URL of the page you want to check
page_url = "https://example.com"

# Make a GET request to fetch the HTML content
response = requests.get(page_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Check if the page contains a title tag
    title_tag = soup.title
    if title_tag is not None:
        print(f"The page has a title: {title_tag.text.strip()}")
    else:
        print("The page does not have a title.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")

#_______________________________________________________________________________________________________
