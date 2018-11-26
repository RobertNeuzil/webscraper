from bs4 import BeautifulSoup
import requests

source = requests.get('http://redditlist.com/').text

soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())