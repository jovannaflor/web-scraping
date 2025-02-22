from bs4 import BeautifulSoup
import requests

url = "https://bme.uniwa.gr/"

data = requests.get(url)
html = data.text

soup = BeautifulSoup(html, "html.parser")

containers = soup.select('.latest_post_title')

all_h5 = []

for container in containers:
    headings = containers.find_all('h5')
    for heading in headings:
        heading_txt = heading.get_text(strip=True)
        all_h5.append(heading_txt)
        print(heading_txt)