"""
This program demonstrate catching multiple exception in a single exception block.
"""

try:
    result = 0
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator / denominator
    print(f"Division: {result}")
except (ValueError, ZeroDivisionError):
    print("Either any of the value is non numeric or denominator is ZERO.")