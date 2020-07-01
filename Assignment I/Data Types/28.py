# Write a Python script to add a key to a dictionary.

def add(dict, key, value):
    dict[key] = value
    return(dict)


dict = {0: 10, 1: 20}
print(add(dict, 2, 30))
