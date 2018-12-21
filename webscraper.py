from bs4 import BeautifulSoup
import requests
import sys
import re
'''
A basic html page of  a ficitional book store that was designed to be tested with a webscraper
'''


def web_scraper(webadd):  # the function allows you to enter your own webadd. Although that won't do much good, since the algorithim is tailored to this specific website
    page = 1  # default
    # html code, converted to text
    source = requests.get(f'{webadd}{page}.html').text

    # BeautifulSoup object, arguments are source code and 'lxml' parser
    soup = BeautifulSoup(source, 'lxml')

    while page <= 20:  # scrape first 19 pages
        # each book has this html class
        for display in soup.find_all(class_='product_pod'):
            # the href will be put into the final write to direct users to a link
            link = display.a.get('href')

            # the append is important. Otherwise the file will just write the last result, overwriting through all iterations of loop
            f = open('webscraper.txt', 'a')
            f.write(
                f'\n The title of the book is \n "{display.h3.a.text}" \n while the link to the book is: \n http://books.toscrape.com/catalogue/{link} \n')
            f.close()  # always remember to close

            #print (f'The title of the book is \n "{display.h3.a.text}" \n while the link to the book is: \n http://books.toscrape.com/catalogue/{link} \n')

        page += 1  # want to make sure while loop doesn't run forever


web_scraper('http://books.toscrape.com/catalogue/page-')  # call function
