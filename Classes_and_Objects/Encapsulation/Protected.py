"""
This program demonstrate working of protected access modifiers.
A protected variable or access modifiers are marked with 'single underscore'
before attribute name or method name.
"""

# Protected variables

class Car():
    def __init__(self, company, model, color):
        self._company = company
        self._model = model
        self._color = color
    
    def car_details(self):
        print(f"Company: {self._company}\nModel: {self._model}\nColor: {self._color}", end='\n\n')

car = Car("Toyota", "Fortuner", "Black")
car.car_details()
# print(car._company)
# ========================================================================

# Protected methods
class EmployeeSalary():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def _salary_increment(self):
        return self.salary * 0.10 # 10% increment

class Employee(EmployeeSalary):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    
    def updated_salary(self):
        return self.salary + self._salary_increment()

emp = Employee("Alex", 15000)
result = emp.updated_salary()
print(f"Updated salary with 10% increment: {result}")
# ========================================================================
