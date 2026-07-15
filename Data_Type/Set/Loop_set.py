fruit_set = {'apple', 'mango', 'dragonfruit', 'pineapple', 'indian gooseberry'}

# Loop through a set using for loop
for fruit in fruit_set:
    print(fruit)
print(end='\n')

# Loop through a set in a specific using for loop
for fruit in sorted(fruit_set):
    print(fruit)
print(end='\n')

# Accessing index of set using 'enumerate'
for index, value in enumerate(fruit_set):
    print(f"Index: {index}, Value: {value}")

# Set Comprehension
set_square = {num**2 for num in range(1, 11)}
print(set_square)