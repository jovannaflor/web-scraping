from bs4 import BeautifulSoup

filename = "html/html_example.html"
with open(filename, "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

elements = soup.select('p')

n=0
for element in elements:
    print(f"\nElement {n+1}")
    print("No strip:")
    print(element.text)
    print("With strip:")
    print(element.get_text(strip=True))
    # Εναλλακτικά: element.get_text().strip() -> ισοδύναμο
    n+=1