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

class TestOrdersAccount(unittest.TestCase):
    url    = TestConfig.url
    driver = webdriver.Chrome(TestConfig.chrome)
    
    def setUp(self):
        pass
    
    def test_I1_QueryResults(self):    
        pass
        
    def test_I2_OperationsButton(self):    
        pass
               
    def test_I3_FallBack(self):   
        pass
        
    