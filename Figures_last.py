import math
import time
from abc import ABC, abstractmethod

class Figures(ABC):
    
    @abstractmethod
    def area(self):
        pass

#fr = Figures() #try run that line  ---> TypeError: Can't instantiate abstract class Figures with abstract method area it mean 

class Rectangle(Figures):
    def __init__(self, width, length):        
        self.width = width
        self.length = length
        
    def area(self):
        return print(int(self.width * self.length), "rectangle area")
    
class Circle(Figures):
    def __init__(self, radius): #  radius instead  rad       
        self.radius=radius    
    
    def area(self): # if u will use class without area method you will get error --> TypeError: Can't instantiate abstract class Circle with abstract method area
        return print(int(math.pi * (self.radius ** 2)), "circle area") # self for get method ot variable of current class
    
class Square(Figures):
    def __init__(self, width):        
        self.width = width
    
    def area(self):
        return print(int(self.width ** 2), "square area") # self for get method ot variable of current class
    
f1=Rectangle(10, 12)
f1.area()   

f2=Circle(10)
f2.area()

f3=Square(12)
f3.area()

#Please dont write console program, just implement some logic and print
# 1.You should read about self (this) in classes, what is abstract classes
# 2. What is function arguments of function
# 3. Function scope
