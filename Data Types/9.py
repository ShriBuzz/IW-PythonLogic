# Write a Python function that takes a list of words and returns the length of the
# longest one.
string = input()
new = string[-1:] + string[1:len(string)-1] + string[:1]
print(new)
