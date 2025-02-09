from abc import ABC, abstractmethod
from math import *

#Câu 1:
class Geometry(ABC):
    def __init__(self, ten):
        self.ten = ten
    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def getPerimeter(self):
        pass
#---------------------------------------------------------


class Triangle(Geometry):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c


    #Heron
    def getArea(self):
        p = self.getPerimeter() / 2
        return round(sqrt(p * (p - self.__a) * (p-self.__b) * (p - self.__c)), 2)

    def getPerimeter(self):
        return round(self.__a + self.__b + self.__c, 2)
    def __str__(self):
        return f"Tam giac thường:\n \t Dien tich {self.getArea()} \n \t Chu vi {self.getPerimeter()}"

class IsoTriangle(Triangle):
    def __init__(self, ab,  c):
        super().__init__(a=ab, b = ab, c = c)
    def __str__(self):
        return f"Tam giac cân:\n \t Dien tich {self.getArea()} \n \t Chu vi {self.getPerimeter()}"

class EquiTriangle(IsoTriangle):
    def __init__(self, abc):
        super().__init__(ab = abc, c = abc)

    def __str__(self):
        return f"Tam giac đều:\n \t Dien tich {self.getArea()} \n \t Chu vi {self.getPerimeter()}"


class Rectangle(Geometry):
    def __init__(self, len, wid):
        self.__len = len
        self.__wid = wid
    def getArea(self):
        return self.__len * self.__wid
    def getPerimeter(self):
        return (self.__len + self.__wid) * 2
    def __str__(self):
        return f"Hình Chữ Nhật:\n \t Dien tich {self.getArea()} \n \t Chu vi {self.getPerimeter()}"

class Square(Rectangle):
    def __init__(self, canh):
        super().__init__(len = canh, wid = canh)
    def __str__(self):
        return f"Hình Vuông:\n \t Dien tich {self.getArea()} \n \t Chu vi {self.getPerimeter()}"

class Ellipse(Geometry):
    def __init__(self,a , b):
        self.__a = a
        self.__b = b
    def getArea(self):
        return self.__a * self.__b * pi
    def getPerimeter(self):
        return ((self.__a + self.__b)/2) * pi
    def __str__(self):
        if self.__a == self.__b:
            return f"Hình tròn:\n \t Dien tich {self.getArea()} \n \t Chu vi {self.getPerimeter()}"
        else:
            return f"Hình ELLIPSE:\n \t Dien tich {self.getArea()} \n \t Chu vi {self.getPerimeter()}"
class Circle(Ellipse):
    def __init__(self, radius):
        super().__init__(a = radius, b = radius)
        



def menu():
    objList = []

    while True:
        print("________________________MENU_______________________")
        print("1. TRIANGLE\n2. IsoTriangle\n3. EquiTriangle\n4. RECTANGLE\n5. Square\n6. ELLIPSE\n7. Circle")
        chon = int(input("YOUR OPTION: "))
        if chon == 8:
            break
        elif chon == 1:
            a, b, c = map(int, input("Nhập độ dài 3 cạnh của tam giác: ").split())
            tg = Triangle(a, b, c)
            objList.append(tg)
        elif chon == 2:
            ab, c = map(int, input("Nhập cạnh bằng nhau và cạnh còn lại: ").split())
            tgc = IsoTriangle(ab, c)
            objList.append(tgc)
        elif chon == 3:
            abc = int(input("Nhập độ dài cạnh tamm giác đều: "))
            tgd = EquiTriangle(abc)
            objList.append(tgd)
        elif chon == 4:
            l, w = map(int, input("Nhập chiều dài và chiều rộng của hinh chữ nhật: "))
            hcn = Rectangle(l, w)
            objList.append(hcn)
        elif chon == 5:
            c = int(input('Nhập cạnh của hình vuông: '))
            hv = Square(c)
            objList.append(hv)
        elif chon == 6:
            a, b = map(int, input("Nhập độ dài trục lớn và trục bé: "))
            el = Ellipse(a, b)
            objList.append(el)
        elif chon == 7:
            r = int(input("Nhập bán kình của hình tròn: "))
            ht = Circle(r)
            objList.append(ht)

        else:
            print("Nhập lại:    ")
    for obj in objList:
        print(obj)
menu()




