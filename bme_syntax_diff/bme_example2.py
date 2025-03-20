from bs4 import BeautifulSoup
import requests

url = "https://bme.uniwa.gr/"

data = requests.get(url)
html = data.text

soup = BeautifulSoup(html, "html.parser")

containers = soup.select('h5.latest_post_title') # all containers with h5

all_h5 = []

for heading in containers:
    heading_txt = heading.get_text(strip=True)
    all_h5.append(heading_txt)
    print(heading_txt)