from bs4 import BeautifulSoup
import requests
import json

url = 'https://bme.uniwa.gr'

response = requests.get(url)
response.raise_for_status()
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
containers = soup.select('.latest_post')

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