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
        
        if(os.path.exists(tempFileName)):
            return True
        else:
            return False        
    
    def test_A2_FileImport(self):
        print 'a2'
        pass
    
    def tearDown(self):
        print 'td'
        #self.driver.quit() 

