'''
    Created on Oct 8, 2016
        @author: Zachary Thompson
'''

class Fix():

    # Constructs a Fix object
    def __init__(self, logFile=None):
        '''
        Constructor
        '''
        if (logFile == None):
            self.fileName = "log.txt"
            self.sightingFile = ""
        else:
            self.fileName = logFile
            self.sightingFile = ""
    
        if (len(self.fileName) < 1):
            raise ValueError('Fix.__init__:  Filename must be at least 1 character long')
    
    def setSightingFile(self, sightingFile=None):
        if(sightingFile == None):
            raise ValueError('Fix.setSightingFile:  expected a sightingFile')
        elif((sightingFile[(len(sightingFile)-4):]) != ".xml"):
            raise ValueError('Fix.setSightingFile: sightingFile must be an xml file')
        if(sightingFile == self.sightingFile):
            return False
        self.sightingFile = sightingFile
        return True
    
    def getSightings(self):
        pass