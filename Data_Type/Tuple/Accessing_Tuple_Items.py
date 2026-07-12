"""
This program demonstrates how to access items in a tuples using indexing and slicing.
"""


tuple_fruits = ('apple', 'guava', 'orange', 'grapes', 'kiwi', 'papaya')

# Check item exist
print("Is 'kiwi' present in tuple?: ", 'kiwi' in tuple_fruits)

# Check item not exist
print("Is 'banana' present in tuple?: ", 'banana' not in tuple_fruits)

# Accessing first element of tuple
print("First element of tuple: ", tuple_fruits[0])

# Accessing second, third, fourth element of tuple
print("Second, Third, Fourth element of tuple: ", tuple_fruits[1:4])

# Accessing every second element of tuple
print("Every second element of tuple: ", tuple_fruits[::2])

# Accessing second item from last
print("Second last element from tuple: ", tuple_fruits[-2])

# Accessing range of indexes using negative index
print("Accessing elements from last: ", tuple_fruits[-4:-2])