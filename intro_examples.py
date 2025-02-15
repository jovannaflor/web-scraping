from bs4 import BeautifulSoup

html2 = """
<html>
<body>
<p>
Hello   world
</p>
<p>
Hello
world
</p>
</body>
</html>
"""

filename = "html_example.html"
with open(filename, "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

elements = soup.select('p')

# print(elements)
n=0
for element in elements:
    print(f"\nElement {n+1}")
    print("No strip:")
    print(element.text)
    print("With strip:")
    print(element.get_text(strip=True))
    # Εναλλακτικά: element.get_text().strip() -> ισοδύναμο
    n+=1
