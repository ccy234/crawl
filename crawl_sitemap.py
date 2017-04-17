from download import *
import re

def crawl_sitemap(url):
    sitemap = download(url)

    links = re.findall('<loc>(.*?)</loc>', sitemap)

    for link in links:
        html = download(link)

if __name__ == '__main__':
    crawl_sitemap('http://example.webscraping.com/sitemap.xml')
