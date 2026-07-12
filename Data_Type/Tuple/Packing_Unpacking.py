"""
This program demonstrates working of packing and unpacking of a tuple.
Packing: Creating a tuple and assigning values to it is called packing.
Unpacking: Extracting values back to the variable is called unpacking.
"""

tuple_color = ('red', 'blue', 'magenta', 'cyan', 'maroon')
a, b, c, d, e = tuple_color

# Original tuple
print("Original tuple: ", tuple_color)

print("Unpacking of tuple: ")
print(a)
print(b)
print(c)
print(d)
print(e)

# Capture first, last and group remaining elements in a tuple
first, *middle, last = tuple_color

print("First element: ", first)
print("Middle elements: ", middle)
print("Last element: ", last)
