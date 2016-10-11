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
        self.degrees = 0
        self.minutes = 0.0
    
    # Sets degrees to int or string included as an argument, 0 if no argument
    def setDegrees(self, degrees=None):
        
        # If there is not an argument, set degrees to 0.
        if (degrees == None):
            self.degrees = 0
            self.minutes = 0.0
            
        # If the argument is not a float or an int raise a Value Error
        elif (not(isinstance(degrees, float)) and not(isinstance(degrees, int))):
            raise ValueError('Angle.setDegrees:  Parameter must be an int or a float')
        
        # If the argument is acceptable, store it
        else:
            # Store the degree portion of the argument
            self.degrees = int(degrees)%360
            
            # Create a string from the argument and try to find a decimal point signifying it is a float
            degstr = str(degrees)
            decloc = degstr.find('.')
            
            # If the argument is a float, get the decimal values, add them to 0, multiply them by 60
            # and store them in minutes
            if (decloc != -1):
                mins = '0.' + str(degrees)[decloc+1:]
                argmins = float(mins)
                argmins = (argmins * 60.0)
                self.minutes = argmins
                
            # Otherwise, set minutes to 0
            else:
                self.minutes = 0.0
                
            # Output the argument as it was passed in
        output = float(self.degrees + round(self.minutes, 1) / 60.0)
        return output
    
    # Sets degrees and minutes based on a string of specific formatting xdy.y
    def setDegreesAndMinutes(self, angleString):
        
        # If the argument is not a string, raise a Value Error
        if (not(isinstance(angleString, str))):
            raise ValueError('Angle.setDegreesAndMinutes:  Parameter should be a string')

        # Used later to check if value entered was negative
        isNegative = False
        
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
        if (not(angleDegrees.isdigit())):
            raise ValueError('Angle.setDegreesAndMinutes:  x must be an integer')
        
        # If the values after the d cannot be converted to a float, raise a Value Error
        try:
            angleMinutes = float(angleString[delimiterIndex+1:])
        except:
            raise ValueError('Angle.setDegreesAndMinutes:  y.y must be an int or a float')
        
        # If minutes is entered as a negative, raise a Value Error
        if (angleMinutes < 0):
            raise ValueError('Angle.setDegreesAndMinutes:  y.y must be positive')
        
        # Set the degrees and minutes based on the argument
        self.degrees = int(angleDegrees)
        self.minutes = angleMinutes
        
        # If degrees is less than 0, set isNegative to true
        if (self.degrees < 0):
            isNegative = True
            
        # Modularize degrees, add the number of times greater than 60 minutes is to degrees, and 
        # Modularize minutes
        self.degrees = self.degrees%360
        self.degrees = self.degrees + (int(self.minutes / 60))
        self.minutes = (self.minutes%60)
        
        # If the argument entered was negative, subtract 60 from minutes
        if (isNegative):
            self.minutes = 60 - self.minutes
            
        # Return the degree as a float with minutes as fractions of degrees
        output = float(self.degrees + (self.minutes / 60.0))
        return output
    
    # Adds an instance of angle to the current instance
    def add(self, angle):
        
        # If the argument is not an angle, raise a Value Error
        if (not(isinstance(angle, Angle))):
            raise ValueError('Angle.add:  Parameter is not an Angle')
        
        # Add the two angles
        self.degrees = (self.degrees + angle.degrees)
        self.degrees = (self.degrees + (int((self.minutes + angle.minutes) / 60))) % 360
        self.minutes = (self.minutes + angle.minutes)%60.0
        
        # Return the output as a float with minutes as fractions of degrees
        output = float(self.degrees + (self.minutes / 60.0))
        return output
    
    # Subtract an Angle from this instance of Angle
    def subtract(self, angle):
        
        # If the argument is not an Angle, raise a Value Error
        if (not(isinstance(angle, Angle))):
            raise ValueError('Angle.subtract:  Parameter is not an Angle')
        
        # Subtract the argument angle from the current angle
        self.degrees = (self.degrees - angle.degrees)%360
        self.degrees = (self.degrees - (int((self.minutes - angle.minutes) / 60))) % 360
        self.minutes = (self.minutes - angle.minutes)%60.0
        
        # Return the output as degrees with minutes as fractions of degrees
        output = float(self.degrees + (self.minutes / 60.0))
        return output
    
    # Compare two angles
    def compare(self, angle):
        
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
            
            # If the current instance's minutes is bigger, return 1
            if (self.minutes > angle.minutes):
                return 1
            
            # If the argument instance's minutes is bigger, return -1
            elif (self.minutes < angle.minutes):
                return -1
            
            # If the angles are equal in value, return 0
            else:
                return 0
    
    # Returns the degrees in the format xdy.y
    def getString(self):
        return str(self.degrees) + 'd' + str(self.minutes)
    
    # Returns the degrees as a float with minutes as fractions of degrees
    def getDegrees(self):
        return float(self.degrees) + (self.minutes / 60.0)