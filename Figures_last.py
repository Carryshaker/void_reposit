import math
import time

class Figures:
    def __init__(self, width, length):
        self.width=wid
        self.length=leng


class Rectangle(Figures):
    def area(self):
        return print(int(self.width*self.length))
    
class Circle(Figures):
    def __init__(self, width, length, radius):
        super().__init__(width, length)
        
        self.radius=rad
    
    
    def area(self):
        return print(int(math.pi*(rad**2)))
    
class Square(Figures):
    def __init__(self, width, length, lenght2):
        super().__init__(width, length, length2)
        
        self.lenght2=leng2
    
    def area(self):
        return print(int(leng2**2))
    



fig=input("There is a rectangle, a square, a circle.\nWhat figura area do you need?\n")
if fig.lower()==str("rectangle"):
    wid=int(input("Width: "))
    leng=int(input("Length: "))
    f1=Rectangle(wid, leng)
    f1.area()
    
elif fig.lower()==str("circle"):
    rad=int(input("Radius: "))
    f2=Circle(rad)
    f2.area()

elif fig.lower()==str("square"):
    leng2=int(input("Length: "))
    f3=Square(leng2)
    f3.area()
