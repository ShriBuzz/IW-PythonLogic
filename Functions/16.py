# Write a Python program to square and cube every number in a given list of
# integers using Lambda.

lis = [1,2,3,4,5]

square = list(map(lambda x: x**2, lis))

print(square)

cube = list(map(lambda x: x**3, lis))

print(cube)
