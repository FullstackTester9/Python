"""
This code demonstrates different ways to loop through a list of countries 
and create new lists using list comprehension. 
It includes examples of using a for loop, a while loop, and list comprehensions 
to filter and transform the data in the list.
"""

list_country = ['USA', 'Canada', 'Germany', 'France', 'Japan', 'India']

# Looping through the list using a for loop
print("Looping through the list using a for loop:")
for country in list_country:
    print("Country:", country)

print("\nLooping through the list using a while loop:")
index = 0
while index < len(list_country):
    print("Country:", list_country[index])
    index += 1

# Using list comprehension to create a new list with countries in uppercase
uppercase_countries = [country.upper() for country in list_country]
print("\nList of countries in uppercase:", uppercase_countries)

# List with countries that have more than 5 characters
long_countries = [country for country in list_country if len(country) > 5]
print("Countries with more than 5 characters:", long_countries)

# List with countries that contain the letter 'r'
countries_with_r = [country for country in list_country if 'r' in country.lower()]
print("Countries with the letter 'r':", countries_with_r)