'''
Created on 2016. 11. 21.

@author: Administrator
'''

import sqlite3

from bs4 import BeautifulSoup
from selenium import webdriver
from threading import Thread


class CPEmart(Thread):
    def __init__(self):
        super(CPEmart, self).__init__()
        
    def run(self):
        CPEmart.compareEmart(self)
    
    def compareEmart(self):
        
        conn=sqlite3.connect("eventDB.db")
        cur=conn.cursor()
        cur.execute("select prodName from CU")        
        
        rows = cur.fetchall()
        driver = webdriver.Chrome('./driver/chromedriver.exe')
        for row in rows:
            prod=row[0]
            prod.replace(' ','%20')
            url="http://emart.ssg.com/search.ssg?target=all&query="+prod
           
            driver.get(url)
            source = driver.page_source
            soup = BeautifulSoup(source,"html.parser")
            
            prodlist=soup.findAll('tr',{'class':'item_emall'})
            
            for prod in prodlist:
                img=prod.find('div',{'class':'thm'}).find('img')['src']
                prodname=prod.find('div',{'class':'title'}).find('a',{'data-unit':'list'})['title']
                price=prod.find('div',{'class':'price'}).find('strong').get_text()
                print(str(prodname)+"     "+str(price).replace(',', ''))
                
            
        driver.quit()
        conn.close()