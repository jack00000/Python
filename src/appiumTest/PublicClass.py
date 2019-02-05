# -*- coding: UTF-8 -*-
'''
Created on 2016年8月24日

@author: willie
'''

from appium import webdriver
import time,os
from appium.webdriver.common.touch_action import TouchAction
from os.path import exists


# 连接设备
def connDevice():
    # 指定平台、启动的设备、包名和启动的activity  unicodeKeyboard是使用unicode编码方式发送字符串  resetKeyboard是将键盘隐藏起来
    desired_caps = {'platformName': 'Android', 'platformVersion': '6.0', 'deviceName': '217706d3','appPackage': 'net.easyconn.carman', 'appActivity': '.MainActivity',
                    'unicodeKeyboard':True,'resetKeyboard':True}
    # 关联Appium
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver

driver = connDevice()

# 获取当前时间
def getMyTime():
    mytime=time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))    
    return mytime

# 获取当前时间 文件夹
def getCreatdirTime():
    mytime=time.strftime('%Y-%m-%d_%H',time.localtime(time.time()))    
    return mytime

# 直接通过键值操作对应的功能
def keypress(keyint):
    driver.keyevent(keyint)
    
# 点击resourceid
def clickResourceID(resourceid):
    try:
        if driver.find_element_by_id(resourceid):   
            getScreenShot("点击id前的界面")
            driver.find_element_by_id(resourceid).click()
            time.sleep(0.3)
            getScreenShot("点击id后的界面")
            return True
                
        else:
            print("未找到该控件："+resourceid)
            getScreenShot("未找到该控件")
            return False
    except :
        print("未找到该控件："+resourceid)

    
# 点击resourceid
def clickXpath(xpath):
    try:
        if driver.find_element_by_xpath(xpath):   
            getScreenShot("点击xpath前的界面")
            driver.find_element_by_xpath(xpath).click()
            time.sleep(0.3)
            getScreenShot("点击xpath后的界面")
            return True                
        else:
            print("未找到该控件："+xpath)
            getScreenShot("未找到该控件")
            return False
    except :
        print("未找到该控件："+xpath)

# 长按
def LongPress(name):
    try:
        if driver.find_element_by_name(name):
            getScreenShot("长按"+name+"前的界面")
            action= TouchAction(driver)
            action.long_press(driver.find_element_by_name(name)).perform()
            getScreenShot("长按"+name+"后的界面")
            return True
        else:
            print("未找到名字："+name)
            getScreenShot("未找到文本："+name)
            return False
    except :
        print("未找到该控件："+name)
        
    
# 点击文本
def clickText(text):
    try:
        if driver.find_element_by_name(text):
            getScreenShot("点击"+text+"前的界面")
            driver.find_element_by_name(text).click()
            time.sleep(0.3)
            getScreenShot("点击"+text+"后的界面")
            return True
        else:
            print("未找到名字："+text)
            getScreenShot("未找到文本："+text)
            return False
    except:
        print("未能点击到文本"+text)  


# 查找文本
def findText(text):
    try:   
        if driver.find_element_by_name(text):
            getScreenShot(text)
            return True
        else:
            getScreenShot("未找到文本："+text)
            return False
    except:
        getScreenShot("未找到文本："+text)
        print("未找到文本"+text)  
       
# 文本输入
def setText(resourceid,text):
    try:
        if driver.find_element_by_id(resourceid):
            getScreenShot("点击id前的界面")
            time.sleep(0.5)
            driver.find_element_by_id(resourceid).send_keys(text)
            time.sleep(0.5)
            getScreenShot("点击id后的界面")
        else:
            print("未找到id")
    except:
        getScreenShot("未找到id界面")
        print("未找到id"+resourceid) 


#创建文件夹
def creatdir():
    try:
        mytime=getCreatdirTime()
        filenameexists="C:/Users/Administrator/Documents/"+mytime+""
        if exists(filenameexists):
            return mytime
        else:
            os.makedirs(filenameexists)
            return mytime
    except IOError:
        print(IOError)
# 截屏
def getScreenShot(filename):
    try:
        mytime=getMyTime()
        mycreatdirtime=creatdir()
        myscreenshot="C:/Users/Administrator/Documents/"+mycreatdirtime+"/"+mytime+filename+".png"
        driver.get_screenshot_as_file(myscreenshot)
    except IOError:
        print(IOError)

# 获得机器屏幕大小x,y
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
 
# 屏幕向上滑动
def swipeUp(duration):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.75)   #起始y坐标
    y2 = int(l[1] * 0.25)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,duration)
# 屏幕向下滑动
def swipeDown(duration):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.25)   #起始y坐标
    y2 = int(l[1] * 0.75)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,duration)
# 屏幕向左滑动
def swipeLeft(duration):
    l=getSize()
    x1=int(l[0]*0.75)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.05)
    driver.swipe(x1,y1,x2,y1,duration)
# 屏幕向右滑动
def swipeRight(duration):
    l=getSize()
    x1=int(l[0]*0.05)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.75)
    driver.swipe(x1,y1,x2,y1,duration)
