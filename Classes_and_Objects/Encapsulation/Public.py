"""
This program demonstrate working of Public access modifier.
"""

class Car():
    def __init__(self, company, model):
        self.company = company
        self.model = model
    
    def info(self):
        print(f"Company name: {self.company} and Model: {self.model}", end='\n\n')

car = Car("Mahindra", "Scorpio")
car.info()
