"""
This is a simple Python program that demonstrates string slicing.
"""

str = "Welcome to Python Programming."

# Slicing a string from index 0 to the end of the string
print("Slicing from index 0 to the end: ", str[:], end='\n\n')

# Slicing a string from index 11 to the end of the string
print("Slicing from index 11 to the end: ", str[11:], end='\n\n')

# Slicing a string from index 0 to 6 (not including 6)
print("Slicing from index 0 to 6: ", str[0:6], end='\n\n')
print("Slicing from index 0 to 6: ", str[:6], end='\n\n')

# Negative indexing in string slicing (not including -6 and -14)
print("Slicing with negative indices: ", str[-14:-6],end='\n\n')

# Slicing a string with step value
print("Slicing with step 2: ", str[::2], end='\n\n')

# Slicing a string in reverse order
print("Reversed string: ", str[::-1], end='\n\n')