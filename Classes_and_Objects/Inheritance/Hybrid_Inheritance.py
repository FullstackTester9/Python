"""
This program demonstrate working of hybrid inheritance.
For this program I've used Multiple inheritance, and hierarchical inheritance.
"""

class Animal:
    def info(self):
        print("I am a living organism.")

class Carnivore(Animal):
    def eat_meat(self):
        print("I eat meat.")

class Herbivore(Animal):
    def eat_plants(self):
        print("I eat plants.")

# Hybrid Inheritance: Combining Hierarchical and Multiple Inheritance
class Omnivore(Carnivore, Herbivore):
    def eat_both(self):
        print("I eat both plants and meat.")

print("--- Bear (Omnivore) ---")
bear = Omnivore()

# 1. Inherited from Animal (Base Parent)
bear.info()

# 2. Inherited from Carnivore (First Parent)
bear.eat_meat()

# 3. Inherited from Herbivore (Second Parent)
bear.eat_plants()

# 4. Unique to Omnivore
bear.eat_both()
