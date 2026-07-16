"""
This program demonstrate working of identity operators.
Identity operators are: IS, IS NOT.
"""

# 'is' identity operator.
# Check whether two variables refer to the exact same memory or not.

list_name = ['john', 'troy', 'sonu']
list_fruit = ['mango', 'banana', 'guava']

list_a = list_fruit # assign list to a new variable.
print("Checking identity using 'is'.")
print("'list_name' = ", list_name)
print("'list_fruit' = ", list_fruit)
print("'list_a' = ", list_a, end='\n\n')

print("list_name is list_fruit: ", list_name is list_fruit)
print("list_fruit is list_a: ", list_fruit is list_a, end='\n\n')

# Verify memory id
print("ID of 'list_name': ", id(list_name))
print("ID of 'list_fruit': ", id(list_fruit))
print("ID of 'list_a': ", id(list_a), end='\n\n')

# 'is not'
print("Checking identity using 'is not'.")

print("list_name is not list_fruit: ", list_name is not list_fruit)
print("list_fruit is not list_a: ", list_fruit is not list_a, end='\n\n')

# Verify memory id
print("ID of 'list_name': ", id(list_name))
print("ID of 'list_fruit': ", id(list_fruit))
print("ID of 'list_a': ", id(list_a), end='\n\n')