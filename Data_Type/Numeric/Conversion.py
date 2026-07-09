# Converting to integer from float
# The int() function is used to convert a value to an integer data type.

price = 12.45
print("Original Price (float):", price, "Data Type:", type(price), end="\n\n")

price_int = int(price)
print("Converted Price (integer):", price_int, "Data Type:", type(price_int), end="\n\n")


# Converting to float from integer
# The float() function is used to convert a value to a float data type.

temperature = 36
print("Original Temperature (integer):", temperature, "Data Type:", type(temperature), end="\n\n")

temperature_float = float(temperature)
print("Converted Temperature (float):", temperature_float, "Data Type:", type(temperature_float), end="\n\n")  


# Converting to complex from integer
# The complex() function is used to convert a value to a complex data type.

from_int = 5
from_float = 3.2

print("Original Integer:", complex(from_int))
print("Original Float:", complex(from_float), end="\n\n")


# Implicite Conversion or Automatic Type Conversion
# Python automatically converts one data type to another when necessary, 
# such as when performing arithmetic operations between different data types.

int_value = 10
float_value = 5.5

result = int_value + float_value
print("Result of adding integer and float:", result, "Data Type:", type(result))