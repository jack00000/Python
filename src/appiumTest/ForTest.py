# -*- coding: UTF-8 -*-
'''
Created on 2016年8月24日

@author: willie
'''
import unittest,HTMLTestRunner,time
from appiumTest.PublicClass import getMyTime, creatdir
from appiumTest.WelcomePage import TanChuangChuLi
from appiumTest.GerenzhongxinPage import gerenzhongxin
from appiumTest.ThreeApp import threeAppTest
from appiumTest.Map import mymap
from appiumTest.MusicPage import musicMain


class Test(unittest.TestCase):
  
    @classmethod
    def setUp(self):
        pass

    @classmethod
    def tearDown(self):
        pass
    
    @classmethod
    def testTanChuang(self):
        TanChuangChuLi.tanChuang(self)
        time.sleep(3)
           
    @classmethod
    def testClickuser(self):
        gerenzhongxin.cilckuser(self)
    
    @classmethod
    def testGeren(self):     
        gerenzhongxin.denglu(self)
        
    @classmethod
    def testYemian(self):     
        gerenzhongxin.yemian(self)
    
    @classmethod
    def testShezhi(self):     
        gerenzhongxin.shezhi(self)   

    @classmethod
    def testFeedback(self):     
        gerenzhongxin.feedback(self)
        
    @classmethod
    def testAbout(self):     
        gerenzhongxin.about(self)
    
    @classmethod
    def testThreeApp(self):     
        threeAppTest.threeApp(self)
           
    @classmethod
    def testMap(self):
        mymap.mySearchtext(self)
        
    @classmethod
    def testMusic(self):
        
        musicMain.musicList(self)    
        
if __name__ == "__main__":

    # 设置一个容器来调用将要执行的测试用例
    myunit =unittest.suite.TestSuite()
    # myunit1 使用此方法运行该类下所有的用例，执行顺序按照字母排序
    # myunit1 = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
    # 需要进行测试的用例，顺序执行
    myunit.addTest(Test("testTanChuang"))
#     myunit.addTest(Test("testClickuser"))
#     myunit.addTest(Test("testGeren"))
#     myunit.addTest(Test("testYemian"))
#     myunit.addTest(Test("testShezhi"))
#     myunit.addTest(Test("testFeedback"))
#     myunit.addTest(Test("testAbout"))
#     myunit.addTest(Test("testThreeApp"))
    myunit.addTest(Test("testMap"))
    myunit.addTest(Test("testMusic"))
    # 获取当前系统时间
    wenjianjia=creatdir()
    mytime=getMyTime()
    myfile="C:/Users/Administrator/Documents/"+wenjianjia+"/result_"+mytime+".html"
    fo = open(myfile,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(
        stream= fo,
        title='测试报告',
        description='用例执行详情'                           
    )
    runner.run(myunit)
    fo.close()