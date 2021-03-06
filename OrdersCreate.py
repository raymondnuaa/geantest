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
    driver = None
    
    def setUp(self):
        if(TestOrdersCreate.driver is None):
            TestOrdersCreate.driver = webdriver.Chrome(TestConfig.chrome) 
        
    def test_C1_MandatoryInputFields(self):
        driver = TestOrdersCreate.driver

        try:
            driver.get(self.url)
            time.sleep(3)
        except Exception as e:        
            print(traceback.format_exc())
            driver.quit()
        
        elemPath = '//div[text()="%s"]' % u"订单管理"        
        elem = driver.find_element_by_xpath(elemPath)        
        elem.click()
        time.sleep(3)
          
        elems = driver.find_elements_by_xpath("//div[@class='third_header_title ']")        
        elems[0].click()
        time.sleep(3)
        
        elem = driver.find_element_by_xpath("//div[@routename='inputOrder']")        
        elem.click()
        time.sleep(3)
        
        driver.switch_to.frame('inputOrder')
        
        
        elem = driver.find_element_by_xpath("//button[@onclick='saveInfoToLocalStorage()']")
        elem.click()
        time.sleep(3)        
        
        elem  = driver.find_element_by_id('alert-title')
        self.assertEqual(elem.text, u'第三方订单号不能为空！', 'Third party number check failed')
        

    def test_C2_OptionalInputFields(self):
        driver = TestOrdersCreate.driver
        
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
        
        driver.quit()
        pass
