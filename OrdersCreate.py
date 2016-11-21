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

class TestOrdersCreate(unittest.TestCase):
    url    = TestConfig.url
    driver = webdriver.Chrome(TestConfig.chrome)
    
    def setUp(self):
        pass
        
    def test_C1_MandatoryInputFields(self):
        driver = self.driver
        try:
            driver.get(self.url)
            time.sleep(3)
        except Exception as e:        
            print(traceback.format_exc())
            self.driver.quit()
        
        pathStr = "//a[@href='%s']" % (self.url+'inputOrder')
        elem = driver.find_element_by_xpath(pathStr)
        elem.click()
        time.sleep(3)
        
        elem = driver.find_element_by_class_name('bluebtu')
        elem.click()
        time.sleep(3)
        
        elem  = driver.find_element_by_id('alert-title')
        self.assertEqual(elem.text, u'第三方订单号不能为空！', 'Third party number check failed')
        

    def test_C2_OptionalInputFields(self):
        driver = self.driver
        elem  = driver.find_element_by_id('alert-yesbtn-title')
        elem.click()
        time.sleep(1)
        
        elem  = driver.find_element_by_name('order_sn')
        elem.send_keys('123456789')
        time.sleep(1)
        
        elem  = driver.find_element_by_name('msisdn_new')
        elem.send_keys('987654321')
        time.sleep(1)
        
        elem = driver.find_element_by_class_name('graybtu')
        elem.click()
        time.sleep(3)
        
        elem  = driver.find_element_by_name('order_sn')
        orderSn = elem.text
        
        elem  = driver.find_element_by_name('msisdn_new')
        msisdn  = elem.text
        
        self.assertEqual(orderSn+msisdn, '')
        
        self.driver.quit()
        pass
