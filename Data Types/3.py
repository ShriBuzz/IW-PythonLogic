# Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.
string = input('Enter string: ')
first = string[0]
new = first
for i in range(1, len(string)):
    if string[i] == first:
        new = new + '$'
    else:
        new = new + string[i]
print(new)
