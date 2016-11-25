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

class TestOrdersFileImport(unittest.TestCase):    
    url    = TestConfig.url
    driver = None
    downLoadPath = TestConfig.downloadPath
    
    def setUp(self):        
        if(TestOrdersFileImport.driver is None):
            TestOrdersFileImport.driver = webdriver.Chrome(TestConfig.chrome)        
    
    # need browser settings to allow auto save download files without
    # file path specifing
    def test_A1_TemplateDownload(self):
        driver = TestOrdersFileImport.driver
        
        tempFileName = self.downLoadPath + '\\ImportOrderTemplate.xls'
        
        if(os.path.exists(tempFileName)):
            os.remove(tempFileName)  
                   
        try:
            driver.get(self.url)
            time.sleep(3)
        except Exception as e:        
            print(traceback.format_exc())
            driver.quit()
        
        btnId="u1"
        elem = driver.find_element_by_id(btnId)
        elem.click()
        time.sleep(3)
        
        btnId="u1156"
        elem = driver.find_element_by_id(btnId)
        elem.click()
        time.sleep(10)
        
        assert os.path.exists(tempFileName), 'Download template file failed'        
    
    def test_A2_FileImport(self):
        driver = TestOrdersFileImport.driver
        try:
            driver.get(self.url)
            time.sleep(3)
        except Exception as e:        
            print(traceback.format_exc())
            driver.quit()
        
        elem = driver.find_element_by_id('u1')
        elem.click()
        time.sleep(3)
        
        elem = driver.find_element_by_id('file')
        tempFileName = self.downLoadPath + '\\ImportOrderTemplate_upload.xls'
        elem.send_keys(tempFileName)
        time.sleep(2)
        
        elem = driver.find_element_by_id('u1151')
        elem.click()
        time.sleep(5)
        
        elem = driver.find_element_by_id('alert-title')
        self.assertEqual(elem.text, u'成功0条，失败10条', 'Import by file failed')
        
        driver.quit() 
        
    #def tearDown(self):
        #print 'td'
        #self.driver.quit() 

