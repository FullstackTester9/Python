str = "Welcome to the world of Python programming!"
name = "Python"
year = 1991
maker = "Guido van Rossum"
price = 48.618
contact = "1234567890"
email = "abc_123"
join_words = ['Python', 'is', 'easy', 'to', 'learn.']


# Capitalizes the first character of the string
print("Capitalized: ", str.capitalize(), end='\n\n')  

# Converts the string to lowercase for caseless matching
print("Casefolded: ", str.casefold(), end='\n\n')  

# Centers the string within a specified width
print("Centered: ", str.center(50, '*'), end='\n\n') 

# Counts the occurrences of a substring in the string
print("Occurrences of 'o': ", str.count('o'), "found in the string.", end='\n\n')

# Encodes the string into bytes using UTF-8 encoding
print("Encoded: ", str.encode(), end='\n\n')  

# Checks if the string ends with a specified suffix
print("Ends with 'programming!': ", str.endswith('programming!'), end='\n\n')  

# Expands tabs in the string to spaces
print("Expanded Tabs: ", str.expandtabs(), end='\n\n')  

# Finds the index of the first occurrence of a substring in the string
print("Index of 'Python': ", str.find('Python'), "is the index of 'Python' in the string.", end='\n\n')

# Formatting the string using f-strings
print(f"{name} was developed by {maker} in {year}.", end='\n\n')

# Formatting the string using format() method
print("{} was developed by {} in {}." .format(name, maker, year), end='\n\n')  

# Positional formatting using format() method
print("{0} was developed by {1} in {2}." .format(name, maker, year), end='\n\n')

# Formatting floats to two decimal places using format() method
print("The price of {} is ${:.2f}." .format(name, price), end='\n\n')

# First occurrence of a substring in the string using index() method
print("First occurrence of 'o' is at index ", str.index('o'), " in the string.", end='\n\n')

# Checks if the string is alphanumeric (contains only letters and numbers)
print("Is the string alphanumeric? ", str.isalnum(), end='\n\n')

# Checks if the string contains only alphabetic characters
print("Does the string contain only alphabetic characters? ", str.isalpha(), end='\n\n')

# Checks if the string contains only decimal characters
print("Is the contact number a decimal number? ", contact.isdecimal(), end='\n\n')

# Checks if the string contains only digits
print("Is the contact number a digit?: ", contact.isdigit(), end='\n\n')

# Checks if the string is a valid identifier (e.g., variable name)
print("Is the email a valid identifier?", email.isidentifier(), end='\n\n')

# Checks if the string is in lowercase
print("Is the string in lowercase? ", str.islower(), end='\n\n')

# Checks if the string contains only numeric characters
print("Is the contact number numeric?: ", contact.isnumeric(), end='\n\n')

# Checks if the string contains only printable characters
print("Is the email printable?", email.isprintable(), end='\n\n')

# Checks if the string contains only whitespace characters
print("Is the string containing only whitespace?", str.isspace(), end='\n\n')

# Checks if the string is in title case (each word starts with an uppercase letter)
print("Is the string in title case?", str.istitle(), end='\n\n')

# Checks if the string is in uppercase
print("Is the string in uppercase?", str.isupper(), end='\n\n')  

# Joins the list of words into a single string
print("Joined string: ", " ".join(join_words), end='\n\n') 

# Left-justifies the string within a specified width
print("Left-justified string: ", str.ljust(70, '*'), end='\n\n')  

# Converts the string to lowercase
print("Lowercase maker: ", maker.lower(), end = '\n\n')

# Removes leading characters from the string
print("String after removing leading '1': ", contact.lstrip('1'), end='\n\n') 

# maketranslation: Replaces specified characters in the string based on a translation table
print("Translation table: ", name.maketrans('aeiou', '12345'), end='\n\n')

# Partitions the string into three parts based on a specified separator
print("Partitioned string: ", str.partition('of'), end='\n\n')

# Replaces occurrences of a substring with another substring
print("Email with replaced underscore: ", email.replace('_', '@'), end='\n\n')

# Finds the index of the last occurrence of a substring in the string
print("Index of last occurrence of 'm': ", str.rfind('m'), end='\n\n')

# Finds the index of the last occurrence of a substring in the string, raises ValueError if not found
print("Index of last occurrence of 'o': ", str.rindex('o'), end='\n\n')

# Right-justifies the string within a specified width
print("Right-justified string: ", str.rjust(70, '*'), end='\n\n')  

# Partitions the string into three parts based on the last occurrence of a specified separator
print("Right-partitioned string: ", str.rpartition('of'), end='\n\n')

# Splits the string into a list of substrings from the right, with a maximum of 3 splits
print("Right-split string: ", str.rsplit(' ', 6), end='\n\n')

# Removes trailing characters from the string
print("String after removing trailing '!': ", str.rstrip('!'), end='\n\n')  

# Splits the string into a list of substrings based on whitespace
print("Split string: ", str.split(' '), end='\n\n')  

# Splits the string into a list of lines
print("Split lines: ", str.splitlines(), end='\n\n') 

# Checks if the string starts with a specified prefix
print("Starts with 'Welcome': ", str.startswith('Welcome'), end='\n\n')  

# Removes leading and trailing whitespace from the string
print("String after removing leading and trailing whitespace: ", str.strip(), end='\n\n')  

# Swaps the case of each character in the string
print("String with swapped case: ", name.swapcase(), end='\n\n')  

# Converts the string to title case
print("String in title case: ", str.title(), end='\n\n') 

# Translates the string using a translation table
str_2 = name.maketrans('P', 'J')
print("String after translation: ", name.translate(str_2), end='\n\n')

# Converts the string to uppercase
print("String in uppercase: ", str.upper(), end='\n\n')  

# Pads the string with zeros on the left to a specified width
print("String with zero padding: ", str.zfill(70), end='\n\n') 