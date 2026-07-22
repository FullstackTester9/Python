"""
This program demonstrate to raise exception manually.
If age is less than 18 years then you are not eligible to vote.
"""

def validate_age(age):
    if age >= 18:
        print("You are eligible to vote.")
    else:
        raise ValueError("Not eligible to vote.")

validate_age(17)