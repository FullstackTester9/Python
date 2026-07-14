"""
This program demonstrates use and implementation of dictionary comprehension.
"""

# Basic dictionary comprehension
dict_squares = {num: num**2 for num in range(1, 11)}
print("Squares from 1 to 10", dict_squares, end='\n\n')

# Combining two list using dictionary comprehension
list_key = ['name', 'age', 'city']
list_value = ['Steve Jobs', '52', 'California']

print("List of key: ", list_key)
print("List of value: ", list_value)

dict_person = {keys: values for keys, values in zip(list_key, list_value)}
print("After combining two list: ", dict_person, end='\n\n')

# Dictionary comprehension with condition
even_squares = {num: num**2 for num in range(1, 11) if num % 2 == 0}
print("Dictionary with square of even number: ", even_squares)