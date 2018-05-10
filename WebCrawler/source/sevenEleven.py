'''
Created on 2016. 11. 28.

@author: Administrator
'''
import codecs
from threading import Thread
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver


class Seven(Thread):
    def __init__(self):
        super(Seven, self).__init__()
        
    def run(self):
        Seven.create7DB(self)
        
    def create7DB(self):
        url="https://www.7-eleven.co.kr/product/presentList.asp"
        driver = webdriver.Chrome('./driver/chromedriver.exe')        
        sqlfile=codecs.open('sevenEleven.sql', 'w', 'utf-8')
        driver.get(url)
        sleep(2)
        dumlist=list()
        dumprod_l=list() 
        for n in range(1,5):
            no=str(n)
            driver.execute_script("fncTab('"+no+"');")
            sleep(4)
            source = driver.page_source
            soup = BeautifulSoup(source,"html.parser")
            check=0
        
            while(1):            
                driver.execute_script("fncMore('"+no+"');")
                sleep(0.8)
                source=driver.page_source
                soup = BeautifulSoup(source,"html.parser")
                tem=(len(soup.find("ul",{"id":"listUl"}).find_all("li")))
                if check==tem: 
                    break;
                else:
                    check=tem
                       
            prodList=soup.find("ul",{"id":"listUl"}).find_all("li")     
             
            for data in prodList:
                if(data.find('div',{'class':'infowrap'})!=None):                
                    prod_name=data.find('div',{'class':'name'}).get_text()
                    prod_price=data.find('div',{'class':'price'}).get_text().replace('\n','')
                    prod_img="https://7-eleven.co.kr"+str(data.find('img')['src'])
                    prod_tag=str(data.find('ul',{'class':'tag_list_01'}).get_text().replace('\n',''))
                    prodDum=data.find_all("div",{"class":"infowrap"})
                    if(len(prodDum)>1):           
                        dum_name=prodDum[1].find('div',{'class':'name'}).get_text()
                        if(prodDum==''): continue
                        dum_price=str(prodDum[1].find('span').get_text())
                        dum_img="https://7-eleven.co.kr"+str(data.find_all('img')[1]['src'])
                        dumlist.append([prod_name,dum_name]) 
                        dumprod_l.append([dum_name,dum_price,dum_img])
                        prodTag="증정"
                    else: prodDum=''
                    sqlfile.write("insert into SevenEleven values(0,'"+prod_name+"' , "+prod_price+" , '"+prod_tag+"' , '"+prod_img+"'); \n")
                    
                    
        d_set = set(map(tuple,dumprod_l))
        dumprod_l=[list(x) for x in d_set]
        for data in dumprod_l:
            sqlfile.write("insert into SevenEleven_Dumprod values(0, '"+data[0]+"' , "+data[1]+" ,'"+data[2]+"'); \n")     
        for data in dumlist:
            sqlfile.write("insert into SevenEleven_Dum values((select prodId from SevenEleven where name='"+data[0]+"'),'"+data[1]+"');\n")            
        sqlfile.close()
                    