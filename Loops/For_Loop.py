"""
This program demonstrate use and working of for loop.
It includes use of range() function, extracting letters from string,
use of continue and break.
"""
# Print numbers upto 5.
# In range() only stop is mentioned.

print("Print numbers less than 5")
for i in range(5):
    print(i, end=' ')
print(end='\n\n')

# Print numbers 1 to 5
# In range() start and stop is mentioned.

print("Print numbers 1 to 5")
for i in range(1, 5):
    print(i, end=' ')
print(end='\n\n')

# Print numbers 1 to 5 skipping 2 digits
# In range() start, stop and step is mentioned.

print("Print numbers 1 to 5 skipping 2 digits")
for i in range(1, 5, 2):
    print(i, end=' ')
print(end='\n\n')

# Print numbers 10 to 1 in reverse order
# In range() start, stop and negative step is mentioned.

print("Print numbers 10 to 1 in reverse order")
for i in range(10, 0, -1):
    print(i, end=' ')
print(end='\n\n')

# Extract letters from given string

word = "Hello World!"
for letter in word:
    print(f"'{letter}'", end=' ')
print(end='\n\n')

# Print table of 3

table = 3

print(f"Table of {table} is:")
for i in range(1, 11):
    result = table * i
    print(f"{table} * {i} = {result}")

# Print numbers using 'continue'.
# Skips the loop when number is divisible by 3.

print("Print numbers using 'continue'.")
for i in range(10):
    if i % 3 == 0:
        continue # skips loop and move to next number
    print(i, end=' ')
print(end='\n\n')

# Print numbers till it satisfies condition to brak the loop.
# Kills\Exits\Stops the loop when number is divisible by 3.

print("Print numbers till it satisfies condition to brak the loop.")
for i in range(1, 10):
    if i % 3 == 0:
        break # kills the loop or exit the loop
    print(i, end=' ')
print(end='\n\n')