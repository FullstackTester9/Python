"""
This program demonstrate ways to declare set using curly brackets and set constructor.
It also demonstrate that other iterable data structure are converted into a set.
After conversion duplicate elements are removed.
"""

# Declaring a set with comma separated values in curly brackets.
set_num = {1, 2, 3, 4, 5}

# Declaring empty set using set constructor
set_constructor = set()

# Converting iterable data structures into set.
# List
num_list = [11, 43, 27, 65, 90, 27]
list_to_set = set(num_list)
print("List is converted into set with duplicate item removed: ", list_to_set, end='\n\n')

# Tuple
num_tuple = (1, 9, 88, 42, 13, 56, 9, 1)
tuple_to_set = set(num_tuple)
print("Tuple is converted into set with duplicate item removed: ", tuple_to_set, end='\n\n')

# String
str_set = "I'm learning Python programming language."
str_to_set = set(str_set)
print("String converted into set with duplicate item removed: ", str_to_set, end='\n\n')
