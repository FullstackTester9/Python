"""
This program demonstrate use and working of while loop.
"""

count = 0

print("Print numbers upto 5")
while count <=5:
    print(f"count: {count}", end=' ')
    count += 1
print(end='\n\n')

# Print numbers less than 5
count = 0

print("Print numbers less than 5")
while count < 5:
    print(f"count: {count}", end=' ')
    count += 1
print(end='\n\n')

# Print numbers in reverse order
count = 10

print("Print numbers in reverse order")
while count > 0:
    print(f"count: {count}", end=' ')
    count -= 1
print(end='\n\n')


# Use of 'continue'
num = 1
print("Use of 'continue'")

while num <= 5:
    if num == 3:
        num += 1 # to avoid an infinite loop
        continue
    print(f"num: {num}", end=' ')
    num += 1 # for other numbers    
print(end='\n\n')

# Use of 'break'
num = 1
print("Use of 'break'")

while num <= 5:
    if num % 5 == 0:
        break
    print(f"num: {num}", end=' ')
    num += 1    
print(end='\n\n')