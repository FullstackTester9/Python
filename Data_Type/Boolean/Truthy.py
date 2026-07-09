"""
This program demonstrates the truthiness of various non-empty and non-zero data types in Python. 
It uses the `bool()` function to evaluate the truth value of different objects, including integers, 
strings, lists, dictionaries, tuples, and sets. 
The output will show that all these non-empty and non-zero objects evaluate to `True`.
"""



print("Non-zero integer: ", bool(2))
print("Non-empty string: ", bool("Python"))
print("Non-empty list: ", bool([1, 'a', 1.4]))
print("Non-empty dictionary: ", bool({1: 'a', 2: 'b'}))
print("Non-empty tuple: ", bool((1, 2, 3)))
print("Non-empty set: ", bool(set([1, 2, 3])))

