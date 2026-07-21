"""

"""

# Declaring a class

class Demo:
    print("This is demo class.", end='\n\n')

Demo() # Calling a class.
# ========================================================================

# Declaring class with function, creating object of a class
# and calling function using object.

class Calling_Function:
    def function(self):
        print("Function called from inside class.", end='\n\n')

# Creating an object
call_function = Calling_Function()

# Calling a methos using object
call_function.function() 
# ========================================================================

# Declaring class with function, creating object of a class
# and calling function using object.

class Calculator:

    # Class Attributes

    num_1 = 10
    num_2 = 15
    result = 0

    def add(self):
        self.result = self.num_1 + self.num_2
        print(f"Addition is {self.result}", end='\n\n')

    # Parameterized method
    def multiplication(self, num1, num2):
        self.result = num1 * num2
        print(f"Multiplication is {self.result}", end='\n\n')

calc = Calculator()

calc.add()
calc.multiplication(9, 19)       
# ========================================================================

# Class with constructor

class User:
    user_id = ''
    user_name = ''

    # Constructor

    def __init__(self, user_id, user_name):
        # instantiates values

        self.user_id = user_id
        self.user_name = user_name
    
    def user_details(self):
        print(f"User ID: {self.user_id} and User name: {self.user_name}", end='\n\n')

user = User("EMP001", 'John Doe')
user.user_details()
# ========================================================================

# Declaring a class with keyword 'pass'

class Class_Pass():
    # Does nothing
    pass
# ========================================================================

# Updating class attributes

class Employee:
    emp_id = 101
    name = 'Patrik'
    city = 'Sydney'

    def getInfo(self):
        print(f"\nEmployee ID: {self.emp_id}\nEmployee Name: {self.name}\nEmployee City: {self.city}"
              , end='\n\n')

emp = Employee()
print("Employee information before updating class attributes:")
emp.getInfo()

# Updating class attributes using class name

Employee.emp_id = 102
Employee.name = 'Alice'
Employee.city = 'NY'

print("Employee information after updating class attributes:")
emp.getInfo()
# ========================================================================

# Modify property of class on object

class Employee:
    emp_id = 101
    name = 'Patrik'
    city = 'Sydney'

    def getInfo(self):
        print(f"\nEmployee ID: {self.emp_id}\nEmployee Name: {self.name}\nEmployee City: {self.city}"
              , end='\n\n')

emp_2 = Employee()
print("Employee information before modifying property of class on object:")
emp.getInfo()

# Updating class attributes using class name

emp_2.emp_id = 102
emp_2.name = 'Alice'
emp_2.city = 'NY'

print("Employee information after modifying property of class on object:")
emp_2.getInfo()
# ========================================================================

# Deleting object
# We will delete object 'emp_2' of class Employee.

del emp_2
# Uncomment the print() otherwise throws 'NameError'
# print(emp_2)
# ========================================================================

# Destructor

class DestructorExample:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __del__(self):
        print("Object is deleted.")

dest = DestructorExample("John", "Doe")
print(f"{dest.first} {dest.last}")    