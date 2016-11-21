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

class TestOrdersAudit(unittest.TestCase):
    url    = TestConfig.url
    driver = webdriver.Chrome(TestConfig.chrome)
    
    def setUp(self):
        pass
    
    def test_F1_ResetQueryCondition(self):    
        driver = self.driver
        try:
            driver.get(self.url)
            time.sleep(3)
        except Exception as e:        
            print(traceback.format_exc())
            self.driver.quit()
        
        pathStr = "//a[@href='%s']" % (self.url+'ManagerIndex')
        elem = driver.find_element_by_xpath(pathStr)
        elem.click()
        time.sleep(3)
        
        elem = driver.find_element_by_xpath("//img[@src='images/down1.png']")
        elem.click()
        time.sleep(3)
        
        elem  = driver.find_element_by_name('seqNo')
        elem.send_keys('123456789')
        time.sleep(1)
        
        elem  = driver.find_element_by_name('netinfo_number')
        elem.send_keys('987654321')
        time.sleep(1)
        
        elem = driver.find_element_by_xpath("//button[@onclick='onclickResetBtn()']")
        elem.click()
        time.sleep(3)
        
        elem  = driver.find_element_by_name('seqNo')
        orderSn = elem.text
        
        elem  = driver.find_element_by_name('netinfo_number')
        msisdn  = elem.text
        
        self.assertEqual(orderSn+msisdn, '')
    
    def test_F2_QueryResult(self):
        driver = self.driver
        elem   = driver.find_element_by_name('seqNo')
        elem.send_keys('14794481969')
        time.sleep(1)
        
        elem = driver.find_element_by_xpath("//button[@onclick='onclickQueryOrdersBtn()']")
        elem.click()
        time.sleep(3)
        
        elem = driver.find_element_by_id("dataTable_g")
        self.assertTrue(elem.text.find('14794481969') != -1)
    
    def test_F3_AuditButton(self):    
        pass
        
    def test_F4_DetailsAudit(self): 
        self.driver.quit()   
        pass
        
    