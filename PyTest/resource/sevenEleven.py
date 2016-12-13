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
        script_list=['1','2','3','4']
        url="https://www.7-eleven.co.kr/product/presentList.asp"
        driver = webdriver.Chrome('./driver/chromedriver.exe')        
        sqlfile=codecs.open('sevenEleven.sql', 'w', 'utf-8')
        dumsql=codecs.open('sevenDum.sql','w','utf-8')   
        driver.get(url)
        sleep(2)
        for no in script_list:
            print("fncTab('"+no+"')")
            driver.execute_script("fncTab('"+no+"');")
            sleep(5)
            source = driver.page_source
            soup = BeautifulSoup(source,"html.parser")
            check=0
        
            while(1):            
                driver.execute_script("fncMore('"+no+"');")
                sleep(1)
                source=driver.page_source
                soup = BeautifulSoup(source,"html.parser")
                tem=(len(soup.find("ul",{"id":"listUl"}).find_all("li")))
                if check==tem: 
                    break;
                else:
                    check=tem
                       
            prodList=soup.find("ul",{"id":"listUl"}).find_all("li")     
            dumlist=[]   
            for data in prodList:
                if(data.find('div',{'class':'infowrap'})!=None):                
                    prodName=data.find('div',{'class':'name'}).get_text()
                    prodPrice=data.find('div',{'class':'price'}).get_text().replace('\n','')
                    prodImg="https://7-eleven.co.kr"+str(data.find('img')['src'])
                    prodTag=str(data.find('ul',{'class':'tag_list_01'}).get_text().replace('\n',''))
                    prodDum=data.find_all("div",{"class":"infowrap"})
                    if(len(prodDum)>1):           
                        dumName=prodDum[1].find('div',{'class':'name'}).get_text()
                        if(prodDum==''): continue
                        dumPrice=str(prodDum[1].find('span').get_text())
                        dumImg="https://7-eleven.co.kr"+str(data.find_all('img')[1]['src'])
                        prodDum=dumName
                        print(prodDum+' '+dumPrice+' '+dumImg)
                        dumlist.append([prodDum,dumPrice,dumImg])
                    else: prodDum=''
                    #print(prodName+"','"+prodPrice+"','"+prodTag+"','"+prodImg+"',"+str(prodDum))
                    sqlfile.write("insert into prodList values('"+prodName+"','"+prodPrice+"','"+prodTag+"','"+prodImg+"','"+prodDum+"','sevenEleven'); \n")
            
            for data in dumlist:
                dumsql.write("insert into dumList values('"+data[0]+"','"+data[1]+"','"+data[2]+"');\n")
                    