#coding=utf-8
import random
import unittest

import time, os
import traceback
from datetime import datetime    
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class TestOrdersFileImport(unittest.TestCase):    
    url    = 'http://115.29.249.35:9999/'
    driver = webdriver.Chrome('C:\Python27\chromedriver.exe')
    downLoadPath = 'C:\Users\zzz\Downloads'
    
    def setUp(self):        
        print 'set up'
    
    # need browser settings to allow auto save download files without
    # file path specifing
    def test_A1_TemplateDownload(self):
        tempFileName = self.downLoadPath + '\\ImportOrderTemplate.xls'
        
        if(os.path.exists(tempFileName)):
            os.remove(tempFileName)  
                   
        try:
            self.driver.get(self.url)
            time.sleep(3)
        except Exception as e:        
            print(traceback.format_exc())
            self.driver.quit()
        
        btnId="u1"
        elem = self.driver.find_element_by_id(btnId)
        elem.click()
        time.sleep(3)
        
        btnId="u1156"
        elem = self.driver.find_element_by_id(btnId)
        elem.click()
        time.sleep(10)
        
        assert os.path.exists(tempFileName), 'Download template file failed'        
    
    def test_A2_FileImport(self):
        try:
            self.driver.get(self.url)
            time.sleep(3)
        except Exception as e:        
            print(traceback.format_exc())
            self.driver.quit()
        
        elem = self.driver.find_element_by_id('u1')
        elem.click()
        time.sleep(3)
        
        elem = self.driver.find_element_by_id('file')
        elem.send_keys('C:\\Users\\zzz\\Downloads\\ImportOrderTemplate_upload.xls')
        time.sleep(2)
        
        elem = self.driver.find_element_by_id('u1151')
        elem.click()
        time.sleep(5)
        
        elem = self.driver.find_element_by_id('alert-title')
        self.assertEqual(elem.text, u'成功0条，失败10条', 'Import by file failed')
        
        self.driver.quit() 
        
    def tearDown(self):
        print 'td'
        #self.driver.quit() 

