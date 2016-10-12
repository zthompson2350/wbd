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
  
# # !!!IMPLEMENTATION CHANGED, TEST NO LONGER VALID!!!        
# #Asserts true the first time it is set, false the second   
#     def test100setSightingFileDuplicateFile(self):
#         aFix = Fix.Fix()
#         self.assertTrue(aFix.setSightingFile("sightingFile.xml"))
#         self.assertFalse(aFix.setSightingFile("sightingFile.xml"))
        
    def test105setSightingFileNotXML(self):
        aFix = Fix.Fix()
        expectedDiag = self.className + "setSightingFile:"
        with self.assertRaises(ValueError) as context:
            aFix.setSightingFile("sightingFile")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)])
        
    def test110setSightingFilePass(self):
        aFix = Fix.Fix()
        expected = "sightingFile.xml"
        self.assertEquals(expected, aFix.setSightingFile("sightingFile.xml"))
            
        
        

    def test200getSightingsNoSightingFile(self):
        aFix = Fix.Fix()
        expectedDiag = self.className + "getSightings:"
        with self.assertRaises(ValueError) as context:
            aFix.getSightings()
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)])
        
    def test205getSightingsPass(self):
        aFix = Fix.Fix()
        aFix.setSightingFile("sightingFile.xml")
        expected = ("0d0.0", "0d0.0")
        self.assertEquals(expected, aFix.getSightings())
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()