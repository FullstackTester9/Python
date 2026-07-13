"""
This program demonstrates different ways to loop through dictionsry.
It include accessing only keys, accessing only keys using for and while loop.
It also includes accessing both keys and values using for and while loop with items() method. 
"""

dict_employee = {

    'emp_id': 'EMP001',
    'name': 'John',
    'detp': 'Accounts'
    }

# Original dictionary.
print("Original dictionary: ", dict_employee,end='\n\n')

# Accessing only keys with for loop.
print("The keys are: ")
for keys in dict_employee:
    print(keys, end=', ')
print(end='\n\n')

# Accessing only values with for loop.
print("The values are: ")
for keys in dict_employee:
    print(dict_employee[keys], end=', ')
print(end='\n\n')

# Accessing keys and values with for loop.
print("Keys and values are: ")
for keys in dict_employee:
    print(f"Key is '{keys}' & it's value is '{dict_employee[keys]}'")
print(end='\n\n')

# OR
# Accessing keys and values using items() method with for loop.
print("Accessing key, value using items() method. ")
for key, value in dict_employee.items():
    print(f"Key is '{key}' & it's value is '{value}'")
print(end='\n\n')

# Accessing only keys with while loop.
key_list = list(dict_employee)
index = 0

print("\nThe keys are: ")

while index < len(key_list):
    key = key_list[index]
    print(key, end=', ')
    index += 1
print(end='\n\n')

# Accessing only values with while loop.
key_list = list(dict_employee)
index = 0

print("The values are: ")

while index < len(key_list):
    key = key_list[index]
    value = dict_employee[key]
    print(value, end=', ')
    index += 1
print('\n')

# Accessing keys and values with while loop.
key_list = list(dict_employee)
index = 0

while index < len(key_list):
    key = key_list[index]
    value = dict_employee[key]
    print(f"Key is '{key}' and it's value is '{value}'", end='\n')
    index += 1
print('\n')

# OR
# Accessing keys and values using items() method with while loop.
item_list = list(dict_employee.items())
index = 0

while index < len(item_list):
    key, value = item_list[index]
    print(f"Key is '{key}' and it's value is '{value}'", end='\n')
    index += 1