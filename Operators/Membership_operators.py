"""
This program demonstrates working of membership operators.
Membership operators are: IN, NOT IN.
Use: Check if a value exist in a sequence or collection.
"""

list_city = ['Nagpur', 'pune', 'mumbai']

# 'in' operator.

print("Original list: ", list_city, end='\n\n')
print("Checking existance of a value using 'in': ")
print("Is 'Nagpur' exist in list? ", 'Nagpur' in list_city)
print("Is 'nagpur' exist in list? ", 'nagpur' in list_city, end='\n\n')

# 'not in'
print("Checking existance of a value using 'not in': ")
print("Is 'nagpur' not exist in list? ", 'nagpur' not in list_city)
print("Is 'Nagpur' not exist in list? ", 'Nagpur' not in list_city)