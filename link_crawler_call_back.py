import re
import urlparse
import robotparser
from download import *
from scrapecallback import *
def link_crawler(seed_url, link_regex, scrape_callback=None):
    rp = robotparser.RobotFileParser()
    rp.set_url(seed_url+'/robots.txt')
    rp.read()
    #user_agent = 'BadCrawler'
    user_agent = 'GoodCrawler'

    crawl_queue = [seed_url]
    
    seen = set(crawl_queue)

    while crawl_queue:
        url = crawl_queue.pop()

        if rp.can_fetch(user_agent, url):
            html = download(url)
        else:
            print 'Blocked by robots.txt:', url
            exit(1)

       	if scrape_callback:
			scrape_callback(url, html)#callback
 
        for link in get_links(html):
            if re.match(link_regex, link):
                link = urlparse.urljoin(seed_url, link)
                if link not in seen:
                    #print seen
                    seen.add(link)
                    crawl_queue.append(link)
def scrape_callback1(url, html):
	if re.search('/index/2', url):
		print url + "---->callback"

def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)

    return webpage_regex.findall(html)

if __name__ == '__main__':
    #url = sys.argv[1]
    #regex = sys.argv[2]
    link_crawler('http://example.webscraping.com', '/(index|view)', scrape_callback=ScrapeCallback())
    #link_crawler(url, regex)
