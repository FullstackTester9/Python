"""
This program demonstrate working of if...else statement.
It includes if ststement with condition and without condition.
Also uses if..elif..else statement. 
"""

num = 5
percentage = 81.23

# Check number is even or odd.

if num % 2 == 0:
    print("Number is even.", end='\n\n')
else:
    print("Number is odd.", end='\n\n')

# Check int number is equal to string or not.

if num == '5':
    print("5 == '5'", end='\n\n')
else:
    print("5 != '5'", end='\n\n')

# If statement without condition

if num:
    print("if without condition always executed", end='\n\n')
else:
    print("if without condition never gets executed", end='\n\n')

# If statement with elif

if percentage >= 75.00 and percentage <= 100:
    print(f"You scored {percentage}% and passed with 'Distinction'", end='\n\n')
elif percentage >= 60.00 and percentage <= 74.99:
    print(f"You scored {percentage}% and passed with 'First class'", end='\n\n')
elif percentage >= 45.00 and percentage <=59.99:
    print(f"You scored {percentage}% and passed with 'Second class'", end='\n\n')
elif percentage >= 35.00 and percentage <=44.99:
    print(f"You scored {percentage}% and passed with 'Third class'", end='\n\n')
elif percentage <= 34.99:
    print(f"You failed. Your score is {percentage}%", end='\n\n')
else:
    print("Not valid percentage", end='\n\n')