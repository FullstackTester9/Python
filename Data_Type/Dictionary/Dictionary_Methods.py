"""
This program demonstrate use and implementation of dictionary methods.
"""
dict_employee = {

    'emp_id': 'EMP001',
    'name': 'John',
    'detp': 'Accounts'
    }

# Original dictionary
print("Original dictionary: ", dict_employee, end='\n\n')

# clear() method
# print("Dictionary after clear() method: ", dict_employee.clear(), end='\n\n')

# copy() method
dict_employee_copy = dict_employee.copy()
print("Copied dictionary: ", dict_employee_copy, end='\n\n')

# fromkeys() method without specific value.
keys = ['apple', 'banana', 'strawberry']
dict_fruit = dict_employee.fromkeys(keys)
print("Fromkeys without specific value: ", dict_fruit, end='\n\n')

# fromkeys() method with specific value.
keys = ['apple', 'banana', 'strawberry']
dict_fruit = dict_employee.fromkeys(keys, 9.6)
print("Fromkeys with specific value: ", dict_fruit, end='\n\n')

# fromkeys() method removing duplicates.
numbers = [11, 48, 21, 17, 36, 11, 78, 48, 21, 36, 81, 25, 46]
unique_numbers = list(dict.fromkeys(numbers))
print("Unique numbers: ", unique_numbers, end='\n\n')

# get() method
print("Value of key 'emp_id' is: ", dict_employee.get('emp_id'), end='\n\n')

# items() method
print("View object returned by items() method: ", dict_employee.items(), end='\n\n')

# keys() method
print("View object returned by keys() method: ", dict_employee.keys(), end='\n\n')

# pop() method
print("Item removed using pop() method: ", dict_employee_copy.pop('detp'), end='\n\n')

# popitem() method
dict_employee_copy['dept'] = 'HR'
print("Last inserted item removed: ", dict_employee_copy.popitem(), end='\n\n')

# setdefault() method when key does not exist.
print("Original dictionary: ", dict_employee, end='\n\n')
city = dict_employee.setdefault('city', 'Mumbai')
print("New key-value pair inserted and returned default value: \n", dict_employee, end='\n\n')

# setdefault() method when key exist.
dict_employee_copy['city'] = 'Chennai'
print("Original dictionary: ", dict_employee_copy, end='\n\n')
city = dict_employee_copy.setdefault('city', 'Mumbai')
print("Returns value of exixting key 'Chennai' not 'Mumbai': \n", dict_employee_copy, end='\n\n')

# update() method using another dictionary
dict_employee.update({'age': 37, 'gender': 'M'})
print("New key-value added using uodate() method: \n", dict_employee, end='\n\n') 

# values() method
print("Values of dictionary: ",dict_employee.values())