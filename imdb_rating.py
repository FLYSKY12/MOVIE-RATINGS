#!/usr/bin/python
import urllib2
query=raw_input()
query.replace(" ", "+")
url = "+".join(query.split())
wiki = "http://www.imdb.com/find?ref_=nv_sr_fn&q="+url+"&s=all"
page = urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)
x=soup.find('table')
y=x.find('tr')
z=y.td
for a in z.find_all('a'):
    if 'href' in a.attrs:
        ans=a['href']
        break
inter="http://www.imdb.com"+ans
cool = urllib2.urlopen(inter)
yo = BeautifulSoup(cool)
z=yo.find_all('strong')
i=0
for k in z:
	i=i+1
	if i==1:
		break
y=k.text
check=0
try:
    float(y)
    check=1
except ValueError:
    print "Not found"
if check ==1 :
    print "rating-->> ",y
    print yo.find('div',{"class" : "summary_text"}).text
    for ss in  yo.findAll('div',{"class" : "credit_summary_item"}):
        print ss.text
