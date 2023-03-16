import requests
from bs4 import BeautifulSoup
import random

# Az URL címet itt tároljuk el egy változóban
url = 'https://www.nosalty.hu/kereses/recept/leves?rendezes=nepszeruseg'

# Lekérjük az adott oldalt a requests modul segítségével
response = requests.get(url)

# Ha sikerült a lekérdezés, elmentjük az eredményt egy HTML fájlba
if response.status_code == 200:
    with open('nosalty.html', 'w', encoding='utf-8') as f:
        f.write(response.text)

# Az eredményből kinyerjük az összes "li" elemet, amelynek "class" attribútuma "m-grid__child", és a "a" elem "class" attribútuma "m-articleCard__headline"
soup = BeautifulSoup(response.text, 'html.parser')
results = soup.find_all('li', {'class': 'm-grid__child'})

# Az összes leves címét és URL címét egy listában tároljuk
recipes = []
for result in results:
    a_element = result.find('a', {'class': 'm-articleCard__headline'})
    if a_element:
        title = a_element.text.strip()
        url = 'https://www.nosalty.hu' + a_element['href']
        recipes.append((title, url))

# Véletlenszerűen választunk egy levest és kiírjuk a címét és URL címét
random_recipe = random.choice(recipes)
print(f"{random_recipe[0]}: {random_recipe[1]}")
