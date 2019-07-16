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

print(container)