# Write a Python program to find if a given string starts with a given character
# using Lambda.

string = 'happy'

check = lambda x: True if x.startswith('h') else False

print(check(string))