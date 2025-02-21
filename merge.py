from bs4 import BeautifulSoup
from io import StringIO
import pandas as pd
import json

choice = 0
while choice <1 or choice >4:
    try:
        choice = int(input("Choice? "))
    except ValueError:
        print("Παρακαλώ εισάγεται αριθμό (1-4).")


if choice == 1:

    filename = "html/html_example.html"
    with open(filename, "r", encoding="utf-8") as file:
        html = file.read()

    soup = BeautifulSoup(html, 'html.parser')

    elements = soup.select('p.text-1')
    # elements = soup.find_all("p", class_="text-1") # -> ισοδύναμο

    # Το prettify() γίνεται by default στο Spyder
    print(soup.prettify())
    print(elements)

    for element in elements:
        print("\nNo strip:")
        print(element.text)
        print("\nWith strip:")
        print(element.get_text(strip=True))
        # Εναλλακτικά:
        # element.get_text().strip() # -> ισοδύναμο

    articles = soup.select('a')

    for article in articles:
        a_link = article.get('href')
        a_txt = article.get_text(strip=True)

    print(f"\n{a_txt}\n{a_link}")

elif choice == 2:

    filename = "html/html_example.html"
    with open(filename, "r", encoding="utf-8") as file:
        html = file.read()

    soup = BeautifulSoup(html, "html.parser")

    containers = soup.select('.bmi-table')

    for container in containers:
        print(container.prettify())

    # 1ος τρόπος
    table = soup.find_all("tr") # ή table

    data = []
    for row in table:
        cols = row.find_all(['th', 'td'])
        cols = [col.get_text(strip=True) for col in cols]
        
        if row.find('th'):
            headers = cols
        else:
            data.append(cols)
            
    df1 = pd.DataFrame(data, columns=headers)

    # 2ος τρόπος - με pandas + StringIO:
    table = soup.select_one(".bmi-table")
    table_io = StringIO(str(table))
    df2 = pd.read_html(table_io)[0] # [0] -> για να τραβήξει μόνο το 1ο table

    print(df1, "\n")
    print(df2)

    # Αποθήκευση σε αρχείο CSV
    filename = "output/example_table.csv"
    df1.to_csv(filename, index=False, header=True)


elif choice == 3:

    filename = "html/bme_table.html"
    with open(filename, "r", encoding="utf-8") as file:
        html = file.read()

    soup = BeautifulSoup(html, 'html.parser')

    tables = soup.find_all('tr')

    data = []
    for row in tables:
        cols = row.find_all(['th', 'td'])
        cols = [col.get_text(strip=True) for col in cols]
        if "εξάμηνο" not in " ".join(cols): 
            data.append(cols)
            # if "ΝΜΒ.8" in " ".join(cols): 
            #     data.append(cols)

    df = pd.DataFrame(data)

    filename = "output/bme_table.xlsx"
    df.to_excel(filename, index=False, header=False)


elif choice == 4:

    # import requests

    # 1ος τρόπος (απαιτεί σύνδεση στο ίντερνετ)---------------------------

    # Μέσω web scraping από HTML ιστοσελίδας:
    # url = 'https://bme.uniwa.gr/category/announcements/undergraduate/'
    # data = requests.get(url)
    # html = data.text
    # --------------------------------------------------------------------

    # 2ος τρόπος (λειτουργεί offline)-------------------------------------

    # Μέσω scraping από κατεβασμένο HTML:
    filename = "html/bme_notices.html"
    with open(filename, "r", encoding="utf-8") as file:
        html = file.read()
    # --------------------------------------------------------------------

    soup = BeautifulSoup(html, 'html.parser')

    containers = soup.select('.entry_title')

    txt_li = []
    links_li = []
    hyperlinks = {}
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
        for i in range(len(txt_li)):
            key = f"Ανακοίνωση {i+1}"
            hyperlinks[key] = {"Κείμενο": txt_li[i], "Σύνδεσμος": links_li[i]}
        
        filename = "output/notices.json"
        
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(hyperlinks,f, ensure_ascii=False, indent=4)