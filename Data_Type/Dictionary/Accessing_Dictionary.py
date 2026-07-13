"""
This program demonstrates ways to access dictionsry.
It include accessing only keys, accessing only values, accessing value with the help of a key. 
"""

dict_employee = {
    'emp_id': 'EMP001',
    'name': 'John',
    'detp': 'Accounts'
    }

# Original dictionary
print("Original dictionary: ", dict_employee, end='\n\n')

# Accessing keys of dictionary
print("Keys of a dictionary: ", dict_employee.keys(), end='\n\n')

# Accessing values of dictionary
print("Values of a dictionary: ", dict_employee.values(), end='\n\n')

# Accessing specific values of a dictionary
print("Value of a key 'name' is: ", dict_employee['name'], end='\n\n')