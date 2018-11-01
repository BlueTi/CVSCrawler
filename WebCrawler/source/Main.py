#-*- coding: utf-8 -*-
'''
Created on 2016. 10. 12.

@author: 305
'''
from threading import Thread
import CU, GS,sevenEleven,Emart24

if __name__ == '__main__':  
    #thread1 = Thread(CU.CU().start())
    #thread2 = Thread(GS.GS().start())    
    #thread3 = Thread(sevenEleven.Seven().start())
    thread4 = Thread(Emart24.Emart24().start())
    