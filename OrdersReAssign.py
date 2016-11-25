#coding=utf-8
import random
import unittest

import time, os
import traceback
from datetime import datetime    
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from TestConfig import *

class TestOrdersReAssign(unittest.TestCase):
    url    = TestConfig.url
    driver = None
    
    def setUp(self):
        if(TestOrdersReAssign.driver is None):
            TestOrdersReAssign.driver = webdriver.Chrome(TestConfig.chrome) 
    
    def test_E1_ResetSettings(self):    
        pass
    
    def test_E2_QueryResults(self):    
        pass
        
    def test_E3_QueryTemplateDownload(self):    
        pass
        
    def test_E4_BatchQuery(self):   
        pass
        
    def test_E5_OrderDetails(self):
        pass
    
    def test_E6_ResultsAssign(self):
        pass
        
    def test_E7_ResultsRecycle(self):
        pass
        
    def test_E8_ResultsBatchAssign(self):
        pass
        
    def test_E9_ResultsBatchRecycle(self):
        driver = TestOrdersReAssign.driver
        driver.quit()
    
    
    

