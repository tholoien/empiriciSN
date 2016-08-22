"""
Test code for empiriciSN class.
"""
import unittest
import numpy as np
from empiriciSN import empiriciSN

class empiriciSNTestCase(unittest.TestCase):
    "TestCase class for empiriciSN class."
    def setUp(self):
        """
        Set up each test with a new empiriciSN object with existing model.
        """
        self.empiriciSN=empiriciSN(model_file = 'empiriciSN_model_7comp.fit')
        self.files=[]
    
    def test_GetSN(self):
        sample = self.empiriciSN.XDGMM.sample()[0]
        testdat=np.append(np.array([np.nan,np.nan,np.nan]),sample[3:])
        sn = self.empiriciSN.get_SN(testdat)
        self.assertEqual(sn.shape,(1,3))

if __name__ == '__main__':
    unittest.main()
