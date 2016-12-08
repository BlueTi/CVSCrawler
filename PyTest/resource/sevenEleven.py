'''
Created on 2016. 11. 28.

@author: Administrator
'''
from threading import Thread
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


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
        check=soup.find_all("li",{'class':'btn_more'})
        
        """
        while(len(check==0)):
            driver.execute("fncMore('1');")
            source=driver.page_source
            soup = BeautifulSoup(source,"html.parser")
            check=soup.find_all("li",{'class':'btn_more'})
            sleep(2)            
        driver.quit()-#
        """
        
        prodList=soup()