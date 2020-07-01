# Write a Python program to sum all the items in a dictionary.

a = {1: 1, 2: 2, 3: 3, 4: 5}


def sum(val):
    x = 0
    for key, value in val.items():
        x += val[key]
    return x


print(sum(a))
