"""
This code demonstrates the declaration of Tuples in Python.
It shows how to create tuples containing different data types.
Additionally, it illustrates the use of the tuple constructor to create a tuple.
"""

empty_tuple = ()
one_element_tuple = (1,)
multiple_tuple_element = (1, 2, 3)
multivalue_tuple = (1, 'a', 1.9)

# Empty tuple
print("Empty tuple: ", empty_tuple)

# Tuple with only one element
print("Tuple with one element: ", one_element_tuple)

# Tuple with multiple element of same type
print("Tuple with multiple element: ", multiple_tuple_element)

# Tuple with multiple element with differnt data type
print("Multivalue tuple: ", multivalue_tuple)

# Creating tuple with a constructor
tuple_constructor = tuple(('Python', 'Java', 'C#', 'Rust'))
print("This tuple is created using tuple constructor: ", tuple_constructor)