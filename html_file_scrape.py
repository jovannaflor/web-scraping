from bs4 import BeautifulSoup

filename = "html/bme_notices.html"
with open(filename, "r", encoding="utf-8") as file:
    html = file.read()