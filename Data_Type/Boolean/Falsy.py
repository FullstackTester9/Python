"""
This program demonstrates the concept of falsy values in Python. 
Falsy values are those that evaluate to False in a boolean context.
The following values are considered falsy:
"""
print("Zero: ",bool(0))
print("Zero (float): ",bool(0.0))
print("Empty string: ",bool(""))
print("Empty list: ",bool([]))
print("Empty dictionary: ",bool({}))
print("Empty set: ",bool(set()))
print("Empty tuple: ",bool(()))
print("None: ",bool(None))
