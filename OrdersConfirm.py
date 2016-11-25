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

class TestOrdersConfirm(unittest.TestCase):
    url    = TestConfig.url
    driver = None
    
    def setUp(self):
        if(TestOrdersConfirm.driver is None):
            TestOrdersConfirm.driver = webdriver.Chrome(TestConfig.chrome)
    
    def test_H1_QueryResults(self):    
        pass
        
    def test_H2_OperationsButton(self):    
        pass
        
    def test_H3_RollBackOrder(self):   
        pass
        
    def test_H4_FallBack(self):   
        driver = TestOrdersConfirm.driver
        
        driver.quit() 
        
    