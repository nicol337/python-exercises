class Complex:
    def __init__(self,real,i):
        self.real = real
        self.i = i
    
    def __add__(self,other):
        #print(self.real+other.real,self.i+other.i)
        return Complex(self.real+other.real,self.i+other.i)
    
    def __sub__(self,other):
        return Complex(self.real-other.real,self.i-other.i)
    
    def __mul__(self,other):
        real = self.real*other.real - self.i*other.i
        i = self.real*other.i + self.i*other.real 
        return Complex(real,i)
    
    def __str__(self):
        s = ""
        hasReal = False
        if self.real != 0:
            s += "%.2f" % self.real
            hasReal = True
        if self.i > 0 and hasReal:
            s += " + " + "%.2f" % self.i + "i"
        elif self.i < 0 and hasReal:
            s += " " + "%.2f" % self.i + "i"
        elif self.i < 0:
            s += "%.2f" % self.i + "i"
        return s
            
            

num = input().split()
num = Complex(int(num[0]),int(num[1]))
num2 = input().split()
num2 = Complex(int(num2[0]),int(num2[1]))

print(num+num2)
print(num-num2)
print(num*num2)
print(num/num2)
print()