import requests
import pandas as pd
from bs4 import BeautifulSoup

#fetching the book scraping website page with the book info
req = requests.get('https://www.newegg.com/p/pl?d=ram')

#creating the soup from which to fetch the book data
soup = BeautifulSoup(req.content, 'html.parser')

#closing the connection
req.close()

#finding the ordered list with the books
container = soup.find('div', class_ = 'items-view is-grid')

#fetching the list of all the items
list = container.findAll('div', class_ = 'item-container')

#creating the array of all the full titles of the items
name_array = [item.find('img')['title'] for item in list]
#print(name_array) #test print

#creating the array of all the prices of the items
price_array = ['$' + item.find('li', class_ = 'price-current').strong.text for item in list]
#print(price_array) #test print

#creating the array of all the ratings of the items
rating_array = [item.find('i', class_ = 'rating')['class'][1][7] for item in list]
#print(rating_array) #test print

#creating the array of all the brands of the items
title_array = [item.find('a', class_ = 'item-brand').img['title'] for item in list]
#print(title_array) #test print

ram_information = pd.DataFrame({
	 'Full Title' : name_array,
	 'Price' : price_array,
	 'Brand' : title_array,
	 'Rating' : rating_array 
	})
	
print(ram_information)

ram_information.to_csv('ram_information.csv')