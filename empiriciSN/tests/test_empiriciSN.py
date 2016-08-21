"""
Test code for empiriciSN class.
"""
import os
import unittest
import numpy as np
from empiriciSN import empiriciSN

class empiriciSNTestCase(unittest.TestCase):
    "TestCase class for empiriciSN class."
    def setUp(self):
        """
        Set up each test with a new empiriciSN object with existing model.
        """
        self.empiriciSN=empiriciSN(model_file = '../../models/empiriciSN_model_7comp.fit')
        self.files=[]

if __name__ == '__main__':
    unittest.main()
