"""
Test code for empiriciSN class.
"""
import unittest
import numpy as np
import empiriciSN
import urllib
import os

class EmpiricistTestCase(unittest.TestCase):
    "TestCase class for Empiricist class."
    def setUp(self):
        """
        Set up each test with a new empiriciSN object with existing model.
        """
        url = 'https://raw.githubusercontent.com/tholoien/empiriciSN/' \
            + 'master/models/empiriciSN_model.fit'
        path = './empiriciSN_model.fit'
        urllib.urlretrieve(url, path)
        self.empiricist = empiriciSN.Empiricist(model_file = 'empiriciSN_model.fit')
        self.files = []

    def tearDown(self):
        """
        Clean up files saved by tests
        """
        os.remove('empiriciSN_model.fit')
        if os.path.isfile('snls_master.csv'):
            os.remove('snls_master.csv')
        if os.path.isfile('empiriciSN_model.fit'):
            os.remove('empiriciSN_model.fit')

    def test_get_SN(self):
        url = 'https://raw.githubusercontent.com/tholoien/empiriciSN/' \
            +'master/models/empiriciSN_model.fit'
        path = './empiriciSN_model.fit'
        urllib.urlretrieve(url, path)
        self.empiricist.read_model('empiriciSN_model.fit')
        sample = self.empiricist.XDGMM.sample()[0]
        testdat = np.append(np.array([np.nan,np.nan,np.nan]),sample[3:])
        sn = self.empiricist.get_SN(testdat)
        self.assertEqual(sn.shape,(1,3))

    def test_fit(self):
        url = 'https://dl.dropboxusercontent.com/u/5900205/' \
            +'empiriciSN_data/snls_master.csv'
        path = './snls_master.csv'
        urllib.urlretrieve(url, path)

        this_model_file = self.empiricist.model_file

        self.empiricist.fit_from_files(['snls_master.csv'],n_components=1)

        self.assertEqual(self.empiricist.model_file,this_model_file)

    def test_get_logR(self):
        url = 'https://raw.githubusercontent.com/tholoien/empiriciSN/' \
            +'master/models/empiriciSN_model.fit'
        path = './empiriciSN_model.fit'
        urllib.urlretrieve(url, path)
        self.empiricist.read_model('empiriciSN_model.fit')
        sample = self.empiricist.XDGMM.sample()[0]

        indeces = np.array([3,5,6,7,8,9,10,11,12,13,14])
        X = sample[indeces]

        logR = self.empiricist.get_logR(indeces,4,X)

        self.assertNotEqual(logR,0.0)
    
    def test_get_local_SB(self):
        sb_params = np.array([1,21.402,0.22,0.8593072,0.7847312,20.426,
                              0.046,0.9257621,0.1127986,19.895,0.03,
                              0.6392374,0.08155595,19.619,0.034,
                              0.7765083,0.08438506,19.311,0.087,
                              1.039772,0.3918832])
        logR = np.log10(1.76/0.6392374)
        
        SB,SBerr = self.empiricist.get_local_SB(sb_params,logR)
        
        self.assertNotEqual(0,len(SB))

if __name__ == '__main__':
    unittest.main()
