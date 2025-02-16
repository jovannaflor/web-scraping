from bs4 import BeautifulSoup

html = """ 
<html>
	<body>
		<table>
			<tr>
				<th>Όνομα</th>
				<th>BMI</th>
			</tr>
			
			<tr>
				<td>Στέλιος</td>
				<td>23.54</td>
			</tr>
			
			<tr>
				<td>Γιώργος</td>
				<td>22.78</td>
			</tr>
		</table>
	</body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')

# Εξαγωγή δεδομένων από πίνακα
ths = soup.select('th') # Εξαγωγή των table headings
th_li = []

for th in ths:
    th = th.text
    th_li.append(th)

tds = soup.select('td') # Εξαγωγή των table data

names = []
bmi_li = []

for td in tds:
    td = td.text
    try:
        td = float(td) # Αν μπορεί να μετατραπεί σε float, είναι το BMI
        bmi_li.append(td)
    except ValueError:
        names.append(td)

print(th_li)
print(names)
print(bmi_li)
