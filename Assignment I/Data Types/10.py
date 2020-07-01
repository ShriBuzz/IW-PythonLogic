# Write a Python function that takes a list of words and returns the length of the
# longest one.
string = input()
temp = ''
for i in range(len(string)):
    if i % 2 == 0:
        temp = temp + string[i]
print(temp)
