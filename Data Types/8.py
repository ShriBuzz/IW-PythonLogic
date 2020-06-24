# Write a Python function that takes a list of words and returns the length of the
# longest one.
string = (input("Enter string: "))
index = int(input("Enter index to remove: "))
print(string[:index-1]+string[index:])
