"""
This program demonstrate working of binaryoperators.
Binary operators are: &, |, ^, ~, <<, >>
Use: Compares binary numbers.
"""

var_a = 10
var_b = 4

print("OPERATOR \t NAME \t\t CODE \t\t RESULT")
print("--------------------------------------------------------")
print(f"& \t\t AND \t\t {var_a} & {var_b} \t", var_a & var_b)
print(f"| \t\t OR \t\t {var_a} & {var_b} \t", var_a | var_b)
print(f"^ \t\t XOR \t\t {var_a} & {var_b} \t", var_a ^ var_b)
print(f"~ \t\t NOT \t\t {var_a} \t\t", ~var_a)
print(f"<< \t\t Left Shift \t {var_a} & {var_b} \t", var_a << var_b)
print(f"& \t\t Roght Shift \t {var_a} & {var_b} \t", var_a >> var_b)
print("--------------------------------------------------------")


