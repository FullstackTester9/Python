"""

"""

# Defining a function

def hello():
    print("Hello from a function.", end='\n\n')

# Calling a function

hello()
# =============================================================
# Function with parameter & argument
# name is a paramenter

def language(name):
    print(f"You are learning {name} programming language.", end='\n\n')

# Python is argument
language("Python")
# =============================================================

# Function returning value

def coordinate(longi, lati):
    return f"Longitude: {longi} and latitude: {lati} of city Chandrapur."

print(coordinate("79.303E", "19.970N"), end='\n\n') # To print result on screen

result = coordinate("79.303E", "19.970N")
print(result, end='\n\n') # Another way to print result
# =============================================================

# Positional Argument

def ide_details(ide, version):
    print(f"IDE Name: {ide}, Version: {version}", end='\n\n')

# First argument mapped to ide parameter.
# Second argument mapped to version parameter.

ide_details("VSCode", 1.129)

# Swap the position of arguments.
# First argument mapped to ide parameter.
# Second argument mapped to version parameter.

ide_details(1.129, "VSCode")
# =============================================================

# Keyword Argument
def ide_details(ide, version):
    print(f"IDE Name: {ide}, Version: {version}", end='\n\n')

# First argument mapped to ide parameter.
# Second argument mapped to version parameter.

ide_details(ide = "VSCode", version = 1.129)

# Revesing the order. Still gets correct result.

ide_details(version = 1.129, ide = "VSCode")
# =============================================================

# Default Argument

def favourite_fruit(fruit = "Mango"):
    print(f"My favourite fruit is {fruit}", end='\n\n')

favourite_fruit("Orange") # Print Orange as favourite fruit

favourite_fruit() # Print default value
# =============================================================

# *args
# The variable with * treated as tuple.

def fruit_price(*price):
    return sum(price)

total = fruit_price(25, 15, 27, 40, 33)
print(f"Total price of fruits is {total}.", end='\n\n')
# =============================================================

# **kwargs
# The variable with ** treated as dictionary.

def emp_details(emp_id, **info):
    print(f"Employee ID: {emp_id}")
    print(f"Additional details: {info}", end='\n\n')

emp_details('EMP0001', name='Rohit', dept='HR', city='Pune')
# =============================================================

# Scope of function
# 1. Local Scope
def ball_price():
    price = 75 # local variable, declared inside function
    print(f"Price of a ball is Rs {price} only.", end='\n\n') 

ball_price()

# 2. Global Scope

price = 120 # global variable.

def ball_price():
    # accessing global variable inside function
    print(f"Price of a ball is Rs {price} only.", end='\n\n') 

ball_price()

# 3. Modify global variable
# Use global keyword

number = 10 # global variable

def print_number():
    global number # point to global variable
    number = 20 # update value
    print(f"This is global variable: ", number, end='\n\n')

print_number()
# =============================================================
