import requests
import pandas as pd
from bs4 import BeautifulSoup

#fetching the book scraping website page with the book info
req = requests.get('https://www.newegg.com/p/pl?d=ram')
