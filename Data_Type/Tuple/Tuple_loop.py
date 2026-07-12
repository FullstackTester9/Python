"""
This program demonstrates different ways to loop through tuple.
It includes example of for loop, while loop, and tuple comprehension.
"""

tuple_name = ('John', 'Scott', 'Pratik', 'Rohit', 'Suraj', 'Amit')

# Accessing tuple elements using for loop
for index in range(len(tuple_name)):
    print(f"Name at index {index} is {tuple_name[index]}")

# Accessing tuple elements using while loop
index = 0
while index < len(tuple_name):
    print(f"Name at index {index} is {tuple_name[index]}")
    index += 1

# Tuple comprehension
# Generate square of number form 1 - 10 using tuple comprehension.
tuple_square = tuple(num**2 for num in range(1, 11))
print("Squares of number from 1 to 10: ", tuple_square)

# Filtering tuple element whose length is equal to 5 using tuple comprehension.
tuple_filter = tuple(name for name in tuple_name if len(name) == 5)
print("Elements whose length is equal to 5 are: ", tuple_filter)