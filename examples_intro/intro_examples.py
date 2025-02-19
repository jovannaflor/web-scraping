from bs4 import BeautifulSoup

filename = "html/html_example.html"
with open(filename, "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

# elements = soup.find_all("p", class_="text-1")
elements = soup.select('p.text-1')

# Το prettify() γίνεται by default στο Spyder
print(soup.prettify())
print(elements)

for element in elements:
    print("\nNo strip:")
    print(element.text)
    print("\nWith strip:")
    print(element.get_text(strip=True))
    # Εναλλακτικά: element.get_text().strip() -> ισοδύναμο