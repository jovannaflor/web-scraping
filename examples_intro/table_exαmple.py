from bs4 import BeautifulSoup
from io import StringIO
import pandas as pd

filename = "html/html_example.html"
with open(filename, "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

containers = soup.select('.bmi-table')

for container in containers:
    print(container.prettify())

print(f'Αριθμός των container με αυτή την κλάση: {len(containers)}')

# 1ος τρόπος
table = soup.find_all("tr")

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
df2 = pd.read_html(table_io)[0]

print(df1, "\n")
print(df2)

filename = "data/example_table.csv"
df1.to_csv(filename, index=False, header=True)