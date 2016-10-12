'''
    Created on Oct 8, 2016
        @author: Zachary Thompson
'''

import os
from xml.etree import ElementTree
import datetime


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
            self.sightingFiles = ""
    
        if (len(self.fileName) < 1):
            raise ValueError('Fix.__init__:  Filename must be at least 1 character long')
        
        if (os.path.isfile('./' + self.fileName)):
            self.sightings = open(self.fileName, 'a')
        else:
            self.sightings = open(self.fileName, 'w')
            
    
    def setSightingFile(self, sightingFile=None):
        if(sightingFile == None):
            raise ValueError('Fix.setSightingFile:  expected a sightingFile')
        elif((sightingFile[(len(sightingFile)-4):]) != ".xml"):
            raise ValueError('Fix.setSightingFile: sightingFile must be an xml file')
        
        if (os.path.isfile('./' + sightingFile)):
            try:
                tryToOpen = open(sightingFile, 'a')
                tryToOpen.close()
            except:
                raise ValueError('Fix.setSightingFile: unable to open sightingFile')
            self.sightingFile = sightingFile
        else:
            raise ValueError('Fix.setSightingFile: unable to find sightingFile')
        self.sightingFile = sightingFile
            
            
            # TODO: write entry to log file
        dom = ElementTree.parse(self.sightingFile)
        sightings = dom.findall('sighting')
        
        today = datetime.datetime.now()
        
        
        print(
            "LOG: " + datetime.date.isoformat(today)
              + " " + str(today.hour) + ":" + str(today.minute) + ":" + str(today.second)
              + "-06:00 Start of log"
              )
        
        today = datetime.datetime.now()
        #time = datetime.time(today.hour, today.minute, today.second, tzinfo=GMT1())
        #print("TIME: " + time.isoformat())
        print(
            "LOG: " + datetime.date.isoformat(today) + " " + str(today.hour)
             + ":" + str(today.minute) + ":" + str(today.second) + "-06:00 Start of sighting file:  "
             + self.sightingFile
            )
        
        for s in sightings:
            today = datetime.datetime.now()
            body = s.find('body')
            sightingDate = s.find('date')
            sightingTime = s.find('time')
            observation = s.find('observation')
            print(
                "LOG: " + datetime.date.isoformat(today) + " " + str(today.hour)
                + ":" + str(today.minute) + ":" + str(today.second) + "-06:00 "
                + body.text + "  " + sightingDate.text + "  " + sightingTime.text
                + "  " + observation.text
                )
        
        today = datetime.datetime.now()
        print(
            "LOG: " + datetime.date.isoformat(today) + " " + str(today.hour)
             + ":" + str(today.minute) + ":" + str(today.second) + "-06:00 "
             + "End of sighting file:  " + self.sightingFile
            )
        #self.fileName.write('LOG: ', date.today())
        
        return self.sightingFile
    
    def getSightings(self):
        if(self.sightingFile == ""):
            raise ValueError('Fix.getSightings: No sightingFile has been set')
        approximateLatitude = "0d0.0"
        approximateLongitude = "0d0.0"
        return(approximateLatitude, approximateLongitude)
    
aFix = Fix()
aFix.setSightingFile("sightingFile.xml")