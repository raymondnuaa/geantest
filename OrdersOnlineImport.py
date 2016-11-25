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

class TestOrdersOnlineImport(unittest.TestCase):
    url    = TestConfig.url
    driver = None
    
    def setUp(self):
        if(TestOrdersOnlineImport.driver is None):
            TestOrdersOnlineImport.driver = webdriver.Chrome(TestConfig.chrome) 
        
    def test_B1_ImportSettings(self):
        driver = TestOrdersOnlineImport.driver
        try:
            driver.get(self.url)
            time.sleep(3)
        except Exception as e:        
            print(traceback.format_exc())
            driver.quit()
            
        elem = driver.find_element_by_id('u5')
        elem.click()
        time.sleep(3)
        
        select = Select(driver.find_element_by_id("u651_input"))        
        select.select_by_visible_text(u"易尊商城")        
        time.sleep(1)
        
        select = Select(driver.find_element_by_id("u665_input"))        
        select.select_by_visible_text(u"预约导入")        
        time.sleep(1)
        
        
        elem = driver.find_element_by_id('u657_input')
        elem.send_keys('2016-11-13 23:25:25')
        time.sleep(1)
        
        elem = driver.find_element_by_id('u661')
        elem.click()
        time.sleep(3)
        
        
        elem  = driver.find_element_by_id('alert-title')
        self.assertEqual(elem.text, u'请选择开始时间！', 'Online import failed')
    
    def test_B2_OnlineImport(self):    
        driver = TestOrdersOnlineImport.driver
        driver.quit()
        pass

