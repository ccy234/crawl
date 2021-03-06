import urllib2
import sys

def download(url, user_agent='wswp', num_retries=2):
    #print 'Downloading', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent, num_retries-1)
    return html

if __name__ == '__main__':
    url = "http://www.allitebooks.com/web-development"
    print download(url)
