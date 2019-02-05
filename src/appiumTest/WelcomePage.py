# -*- coding: UTF-8 -*-
'''
Created on 2016年8月24日

@author: willie
'''

'''
此类用来处理系统弹窗，各种权限
但是优先执行

'''

from appiumTest.PublicClass import clickText


class TanChuangChuLi():
    def tanChuang(self):
        myBoolean=True
        while myBoolean:   
            try:
                if clickText("允许"):                        
                    continue                                      
                elif clickText("跳过"):                        
                    continue
                elif clickText("同 意"):                        
                    continue
                elif clickText("不喜欢"):                        
                    continue
                else:
                    print("未弹出权限处理")   
                    myBoolean=False     
            except:
                print("捕获到异常")
                continue
        else:
            print("退出弹框处理")
