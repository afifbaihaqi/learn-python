import requests
from bs4 import BeautifulSoup

data_1 = requests.get('https://www.kompas.com/tren')
tren = BeautifulSoup(data_1.text, 'html.parser')
tren_area = tren.find(attrs={'class':'col-bs10-7'})
titles = tren_area.findAll(attrs={'class':'trenLatest__img'})
for titel in titles:
    print(titel.find('a').find('img')['alt'])
