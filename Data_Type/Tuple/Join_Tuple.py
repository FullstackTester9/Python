"""
This program demonstrate joinning of tuple using '+' and '*'.
'+' sign adds two tuples, whereas, '*' multiplies(reprats) content of tuple
specified times.
"""

tuple_country = ('India', 'Australia', 'New Zealand')
national_animal = ('Tiger', 'Kangaroo', 'Kiwi')

# Adding two tuples
country_national_animal = tuple_country + national_animal
print("Countries followed by their national animals: ", country_national_animal)

# Multiply tuples
tuple_multiply = national_animal * 2
print("After multiplication of tuple: ", tuple_multiply)

tuple_number = (11, 21, 25, 30)
tuple_multiply = tuple_number * 3
print("After multiplication of tuple: ", tuple_multiply)