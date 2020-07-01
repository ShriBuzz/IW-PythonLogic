# Write a Python program to multiply all the items in a dictionary.

a = {1: 2, 2: 3, 3: 2}


def mul(val):
    x = 1
    for key, value in val.items():
        x *= val[key]
    return x


print(mul(a))
