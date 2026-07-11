"""
This program demonstrates how to access items in a list using indexing and slicing.
"""

list_fruit = ['grapes', 'bananas', 'papaya', 'mango', 'orange']

# Original list
print("List that contains Fruits:", list_fruit)

# Accessing list items using positive indexing
print("Third item in the list:", list_fruit[2])

# Accessing list items using negative indexing
print("Second item from the end in the list:", list_fruit[-2])

# Accessing third and fourth items in the list
print("Third and fourth items in the list:", list_fruit[2:4])  

# Accessing every second item in the list
print("Every second item in the list:", list_fruit[::2])

# Checking if an item exists in the list
print("Is 'mango' in the list?", "mango" in list_fruit)

# Checking if an item does not exist in the list
print("Is 'orange' in the list?", "orange" not in list_fruit)
