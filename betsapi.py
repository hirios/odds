from bs4 import BeautifulSoup
import requests


var = requests.get('https://pt.betsapi.com/')
soup = BeautifulSoup(var.text, 'html.parser')
div = soup.find_all("div", {"class": "table-responsive"})
a = div[0].find_all(href=True)

for x in range(0, len(a)):

    if a[x].get_text().strip() == 'Futebol':
        print(a[x].get_text().strip())
        print(a[x + 1].get_text().strip())
        print(a[x + 2].get_text().strip())
        print(a[x + 3].get_text().strip())
        print()
        
      
