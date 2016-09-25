import math
class TCurve(object):

# outward facing methods
    def __init__(self, n=None):
        functionName = "TCurve.__init__: "
        if(n == None):
            raise ValueError(functionName + "invalid n")
        if(not(isinstance(n, int))):
            raise ValueError(functionName + "invalid n")
        if((n < 2) or (n >= 30)):
            raise ValueError(functionName + "invalid n")
        self.n = n

    
    def p(self, t=None, tails=1):
        functionName = "TCurve.p: "
        if(t == None):
            raise ValueError(functionName + "missing t")
        if(not(isinstance(t, float))):
            raise ValueError(functionName + "invalid t")
        if(t < 0.0):
            raise ValueError(functionName + "invalid t")
        
        if(not(isinstance(tails, int))):
            raise ValueError(functionName + "invalid tails")
        if((tails != 1) & (tails != 2)):
            raise ValueError(functionName + "invalid tails")
        
        constant = self.calculateConstant(self.n)
        integration = self.integrate(t, self.n, self.f)
        if(tails == 1):
            #integration = self.integrate(t, self.n, self.f, lowbound)
            result = constant * integration + 0.5
        else:
            #integration = self.integrate(t, self.n, self.f, lowbound)
            result = constant * integration * 2
            
        if(result > 1.0):
            raise ValueError(functionName + "result > 1.0")
        
        return result
        
# internal methods
    def gamma(self, x):
        if(x == 1):
            return 1
        if(x == 0.5):
            return math.sqrt(math.pi)
        return (x - 1) * self.gamma(x - 1)
    
    def calculateConstant(self, n):
        n = float(n)
        numerator = self.gamma((n + 1.0) / 2.0)
        denominator = self.gamma(n / 2.0) * math.sqrt(n * math.pi)
        result = numerator / denominator
        return result
    
    def f(self, u, n):
        n = float(n)
        base = (1 + (u ** 2) / n)
        exponent = -(n + 1.0) / 2
        result = base ** exponent
        return result
    
    def integrate(self, t, n, f):
        epsilon = 0.001
        simpsonOld = 0
        simpsonNew = epsilon
        upperBound = t
        lowerBound = 0
        s = 4
        multiplicand = 0
        while(abs((simpsonNew - simpsonOld) / simpsonNew) > epsilon):
            simpsonOld = simpsonNew
            w = (upperBound - lowerBound) / s
            i = 1
            iteration = 1
            
            multiplicand = f(lowerBound, n)
            while(i < s):
                i = i + 1
                if (i % 2 == 0):
                    multiplicand = multiplicand + (4 * f(lowerBound + (iteration * w), n))
                    iteration = iteration + 1
                else:
                    multiplicand = multiplicand + (2 * f(lowerBound + (iteration * w), n))
                    iteration = iteration + 1
                
            multiplicand = multiplicand + f(upperBound, n)
                
                
                
                
            simpsonNew = (w/3) * multiplicand       
            s = s * 2
        return simpsonNew
    
        
            
        
