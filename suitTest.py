#coding=utf-8
import random
import unittest
import HTMLTestRunner

#F1S1 functionalities
from OrdersFileImport import TestOrdersFileImport
from OrdersOnlineImport import TestOrdersOnlineImport
from OrdersCreate import TestOrdersCreate
from OrdersQuery import TestOrdersQuery
from OrdersReAssign import TestOrdersReAssign

suite11 = unittest.TestLoader().loadTestsFromTestCase(TestOrdersFileImport)
suite12 = unittest.TestLoader().loadTestsFromTestCase(TestOrdersOnlineImport)
suite13 = unittest.TestLoader().loadTestsFromTestCase(TestOrdersCreate)
suite14 = unittest.TestLoader().loadTestsFromTestCase(TestOrdersQuery)
suite15 = unittest.TestLoader().loadTestsFromTestCase(TestOrdersReAssign)

s1 = [suite11, suite12, suite13, suite14, suite15]

suite = unittest.TestSuite(s1)


#F1S2 functionalities  
from OrdersAudit import TestOrdersAudit
from OrdersReceive import TestOrdersReceive
from OrdersConfirm import TestOrdersConfirm
from OrdersAccount import TestOrdersAccount
from OrdersDelivery import TestOrdersDelivery
    
suite21 = unittest.TestLoader().loadTestsFromTestCase(TestOrdersAudit)
suite22 = unittest.TestLoader().loadTestsFromTestCase(TestOrdersReceive)
suite23 = unittest.TestLoader().loadTestsFromTestCase(TestOrdersConfirm)
suite24 = unittest.TestLoader().loadTestsFromTestCase(TestOrdersAccount)
suite25 = unittest.TestLoader().loadTestsFromTestCase(TestOrdersDelivery)

s2 = [suite21, suite22, suite23, suite24, suite25]


suite = unittest.TestSuite(s1+s2)


#unittest.TextTestRunner(verbosity=2).run(suite)

fp = file('TestReport.html', 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=u'益亨格安自动化生产中心系统',
            description=u'测试用例执行结果统计'
         )
runner.run(suite)