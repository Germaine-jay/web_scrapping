# this code scrapes data from a website and converts to a c.s.v file using beautiful soup

'''import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import csv

csv_file = open('C:/Users/INTEL/Desktop/environment/scraped.csv' , 'w')
csv_read = csv.writer(csv_file)
csv_read.writerow(['Item', 'price', 'Image'])

with open('C:/Users/INTEL/Desktop/environment/environ/mee.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    # images = soup.find_all('img')
    title= soup.find('table', id="giftList")

for tr in title.find_all('tr')[1:]:
    for td in tr.find_all('td')[0]:
        Item = td.strip().replace('\n','')
    for price in tr.find_all('td')[2]:
        price = price.strip().replace('\n','')
    for img in tr.find_all('img'):
        Image = img['src']
    csv_read.writerow([Item, price, Image])
csv_file.close()'''



# a prog that collects the headline of a website using beautiful soup
''''bs = BeautifulSoup(html, 'html.parser')
import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import csv

with open('C:/Users/INTEL/Desktop/environment/corey.html', encoding='utf-8') as html:
# html = urlopen('https://coreyms.com')
    soup = BeautifulSoup(html, 'lxml')
    # print(soup.prettify)
    exit
    article = soup.find('article  ')
    headline = article
    print(headline)
''''