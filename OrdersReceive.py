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

class TestOrdersReceive(unittest.TestCase):
    url    = TestConfig.url
    driver = None
    
    def setUp(self):
        if(TestOrdersReceive.driver is None):
            TestOrdersReceive.driver = webdriver.Chrome(TestConfig.chrome)
    
    def test_G1_QueryResults(self):    
        driver = TestOrdersReceive.driver
        try:
            driver.get(self.url)
            time.sleep(3)
        except Exception as e:        
            print(traceback.format_exc())
            driver.quit()
        
        pathStr = "//a[@href='%s']" % (self.url+'fetchreceiveOrders')
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
        
    def test_G2_ReceiveButton(self):    
        pass
        
    def test_G3_DetailsCheck(self):   
        driver = TestOrdersReceive.driver
        
        driver.quit() 
        pass
        
    