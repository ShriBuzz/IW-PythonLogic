# Write a Python program to check whether a given string is number or not
# using Lambda.

string = '128'

is_num = lambda x: True if x.isnumeric() else False

print(is_num(string))