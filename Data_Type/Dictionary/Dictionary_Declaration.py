empty_dict = {}

dict_empty_constructor = ()

dict_constructor_data = dict(country='India', code='+91')

dict_with_list = [('brand', 'Bajaj'), ('model', 'Pulsar'), ('Year', 2003)]

dict_car = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : 1964
} 

# Declaring empty dictionary
print("Empty dictionary: ", empty_dict, end='\n\n')

# Declaring empty dictionary with constructor
print("Empty dictionary with constructor: ", dict_empty_constructor, end='\n\n')

# Declaring dictionary constructor with data
print("Dictionary constructor with data: ", dict_constructor_data, end='\n\n')

# Declaring dictonary with tuple inside list.
print("Dictionary with tuple inside list: ", dict(dict_with_list), end='\n\n')

# Pairing two list to create a dictionary.
keys = ['emp_id', 'name', 'detp']
values = ['EMP001', 'John', 'Accounts']
pair_two_list = dict(zip(keys, values))
print("Pairing two list to create a dictionary: ",pair_two_list, end='\n\n')

# Dictionary with data
print("Dictionary with data: ",dict_car, end='\n\n')