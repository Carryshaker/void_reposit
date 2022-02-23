import math
from abc import ABC, abstractmethod

class Figures(ABC):
    
    @abstractmethod
    def area(self):
        pass


class Rectangle(Figures):
    def __init__(self, width, length):
        self.width=width
        self.length=length
    
    def area(self):
        return print("Rectangle area",int(self.width*self.length))
    
class Circle(Figures):
    def __init__(self, radius):     
        self.radius=radius
    
    
    def area(self):
        return print("Circle area",int(math.pi*(radius**2)))
    
class Square(Figures):
    def __init__(self, length2):        
        self.length2=length2
    
    def area(self):
        return print("Square area",int(length2**2))
    



fig=input("There is a rectangle, a square, a circle.\nWhat figura area do you need?\n")
if fig.lower()==str("rectangle"):
    width=int(input("Width: "))
    length=int(input("Length: "))
    f1=Rectangle(width, length)
    f1.area()
    
elif fig.lower()==str("circle"):
    radius=int(input("Radius: "))
    f2=Circle(radius)
    f2.area()

elif fig.lower()==str("square"):
    length2=int(input("Length: "))
    f3=Square(length2)
    f3.area()
    

    
