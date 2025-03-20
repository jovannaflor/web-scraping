from bs4 import BeautifulSoup

filename = "html/filename_example.html"
with open(filename, "r", encoding="utf-8") as file:
    html = file.read()