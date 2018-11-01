'''
Created on 2016. 10. 20.

@author: 305
'''
import codecs
from threading import Thread
from time import sleep, strftime

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
        
        sqlFile=codecs.open("CU.sql","w","utf-8")
        
        c=0
        code=0
        for d in prodList[0].find_all('li'):
            if(c%2==0):
                if(d.find('img')['src']) is None:
                    prod_img=''
                else : prod_img=(str(d.find('img')['src']))              
                prod_name=(str(d.find('p',{'class':'prodName'})).split('>')[2].split('<')[0])
                prod_price=(str(d.find('p',{'class':'prodPrice'})).split('>')[2].split('<')[0].replace(',',''))
                prod_tag=(str(d.find('li')).split('>')[1].split('<')[0])
                sqlFile.write("insert into prod_list values(1"+strftime("%y%m")+str(code).zfill(3)+",'"+prod_name+"','"+prod_img+"','"+prod_price+"','"+prod_tag+"');\n")
                code+=1                     
            c+=1
        sqlFile.close()

    