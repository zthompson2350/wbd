class Angle():
    def __init__(self):
        #set to 0 degrees 0 minutes
        self.degrees = 0
        self.minutes = 0.0
    
    def setDegrees(self, degrees=None):
        if (degrees == None):
            self.degrees = 0
        elif (not(isinstance(degrees, float)) and not(isinstance(degrees, int))):
            raise ValueError('Angle.setDegrees:  Parameter must be an int or a float')
        else:
            self.degrees = int(degrees)%360
            degstr = str(degrees)
            decloc = degstr.find('.')
            mins = str(degrees)[decloc+1:]
            self.minutes = float(mins)%60
            self.degrees = self.degrees + (int(mins) / 60)
            output = float(self.degrees + (self.minutes / 100))
        return output
    
    def setDegreesAndMinutes(self, angleString):
        if (not(isinstance(angleString, str))):
            raise ValueError('Angle.setDegreesAndMinutes:  Parameter should be a string')
        isNegative = False
        delimeter = 'd'
        delimiterIndex = angleString.find(delimeter)
        if (delimiterIndex == -1):
            raise ValueError('Angle.setDegreesAndMinutes:  Parameter should be in format xdy.y')
        if (delimiterIndex == 0):
            raise ValueError('Angle.setDegreesAndMinutes:  No Degrees Specified')
        if (angleString[delimiterIndex] == angleString[-1]):
            raise ValueError('Angle.setDegreesAndMinutes:  No Minutes Specified')
        angleDegrees = angleString[:delimiterIndex]
        if (not(angleDegrees.isdigit())):
            raise ValueError('Angle.setDegreesAndMinutes:  x must be an integer')
        try:
            angleMinutes = float(angleString[delimiterIndex+1:])
        except:
            raise ValueError('Angle.setDegreesAndMinutes:  y.y must be an int or a float')
        if (angleMinutes < 0):
            raise ValueError('Angle.setDegreesAndMinutes:  y.y must be positive')
        self.degrees = int(angleDegrees)
        self.minutes = float(angleMinutes)
        if (self.degrees < 0):
            isNegative = True
        self.degrees = self.degrees%360
        self.degrees = self.degrees + (int(self.minutes / 60))
        self.minutes = (self.minutes%60)
        if (isNegative):
            self.minutes = 60 - self.minutes
        output = float(self.degrees + (self.minutes / 100))
        return output
    
    def add(self, angle):
        if (not(isinstance(angle, Angle))):
            raise ValueError('Angle.add:  Parameter is not an Angle')
        self.degrees = (self.degrees + angle.degrees)
        self.degrees = (self.degrees + (int((self.minutes + angle.minutes) / 60))) % 360
        self.minutes = (self.minutes + angle.minutes)%60.0
        output = float(self.degrees + (self.minutes / 100))
        return output
    
    def subtract(self, angle):
        if (not(isinstance(angle, Angle))):
            raise ValueError('Angle.subtract:  Parameter is not an Angle')
        self.degrees = (self.degrees - angle.degrees)%360
        self.degrees = (self.degrees - (int((self.minutes - angle.minutes) / 60))) % 360
        self.minutes = (self.minutes - angle.minutes)%60.0
        output = float(self.degrees + (self.minutes / 100))
        return output
    
    def compare(self, angle):
        if (not(isinstance(angle, Angle))):
            raise ValueError('Angle.compare:  Parameter is not an Angle')
        if (self.degrees > angle.degrees):
            return 1
        elif (self.degrees < angle.degrees):
            return -1
        elif (self.degrees == angle.degrees):
            if (self.minutes > angle.minutes):
                return 1
            elif (self.minutes < angle.minutes):
                return -1
            else:
                return 0
    
    def getString(self):
        return str(self.degrees) + 'd' + str(self.minutes)
    
    def getDegrees(self):
        return float(self.degrees) + (self.minutes / 100.0)