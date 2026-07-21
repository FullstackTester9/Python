"""
This program demonstrate working of abstraction in OOP.
It shows how to create abstract method, abstract class.
You can not create object of abstract class. 
If you do so it throws "TypeError"
"""

from abc import ABC, abstractmethod
import math

# Class 'Shape' is an abstract class.
# You can not instantiate abstract classes, because the class contain
# methods that are declared abstract or not fully implemented.

class Shape(ABC):
    # Abstract method no implementation here.
    @abstractmethod
    def area(self): 
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

circle = Circle(4)
print(f"Area of a circle is: {circle.area():.2f}")

# shape = Shape() # TypeError
