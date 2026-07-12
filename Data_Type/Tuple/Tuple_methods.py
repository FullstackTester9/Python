"""
This program demonstrate wirking of tuple methods.
"""

tuple_num = (10, 15, 68, 97, 105, 84, 10, 20)

# Original tuple
print("Original tuple: ", tuple_num)

# Check how many times value appeared in tuple.
repeat = tuple_num.count(10)
print("Value '10' repeated", repeat, 'times.')

# Check first occurance of specified value.
first_occurance = tuple_num.index(10)
print("First occurance of '10' is at index: ", first_occurance)