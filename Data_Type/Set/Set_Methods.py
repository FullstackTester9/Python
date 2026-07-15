"""

"""

fruit_set = {'apple', 'mango', 'dragonfruit', 'pineapple', 'indian gooseberry'}
num_set_1 = {1, 4, 5, 8, 6, 3}
num_set_2 = {5, 8, 3, 7, 2, 9}

# add() will add new element to the set. 
# If element already exist then element will not be added to the set.
fruit_set.add('grapes')
print("After adding new element: ", fruit_set, end='\n\n')

# copy() copies the set.
fruit_set_copy = fruit_set.copy()
print("Copied set: ", fruit_set_copy, end='\n\n')

# clear()
fruit_set_copy.clear()
print("After clearing the set: ", fruit_set_copy, end='\n\n')

# difference(). Return a set that contains elements exist only in first set.
print("Values exist in first set but, not in second set: ", num_set_1.difference(num_set_2), end='\n\n')

# difference_upate(). Removes element that exist in both set.
num_set_1.difference_update(num_set_2)
print("After removal of elements that exist in both set: ", num_set_1, end='\n\n')

# discard(). Removes specified element from set.
print("Origial set: ", fruit_set, end='\n\n')
fruit_set.discard('grapes')
print("After discarding value from set: ", fruit_set, end='\n\n')

# intersection(). Returns a set that contain similarity between two or more set.
city_set_1 = {'Mumbai', 'Delhi', 'Kolkata', 'Chennai', 'Bhopal'}
city_set_2 = {'Jodhpur', 'Amritsar', 'Chennai', 'Lucknow', 'Nagpur', 'Bhopal'}

print("Intersection: ", city_set_1.intersection(city_set_2), end='\n\n')

# intersection_update(). Keeps element present in both set.
city_set_1.intersection_update(city_set_2)
print("Elements present in both set: ", city_set_1, end='\n\n')

# isdisjoint().Returns TRUE if none of the items are present in both set.
num_set_1 = {1, 4, 5, 8, 6, 3}
num_set_2 = {15, 81, 13, 7, 2, 9}
print("Are both set unique? ",num_set_1.isdisjoint(num_set_2), end='\n\n')

# issubset(). Returns TRUE if all elements are present in specified set.
num_set_1 = {1, 4, 5, 8, 6, 3}
num_set_2 = {5, 8, 3, 7, 2, 9}
print("Elements in both set are same?: ",num_set_1.issubset(num_set_2), end='\n\n')

# issuperset(). Returns TRUE if all elements in specified set are present in original set.
num_set_1 = {1, 4, 5, 8, 6, 3}
num_set_2 = {1, 4, 5, 8, 6, 3}
print("Elements in second set are same as first set?: ",num_set_1.issuperset(num_set_2), end='\n\n')

# pop(). Removes random item from set.
print("Before pop: ", num_set_2)
result = num_set_2.pop()
print("After pop: ", result, end='\n\n')

# remove(). Removes specified element from set.
fruit_set.remove('apple')
print("'apple' element removed: ", fruit_set, end='\n\n')

# symmetric_difference(). Returns set that contain elements that are not present in 
# either of the sets but not in both set.
num_set_1 = {1, 4, 5, 8, 6, 3}
num_set_2 = {5, 8, 3, 7, 2, 9}

#num_set_1.symmetric_difference(num_set_2)
print("Elements present on either of the sets:", num_set_1.symmetric_difference(num_set_2), end='\n\n')

# symmetric_difference_update(). Keeps only the elements found in either set but not in both set.
num_set_1 = {1, 4, 5, 8, 6, 3}
num_set_2 = {5, 8, 3, 7, 2, 9}

num_set_1.symmetric_difference_update(num_set_2)
print("Elements found in both sets: ", num_set_1, end='\n\n')

# union(). Returns a set that contains all elements from both sets.
num_set_1 = {1, 4, 5, 8, 6, 3}
num_set_2 = {5, 8, 3, 7, 2, 9}

print("Union of two sets: ", num_set_1.union(num_set_2), end='\n\n')

# update(). Update current set by adding elements from another set.
num_set_1.update(num_set_2)
print("Updating set 1: ", num_set_1)