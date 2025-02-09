#PTB2
from math import *
class PTB2:
    def __init__(self,a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def getDelta(self):
        return pow(self.b, 2) - 4 * (self.a * self.c)
    def getX1(self):
        dt = self.getDelta()
        return (-self.b + sqrt(dt)) / (2 * self.a)
    def getX2(self):
        dt = self.getDelta()
        return (-self.b - sqrt(dt)) / (2 * self.a)
    def __str__(self):
        return f"{self.a}.X ^ 2  + {self.b}.X + {self.c} = 0"

a, b, c = map(float,input("Nhập a, b, c: ").split())
ptb2 = PTB2(a, b, c)
print(ptb2)

dt = ptb2.getDelta()
if dt < 0:
    print("Phương trình vô nghiệm:")
elif dt == 0:
    print("X = ", -b / (2 * a))
else:
    print("X1 = ", ptb2.getX1())
    print("X2 = ", ptb2.getX2())









