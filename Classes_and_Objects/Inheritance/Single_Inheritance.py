"""
This program demonstrate working of single inheritance.
"""

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self):
        super().__init__()
    
    def make_sound(self):
        return "barking"

dog = Dog()
print(f"The dog is making a {dog.make_sound()} sound.")