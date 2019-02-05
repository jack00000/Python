# -*- coding: UTF-8 -*-
'''
Created on 2017年1月17日

@author: willie
'''
from appiumTest.PublicClass import swipeLeft,getScreenShot,LongPress,keypress,clickXpath,clickText,swipeRight
import time

class threeAppTest():
    
    def threeApp(self):
        swipeLeft(1000)
        time.sleep(2)
        getScreenShot("swipe left")
        LongPress("微信")
        keypress(4)
        time.sleep(1)
        clickXpath('//android.widget.TextView[@text="微信"]/../../../android.widget.RelativeLayout[3]/android.widget.ImageView[1]')
        time.sleep(2)
        keypress(4)
        time.sleep(2)
        clickText("添加应用")
        time.sleep(2)
        keypress(4)
        time.sleep(1)
        swipeRight(1000)
        
        