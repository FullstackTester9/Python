"""
This is a Python code snippet that demonstrates how to change items in a list. 
The code starts with a list of fruits and shows how to modify individual items 
as well as slices of the list. 
It includes examples of changing a single item, changing multiple items, 
and replacing a slice of the list with more or fewer items. 
The output of each change is printed to the console to illustrate the modifications made to the list.
"""

list_fruit = ['watermelon', 'kiwi', 'pineapple', 'strawberry', 'blueberry']

# Original list
print("List that contains Fruits:", list_fruit)

# Changing the first item in the list
list_fruit[0] = 'dragonfruit'
print("List after changing the first item:", list_fruit)

# Changing the second and third items in the list
list_fruit[1:3] = ['papaya', 'mango']
print("List after changing the second and third items:", list_fruit)

# Changing the second and third items in the list with more items
list_fruit[1:3] = ['papaya', 'mango', 'grapefruit', 'cantaloupe']
print("List after changing the second and third items:", list_fruit)

# Changing the second and third items in the list with fewer items
list_fruit[1:3] = ['guava']
print("List after changing the second and third items:", list_fruit)
