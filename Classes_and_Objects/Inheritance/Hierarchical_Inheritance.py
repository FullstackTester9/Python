"""
This program demonstrate working of Hierarchical inhetitance.
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} is breathing.")

class Carnivore(Animal):
    def eat_meat(self):
        print(f"{self.name} eats meat.")

class Herbivore(Animal):
    def eat_plants(self):
        print(f"{self.name} eats plants.")

# 1. Create an instance of Carnivore

lion = Carnivore("Lion")
lion.breathe()   # Inherited from Animal
lion.eat_meat()  # Specific to Carnivore

print("-" * 20)

# 2. Create an instance of Herbivore

deer = Herbivore("Deer")
deer.breathe()    # Inherited from Animal
deer.eat_plants() # Specific to Herbivore