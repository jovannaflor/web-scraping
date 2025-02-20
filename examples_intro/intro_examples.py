from bs4 import BeautifulSoup

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

# Προφορικά
# print('\n')
# elements_source = soup.select('.source-1')
# print(len(elements_source), '\n')

# elements_content = soup.select('.content')
# print(len(elements_content)) # πόσες φορές εμφανίζεται αυτή η κλάση