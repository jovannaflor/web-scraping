from bs4 import BeautifulSoup

filename = "bme_table.html"
with open(filename, "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

containers = soup.find_all('tr')

print(containers[0])