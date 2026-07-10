"""
This is a simple Python program that demonstrates string concatenation.
"""

str_1 = "Hello"
str_2 = "World!"

# Concatenating two strings using the + operator
print("Concatenated String using + operator: ", str_1 + str_2, end='\n\n')

# Using comma to concatenate strings in print function
print("Concatenated String using comma: ", str_1, str_2, end='\n\n')

# Using f-string to concatenate strings
print("Concatenated String using f-string: ", f"{str_1}{str_2}", end='\n\n')

# Concatenating with an additional space in between
print("Concatenated String with space: ", str_1 + " " + str_2, end='\n\n')  