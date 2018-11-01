from threading import Thread
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep, strftime
import codecs
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Emart24(Thread):
    def __init__(self):
        super(Emart24,self).__init__()
    
    def run(self):
        Emart24.create_Emart24_DB(self)
        
    def create_Emart24_DB(self):
        url="https://www.emart24.co.kr/product/eventProduct.asp"
        driver=webdriver.Chrome("./driver/chromedriver.exe")
        driver.get(url)
        
        page_numb=1
        check=True
        item_list=list()
        while(check):
            driver.execute_script("javascript:goPage('"+str(page_numb)+"')")
            sleep(0.2)
            page_numb+=1
            soup=BeautifulSoup(driver.page_source,"html.parser")
            for d in soup.find_all("div",{"class":"box"}):
                item_list.append(d)
                next=soup.find("a",{"class":"next bgNone"})["href"]
                if(next=="#none"):
                    check=False
        driver.quit()

        sql_file=codecs.open("Emart24.sql","w","utf8")
        position=1
        for data in item_list:
            item_name=str(data.find("p",{"class":"productDiv"})).split('>')[1].split('<')[0]
            item_price=str(data.find("p",{"class":"price"})).replace('<p class="price">',"").replace("</p>","")

            if "→" in item_price:
                item_price=item_price.replace("<span><s>","")
                item_price=item_price.replace("</s>","")
                item_price=item_price.replace("</span>","")

            item_img="https://www.emart24.co.kr/"+str(data.find("p",{"class":"productImg"}).find("img")["src"])
            item_tag=str(data.find("div",{"class":"lable"}).find("img")["alt"]).split("뱃지")[0].replace(" ","")
            if(item_tag=="X2더블"):
                item_tag="덤증정"
            print(item_name+":"+item_price+":"+item_img+":"+item_tag)
            print("========================================================================================")
            sql_file.write("insert into prod_list values(4"+strftime("%y%m")+str(position).zfill(3)+",'"+item_name+"','"+item_img+"','"+item_price+"','"+item_tag+"');\n")
            position+=1
        sql_file.close()

        
        
    
        
    
    