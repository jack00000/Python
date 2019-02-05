# -*- coding:UTF-8 -*-
'''
Created on 2017年1月23日

@author: willie
'''
from appiumTest.PublicClass import clickResourceID, clickXpath, keypress,setText,clickText
import time
class musicMain():

    '''
    net.easyconn.carman:id/img_back
    net.easyconn.carman:id/rl_music_prev
    net.easyconn.carman:id/rl_music_next
    net.easyconn.carman:id/rl_music_third
    net.easyconn.carman:id/rl_music_play_pause
    net.easyconn.carman:id/tv_more  乐库
    
    net.easyconn.carman:id/tv_recommend
    net.easyconn.carman:id/tv_local
    net.easyconn.carman:id/tv_collection
    net.easyconn.carman:id/tv_download
    '''
    def musicList(self):
        clickResourceID('net.easyconn.carman:id/rl_cover_album')
        time.sleep(1)
        clickResourceID('net.easyconn.carman:id/tv_more')
        time.sleep(3)
        clickResourceID('net.easyconn.carman:id/tv_local')
        time.sleep(2)
        clickText("收藏")
        time.sleep(2)
        clickText("下载")
        time.sleep(2)
        clickResourceID("net.easyconn.carman:id/tv_recommend")
        time.sleep(2)
        clickXpath('//android.widget.TextView[@text="晓松奇谈"]/../../android.widget.ImageView')
        time.sleep(2)

        clickResourceID("net.easyconn.carman:id/tv_play_select")
        time.sleep(3)
        #排序
        clickResourceID("net.easyconn.carman:id/tv_sort")
        time.sleep(2)
        clickResourceID("net.easyconn.carman:id/tv_sort")
        time.sleep(1)
        #上下曲、暂停播放
        clickResourceID("net.easyconn.carman:id/rl_music_next")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/rl_music_prev")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/rl_music_play_pause")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/rl_music_play_pause")
        time.sleep(1)
        
        #搜索功能
        clickResourceID('net.easyconn.carman:id/tv_more')
        time.sleep(2)
        clickResourceID("net.easyconn.carman:id/rl_search")
        time.sleep(1)
        clickXpath('//android.widget.TextView/../../../../android.widget.LinearLayout/android.widget.LinearLayout')
        setText("net.easyconn.carman:id/et_search","郭德纲")
        keypress(4)
        
         
        clickResourceID("net.easyconn.carman:id/img_back")
        clickResourceID("net.easyconn.carman:id/tv_download")
        time.sleep(5)
        keypress(4)
        clickResourceID("net.easyconn.carman:id/img_back")
        
        
        
        
        
        
        