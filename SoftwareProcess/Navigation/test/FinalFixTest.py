'''
Created on Dec 3, 2016

@author: zat00
'''
import unittest
import uuid
import os
import Navigation.prod.Fix as F

class TestFix2(unittest.TestCase):

    def setUp(self):
        self.className = "Fix."
        self.logStartString = "Log file"
        self.logSightingString = "Sighting file"
        self.logAriesString = "Aries file"
        self.logStarString = "Star file"
        
        # set default log file name
        self.DEFAULT_LOG_FILE = "log.txt"
        if(os.path.isfile(self.DEFAULT_LOG_FILE)):
            os.remove(self.DEFAULT_LOG_FILE)
            
        # generate random log file name
        self.RANDOM_LOG_FILE = "log" + str(uuid.uuid4())[-12:] + ".txt"

    def test100_010_ShouldConstructFix(self):
        'Fix.__init__'
        self.assertIsInstance(F.Fix(), F.Fix, 
                              "Major error:  Fix not created")
        
    def test100_020_ShouldConstructFixWithDefaultFile(self):
        theFix = F.Fix()
        try:
            theLogFile = open(self.DEFAULT_LOG_FILE, 'r')
            entry = theLogFile.readline()
            del theLogFile
            self.assertNotEquals(-1, entry.find("Log file"), 
                                 "Minor:  first line of log is incorrect")
        except IOError:
            self.fail()
        self.assertIsInstance(theFix, F.Fix, 
                              "Major:  log file failed to create")
        
    def test100_025_ShouldConstructWithKeywordParm(self):
        try:
            theFix = F.Fix(logFile=self.RANDOM_LOG_FILE)
            self.assertTrue(True)
        except:
            self.fail("Minor: incorrect keyword specified")
            self.cleanup()
            
    def test100_030_ShouldConstructFixWithNamedFile(self):
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        try:
            theLogFile = open(self.RANDOM_LOG_FILE, 'r')
            entry = theLogFile.readline()
            del theLogFile
            self.assertNotEquals(-1, entry.find(self.logStartString), 
                                 "Minor:  first line of log is incorrect")
        except IOError:
            self.fail()
        self.assertIsInstance(theFix, F.Fix, "major:  log file failed to create")
        self.cleanup() 
        
    def test100_040_ShouldConstructFixWithExistingFile(self):
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        theFix = F.Fix(self.RANDOM_LOG_FILE)
        try:
            theLogFile = open(self.RANDOM_LOG_FILE, 'r')
            numberOfExpectedEntries = 2
            for _ in range(numberOfExpectedEntries):
                entry = theLogFile.readline()
                self.assertNotEquals(-1, entry.find(self.logStartString), 
                                     "Minor:  first line of log is incorrect")
        except IOError:
            self.fail()
        self.assertIsInstance(theFix, F.Fix, 
                              "Major:  log file failed to create")
        pass
        del theLogFile
        self.cleanup()
        
    def test100_910_ShouldRaiseExceptionOnFileNameLength(self):
        expectedDiag = self.className + "__init__:"
        with self.assertRaises(ValueError) as context:
            F.Fix("")
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)], 
                          "Minor:  failure to check for log file name length") 
        
    def test100_920_ShouldRaiseExceptionOnNonStringFile(self):
        expectedDiag = self.className + "__init__:"
        with self.assertRaises(ValueError) as context:
            F.Fix(42)
        self.assertEquals(expectedDiag, context.exception.args[0][0:len(expectedDiag)], 
                          "Minor:  failure to check for non-string log file name") 


#  helper methods
    def indexInList(self, target, searchList):
        for index in range(len(searchList)):
            if(target in searchList[index]):
                return index
        return -1
    
    def cleanup(self):
        if(os.path.isfile(self.RANDOM_LOG_FILE)):
            os.remove(self.RANDOM_LOG_FILE) 