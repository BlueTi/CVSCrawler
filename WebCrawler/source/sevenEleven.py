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
        
        driver.get(url)
        sleep(2)
        prod_list=list()
        dum_list=list()
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
                    prod_price=data.find('div',{'class':'price'}).get_text().replace('\n','').replace(',','')
                    prod_img="https://7-eleven.co.kr"+str(data.find('img')['src'])
                    prod_tag=str(data.find('ul',{'class':'tag_list_01'}).get_text().replace('\n',''))
                    prodDum=data.find_all("div",{"class":"infowrap"})
                    if(len(prodDum)>1):           
                        dum_name=prodDum[1].find('div',{'class':'name'}).get_text()
                        if(prodDum==''): continue
                        dum_price=str(prodDum[1].find('span').get_text()).replace(',','')
                        dum_img="https://7-eleven.co.kr"+str(data.find_all('img')[1]['src'])
                        dum_list.append([prod_name,dum_name]) 
                        prod_list.append([dum_name, dum_img  , dum_price, "증정품"])
                        prod_tag="증정"
                    else: prodDum=''
                    prod_list.append([prod_name,prod_img,prod_price,prod_tag])
                    
        p_set=set(map(tuple,prod_list))
        prod_list=[list(x)for x in p_set]
        sqlFile=codecs.open("sevenEleven.sql","w","utf-8")
        numb=0   
        for data in prod_list:
            numb+=1
            sqlFile.write("insert into prod values((select concat(date_format(now(), '%Y%m'),7"+str(numb)+")),'"+data[0]+"' , '"+data[1]+"' , "+data[2]+", '"+data[3]+"' ,'seven'); \n")
            
           
        for data in dum_list:
            sqlFile.write("insert into prod_dum values((select prodId from prod where name='"+data[0]+"' and tag='증정'),(select prodId from prod where name='"+data[1]+"' and tag='증정품'));\n")            
        sqlFile.close()
                    