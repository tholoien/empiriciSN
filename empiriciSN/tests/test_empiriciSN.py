"""
Test code for empiriciSN class.
"""
import unittest
import numpy as np
from empiriciSN import empiriciSN
import urllib
import os

class empiriciSNTestCase(unittest.TestCase):
    "TestCase class for empiriciSN class."
    def setUp(self):
        """
        Set up each test with a new empiriciSN object with existing model.
        """
        url='https://raw.githubusercontent.com/tholoien/empiriciSN/master/models/empiriciSN_model_6comp.fit'
        path='./empiriciSN_model_6comp.fit'
        urllib.urlretrieve(url, path)
        self.empiriciSN=empiriciSN(model_file = 'empiriciSN_model_6comp.fit')
        self.files=[]
    
    def tearDown(self):
        """
        Clean up files saved by tests
        """
        os.remove('empiriciSN_model_6comp.fit')
    
    def test_GetSN(self):
        sample = self.empiriciSN.XDGMM.sample()[0]
        testdat=np.append(np.array([np.nan,np.nan,np.nan]),sample[3:])
        sn = self.empiriciSN.get_SN(testdat)
        self.assertEqual(sn.shape,(1,3))

if __name__ == '__main__':
    unittest.main()
