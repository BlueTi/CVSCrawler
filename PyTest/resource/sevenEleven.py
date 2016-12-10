'''
Created on 2016. 11. 28.

@author: Administrator
'''
from threading import Thread
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver
import codecs


class Seven(Thread):
    def __init__(self):
        super(Seven, self).__init__()
        
    def run(self):
        Seven.create7DB(self)
        
    def create7DB(self):
        url="https://www.7-eleven.co.kr/product/presentList.asp"
        driver = webdriver.Chrome('./driver/chromedriver.exe')
        driver.get(url)
        source = driver.page_source
        soup = BeautifulSoup(source,"html.parser")
        check=0
        
        while(1):            
            driver.execute_script("fncMore('1');")
            sleep(2)
            source=driver.page_source
            soup = BeautifulSoup(source,"html.parser")
            tem=(len(soup.find("ul",{"id":"listUl"}).find_all("li")))
            if check==tem: 
                break;
            else:
                check=tem
            
        driver.quit()      
        prodList=soup.find("ul",{"id":"listUl"}).find_all("li")        
        for data in prodList:
            print()
            
            
        