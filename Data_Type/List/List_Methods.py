list_players = ['Rohit', 'Surya', 'Jaspreet', 'Sanju', 'Rohit']

# Original list
print("Original list", list_players)

# Adding new element to the end of list
list_players.append("Williamson")
print("List with new element: ", list_players)

# Clearing list using clear method which return empty list
#list_players.clear()
#print("Cleared list: ", list_players)

# Copying list which will return copy of specified list.
list_players.copy()
print("", list_players)

# Counting occurances of specified value form list 
player_count = list_players.count('Rohit')
print("Count of player name 'Rohit' is: ", player_count)

# New list is added to the end of existing list
extra_players = ['Shreyas', 'Ravi', 'Rishab']
list_players.extend(extra_players)
print("Extended list: ", list_players)


# Returns index of first occurance of specified value
print("Index of 'Sanju' is: ", list_players.index('Sanju'))

# Inserting new value at specified index
list_players.insert(5, 'Gill')
print(list_players)

# Rmoving last element from list
player_removed = list_players.pop()
print("Popped player: ", player_removed)
print("Updated list: ", list_players)

# First occurance of specified value is removed 
list_players.remove('Rohit')
print("After removing first occurance of 'Rohit': ", list_players)

# Reversing list using reverse method
list_players.reverse()
print("Reversed list: ", list_players)

# Sorting list in ascending order(default)
list_players.sort()
print("Sorted list: ", list_players)