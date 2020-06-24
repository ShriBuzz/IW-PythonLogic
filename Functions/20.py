# Write a Python program to find intersection of two given arrays using
# Lambda.

arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [1, 4, 6, 8, 9]
intersect = list(filter(lambda x: x in arr1, arr2))

print(intersect)
