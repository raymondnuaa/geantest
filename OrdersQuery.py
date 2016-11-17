#coding=utf-8
import random
import unittest

import time, os
import traceback
from datetime import datetime    
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class TestOrdersQuery(unittest.TestCase):
    url    = 'http://115.29.249.35:9999/'
    driver = webdriver.Chrome('C:\Python27\chromedriver.exe')
    
    def setUp(self):
        pass
        
    def test_D1_ResetSettings(self):
        driver = self.driver
        try:
            driver.get(self.url)
            time.sleep(3)
        except Exception as e:        
            print(traceback.format_exc())
            self.driver.quit()
        
        pathStr = "//a[@href='%s']" % (self.url+'queryOrders')
        elem = driver.find_element_by_xpath(pathStr)
        elem.click()
        time.sleep(3)
        
        elem  = driver.find_element_by_name('seqNo')
        elem.send_keys('123456789')
        time.sleep(1)
        
        elem  = driver.find_element_by_name('simCardNo')
        elem.send_keys('987654321')
        time.sleep(1)
        
        elem = driver.find_element_by_xpath("//button[@onclick='onclickResetBtn()']")
        elem.click()
        time.sleep(3)
        
        elem  = driver.find_element_by_name('seqNo')
        orderSn = elem.text
        
        elem  = driver.find_element_by_name('simCardNo')
        msisdn  = elem.text
        
        self.assertEqual(orderSn+msisdn, '')
        
    def test_D2_QueryResults(self):    
        driver = self.driver
        
        elem  = driver.find_element_by_name('seqNo')
        elem.send_keys('423696703')
        time.sleep(1)
        
        elem = driver.find_element_by_xpath("//button[@onclick='onclickQueryOrdersBtn()']")
        elem.click()
        time.sleep(3)        
        
        elem = driver.find_element_by_xpath("//table[@id='table_id_example']/tbody/tr/td[2]/div[2]")
        self.assertEqual(elem.text, u"订单编号：423696703", 'Order query failed')

    def test_D3_OrderDetails(self):
        driver = self.driver
        elem = driver.find_element_by_xpath("//table[@id='table_id_example']/tbody/tr/td[6]/a")
        elem.click()
        time.sleep(3)
        
        for handle in driver.window_handles:
            driver.switch_to_window(handle)
            
        
        elem = driver.find_element_by_xpath("//table[@id='productList']/thead/tr/th[1]")
        #imgSrc = elem.get_attribute('src')
        
        
        self.assertTrue(elem.text, u'入网信息')
        
    def test_D4_ResultsExport(self):
        self.driver.quit()