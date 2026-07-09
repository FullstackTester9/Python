"""
This is a simple Python program that demonstrates the use of complex numbers. 
It creates two complex numbers, performs basic arithmetic operations on them, 
and prints the results along with their data types and real/imaginary parts.
"""


#Complex: Numbers with a real and an imaginary part.

num_1 = 2 + 3j
num_2 = 4 - 5j

print("Complex Number 1:", num_1, "Data Type:", type(num_1))
print("Complex Number 2:", num_2, "Data Type:", type(num_2), end="\n\n")

print("Real Part of num_1:", num_1.real)
print("Imaginary Part of num_1:", num_1.imag, end="\n\n")

print("Addition: ", num_1 + num_2)  # Addition of complex numbers
print("Subtraction: ", num_1 - num_2)  # Subtraction of complex numbers
print("Multiplication: ", num_1 * num_2)  # Multiplication of complex numbers
print("Division: ", num_1 / num_2)  # Division of complex numbers