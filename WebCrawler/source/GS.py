'''
Created on 2016. 10. 28.

@author: 305
'''
from builtins import list
import codecs
from threading import Thread
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver
import itertools


class GS(Thread):
    def __init__(self):
        super(GS, self).__init__()
        
    def run(self):
        GS.createGS25_DB(self)
        
    def createGS25_DB(self):
        url="http://gs25.gsretail.com/gscvs/ko/products/event-goods#;"
        driver = webdriver.Chrome('./driver/chromedriver.exe')
        driver.get(url)
        source = driver.page_source
        soup = BeautifulSoup(source,"html.parser")
        driver.find_element_by_link_text("전체").click()
        sleep(2)
        check= soup.find('ul',{"class":"prod_list"}).find("div")
        
        prodList=list()
        while(check!=None):           
            sleep(1)
            driver.execute_script("goodsPageController.moveControl(1)")
            source = driver.page_source
            soup = BeautifulSoup(source,"html.parser")
            s=soup("div",{"class":"tblwrap mt50"})       
            prodList.append(s[3])    
            check= soup.find('ul',{"class":"prod_list"}).find("div")   
        driver.quit()  
    
    
    
        sqlFile=codecs.open("GS.sql","w","utf-8")        
        dumlist=list()
        dumprod_l=list()
        for d in prodList:
            for p in d.find_all("div",{'class':'prod_box'}):
                prod_name=str(p.find('p',{'class':'tit'})).split('>')[1].split('<')[0]
                prod_price=(str(p.find('span',{'class':'cost'})).split('>')[1].split('<')[0])
                if p.find('img') is None:                    
                    prod_img=""                    
                else:
                    prod_img=str(p.find('img')['src'])
                    
                prod_tag=p.find('div',{'class':'flag_box'})
                prod_dum=""
                if(p.find('div',{'class',"ONE_TO_ONE"})!=None):
                    prod_tag='1+1'
                if(p.find('div',{'class',"TWO_TO_ONE"})!=None):
                    prod_tag='2+1'
                if(p.find('div',{'class',"GIFT"})!=None):
                    prod_tag='증정'
                    dum=p.find('div',{'class':'dum_box'})
                    prod_dum=dum_name=str(dum.find('p',{'class':'name'})).split('>')[2].split('<')[0]
                    dum_price=str(dum.find('p',{'class':'price'})).split('>')[2].split('<')[0]
                    dum_img=str(dum.find('img')['src'])                    
                    dumlist.append([prod_name,dum_name]) 
                    dumprod_l.append([dum_name,dum_price,dum_img])                           
                sqlFile.write("insert into GS values(0,'"+prod_name+"' , "+prod_price+" , '"+prod_tag+"' , '"+prod_img+"'); \n")
        
        d_set = set(map(tuple,dumprod_l))
        dumprod_l=[list(x) for x in d_set]
        for data in dumprod_l:
            sqlFile.write("insert into GS_Dumprod values(0, '"+data[0]+"' , "+data[1]+" ,'"+data[2]+"'); \n")     
        for data in dumlist:
            sqlFile.write("insert into GS_Dum values((select prodId from SevenEleven where name='"+data[0]+"'),'"+data[1]+"');\n")            
        sqlFile.close()