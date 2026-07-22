"""
This program demonstrate working of multilevel inheritance.
"""

class Animal:
    def feature(self):
        return "Multicellular, eukaryotic organisms that are heterotrophic."

class Mammal(Animal):
    def __init__(self):
        super().__init__()
    
    def feature(self):
        return "A mammal is vertibrate animal."
    
    def move(self):
        return "Most mammals use 4 limbs to move. But, in some limbs are adapted for life at sea, in air."

class Felidae(Mammal):
    def __init__(self):
        super().__init__()
    
    def feature(self):
        return "Flexible, strong spine."

    def walk(self):
        return "Walk on toes rather than flat feet."

felidae = Felidae()

print(felidae.move()) # From Mammal class
print(felidae.feature()) # From Felidae class
print(felidae.walk()) # From Felidae class

# Method 1
# Call feature() of grandparent and parent class.

print(Animal.feature(felidae)) # From Animal class
print(Mammal.feature(felidae)) # From Mammal class

