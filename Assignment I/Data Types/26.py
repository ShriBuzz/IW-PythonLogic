# Write a Python program to insert a given string at the beginning of all items in
# a list.

list = [1, 2, 3, 4]
string = 'emp'
for i in range(len(list)):
    list[i] = string + str(list[i])
print(list)
