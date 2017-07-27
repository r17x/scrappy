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
    def result(self,tag,val):
        if not self.bs:
            return False
        self.result_txt = self.bs.find_all(tag,val)
        return self.result_txt
    def getResult(self):
        self.req = requests.get(self.web_search+self.query)
        self.bs = BeautifulSoup(self.req.content, 'html.parser')
        self.content = self.bs
        return True
    def Save(self):
        pass
    def data(self):
        f = open('scrap_'+str(self.query.replace(' ',''))+'.txt','w') 
        dt = self.result_txt
        data =''
        for dat in dt:
            for title in dat.find_all('h3'):
                title =  u''.join(title.get_text()).encode('utf-8').strip()
            for desc in dat.find_all('span','st'):
                desc = u''.join(desc.get_text()).encode('utf-8').strip()
            uri = str(dat.find_all('a')[0].get('href')).encode('utf-8')
            data = "Title : %s\nDescription : %s\nURI : %s\n" % (title,desc,uri)
            if f.write(data):
                f.write('='*20)
                print "Success write on text file scrap_%s" % (str(self.query.replace(' ','')))
            data ='' 
            #f.write("===============================")
        if f.closed: f.close()            
        return data
sc = Scrappy(raw_input('Query Search:'))
if sc.getResult():
    q= sc.result(raw_input('Tag:'),raw_input('Value of tag html:'))
    print sc.data()
