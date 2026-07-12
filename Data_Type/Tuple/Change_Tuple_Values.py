"""
This program demonstrate how to convert a tuple into list and perform 
adding new items, ermoving exsting items from list and converting that list into tuple.
"""

tuple_country = ('India', 'Germany', 'Italy', 'Russia', 'China', 'Japan')

# Original tuple
print("Original tuple: ", tuple_country)

# Adding an element to a tuple.
list_country = list(tuple_country)
list_country.append('Qatar')
tuple_country = tuple(list_country)
print("Updated tuple with new country: ", tuple_country)

# Removing an element from tuple
list_country = list(tuple_country)
list_country.remove('China')
tuple_country = tuple(list_country)
print("After removing specified country: ", tuple_country)

# OR
list_country.pop()
tuple_country = tuple(list_country)
print("After popping element: ", tuple_country)

# Adding tuple to tuple
tuple_country_2 = ('USA', 'UAE')
tuple_country += tuple_country_2
print("After ading tuple: ", tuple_country)