"""
This program demonstrate accessing set element by index. For this set is converted into a list.
One thing to note that set is unordered hence, you can not access set by its index.
Following programs output shows that every time you run the program item at index 0 is changed.
"""

fruit_set = {'apple', 'mango', 'dragonfruit', 'pineapple', 'indian gooseberry'}

# Original set
print("Original set: ", fruit_set, end='\n\n')

# Accessing set element index wise by converting set to list. 
set_to_list = list(fruit_set)
print("After converting set to list, list is: ", set_to_list)
print(f"Value at index '0' is: ", set_to_list[0], end='\n\n')
