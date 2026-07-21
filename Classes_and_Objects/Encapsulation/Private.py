"""
This program demonstrate working of private access modifiers.
A private variable or access modifiers are marked with 'double underscore'
before attribute name or method name.
"""

# Accessing private data members using GETTERS & SETTERS

class Employee:
    def __init__(self):
        self.__salary = 20000
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid amount.")

emp = Employee()
print("Initial salary: ",emp.get_salary())
emp.set_salary(30000)
print("Updated salary: ",emp.get_salary(), end='\n\n')
# ========================================================================

# Accessing private data members using @property

class Employee:
    def __init__(self):
        self.__salary = 40000
    
    @property # GETTER
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid amount.")

emp = Employee()
print("Initial salary: ", emp.salary)
emp.salary = 45000
print("Updated salary: ",emp.salary)
# ========================================================================
