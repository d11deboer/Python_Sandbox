import pandas as pd
import requests
from bs4 import BeautifulSoup

pageRequest = requests.get('https://www.newegg.com/p/pl?d=RAM')

#make webscraping easy
soup = BeautifulSoup(pageRequest.content,'html.parser')

#Each Item container is contained within div class (items-view is-grid)
item_container = soup.find('div',class_ = 'items-view is-grid')

#A variable that stores all items(remember,it behaves like an array)
items = item_container.findAll('div',class_ = 'item-container')

#Title
itemInfoContainer = items[0].find('div',class_ ='item-info')
brandInfoContainer = itemInfoContainer.find('a',class_='item-brand')
brandName = brandInfoContainer.find('img')['title']
print(brandName)

