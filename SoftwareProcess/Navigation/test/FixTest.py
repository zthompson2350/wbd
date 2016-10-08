'''
    Created on Oct 8, 2016
        @author: Zachary Thompson
'''
import unittest
import Navigation.prod.Fix as Fix

class FixTest(unittest.TestCase):

    def setUp(self):
        self.className = "Fix."   
    def tearDown(self):
        pass
    
    def testName(self):
        pass

    def test000InitializationTest(self):
        self.assertIsInstance(Fix.Fix(), Fix.Fix)
        
    def test005setSightingFileValueError(self):
        aFix = Fix.Fix()
        expectedDiag = self.className + "setSightingFile:"
        with self.assertRaises(ValueError) as context:
            aFix.setSightingFile()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)])
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()