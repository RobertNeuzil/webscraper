import sys
from bs4 import BeautifulSoup
import requests

x = 360
while x <= 1000:
	
	source = requests.get('https://jacksonville.craigslist.org/search/apa?s=' + str(x)).text
	soup = BeautifulSoup(source, 'lxml')
	listings = soup.find_all('a', class_='result-title hdrlnk')
	
	for y in listings:
		file = open('webscraperlist.txt', 'w', encoding='UTF-8')
		file.write(y.text + '\n')
		
	
	file.close()	
	x += 120




