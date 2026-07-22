"""
This program demonstrate implementation of custom exception. 
"""

class DataTypeMisMatchError(Exception):
    """Raised when user compare or perform arithmetic operation with wrong data type."""
    pass

def validate_age(age):
    if not isinstance(age, (int, float)):
        raise DataTypeMisMatchError("Neither an int nor float.")
    if age >= 18:
        return "You can vote."
    else:
        return "you can not vote."

try:
    print(validate_age(17))
    print(validate_age(-10))
    print(validate_age(22))
    print(validate_age(33.6))
    print(validate_age('f'))
except DataTypeMisMatchError as e:
    print(e)