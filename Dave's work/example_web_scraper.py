import requests
import pandas as pd
from bs4 import BeautifulSoup

#fetching the book scraping website page with the book info
req = requests.get('http://books.toscrape.com/')

#creating the soup from which to fetch the book data
soup = BeautifulSoup(req.content, 'html.parser')

#closing the connection
req.close()

#finding the ordered list with the books
container = soup.find('ol', class_ = 'row')

#grabbing the list of books
library = container.findAll('li', 'col-xs-6 col-sm-4 col-md-3 col-lg-3')

#grabbing the tag for the book price
book_price = library[0].find('p', class_ = 'price_color')

#test print
#print(book_price.text)

#grab the rating tag
rating_tag = library[0].find('p', class_ = 'star-rating')

#test printing the star count
#print(rating_tag['class'][1])

#grabbing an array of the book names
name_array = [book.find('h3').text for book in library]

# test printing all of the book names
#for i in name_array : 
#	print(i)

# grabbing and test printing an array of all the book prices
price_array = [book.find('p', class_ = 'price_color').text for book in library]
#for i in price_array : 
#	print(i)

# grabbing and test printing an array of all the book ratings
ratings_array = [book.find('p', class_ = 'star-rating')['class'][1] for book in library]
#for i in ratings_array :
#	print(i + ' Stars')

#creating a rudimentary class for the book info
book_information = pd.DataFrame(
	{'Title' : name_array,
	 'Cash Money' : price_array,
	 'Ratings' : ratings_array
	})

#test print the data	
#print(book_information)

#export to csv
book_information.to_csv('book_information.csv')