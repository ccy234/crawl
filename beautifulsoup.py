from bs4 import BeautifulSoup
from download import *
from urllib import urlencode


def replace(a):
        return a.replace(" ", "%20")

url = "http://www.allitebooks.com/modern-programming-made-easy/"

html = download(url)

soup = BeautifulSoup(html)

span = soup.find(attrs={'class':'download-links'})

#a = span.find(attrs={hr})
url=span.a['href']
#print url
url = replace(url)
#print url
print download(url)
