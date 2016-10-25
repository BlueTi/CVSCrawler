#-*- coding: utf-8 -*-
'''
Created on 2016. 10. 12.

@author: 305
'''

import re
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from resource import CU 


def createGS25_DB():
    url="http://gs25.gsretail.com/gscvs/ko/products/event-goods#;"
    driver = webdriver.Chrome('./driver/chromedriver.exe')
    driver.get(url)
    source = driver.page_source
    soup = BeautifulSoup(source,"html.parser")    
    driver.find_element_by_id("TOTAL").click()
    sleep(2)
    check= soup.find('ul',{"class":"prod_list"}).find("div")
    
    prodList=list()
    while(check!=None):           
        sleep(2)
        driver.execute_script("goodsPageController.moveControl(1)")
        source = driver.page_source
        soup = BeautifulSoup(source,"html.parser")
        s=soup("div",{"class":"tblwrap mt50"})       
        prodList.append(s[3])    
        check= soup.find('ul',{"class":"prod_list"}).find("div")   
    driver.quit()  
    
    
    for d in prodList:
        for p in d.find_all("div",{'class':'prod_box'}):
            prod_name=str(p.find('p',{'class':'tit'})).split('>')[1].split('<')[0]
            prod_price=(str(p.find('span',{'class':'cost'})).split('>')[1].split('<')[0])
            prod_img=str(p.find('img')['src'])
            prod_tag=p.find('div',{'class':'flag_box'})
            if(p.find('div',{'class',"ONE_TO_ONE"})!=None):
                #print(str(prod_tag))
                pass
            if(p.find('div',{'class',"TWO_TO_ONE"})!=None):
                #print(str(prod_tag))
                pass
            if(p.find('div',{'class',"GIFT"})!=None):
                print(str(p.find('div',{'class':'dum_box'})))
                pass      
    
    
    
def create717_DB():
    pass
if __name__ == '__main__':
    pass
    #CU.CU()
    createGS25_DB()
    