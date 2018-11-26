from bs4 import BeautifulSoup
import requests

source = requests.get('http://redditlist.com/').text


# creates a BeautifulSoup object
soup = BeautifulSoup(source, 'lxml')
'''
links = soup.find_all('a')
print(links)
'''


# inspect the page and find the html tags that you can pass to the soup object
header = soup.find_all('a', class_= "sfw", target='_blank')
print (header)