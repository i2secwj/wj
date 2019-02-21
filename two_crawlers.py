# -*- coding: cp949 -*-
import requests
from bs4 import BeautifulSoup
class Crawler:
    def __init__(self,url):
        self.url = url

    def res(self):
        r=requests.get(self.url)
        return r.content

    def soup(self,content):
        s = BeautifulSoup(content,"html.parser")
        return s



class Inews_Class(Crawler):
    def pins(self,s,m):
        titles = s.select(m)
        
        for title in titles:
             print title.get_text()


    
class Boan_Class(Crawler):
    def pins(self, s, m):
        titles = s.find_all(class_=m)
        for title in titles:
            print title.get_text()



if __name__ =="__main__":
    print "i_news"
    inews = Inews_Class("http://www.inews24.com/list/it")
    r = inews.res()
    s = inews.soup(r)
    inews.pins(s,"body > main > article > ol > li > a")
    print ""
    print ""

    
    print "boan_news"
    boan =Boan_Class("https://www.boannews.com/media/list.asp")
    r = boan.res()
    s = boan.soup(r)
    boan.pins(s,"news_txt")
