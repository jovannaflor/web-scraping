from bs4 import BeautifulSoup
# import requests
import json

url = 'https://bme.uniwa.gr'

# 1ος τρόπος (απαιτεί σύνδεση στο ίντερνετ)---------------------------
# Μέσω web scraping από HTML ιστοσελίδας:
# data = requests.get(url)
# html = data.text
# --------------------------------------------------------------------

# 2ος τρόπος (λειτουργεί offline)-------------------------------------
# Μέσω scraping από κατεβασμένο HTML:
filename = "html/bme_page.html"
with open(filename, "r", encoding="utf-8") as file:
    html = file.read()
# --------------------------------------------------------------------

soup = BeautifulSoup(html, 'html.parser')

containers = soup.select('.entry_title')

txt_li = []
links_li = []

hyperlinks = {
                "text": "",
                "href": ""
                }

last_url = "https://bme.uniwa.gr/announcements/aitiseis-veltiosis-vathmologias-5/"

for container in containers:
    link = container.find('a')
    txt = link.get_text(strip=True)
    href = link.get('href')

    if href == last_url:
        break

    if href not in links_li:
        txt_li.append(txt)
        links_li.append(href)
        print(f"{txt}\n{href}")
        print("---------------------------------------------------------------------")

if len(links_li) > 1:
    print(f'{len(links_li)} νέες ειδοποιήσεις')
elif len(links_li) == 1:
    print(f'{len(links_li)} νέα ειδοποίηση')
else:
    print('Καμία νέα ανακοίνωση.')

if links_li:
    hyperlinks["text"] = txt_li[0]
    hyperlinks["href"] = links_li[0]
    
    filename = "data/urls.json"
    
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(hyperlinks,f, ensure_ascii=False, indent=4)