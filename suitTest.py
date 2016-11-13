#coding=utf-8
import random
import unittest
import HTMLTestRunner

from OrdersFileImport import TestOrdersFileImport
from OrdersOnlineImport import TestOrdersOnlineImport
from OrdersCreate import TestOrdersCreate
from OrdersQuery import TestOrdersQuery
from OrdersReAssign import TestOrdersReAssign

from PassFailErrorExample import TestPassFailErrorExample

if __name__ == '__main__':    
    
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestOrdersFileImport)
    #suite2 = unittest.TestLoader().loadTestsFromTestCase(TestOrdersOnlineImport)
    #suite3 = unittest.TestLoader().loadTestsFromTestCase(TestOrdersCreate)
    #suite4 = unittest.TestLoader().loadTestsFromTestCase(TestOrdersQuery)
    #suite5 = unittest.TestLoader().loadTestsFromTestCase(TestOrdersReAssign)
    #suite6 = unittest.TestLoader().loadTestsFromTestCase(TestPassFailErrorExample)
    
    #suite = unittest.TestSuite([suite1, suite2, suite3, suite4, suite5, suite6])
    
    suite = unittest.TestSuite([suite1])
    
    #unittest.TextTestRunner(verbosity=2).run(suite)
    
    
    fp = file('TestReport.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title=u'益亨格安自动化生产中心系统',
                description=u'测试用例执行结果统计'
             )
    runner.run(suite)