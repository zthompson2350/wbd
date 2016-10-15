'''
    Created on 10 September 2016
        @author: Zachary Thompson
        
    Last Edited on 11 September 2016
        By: Zachary Thompson
'''

class Angle():
    # Constructs an Angle object
    def __init__(self):
        #set to 0 degrees 0 minutes
        self.degrees = 0.0
    
    # Sets degrees to int or string included as an argument, 0 if no argument
    def setDegrees(self, degrees=None):
        
        # If there is not an argument, set degrees to 0.
        if (degrees == None):
            self.degrees = 0.0
            
        # If the argument is not a float or an int raise a Value Error
        elif (not(isinstance(degrees, float)) and not(isinstance(degrees, int))):
            raise ValueError('Angle.setDegrees:  Parameter must be an int or a float')
        
        # If the argument is acceptable, store it
        else:
            # Store the degree portion of the argument    
            degrees = degrees%360.0
            degString = str(degrees)
            for c in degString:
                if (c == '.'):
                    hasDecimal = True
                    break
                else:
                    hasDecimal = False
            
            if(hasDecimal):
                decLoc = degString.find('.')
                mins = float('0' + degString[decLoc:])
                mins = mins * 60.0
                mins = round(mins, 1)
                mins = mins / 60.0
                degs = float(degString[:decLoc])
            else:
                mins = 0
                degs = degrees
            
                    
            self.degrees = degs + mins

        return self.degrees
    
    # Sets degrees and minutes based on a string of specific formatting xdy.y
    def setDegreesAndMinutes(self, angleString):
        
        # If the argument is not a string, raise a Value Error
        if (not(isinstance(angleString, str))):
            raise ValueError('Angle.setDegreesAndMinutes:  Parameter should be a string')

        
        # Find the d in the argument string
        delimeter = 'd'
        delimiterIndex = angleString.find(delimeter)
        
        # If d does not exist in the string, raise a Value Error
        if (delimiterIndex == -1):
            raise ValueError('Angle.setDegreesAndMinutes:  Parameter should be in format xdy.y')
        
        # If d is first character, raise a Value Error
        if (delimiterIndex == 0):
            raise ValueError('Angle.setDegreesAndMinutes:  No Degrees Specified')
        
        # If d is last character, raise a Value Error
        if (angleString[delimiterIndex] == angleString[-1]):
            raise ValueError('Angle.setDegreesAndMinutes:  No Minutes Specified')
        
        # If all those pass, set degrees to all characters before the d
        angleDegrees = angleString[:delimiterIndex]
        
        # If those values are not an integer, raise a Value Error
        try:
            int(angleDegrees)
        except:
            raise ValueError('Angle.setDegreesAndMinutes: x cannot be cast to a integer value')

        
        # If the values after the d cannot be converted to a float, raise a Value Error
        try:
            angleMinutes = float(angleString[delimiterIndex+1:])
        except:
            raise ValueError('Angle.setDegreesAndMinutes:  y.y must be an int or a float')
        
        minuteString = angleString[delimiterIndex+1:]
        for c in minuteString:
            if(c == '.'):
                foundDecimal = True
                break
            else:
                foundDecimal = False
        if (foundDecimal == True):
            if (minuteString[len(minuteString) - 2] != '.'):
                raise ValueError('Angle.setDegreesAndMinutes: y.y must be be rounded to the nearest tenth')
        
        # If minutes is entered as a negative, raise a Value Error
        if (angleMinutes < 0):
            raise ValueError('Angle.setDegreesAndMinutes:  y.y must be positive')
        
        # Set the degrees and minutes based on the argument
        if(int(angleDegrees) >= 0):
            self.degrees = float(angleDegrees) + (angleMinutes / 60.0)
        else:
            self.degrees = float(angleDegrees) - (angleMinutes / 60.0)
            
        # Modularize degrees, add the number of times greater than 60 minutes is to degrees, and 
        # Modularize minutes
        self.degrees = self.degrees%360
        return self.degrees
    
    # Adds an instance of angle to the current instance
    def add(self, angle=None):
        if(angle == None):
            raise ValueError('Angle.add: Expected an Angle Parameter')
        
        # If the argument is not an angle, raise a Value Error
        if (not(isinstance(angle, Angle))):
            raise ValueError('Angle.add:  Parameter is not an Angle')
        
        # Add the two angles
        self.degrees = (self.degrees + angle.degrees) % 360
        return self.degrees
    
    # Subtract an Angle from this instance of Angle
    def subtract(self, angle=None):
        if(angle == None):
            raise ValueError('Angle.subtract: Expected an Angle Parameter')
        
        # If the argument is not an Angle, raise a Value Error
        if (not(isinstance(angle, Angle))):
            raise ValueError('Angle.subtract:  Parameter is not an Angle')
        
        # Subtract the argument angle from the current angle
        self.degrees = (self.degrees - angle.degrees)%360
        return self.degrees
    
    # Compare two angles
    def compare(self, angle=None):
        if(angle == None):
            raise ValueError('Angle.compare: Expected an Angle Parameter')
        
        # If the argument is not an angle, raise a Value Error
        if (not(isinstance(angle, Angle))):
            raise ValueError('Angle.compare:  Parameter is not an Angle')
        
        # If the current instance's degree is bigger, return 1
        if (self.degrees > angle.degrees):
            return 1
        
        # If the Argument instance's degree is bigger, return -1
        elif (self.degrees < angle.degrees):
            return -1
        
        # If both angles degrees are equal, check the minutes
        elif (self.degrees == angle.degrees):
            return 0
    
    # Returns the degrees in the format xdy.y
    def getString(self):
        degString = str(self.degrees)
        decLoc = degString.find('.')
        degs = degString[:decLoc]
        minsUnfixed = '0' + degString[decLoc:]
        minsFixed = 60 * float(minsUnfixed)
        return degs + 'd' + str(round(minsFixed, 1))
    
    # Returns the degrees as a float with minutes as fractions of degrees
    def getDegrees(self):
        return self.degrees