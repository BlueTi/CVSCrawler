'''
Created on 2016. 10. 20.

@author: 305
'''
import codecs
from threading import Thread
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver


class CU(Thread):
    def __init__(self):
        super(CU, self).__init__()
    
    def run(self):
        CU.createCU_DB(self)
       
    def createCU_DB(self):
        url="http://cu.bgfretail.com/event/plus.do?category=event&depth2=1"
        driver = webdriver.Chrome('./driver/chromedriver.exe')
        driver.get(url)
        source = driver.page_source
        soup = BeautifulSoup(source,"html.parser")
        check=soup.find_all("div",{'id':'nothing'})
        
        while(len(check)==0):
            driver.execute_script("nextPage(1);")
            source = driver.page_source
            soup = BeautifulSoup(source,"html.parser")
            check=soup.find_all("div",{'id':'nothing'})
            sleep(2)    
        driver.quit()
            
        prodList = soup("div",{'class':'prodListWrap'})    
        
        sqlfile=codecs.open("CU.sql","w","utf-8")
        
        c=0        
        for d in prodList[0].find_all('li'):
            if(c%2==0):
                prodImg=(str(d.find('img')['src']))
                prodName=(str(d.find('p',{'class':'prodName'})).split('>')[2].split('<')[0])
                prodPrice=(str(d.find('p',{'class':'prodPrice'})).split('>')[2].split('<')[0])
                prodTag=(str(d.find('li')).split('>')[1].split('<')[0])
                sqlfile.write("insert into prodList values('"+prodName+"','"+prodPrice+"','"+prodTag+"','"+prodImg+"','','CU'); \n")                     
            c+=1
        sqlfile.close()

    
    

class CU_List(Thread):
    def __init__(self):
        super(CU_List, self).__init__()    
    
    def run(self):
        CU_List.createList(self)
    
    def createList(self):
        url="http://cu.bgfretail.com/product/product.do?category=product&depth2=3&depth3=5"
        
        driver = webdriver.Chrome('./driver/chromedriver.exe')
        driver.get(url)
        
        driver.execute_script("setCond('setB');")
        sleep(2)
        source = driver.page_source
        soup = BeautifulSoup(source,"html.parser")
        check=0
        
        while(check==0):
            driver.execute_script("nextPage(1);")            
            sleep(2)
            source = driver.page_source
            soup = BeautifulSoup(source,"html.parser")
            for s in soup.find_all("div",{"class":"prodListWrap"}):
                if(s.get_text().find("조회된 상품이 없습니다.")):
                    check=1    
        
        #sqlfile=codecs.open("menu.sql",'w','utf-8')
        for d in soup.find_all("div",{"class":"prodListWrap"}):
            for a in d.find_all('p',{'class','prodName'}):
                #sqlfile.write("insert into menu values('"+a.get_text()+"','식품');\n")
                print()
            
        
        """
        url="http://cu.bgfretail.com/product/product.do?category=product&depth2=3&depth3=3"
        driver.get(url)
        driver.execute_script("setCond('setB');")
        sleep(2)
        source = driver.page_source
        soup = BeautifulSoup(source,"html.parser")
        check=0
        
        while(check==0):
            driver.execute_script("nextPage(1);")            
            sleep(2)
            source = driver.page_source
            soup = BeautifulSoup(source,"html.parser")
            for s in soup.find_all("div",{"class":"prodListWrap"}):
                if(s.get_text().find("조회된 상품이 없습니다.")):
                    check=1                          
        driver.quit()
        
        for d in soup.find_all("div",{"class":"prodListWrap"}):
            for a in d.find_all('p',{'class','prodName'}):
                sqlfile.write("insert into menu values('"+a.get_text()+"','과자');\n")
        """
            