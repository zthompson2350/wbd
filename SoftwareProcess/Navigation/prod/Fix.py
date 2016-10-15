'''
    Created on Oct 8, 2016
        @author: Zachary Thompson
    Last Edited on Oct 12, 2016
        By: Zachary Thompson
'''

import os
from xml.etree import ElementTree
import datetime
import math
import Angle

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
            self.log = open(self.fileName, 'a')
        else:
            self.log = open(self.fileName, 'w')
            
    def __timeAndDate__(self, today):
        return(
            datetime.date.isoformat(today) + " " + str(today.hour) + ":"
            + str(today.minute) + ":" + str(today.second) + "-06:00 "
            )
            
    def __getOrder__(self, sightings):
        years = [None] * len(sightings)
        months = [None] * len(sightings)
        days = [None] * len(sightings)
        hours = [None] * len(sightings)
        mins = [None] * len(sightings)
        seconds = [None] * len(sightings)
        i = 0
        
        
        for s in sightings:
            years[i] = s.find('date').text[0:4]
            months[i] = s.find('date').text[5:7]
            days[i] = s.find('date').text[8:]
            hours[i] = s.find('time').text[0:2]
            mins[i] = s.find('time').text[3:5]
            seconds[i] = s.find('time').text[6:] 
            i = i + 1
        
        bestYear = 9999
        bestMonth = 9999
        bestDay = 9999
        bestHour = 9999
        bestMin = 9999
        bestSecond = 9999
        numBests = 0
        orderSet = 0
        
        order = [None] * len(sightings)
        ordered = [0] * len(sightings)
        bests = [0] * len(sightings)
        
        while (orderSet < len(order)):
            i = 0
            while (i < len(bests)):
                bests[i] = 0
                i = i + 1
            
            i = 0
            while (i < len(years)):
                if (int(years[i]) < bestYear and ordered[i] == 0):
                    bestYear = int(years[i])
                i = i + 1
            i = 0
            while (i < len(years)):
                if (int(years[i]) == bestYear and ordered[i] == 0):
                    bests[i] = 1
                    numBests = numBests + 1
                i = i + 1
        
            i = 0
            if (numBests == 1):
                while(i < len(bests)):
                    if(bests[i] == 1):
                        order[orderSet] = i
                        ordered[i] = 1
                        break
                    i = i + 1
            else:
                while (i < len(months)):
                    if(bests[i] == 1):
                        if(int(months[i]) < bestMonth and ordered[i] == 0):
                            bestMonth = int(months[i])
                    i = i + 1
                    
            if (order[orderSet] != None):
                orderSet = orderSet + 1
                continue
                        
            numBests = 0
            i = 0
            while (i < len(months)):
                if (bests[i] == 1):
                    if(int(months[i]) == bestMonth and ordered[i] == 0):
                        numBests = numBests + 1
                    else:
                        bests[i] = 0
                i = i + 1
            
            i = 0            
            if (numBests == 1):
                while (i < len(bests)):
                    if(bests[i] == 1):
                        order[orderSet] = i
                        ordered[i] = 1
                        break
                    i = i + 1
            else:
                while (i < len(days)):
                    if(bests[i] == 1):
                        if(int(days[i]) < bestDay and ordered[i] == 0):
                            bestDay = int(days[i])
                    i = i + 1
                    
            if (order[orderSet] != None):
                orderSet = orderSet + 1
                continue
                    
            numBests = 0
            i = 0
            while (i < len(days)):
                if (bests[i] == 1):
                    if(int(days[i]) == bestDay and ordered[i] == 0):
                        numBests = numBests + 1
                    else:
                        bests[i] = 0
                i = i + 1
                        
            i = 0            
            if (numBests == 1):
                while (i < len(bests)):
                    if(bests[i] == 1):
                        order[orderSet] = i
                        ordered[i] = 1
                        break
                    i = i + 1
            else:
                while (i < len(hours)):
                    if(bests[i] == 1):
                        if(int(hours[i]) < bestHour and ordered[i] == 0):
                            bestHour = int(hours[i])
                    i = i + 1
                    
            if (order[orderSet] != None):
                orderSet = orderSet + 1
                continue
                    
            numBests = 0
            i = 0
            while (i < len(hours)):
                if (bests[i] == 1):
                    if(int(hours[i]) == bestHour and ordered[i] == 0):
                        numBests = numBests + 1
                    else:
                        bests[i] = 0
                        
            i = 0            
            if (numBests == 1):
                while (i < len(bests)):
                    if(bests[i] == 1):
                        order[orderSet] = i
                        ordered[i] = 1
                        break
            else:
                while (i < len(mins)):
                    if(bests[i] == 1):
                        if(int(mins[i]) < bestMin and ordered[i] == 0):
                            bestMin = int(mins[i])
                    i = i + 1
                    
            if (order[orderSet] != None):
                orderSet = orderSet + 1
                continue
                    
            numBests = 0
            i = 0
            while (i < len(mins)):
                if (bests[i] == 1):
                    if(int(mins[i]) == bestMin and ordered[i] == 0):
                        numBests = numBests + 1
                    else:
                        bests[i] = 0
                        
            i = 0            
            if (numBests == 1):
                while (i < len(bests)):
                    if(bests[i] == 1):
                        order[orderSet] = i
                        ordered[i] = 1
                        break
            else:
                while (i < len(seconds)):
                    if(bests[i] == 1):
                        if(int(seconds[i]) < bestSecond and ordered[i] == 0):
                            bestSecond = int(seconds[i])
                    i = i + 1
                    
            if (order[orderSet] != None):
                orderSet = orderSet + 1
                continue
                    
            numBests = 0
            i = 0
            while (i < len(seconds)):
                if (bests[i] == 1):
                    if(int(seconds[i]) == bestSecond and ordered[i] == 0):
                        numBests = numBests + 1
                    else:
                        bests[i] = 0
                        
        return order
    
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
        
        today = datetime.datetime.now()
        self.log.write("LOG: " + self.__timeAndDate__(today) + "Start of log\n")
        self.log.write("LOG: " + self.__timeAndDate__(today) + "Start of sighting file:  " + self.sightingFile + "\n")
        
#         for s in sightings:
#             today = datetime.datetime.now()
#             body = s.find('body')
#             sightingDate = s.find('date')
#             sightingTime = s.find('time')
#             observation = s.find('observation')
#             print(
#                 "LOG: " + self.__timeAndDate__(today) + body.text + "  " 
#                 + sightingDate.text + "  " + sightingTime.text + "  " + observation.text
#                 )
#         
#         today = datetime.datetime.now()
#         print("LOG: " + self.__timeAndDate__(today) + "End of sighting file:  " + self.sightingFile)
        #self.fileName.write('LOG: ', date.today())
        
        return self.sightingFile
    
    def getSightings(self):
        if(self.sightingFile == ""):
            raise ValueError('Fix.getSightings: No sightingFile has been set')
        approximateLatitude = "0d0.0"
        approximateLongitude = "0d0.0"
        
        dom = ElementTree.parse(self.sightingFile)
        myAngle = Angle.Angle()
        sightings = dom.findall('sighting')
        order = self.__getOrder__(sightings)
        
            
        i = 0
        while (i < len(order)):
            j = order[i]
            if(sightings[j].find('horizon').text == 'Natural'):
                dip = (-0.97) * math.sqrt(float(sightings[j].find('height').text))      
            else:
                dip = 0
            obsv = sightings[j].find('observation').text
            myAngle.setDegreesAndMinutes(obsv)
            altitude = myAngle.getDegrees()
            temp = (int(sightings[j].find('temperature').text) - 32) * (5/9)
            refraction = ((-0.00452) * float(sightings[j].find('pressure').text)) / ((273 +temp) / math.tan(math.radians(altitude)))
            adjAlt = altitude + dip + refraction
            adjAltString = str(adjAlt)
            for a in adjAltString:
                if (a == '.'):
                    hasDec = True
                    break
                else:
                    hasDec = False
                    
            if (hasDec):
                decLoc = adjAltString.find('.')
                mins = float('0' + adjAltString[decLoc:])
                mins = mins * 60.0
                mins = round(mins, 1)
                mins = mins / 60.0
                degs = float(adjAltString[:decLoc])
            else:
                mins = 0
                degs = adjAlt
                
            adjAlt = degs + mins
#             adjAlt = round(adjAlt, 1)
            myAngle.setDegrees(adjAlt)
            adjAltAngle = myAngle.getString()
#             adjAltStr = str(adjAlt)
            
            today = datetime.datetime.now()
            self.log.write(
                            "Log: " + self.__timeAndDate__(today) + sightings[j].find('body').text + " "
                            + sightings[j].find('date').text + " " + sightings[j].find('time').text + " "
                            + adjAltAngle + "\n"
                           )
            
            i = i + 1
            
        today = datetime.datetime.now()
        self.log.write("Log: " + self.__timeAndDate__(today) + "End of sighting file: " + self.sightingFile)
            
        return(approximateLatitude, approximateLongitude)