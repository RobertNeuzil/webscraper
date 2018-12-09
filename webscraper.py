from bs4 import BeautifulSoup
import requests
import sys
import re
'''
A basic html page of  a ficitional book store that was designed to be tested with a webscraper
'''
def web_scraper(webadd)
	page = 1
	source = requests.get(f'{webadd}{page}.html').text

	soup = BeautifulSoup(source, 'lxml')

	while page <= 20:
		for display in soup.find_all(class_='product_pod'):
			link = display.a.get('href')
			
			f = open('webscraper.txt','a')
			f.write(f'\n The title of the book is \n "{display.h3.a.text}" \n while the link to the book is: \n http://books.toscrape.com/catalogue/{link} \n')
			f.close()
			#print (f'The title of the book is \n "{display.h3.a.text}" \n while the link to the book is: \n http://books.toscrape.com/catalogue/{link} \n')
		page += 1

web_scraper('http://books.toscrape.com/catalogue/page-')