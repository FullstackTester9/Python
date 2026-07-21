"""
This program demonstrate implementation of multiple inheritance.
Parent classes: Herbivores, Carnivores.
Child class: Omnivores.
"""

class Herbivores:
    
    def plant_diet(self):
        print("Eats plants, fruits.")

class Carnivores:
    
    def meat_diet(self):
        print("Eats meat.")

class Omnivores(Herbivores, Carnivores):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def eats_everything(self):
        print(f"{self.name} eats both plant and meat.")
        self.plant_diet()
        self.meat_diet()

bear = Omnivores("Bear")
bear.eats_everything()