#coding=utf-8
import random
import unittest

import time, os
import traceback
from datetime import datetime    
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from TestConfig import *

class TestOrdersFileImport(unittest.TestCase):    
    url    = TestConfig.url
    driver = None
    downLoadPath = TestConfig.downLoadPath
    
    def setUp(self):        
        if(TestOrdersFileImport.driver is None):
            TestOrdersFileImport.driver = webdriver.Chrome(TestConfig.chrome)        
    
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
        
        elemPath = '//div[text()="%s"]' % u"订单管理"        
        elem = driver.find_element_by_xpath(elemPath)        
        elem.click()
        time.sleep(3)        
        
        #elemPath = "//div[@class='third_header_title'][starts-with(text(), %s)]" % u'订单导入*'
        #elemPath = '//div[text()="%s"]' % u"订单导入"
        #elemPath = '//div[starts-with(text(), %s)]' % u'订单导入'
        
        elems = driver.find_elements_by_xpath("//div[@class='third_header_title ']")        
        elems[0].click()
        time.sleep(3)
        
        elem = driver.find_element_by_xpath("//div[@routename='batchImportOrder']")        
        elem.click()
        time.sleep(3)
        
        driver.switch_to.frame('batchImportOrder')
                
        btnId="u1156"
        elem = driver.find_element_by_id(btnId)
        elem.click()
        time.sleep(10)
        
        assert os.path.exists(tempFileName), 'Download template file failed'        
    
    def test_A2_FileImport(self):
        driver = TestOrdersFileImport.driver
                
        elem = driver.find_element_by_id('file')
        tempFileName = self.downLoadPath + '\\ImportOrderTemplate_upload.xls'
        elem.send_keys(tempFileName)
        time.sleep(2)
        
        elem = driver.find_element_by_id('u1151')
        elem.click()
        time.sleep(5)
        
        elem = driver.find_element_by_xpath("//button[@class='ok_btu']")        
        elem.click()
        time.sleep(5)
        
        elem = driver.find_element_by_xpath("//button[@onclick='errorRecode()']")        
        elem.click()
        time.sleep(3)
        
        elem = driver.find_element_by_xpath("//table[@id='error']/tbody/tr/td[1]")         
        
        self.assertEqual(elem.text, u'11222222433436', 'Import by file failed')
        
        driver.quit() 
        
    #def tearDown(self):
        #print 'td'
        #self.driver.quit() 

