# Write a Python program to add an item in a tuple.

tup = (1, 5, 2)


def add_item(tup, new):
    new = tup + (new,)
    return new


print(add_item(tup, 8))
