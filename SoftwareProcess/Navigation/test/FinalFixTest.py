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


#  helper methods
    def indexInList(self, target, searchList):
        for index in range(len(searchList)):
            if(target in searchList[index]):
                return index
        return -1
    
    def cleanup(self):
        if(os.path.isfile(self.RANDOM_LOG_FILE)):
            os.remove(self.RANDOM_LOG_FILE) 