from bs4 import BeautifulSoup
import requests

url = "https://bme.uniwa.gr/"

data = requests.get(url)
html = data.text

soup = BeautifulSoup(html, "html.parser")

containers = soup.select('.latest_post_text_inner') # container that contains h5 containers

all_h5 = []
all_headings = []

for container in containers:
    headings = container.select('h5')
    all_headings.append(headings)
    for heading in headings:
        heading_txt = heading.get_text(strip=True)
        all_h5.append(heading_txt)
        print(heading_txt)