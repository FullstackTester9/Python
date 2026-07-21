"""
This program demonstrate working of polymorphism.
It includes polymorphism with inheritance and method overriding.
Python does not support method overloading. 
Because, method arguments do not have data type.
"""

# Method overriding

class Vehicle:
    def __init__(self, color):
        self.color = color
    
    def print_me(self):
        print(f"This is vehicle and color is {self.color}")

class Bike(Vehicle):
    def __init__(self, color, engine):
        self.color = color
        self.engine = engine
    
    def print_me(self):
        print(f"Bike with color {self.color} with engine {self.engine}CC")
    
class Truck(Vehicle):
    def __init__(self, color, capacity):
        self.color = color
        self.capacity = capacity
    
    def print_me(self):
        print(f"Truck with color {self.color} & capacity {self.capacity} ton", end='\n\n')

vehicle = Vehicle("Black")
vehicle.print_me()

bike = Bike("Red", 220)
bike.print_me()

truck =Truck("Yellow", 1200)
truck.print_me()
# ========================================================================

# Polymorphism with inheritance

class Shapes:
    def perimeter(self):
        pass

    def area(self):
        pass

class Square(Shapes):
    def __init__(self, side):
        self.side = side
    
    def perimeter(self):
        return 4 * self.side
    
    def area(self):
        return self.side * self.side

class Circle(Shapes):
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return (2 * self.pi * self.radius)
    
    def area(self):
        return (self.pi * (self.radius * self.radius))
    
square = Square(side=5)
print(f"Area of a square: ", square.area())
print(f"Perimeter of a square: ", square.perimeter(), end='\n\n')

circle = Circle(radius=6)
print(f"Area of a circle: ", circle.area())
print(f"Perimeter of a circle: ", circle.perimeter(), end='\n\n')
# ========================================================================
