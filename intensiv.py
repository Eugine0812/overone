import requests
from bs4 import BeautifulSoup

r = requests.get('https://auto.ru/')
soup = BeautifulSoup(r.text, 'lxml')
for car in soup.find_all('a': {'class'}):
    brent_name = ''
    brent_count =
    for child in car.children:

