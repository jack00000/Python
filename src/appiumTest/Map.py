# -*- coding:utf-8 -*-
'''
Created on 2017年1月18日

@author: willie
'''
from asyncio.tasks import sleep


'''
    net.easyconn.carman:id/ll_normal
    net.easyconn.carman:id/tv_search
    net.easyconn.carman:id/et_search
    net.easyconn.carman:id/tv_enter
'''
from appiumTest.PublicClass import setText,clickResourceID,clickXpath,keypress,getScreenShot
import time

class mymap():
    
    def mySearchtext(self):
        clickResourceID("net.easyconn.carman:id/ll_normal")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/tv_search")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/tv_input")
        time.sleep(1)
        setText("net.easyconn.carman:id/et_search", "汉街")
        time.sleep(1)
        clickXpath('//android.widget.TextView[@text="汉街(楚河南路)"]')
        time.sleep(2)
        clickXpath('//android.widget.TextView[@text="汉街(楚河南路)"]/../../android.widget.ImageView')
        time.sleep(1)
        clickXpath('//android.widget.TextView[@text="汉街(楚河南路)"]/../../android.widget.ImageView')
        time.sleep(1)
        clickXpath('//android.widget.TextView[@text="汉街(楚河南路)"]/../../android.widget.LinearLayout[2]')
        time.sleep(13)
        getScreenShot("导航界面")
        keypress(4)
        time.sleep(2)
        getScreenShot("返回主界面")
        time.sleep(2)
        keypress(4)
        time.sleep(2)
        
        
        