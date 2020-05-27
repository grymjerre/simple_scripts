#!/usr/bin/python3

# MIT License Copyright 2020 Jeremias Grym
# Webbskrapare för att hämta aktuellt pris på silver resp guld från Avanza

import requests
import urllib.request
from bs4 import BeautifulSoup
import re

urls='https://www.avanza.se/index/om-indexet.html/18991/silver'
urlg='https://www.avanza.se/index/om-indexet.html/18986/guld'
response_s = requests.get(urls)
response_g = requests.get(urlg)
soup_s = BeautifulSoup(response_s.text, 'html.parser')
soup_g = BeautifulSoup(response_g.text, 'html.parser')
#data_Variable is for debugging
data_s = soup_s.find('span', {'class':'pushBox roundCorners3'})
data_g = soup_g.find('span', {'class':'pushBox roundCorners3'})
price_s = re.sub(r'\s+', '', soup_s.find('span', {'class':'pushBox roundCorners3'}).get_text())
price_g = re.sub(r'\s+', '', soup_g.find('span', {'class':'pushBox roundCorners3'}).get_text())
update_s = re.findall('[0-9]*:[0-9]*:[0-9]*', soup_s.find('span', {'class':'pushBox roundCorners3'}).attrs.get('title'))[0]
update_g = re.findall('[0-9]*:[0-9]*:[0-9]*', soup_g.find('span', {'class':'pushBox roundCorners3'}).attrs.get('title'))[0]

#price_g = ''.join(soup_g.find('span', {'class':'pushBox roundCorners3'}).get_text().split())
#target = float(re.sub(',', '.', re.findall('[0-9]*,[0-9]*', str(data))[0]))
print('Silver')
print(update_s, price_s)
print('Guld')
print(update_g, price_g)

