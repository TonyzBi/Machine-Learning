# -*- coding:utf-8 -*-
import urllib2,re
#import requests

import HTMLParser

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://daily.zhihu.com/'
def getHtml(url):
    header = {'User-Agent':'Mozilla / 5.0(Windows NT 6.1; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 57.0 .2987 .133 Safari / 537.36'}
    request = urllib2.Request(url, headers= header)
    response = urllib2.urlopen(request)
    context = response.read()
    return context

def getUrls(html):
    pattern = re.compile('<a href="/story/(.*?)"',re.S)
    items = re.findall(pattern, html)
    urls = []
    for item in items:
        urls.append('http://daily.zhihu.com/story/'+item)
    return urls

def getContent(url):
    html = getHtml(url)
    pattern = re.compile('<h1 class="headline-title">.*?</h1>',re.S)
    items = re.findall(pattern, html)
    if len(items) > 0:
        print '*******'+items[0] + '**************'

html = getHtml(url)
urls = getUrls(html)
for url in urls:
    getContent(url)

