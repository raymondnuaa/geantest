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

class TestOrdersQuery(unittest.TestCase):
    url    = TestConfig.url
    driver = None
    
    def setUp(self):
        if(TestOrdersQuery.driver is None):
            TestOrdersQuery.driver = webdriver.Chrome(TestConfig.chrome) 
        
    def test_D1_ResetSettings(self):
        driver = TestOrdersQuery.driver
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
          
        elems = driver.find_elements_by_xpath("//div[@class='third_header_title third_header_title_on']")        
        elems[0].click()
        time.sleep(3)
        
        elem = driver.find_element_by_xpath("//div[@routename='queryOrders']")        
        elem.click()
        time.sleep(3)
        
        driver.switch_to.frame('queryOrders')        
        
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
        
    def test_D2_QueryResults(self):    
        driver = TestOrdersQuery.driver
        
        elem  = driver.find_element_by_name('seqNo')
        elem.send_keys('1114')
        time.sleep(1)
        
        elem = driver.find_element_by_xpath("//button[@onclick='onclickQueryOrdersBtn()']")
        elem.click()
        time.sleep(3)        
        
        elem = driver.find_element_by_xpath("//table[@id='table_id_example']/tbody/tr/td[2]/div[2]")
        self.assertEqual(elem.text, u"订单编号：1114", 'Order query failed')

    def test_D3_OrderDetails(self):
        driver = TestOrdersQuery.driver
        elem = driver.find_element_by_xpath("//table[@id='table_id_example']/tbody/tr/td[6]/a")
        elem.click()
        time.sleep(3)
        
        nowHandle=driver.current_window_handle
        
        for handle in driver.window_handles:
            if handle!=nowHandle:
                driver.switch_to_window(handle)
            
        elem = driver.find_element_by_xpath("//table[@class='tableforinput']/tbody/tr[2]/td[1]")
        self.assertEqual(elem.text, u'第三方订单号：')
        
        driver.switch_to_window(nowHandle)
        driver.switch_to.frame('queryOrders')   
        
    def test_D4_ResultsExport(self):
        driver = TestOrdersQuery.driver        
        
        curTime = time.time()
        time.sleep(2)
        newFile = False
                
        elem = driver.find_element_by_xpath("//button[@onclick='onclickExportQueryRes(this)']")
        elem.click()
        time.sleep(3)
        
        for f in os.listdir(TestConfig.downLoadPath):
            fileTime = os.path.getctime(os.path.join(TestConfig.downLoadPath, f))
            if(fileTime>curTime):
                newFile = True
                os.remove(os.path.join(TestConfig.downLoadPath, f))
        
        self.assertTrue(newFile)
        driver.quit()