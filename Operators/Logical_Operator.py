"""
This program demonstrate basic working of logical operators using truth table.
"""

print("Truth table for 'AND' operator.", end='\n\n')
print('True' '\t' 'False' '\t' 'Result')
print("----------------------")
print('True' '\t' 'True' '\t' , True and True)
print('True' '\t' 'False' '\t' , True and False)
print('False' '\t' 'True' '\t' , True and False)
print('False' '\t' 'False' '\t' , False and False, end='\n\n')

print("Truth table for 'OR' operator.", end='\n\n')
print('True' '\t' 'False' '\t' 'Result')
print("----------------------")
print('True' '\t' 'True' '\t' , True or True)
print('True' '\t' 'False' '\t' , True or False)
print('False' '\t' 'True' '\t' , True or False)
print('False' '\t' 'False' '\t' , False or False, end='\n\n')

print("Truth table for 'NOT' operator.", end='\n\n')
print('True\False' '\t' 'Result')
print("----------------------")
print("True" '\t''\t', not True)
print("False" '\t''\t', not False, end='\n\n')
