"""
This program demonstrate adding a new key-value pair to the dictionary and updating 
value of an existing key.
"""

dict_employee = {

    'emp_id': 'EMP001',
    'name': 'John',
    'detp': 'Accounts'
    }

# Original dictionary
print("Original dictionary: ", dict_employee)

# Add a new key-value pair
dict_employee['email'] = 'john_doe@sample.com'
print("After adding key 'email' its value is: ", dict_employee)

# Changing value of an exixting item.
print("Before updating 'name' key its value is: ", dict_employee['name'])
dict_employee['name'] = 'John Doe'
print("After updating 'name' key its new value is: ", dict_employee['name'])