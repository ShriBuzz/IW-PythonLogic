# Write a Python program to filter a list of integers using Lambda.

lis = [2,3,4,1,6]

even = list(filter(lambda x: x%2 == 0, lis))

print(even)