# Write a Python function that takes a list and returns a new list with unique
# elements of the first list.

x = [1, 2, 3, 3, 3, 3, 4, 5]


def no_repeat(x):
    return(list(set(x)))


print(no_repeat(x))
