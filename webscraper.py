from bs4 import BeautifulSoup
import requests
import sys
import re
'''
A basic html page of  a ficitional book store that was designed to be tested with a webscraper
'''
x = 1
source = requests.get(f'http://books.toscrape.com/catalogue/page-{x}.html').text

soup = BeautifulSoup(source, 'lxml')

while x <= 5:
	for display in soup.find_all(class_='product_pod'):
		link = display.a.get('href')
		print (f'The title of the book is \n "{display.h3.a.text}" \n while the link to the book is: \n http://books.toscrape.com/catalogue/{link} \n')
	x += 1

