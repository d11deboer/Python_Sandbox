import pandas as pd
import requests
from bs4 import BeautifulSoup

pageRequest = requests.get('https://www.newegg.com/p/pl?d=RAM')

#make webscraping easy
soup = BeautifulSoup(pageRequest.content,'html.parser')

#closing connection
pageRequest.close()

#Each Item is contained within this div class (items-view is-grid)
item_container = soup.find('div',class_ = 'items-view is-grid')

#A variable that stores all items(remember,it behaves like an array)
items = item_container.findAll('div',class_ = 'item-container')

###########################BRAND NAME###########################

#VERSION 1: Traditional for loop, appending to a list.
#brands = []
##
##for brand in items:
##     
##     #Title
##     itemInfoContainer = brand.find('div',class_ ='item-info')
##     brandInfoContainer = itemInfoContainer.find('a',class_='item-brand')
##     brandName = brandInfoContainer.find('img')['title']
##     brands.append(brandName)
##
##print(brands)

#VERSION 2: 
#brand name
brand = [item.find('div',class_ ='item-info').find('a',class_='item-brand').find('img')['title'] for item in items]
#print(brand)

#################################################################



###########################RATINGS###########################


#VERSION 1: Traditional for loop, appending ratings to a list
##ratings = []
##
##for rating in items:
##     itemInfoContainer = rating.find('div',class_ ='item-info')
##     ratingInfoContainer = itemInfoContainer.find('a',class_='item-rating')
##     rating = ratingInfoContainer.i['class'][1][7]
##     ratings.append(rating)
##print(ratings)


#VERSION 2:
ratings = [rating.find('div',class_ ='item-info').find('a',class_='item-rating').i['class'][1][7] for rating in items]
print("Ratings: ", ratings)

###################################################################

###########################Number of reviews###########################
#VERSION 1: Traditional for loop, appending number of reviews to a list
##numOfReviews = []
##
##for review in items:
##     itemInfoContainer = review.find('div',class_ ='item-info')
##     ratingInfoContainer = itemInfoContainer.find('span',class_='item-rating-num')
##     numOfReviews.append(ratingInfoContainer.text.strip('()'))
##
##print(numOfReviews)

#VERSION 2:
numOfReviews = [review.find('div',class_ ='item-info').find('span',class_='item-rating-num').text.strip('()') for review in items]
print("reviews: ", numOfReviews)
###################################################################


###########################Title###########################
#VERSION 1: Traditional for loop, appending number of reviews to a list
##titles = []
##
##for title in items:
##     itemInfoContainer = title.find('div',class_ ='item-info')
##     titleInfoContainer = itemInfoContainer.find('a',class_='item-title')
##     title = titleInfoContainer.text
##     titles.append(title)
##print("Titles: ", titles)

#VERSION 2:
titles = [title.find('div',class_ ='item-info').find('a',class_='item-title').text for title in items]
print("Titles: ",titles)
###################################################################



###########################PRICING###########################
#VERSION 1: Traditional for loop, appending prices  to a list
##prices = []
##print('\n\n\n')
##for price in items:
##     priceContainer = price.find('ul',class_ ='price')
##     priceInfoContainer = priceContainer.find('li',class_='price-current')
##     pricing = (priceInfoContainer.strong.text) + (priceInfoContainer.sup.text)
##     prices.append(pricing)
##print("Pricing: ", prices)

###VERSION 2:
titles = [price.find('ul',class_ ='price').find('li',class_='price-current').strong.text + price.sup.text for price in items]
print("Pricing: ",titles)
###################################################################
