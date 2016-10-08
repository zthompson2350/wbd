'''
    Created on Oct 8, 2016
        @author: Zachary Thompson
'''
import unittest
import Navigation.prod.Fix as Fix

class FixTest(unittest.TestCase):

    def setup(self):
        pass
    
    def tearDown(self):
        pass
    
    def testName(self):
        pass

    def test0InitializationTest(self):
        self.assertIsInstance(Fix.Fix(), Fix.Fix)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()