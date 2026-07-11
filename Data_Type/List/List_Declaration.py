"""
This code demonstrates the declaration of lists in Python. 
It shows how to create lists containing different data types, including alphabets, numbers, 
booleans, mixed types, and nested lists. 
Additionally, it illustrates the use of the list constructor to create a list from a tuple.
"""

list_alphabet = ['a', 'b', 'c', 'd']
list_numbers = [1, 2, 3, 4]
list_boolean = [True, False, True, False]
list_mixed = ['a', 1, True, 3.14]
list_constructor = list(('a', 'b', 'c', 'd'))
list_nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("List that contains Alphabets:", list_alphabet)
print("List that contains Numbers:", list_numbers)
print("List that contains Booleans:", list_boolean)
print("List that contains Mixed Types:", list_mixed)
print("List that contains Nested Lists:", list_nested)
print("List created with constructor:", list_constructor)