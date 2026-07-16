"""
This program demonstrate basic working of assignment operators.
Assignment operators are:
=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=
"""

# '=' operator
# Assigns right hand side value to the left hand side variable.

distance = 87.6
print("Distance: ", distance, end='\n\n')

# '+=' augmented assignment operator or add and assign operator
# adds the value on its right to the variable on its left,
# and then assigns the updated result back to that same variable.

count = 0
print("Initial count: ", count)
count += 1 # Equivalent to count = count + 1
print("Count after incrementing by 1: ", count, end='\n\n')

# '-=' augmented assignment operator or subtraction assignment operator
# subtracts the value on its right to the variable on its left,
# and then assigns the updated result back to that same variable.

count = 5
print("Initial count: ", count)
count -= 1 # Equivalent to count = count - 1
print("Count after decrementing by 1: ", count, end='\n\n')

# '*=' augmented assignment operator or multiplication assignment operator
# multiply the value on its right to the variable on its left,
# and then assigns the updated result back to that same variable.

count = 5
print("Initial count: ", count)
count *= 2 # Equivalent to count = count * 2
print("Count after multiply by 2: ", count, end='\n\n')

# '/=' augmented assignment operator or division assignment operator
# divide the value on its right to the variable on its left,
# and then assigns the updated result back to that same variable.

count = 10
print("Initial count: ", count)
count /= 2 # Equivalent to count = count / 2
print("Count after divide by 2: ", count, end='\n\n')

# '%=' augmented assignment operator or modulus assignment operator
# modulus the value on its right to the variable on its left,
# and then assigns the updated result back to that same variable with remainder.

count = 11
print("Initial count: ", count)
count %= 2 # Equivalent to count = count % 2
print("Count after modulus by 2: ", count, end='\n\n')

# '//=' augmented assignment operator or floor division assignment operator
# divide the two values and roundoff the result to the nearest whole integer.

count = 9
print("Initial count: ", count)
count //= 2 # Equivalent to count = count // 2
print("Count after floor division by 2: ", count, end='\n\n')

# '**=' augmented assignment operator or exponentiation assignment operator
# raises a variable to the power of a given value and assigns result back to the same variable.

count = 14
print("Initial count: ", count)
count **= 2 # Equivalent to count = count ** 2
print("Count after exponentiation by 2: ", count, end='\n\n')

# '&=' bitwise AND assignment operator
# updating a variable by performing AND operation between current value and new value.

var_x = 12
var_y = 6
print(f"x: {var_x}, y: {var_y}")
var_x &= var_y # Equivalent to var_x = var_x & var_y
print("Count after bitwise AND: ", var_x, end='\n\n')

# '|=' bitwise OR assignment operator
# updating a variable by performing OR operation between
# variable on left and the value on the right, and assigns result back to the variable on left.

var_x = 12
var_y = 6
print(f"x: {var_x}, y: {var_y}")
var_x |= var_y # Equivalent to var_x = var_x | var_y
print("Count after bitwise OR: ", var_x, end='\n\n')

# '^=' bitwise Exclusive OR (XOR) assignment operator
# Performs XOR operation between a variable and a value, 
# and then assigns the result back to that same variable.

var_x = 12
var_y = 6
print(f"x: {var_x}, y: {var_y}")
var_x ^= var_y # Equivalent to var_x = var_x ^ var_y
print("After bitwise XOR: ", var_x, end='\n\n')

# '>>=' bitwise Right Shift assignment operator
# Performs Right Shift operation on a variables value, 
# and then assigns the result back to that same variable.

var_x = 20
var_y = 2
print(f"x: {var_x}, shifts bit to the right by: {var_y}")
var_x >>= var_y # Equivalent to var_x = var_x >> var_y
print("After Right Shift: ", var_x, end='\n\n')

# '<<=' bitwise Left Shift assignment operator
# Performs Left Shift operation between a variables value, 
# and then assigns the result back to that same variable.

var_x = 5
var_y = 2
print(f"x: {var_x}, shifts bit to the left by: {var_y}")
var_x <<= var_y # Equivalent to var_x = var_x << var_y
print("After left shift: ", var_x, end='\n\n')