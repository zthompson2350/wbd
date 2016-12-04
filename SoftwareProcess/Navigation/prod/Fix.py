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
            self.ariesFile = ""
            self.starFile = ""
        elif (not(isinstance(logFile, basestring))):
            raise ValueError('Fix.__init__: Filename must be of type String')
        else:
            self.fileName = logFile
            self.sightingFiles = ""
            self.ariesFile = ""
            self.starFile = ""
    
        if (len(self.fileName) < 1):
            raise ValueError('Fix.__init__:  Filename must be at least 1 character long')
        
        if (os.path.isfile('./' + self.fileName)):
            self.log = open(self.fileName, 'a')
        else:
            self.log = open(self.fileName, 'w')
        today = datetime.datetime.now()
        path = os.path.abspath('./' + self.fileName)
        self.log.write("LOG: " + self.__timeAndDate__(today) + "Log file:\t" + path + "\n")    
        self.log.close()
            
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
        bodies = [None] * len(sightings)
        i = 0
        
        
        for s in sightings:
            years[i] = s.find('date').text[0:4]
            months[i] = s.find('date').text[5:7]
            days[i] = s.find('date').text[8:]
            hours[i] = s.find('time').text[0:2]
            mins[i] = s.find('time').text[3:5]
            seconds[i] = s.find('time').text[6:] 
            bodies[i] = s.find('body').text
            i = i + 1
        
        bestYear = 9999
        bestMonth = 9999
        bestDay = 9999
        bestHour = 9999
        bestMin = 9999
        bestSecond = 9999
        bestBody = "zzzz"
        numBests = 0
        orderSet = 0
        
        order = [None] * len(sightings)
        ordered = [0] * len(sightings)
        bests = [0] * len(sightings)
        
        while (orderSet < len(order)):
            bestYear = 9999
            bestMonth = 9999
            bestDay = 9999
            bestHour = 9999
            bestMin = 9999
            bestSecond = 9999
            bestBody = "zzzz"
        
        
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
                        numBests = numBests + 1 #100
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
                        numBests = numBests + 1 #200
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
                while (i < len(bodies)):
                    if(bests[i] == 1):
                        if(bodies[i] > bestBody and ordered[i] == 0):
                            bestBody = bodies[i]
                    i = i + 1
                    
            if (order[orderSet] != None):
                orderSet = orderSet + 1
                continue
            
            i = 0            
            if (numBests == 1):
                while (i < len(bests)):
                    if(bests[i] == 1):
                        order[orderSet] = i
                        ordered[i] = 1
                        break
                    i = i + 1
                        
        return order
    
    def setSightingFile(self, sightingFile=None):
        if(sightingFile == None):
            raise ValueError('Fix.setSightingFile:  expected a sightingFile')
        elif(not(isinstance(sightingFile, basestring))):
            raise ValueError('Fix.setSightingFile: sightingFile must be of type String')
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
        path = os.path.abspath('./' + sightingFile)
        self.log = open(self.fileName, 'a')
        self.log.write("LOG: " + self.__timeAndDate__(today) + "Sighting file:\t" + path + "\n")
        self.log.close()
        
        return path
    
    def setAriesFile(self, ariesFile=None):
        if (ariesFile == None):
            raise ValueError('Fix.setAriesFile:  Expected an Aries File')
        elif(not(isinstance(ariesFile, basestring))):
            raise ValueError('Fix.setAriesFile:  Aries File must be of type String')
        elif((ariesFile[(len(ariesFile)-4):]) != ".txt"):
            raise ValueError('Fix.setAriesFile:  Aries File must be a txt file')
        
        if(os.path.isfile('./' + ariesFile)):
            try:
                tryToOpen = open(ariesFile, 'a')
                tryToOpen.close()
            except:
                raise ValueError('Fix.setAriesFile: Unable to open Aries File')
            self.ariesFile = ariesFile
        else:
            raise ValueError('Fix.setAriesFile:  Unable to find Aries File')
        
        today = datetime.datetime.now()
        path = os.path.abspath('./' + ariesFile)
        self.log = open(self.fileName, 'a')
#         self.log.write("LOG: " + self.__timeAndDate__(today) + "Start of log\n")
        self.log.write("LOG: " + self.__timeAndDate__(today) + "Aries file:\t" + path + "\n")
        self.log.close()
        
        return path
    
    def setStarFile(self, starFile=None):
        if (starFile == None):
            raise ValueError('Fix.setStarFile:  Expected a Star File')
        elif(not(isinstance(starFile, basestring))):
            raise ValueError('Fix.setStarFile:  Star File must be of type string')
        elif((starFile[len(starFile)-4:]) != ".txt"):
            raise ValueError("Fix.setStarFile:  Star File must be a txt file")
        
        if (os.path.isfile('./' + starFile)):
            try:
                tryToOpen = open(starFile, 'a')
                tryToOpen.close()
            except:
                raise ValueError('Fix.setStarFile:  Unable to open Star File')
            self.starFile = starFile
        else:
            raise ValueError('Fix.setStarFile:  Unable to find Star File')
        
        today = datetime.datetime.now()
        path = os.path.abspath('./' + starFile)
        self.log = open(self.fileName, 'a')
        self.log.write("LOG: " + self.__timeAndDate__(today) + "Star file:\t" + path + "\n")
        self.log.close()
        
        return path
    
    def getSightings(self, assumedLatitude=None, assumedLongitude=None):
        if(self.sightingFile == ""):
            raise ValueError('Fix.getSightings: No sightingFile has been set')
        elif(self.ariesFile == ""):
            raise ValueError('Fix.getSightings:  No Aries File has been set')
        elif(self.starFile == ""):
            raise ValueError('Fix.getSightings:  No Star File has been set')
        if(assumedLatitude == None):
            assumedLatitude = "0d0.0"
        if(not(isinstance(assumedLatitude, str))):
            raise ValueError('Fix.getSightings: assumedLatitude must be of type str')
        delimiter = 'd'
        delimiterIndex = assumedLatitude.find(delimiter)
        if(delimiterIndex == -1):
            raise ValueError('Fix.getSightings: assumedLatitude must be in format hxdy.y')
        if(delimiterIndex == 0):
            raise ValueError('Fix.getSightings: assumedLatitude must be in format hxdy.y')
        if(delimiterIndex == 1):
            if(not(assumedLatitude == '0d0.0')):
                raise ValueError('Fix.getSightings: if no direction specified, assumedLatitude must be 0d0.0')
        if(assumedLatitude[delimiterIndex] == assumedLatitude[-1]):
            raise ValueError('Fix.getSightings: assumedLatitude must be in format hxdy.y')
        if(not(assumedLatitude == "0d0.0")):
            if(not(assumedLatitude[0] == 'N' or assumedLatitude[0] == 'S')):
                raise ValueError('Fix.getSightings: hemisphere indicator in assumedLatitude must be N or S')
            latDegs = assumedLatitude[1:delimiterIndex]
            try:
                latDegs = int(latDegs)
            except:
                raise ValueError('Fix.getSightings: assumedLatitude degrees value needs to be an integer')
            try:
                latMins = float(assumedLatitude[delimiterIndex+1:])
            except:
                raise ValueError('Fix.getSightings: assumedLatitude minutes should be able to cast to float')
            if(latMins < 0.0):
                raise ValueError('Fix.getSightings: assumedLatitude minutes must be positive')
            minuteString = assumedLatitude[delimiterIndex+1:]
            for c in minuteString:
                if(c == '.'):
                    foundDecimal = True
                    break
                else:
                    foundDecimal = False
            if(foundDecimal):
                if(minuteString[len(minuteString) - 2] != '.'):
                    raise ValueError('Fix.getSightings: assumedLatitude minutes should be rounded to nearest tenth')
            if(latDegs < 0 or latDegs >= 90):
                raise ValueError("Fix.getSightings: assumedLatitude degrees should be between 0 and 90")
            if(latMins >= 60.0):
                raise ValueError("Fix.getSightings: assumedLatitude minutes should be less than 60.0")
            
        if(assumedLongitude == None):
            assumedLongitude = "0d0.0"
        if(not(isinstance(assumedLongitude, str))):
            raise ValueError('Fix.getSightings: assumedLongitude must be of type str')
        delimiterIndex = assumedLongitude.find(delimiter)
        if(delimiterIndex == -1):
            raise ValueError('Fix.getSightings: assumedLongitude must be in format xdy.y')
        if(delimiterIndex == 0):
            raise ValueError('Fix.getSightings: assumedLongitude must be in format xdy.y')
        if(assumedLongitude[delimiterIndex] == assumedLongitude[-1]):
            raise ValueError('Fix.getSightings: assumedLongitude must be in format xdy.y')
        if(not(assumedLongitude == "0d0.0")):
            longDegs = assumedLongitude[:delimiterIndex]
            try:
                longDegs = int(longDegs)
            except:
                raise ValueError('Fix.getSightings: assumedLongitude degrees value needs to be an integer')
            try:
                longMins = float(assumedLongitude[delimiterIndex+1:])
            except:
                raise ValueError('Fix.getSightings: assumedLongitude minutes should be able to cast to float')
            if(longMins < 0.0):
                raise ValueError('Fix.getSightings: assumedLongitude minutes must be positive')
            minuteString = assumedLongitude[delimiterIndex+1:]
            for ch in minuteString:
                if(ch == '.'):
                    foundDecimal = True
                    break
                else:
                    foundDecimal = False
            if(foundDecimal):
                if(minuteString[len(minuteString) - 2] != '.'):
                    raise ValueError('Fix.getSightings: assumedLongitude minutes should be rounded to nearest tenth')
        
            if(longDegs < 0 or longDegs >= 360):
                raise ValueError('Fix.getSightings: assumedLongitude degrees should be between 0 and 360')
            if(longMins >= 60.0):
                raise ValueError('Fix.getSightings: assumedLongitude minutes should be less than 60.0')
        
        approximateLatitude = "0d0.0"
        approximateLongitude = "0d0.0"
        
        dom = ElementTree.parse(self.sightingFile)
        myAngle = Angle.Angle()
        sightings = dom.findall('sighting')
        order = self.__getOrder__(sightings)
        
        sightingErrors = 0    
        i = 0
        while (i < len(order)):
            j = order[i]
            test = sightings[j].find('horizon')
            if(test == None):
                sightingErrors = sightingErrors + 1
                i = i + 1
                continue
            if(sightings[j].find('horizon').text == 'Natural'):
                dip = ((-0.97) * math.sqrt(float(sightings[j].find('height').text))) / 60.0      
            else:
                dip = 0.0
            obsv = sightings[j].find('observation').text
            myAngle.setDegreesAndMinutes(obsv)
            altitude = myAngle.getDegrees()
            temp = (float(sightings[j].find('temperature').text) - 32) * (5.0/9.0)
            refraction = ((-0.00452) * float(sightings[j].find('pressure').text)) / (273.0 +temp) / math.tan(math.radians(altitude))
            adjAlt = altitude + dip + refraction
            myAngle.setDegrees(adjAlt)
            adjAltAngle = myAngle.getString()
            
            
            
            targDate = sightings[j].find('date').text
            targMonth = targDate[5:7]
            targDay = targDate[8:]
            starfile = open(self.starFile, 'r')
            oldDate = None
            for row in starfile:
                if sightings[j].find('body').text in row:
                    lindex = 0
                    while(i < len(row)):
                        try:
                            int(row[lindex])
                            break
                        except:
                            lindex = lindex + 1
                            
                    rindex = lindex
                    while (rindex < len(row)):
                        if(row[rindex].isspace()):
                            break
                        rindex = rindex + 1
                        
                    currDate = row[lindex:rindex]
                    if (oldDate == None):
                        oldDate = currDate
                    currMonth = currDate[0:2]
                    currDay = currDate[3:5]
                        
                    if(currMonth == targMonth):
                        if (currDay == targDay):
                            oldDate = currDate
                            break
                        elif(currDay > targDay):
                            break
                        else:
                            oldDate = currDate
                    elif(currMonth > targMonth):
                        break
                    else:
                        oldDate = currDate
             
#             targDate = oldDate
            starfile.close()
            starfile = open(self.starFile, 'r')
            for row in starfile:
                if sightings[j].find('body').text in row:
                    if oldDate in row:
                        lindex = 0
                        dindex = 0
                        rindex = 0
                        
                        while (dindex < len(row)):
                            if (row[dindex] == 'd'):
                                break
                            dindex = dindex + 1
                            
                        lindex = row.rfind('\t', 0, dindex) + 1
                        rindex = row.find('\t', dindex)
                        SHAstar = row[lindex:rindex]
                        
                        dindex = dindex + 1
                        while (dindex < len(row)):
                            if (row[dindex] == 'd'):
                                break
                            dindex = dindex + 1
                        lindex = row.rfind('\t', rindex, dindex) + 1
                        rindex = row.find('\t', dindex)
                        latitude = row[lindex:rindex]
                        break
            
            starfile.close()
            
            
            dindex = 0
            while(dindex < len(SHAstar)):
                if SHAstar[dindex] == 'd':
                    break
                dindex = dindex + 1
            
            x = int(SHAstar[:dindex])
            yy = float(SHAstar[dindex+1:])
            
            dindex = 0
            while(dindex < len(latitude)):
                if (latitude[dindex] == 'd'):
                    break
                dindex = dindex + 1
                
            w = int(latitude[:dindex])
            zz = float(latitude[dindex+1:])
            
            if (x < 0 or x >= 360):
                sightingErrors = sightingErrors + 1
                i = i + 1
                continue
            elif (yy < 0.0 or yy >= 60.0):
                sightingErrors = sightingErrors + 1
                i = i + 1
                continue
            elif (w <= -90 or w >= 90):
                sightingErrors = sightingErrors + 1
                i = i + 1
                continue
            elif (zz < 0.0 or zz >= 60.0):
                sightingErrors = sightingErrors + 1
                i = i + 1
                continue
            
                    
            today = datetime.datetime.now()
            sightTime = sightings[j].find('time').text
            sightHour = int(sightTime[0:2])
            
            ariesfile = open(self.ariesFile, 'r')
            for row in ariesfile:
                if (targMonth + "/" + targDay + "/17") in row:
                    lindex = 0
                    while (lindex < len(row)):
                        if (row[lindex].isspace()):
                            break
                        lindex = lindex + 1
                    lindex = lindex + 1
                    rindex = lindex
                    while (rindex < len(row)):
                        if(row[rindex].isspace()):
                            break
                        rindex = rindex + 1
                    ariesHour = int(row[lindex:rindex])
                    if (ariesHour == sightHour):
                        ariesEntry = unicode(row)
                        break
            lindex = rindex
            while (lindex < len(ariesEntry)):
                if (ariesEntry[lindex].isnumeric()):
                    break
                lindex = lindex + 1
            GHAaries1 = ariesEntry[lindex:len(ariesEntry)-1]
            
            for row in ariesfile:
                ariesEntry = unicode(row)
                break
            lindex = row.rfind('\t')
            while (lindex < len(ariesEntry)):
                if (ariesEntry[lindex].isnumeric()):
                    break
                lindex = lindex + 1
            GHAaries2 = ariesEntry[lindex:len(ariesEntry)-1]
            minutes = float(sightTime[3:5])
            seconds = float(sightTime[6:])
            s = (minutes * 60.0) + seconds
            
            
            GHAangle1 = Angle.Angle()
            GHAangle1.setDegreesAndMinutes(str(GHAaries1))
            GHAangle2 = Angle.Angle()
            GHAangle2.setDegreesAndMinutes(str(GHAaries2))
            subAngle = GHAangle2
            subAngle.subtract(GHAangle1)
            subDegs = subAngle.getDegrees()
            mulDegs = subDegs * (s / 3600.0)
            mulAngle = Angle.Angle()
            mulAngle.setDegrees(mulDegs)
            GHAariesAngle = GHAangle1
            GHAariesAngle.add(mulAngle)
            SHAstarAngle = Angle.Angle()
            SHAstarAngle.setDegreesAndMinutes(SHAstar)
            GHAobservation = GHAariesAngle
            GHAobservation.add(SHAstarAngle)
            ariesfile.close()
            
            #Local Hour Angle
            #LHA = geographic position longitude - assumed longitude
            #Corrected Altitude = 
            # arcsin((sin(geographicpositionlatitude) * sin(assumedlatitude)) + (cos(geographicpositionlatitude) * cos(assumedlatitude)))
            #Distance Adjustment = (adjusted altitude - corrected altitude) rounded to nearest whole arc-minute
            #Azimuth Adjustment = 
            # arcsin((sin(geographicpositionlatitude) - sin(assumedlatitude)) * (cos(assumedlatitude) - cos(distanceadjustment)))
            #Write azimuth adjustment and distance adjustment to log
            
            
            
            self.log = open(self.fileName, 'a')
            self.log.write(
                    "Log: " + self.__timeAndDate__(today) + sightings[j].find('body').text + "\t"
                    + sightings[j].find('date').text + "\t" + sightTime + "\t"
                    + adjAltAngle + "\t" + latitude + "\t" + GHAobservation.getString() + "\t"
                    + assumedLatitude + "\t" + assumedLongitude + "\n"
                    )
            self.log.close()
            
            i = i + 1
        today = datetime.datetime.now()
        self.log = open(self.fileName, 'a')
        self.log.write("Log: " + self.__timeAndDate__(today) + "Sighting errors:\t" + str(sightingErrors) + "\n")
        self.log.close()
            
        return(approximateLatitude, approximateLongitude)
    