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
        
        sqlfile=codecs.open("CU.txt","w","utf-8")
        
        c=0        
        for d in prodList[0].find_all('li'):
            if(c%2==0):
                prodImg=(str(d.find('img')['src']))
                prodName=(str(d.find('p',{'class':'prodName'})).split('>')[2].split('<')[0])
                prodPrice=(str(d.find('p',{'class':'prodPrice'})).split('>')[2].split('<')[0])
                prodTag=(str(d.find('li')).split('>')[1].split('<')[0])
                sqlfile.write(prodName+"','"+prodPrice+"','"+prodTag+"','"+prodImg+"\n")                     
            c+=1
        sqlfile.close()

    