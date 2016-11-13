#coding=utf-8
import random
import unittest

class TestPassFailErrorExample(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_1_PassExample(self):
        pass
        
    def test_2_FailExample(self):
        self.assertFalse(True, "Test fail message")    

    def test_3_ErrorExample(self):
        self.assertFalse(False, failedinfo)
        
