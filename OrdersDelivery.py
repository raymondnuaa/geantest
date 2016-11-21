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

class TestOrdersDelivery(unittest.TestCase):
    url    = TestConfig.url
    driver = webdriver.Chrome(TestConfig.chrome)
    
    def setUp(self):
        pass
    
    def test_J1_QueryResults(self):  
        driver = self.driver
        try:
            driver.get(self.url)
            time.sleep(3)
        except Exception as e:        
            print(traceback.format_exc())
            self.driver.quit()
        
        pathStr = "//a[@href='%s']" % (self.url+'OrderDelivery')
        elem = driver.find_element_by_xpath(pathStr)
        elem.click()
        time.sleep(3)   
        
        
    def test_J2_DeliveryButton(self):    
        pass
               
    def test_J3_FallBack(self):   
        pass
        
    def test_J3_Details(self):
        driver = self.driver
        elem = driver.find_element_by_xpath("//table[@id='dataTable_g']/tbody/tr/td[6]/div/button")
        elem.click()
        time.sleep(3)
          
        driver.quit()