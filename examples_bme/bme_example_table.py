from bs4 import BeautifulSoup
import pandas as pd

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