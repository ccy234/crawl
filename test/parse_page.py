from bs4 import BeautifulSoup
from download import *
from urllib import urlencode
from urllib import quote
import string


def replaceSpace(s):
    s = s.replace(' ','%20')
    return s

def get_file_addr(url):
    html = download(url)
    if html != None:
        soup = BeautifulSoup(html, "lxml")
        load = soup.find_all("span", class_="download-links")
        for link in load:
            pdf = link.a["href"]
            if "http" in pdf:
                print pdf
                return pdf

def get_one_page(url):
    html = download(url)
    if html != None: 
        soup = BeautifulSoup(html, "lxml")
        entry_title = soup.find_all("h2", class_="entry-title")
        for entry in entry_title:
            a = entry.find("a")
            #print a["href"]
            #return a["href"]
            get_file_addr(a["href"])

def get_page_nums(url):
    html = download(url)
    if html != None: 
        soup = BeautifulSoup(html, "lxml")
        page = soup.find("span", class_="pages")
        s = str(page.string)
        num = s.split() 
        #print num[2] 
        return num[2] 
        
     



	
url1 = "http://www.allitebooks.com/web-development/"
get_page_nums(url1)

#url2 = "http://www.allitebooks.com/pro-html5-games-2nd-edition/"
#for i in range(3):
#    url = "http://www.allitebooks.com/web-development/page/%d/" % (i+1)
#    print url
#    get_one_page(url)

#print download(get_file_addr(url2))
#get_file_addr(url2)


