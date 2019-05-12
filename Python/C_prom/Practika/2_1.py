import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
x1=1/(c*math.sqrt(2*math.pi))
x2=-(((a-b)/(math.sqrt(2)*c))**2)
x3=x1*math.exp(x2)
print x3
