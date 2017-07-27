# Task : Scrapper web
# Coach : Jim aka Rahmat Ramadhan
# Author : ri7nz

#This Mini Simple Project/Task
"""
Task:
    1. QUery Google
"""
from bs4 import BeautifulSoup as BS
import requests as req

class Scrap(object):
    web_search = 'http://www.google.com/search?q='
    keyword=''
    def __init__(self,keyword):
        self.keyword = keyword
        self.uri = self.web_search+str(keyword)
    """
        google.com+keyword
    """
    def browse_uri(self):
        return req.get(self.uri)
    def parse_html(self):
        return BS(self.browse_uri().content, 'html.parser')
    def getUriList(self):
        content = self.parse_html()
        body = content.find_all('div','g')#Google Search Result
        #uri_list = []
        for b in body:
       # uri_list = [x.get('href') for x in body.find_all('a')]
            for url in body.find_all('a'):
                url_list.append(url.get('href'))
        return True
        
