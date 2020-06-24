# Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.
val1 = input()
val2 = input()
temp1 = val2[:2] + val1[2:]
temp2 = val1[:2] + val2[2:]
temp = temp1 + " " + temp2
print(temp)
