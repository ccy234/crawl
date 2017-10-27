from bs4 import BeautifulSoup
from download import *
from urllib import urlencode


def replace(a):
        return a.replace(" ", "%20")

url = "http://www.allitebooks.com/web-development/"

html = download(url)

soup = BeautifulSoup(html)
print soup.title
#article_all = soup.find_all("article")
#for article in article_all:
    #print article
    #entry_title = BeautifulSoup(article)
    #print entry_title.find_all("h2", class_="entry_title")
entry_title = soup.find_all("h2", class_="entry-title")
for entry in entry_title:
    print entry
print len(entry_title)
#print soup.article
#print soup.head
#span = soup.find(attrs={'class':'download-links'})
#
##a = span.find(attrs={hr})
#url=span.a['href']
##print url
#url = replace(url)
##print url
#print download(url)
