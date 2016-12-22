'''
Created on 2016. 11. 21.

@author: Administrator
'''

import sqlite3
from threading import Thread

from bs4 import BeautifulSoup
from selenium import webdriver
import codecs



class CPEmart(Thread):
    def __init__(self):
        super(CPEmart, self).__init__()
        
    def run(self):
        #CPEmart.compareEmart(self) 
        CPEmart.removingduplication(self)
    
    
    def compareEmart(self):
        
        conn=sqlite3.connect("eventDB.db")
        cur=conn.cursor()
        CUSQL=open('CU.sql','r').read()
        cur.execute(CUSQL)
        conn.commit()
        cur.execute("select prodName from CU")        
        
        rows = cur.fetchall()
        driver = webdriver.Chrome('./driver/chromedriver.exe')
        
        sqlfile=codecs.open("compare.sql","w","utf-8")
        sqlfile.write("create table compare(prodname text, compname text, price text, img text);")
        for row in rows:
            word=row[0]
            word.replace(' ','%20')
            url="http://emart.ssg.com/search.ssg?target=all&query="+word
           
            driver.get(url)
            source = driver.page_source
            soup = BeautifulSoup(source,"html.parser")
            
            prodlist=soup.findAll('tr',{'class':'item_emall'})
            
            for prod in prodlist:
                img=prod.find('div',{'class':'thm'}).find('img')['src']
                prodname=prod.find('div',{'class':'title'}).find('a',{'data-unit':'list'})['title']
                price=prod.find('div',{'class':'price'}).find('strong').get_text()
                print(str(prodname)+"     "+str(price).replace(',', ''))
                sqlfile.write("insert into compare values('"+word+"','"+str(prodname)+"','"+price+"','"+img+"')")         
        driver.quit()
        conn.close()
        
    def removingduplication(self):
        scriptList=['sevenDum.sql','GS_DUM.sql']
        
        for name in scriptList:
            sqlfile=codecs.open(name, 'r', 'utf-8')
        
            list=[]
            for line in sqlfile:
                    if line not in list:
                        list.append(line)
            newfile =codecs.open(name,'w','utf-8')
            for d in list:
                newfile.write(d)
        
        