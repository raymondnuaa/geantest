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
        driver = TestOrdersReAssign.driver
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
        elems[1].click()
        time.sleep(3)
        
        elem = driver.find_element_by_xpath("//div[@routename='OrderAllocation']")        
        elem.click()
        time.sleep(3)
        
        driver.switch_to.frame('OrderAllocation')        
        
        elem  = driver.find_element_by_name('seqNo')
        elem.send_keys('123456789')
        time.sleep(1)
        
        elem  = driver.find_element_by_name('mSISDN')
        elem.send_keys('987654321')
        time.sleep(1)
        
        elem = driver.find_element_by_xpath("//button[@onclick='onclickResetBtn()']")
        elem.click()
        time.sleep(3)
        
        elem  = driver.find_element_by_name('seqNo')
        orderSn = elem.text
        
        elem  = driver.find_element_by_name('mSISDN')
        msisdn  = elem.text
        
        self.assertEqual(orderSn+msisdn, '')
    
    def test_E2_QueryResults(self):    
        driver = TestOrdersReAssign.driver
        
        elem  = driver.find_element_by_name('seqNo')
        elem.send_keys('1128')
        time.sleep(1)
        
        elem = driver.find_element_by_xpath("//button[@onclick='onclickQueryOrdersBtn()']")
        elem.click()
        time.sleep(3)        
        
        elem = driver.find_element_by_xpath("//table[@id='dataTable_g']/tbody/tr[2]/td[2]/div[1]")
        self.assertEqual(elem.text, u"订单编号：1128", 'Order query failed')    
        
    def test_E3_OrderDetails(self):
        driver = TestOrdersReAssign.driver
        elem = driver.find_element_by_xpath("//table[@id='dataTable_g']/tbody/tr[2]/td[6]/span/a")
        elem.click()
        time.sleep(3)
        
        nowHandle=driver.current_window_handle
        
        for handle in driver.window_handles:
            if handle!=nowHandle:
                driver.switch_to_window(handle)
            
        elem = driver.find_element_by_xpath("//table[@class='productList']/thead/tr[1]/th[1]")
        self.assertEqual(elem.text, u'入网信息')
        
        driver.switch_to_window(nowHandle)
        driver.switch_to.frame('queryOrders') 
    
    def test_E4_ResultsAssign(self):
        pass
        
    def test_E5_ResultsRecycle(self):
        pass
        
    def test_E6_ResultsBatchAssign(self):
        pass
        
    def test_E7_ResultsBatchRecycle(self):
        driver = TestOrdersReAssign.driver
        driver.quit()
    
    
    

