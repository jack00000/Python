# -*- coding: UTF-8 -*-
'''
Created on 2017年1月4日

@author: willie
'''


'''
    net.easyconn.carman:id/iv_system_back 返回
    net.easyconn.carman:id/ci_user_icon
    net.easyconn.carman:id/tv_nick_name  登录
    
    net.easyconn.carman:id/rl_system_settings 设置
    net.easyconn.carman:id/rl_system_feedback 反馈
    net.easyconn.carman:id/rl_system_about 关于


'''

from appiumTest.PublicClass import clickResourceID,clickText,swipeUp,swipeDown,getScreenShot,swipeLeft,swipeRight, clickXpath
import time

class gerenzhongxin():
    
    def cilckuser(self):
        clickResourceID("net.easyconn.carman:id/id_home_main_user")
    
    def denglu(self):
        clickResourceID("net.easyconn.carman:id/tv_nick_name")
        time.sleep(2)
        clickResourceID("net.easyconn.carman:id/rl_left")
        
    def yemian(self):
        time.sleep(2)
        clickText("我的足迹")
        time.sleep(2)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(2)
        clickText("离线地图")
        time.sleep(1)
        swipeLeft(1000)
        time.sleep(1)
        getScreenShot("xiazaiguanli")
        time.sleep(1)
        swipeRight(1000)
        time.sleep(1)
        getScreenShot("chengshiliebiao")
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        clickText("汽车互联")
        time.sleep(2)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        clickText("连接方控")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        clickText("里程排行")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        clickText("路况提醒")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(2)
        clickText("胎压检测")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)

#         clickText("查找爱车")
#         time.sleep(1)
#         clickResourceID("net.easyconn.carman:id/iv_system_back")
#         time.sleep(1)
               
    def shezhi(self):
        clickResourceID("net.easyconn.carman:id/tv_system_settings")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/cb_screen_always_on")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/welcom_xiaoyi_cb")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/cb_auto_playing_music")
        time.sleep(1)       
        clickResourceID("net.easyconn.carman:id/rb_light")
        time.sleep(1)
        swipeUp(1000)
        time.sleep(1)
        getScreenShot("shiyanshi")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/tv_navi_setting")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/rb_night")
        time.sleep(1)

        clickResourceID("net.easyconn.carman:id/tv_wrc_setting")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        
        clickResourceID("net.easyconn.carman:id/iv_system_lib")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        swipeDown(1000)
        time.sleep(1)
        getScreenShot("wushiyanshi")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/cb_screen_always_on")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/welcom_xiaoyi_cb")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/cb_auto_playing_music")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/rb_auto")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
    
    def feedback(self):
        clickResourceID("net.easyconn.carman:id/rl_system_feedback")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        
    def about(self):
        clickResourceID("net.easyconn.carman:id/rl_system_about")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
    
    