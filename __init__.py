# Task : Scrapper web
# Coach : Jim aka Rahmat Ramadhan
# Author : ri7nz

#This Mini Simple Project/Task
"""
Task:
    1. QUery Google
"""
from bs4 import BeautifulSoup
import requests

class Scrappy(object):
    query = ''
    web_search = 'http://www.google.com/search?q='
    def __init__(self,query):
        self.query = query
    def result(self):
        if not self.bs:
            return False
        return self.bs.find_all('div','med')
    def getResult(self):
        self.content = requests.get(self.web_search+self.query)
        self.bs = BeautifulSoup(self.content,'parse.html')
        return True


