class Angle():
    def __init__(self):
        #set to 0 degrees 0 minutes
        self.degrees = 0
        self.minutes = 0.0
    
    def setDegrees(self, degrees=None):
        if (degrees == None):
            self.degrees = 0
        else:
            self.degrees = degrees%360
        return float(self.degrees)
    
    def setDegreesAndMinutes(self, angleString):
        delimeter = 'd'
        delimiterIndex = angleString.find(delimeter)
        self.degrees = int(angleString[:delimiterIndex])
        self.minutes = float(angleString[delimiterIndex+1:])
        self.degrees = self.degrees%360
        self.degrees = self.degrees + (int(self.minutes / 60))
        self.minutes = (self.minutes%60)
        output = float(self.degrees + (self.minutes / 100))
        return output
    
    def add(self, angle):
        self.degrees = (self.degrees + angle.degrees)
        self.degrees = (self.degrees + (int((self.minutes + angle.minutes) / 60))) % 360
        self.minutes = (self.minutes + angle.minutes)%60.0
        output = float(self.degrees + (self.minutes / 100))
        return output
    
    def subtract(self, angle):
        self.degrees = (self.degrees - angle.degrees)%360
        self.degrees = (self.degrees - (int((self.minutes - angle.minutes) / 60))) % 360
        self.minutes = (self.minutes - angle.minutes)%60.0
        output = float(self.degrees + (self.minutes / 100))
        return output
    
    def compare(self, angle):
        pass
    
    def getString(self):
        pass
    
    def getDegrees(self):
        return self.degrees
    
myAngle = Angle()
myAngle2 = Angle()
angleString = '10d179'
angleString2 = '3d1'
myAngleFloat = myAngle.setDegreesAndMinutes(angleString)
myAngleFloat2 = myAngle2.setDegreesAndMinutes(angleString2)
print(myAngleFloat)
print(myAngleFloat2)
print('Adding')
myAngleFloat = myAngle.add(myAngle2)
print(myAngleFloat)
print('Resetting Angles')
myAngleFloat = myAngle.setDegreesAndMinutes(angleString)
myAngleFloat2 = myAngle2.setDegreesAndMinutes(angleString2)
print(myAngleFloat)
print(myAngleFloat2)
print('Subtracting')
myAngleFloat = myAngle.subtract(myAngle2)
print(myAngleFloat)