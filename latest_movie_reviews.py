#!/usr/bin/python
import urllib2
wiki = "http://timesofindia.indiatimes.com/entertainment/hindi/movie-reviews"
page = urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)
x=soup.find('div',id='articlenew')
for y in x.find_all('div'):
	print y.text