# Write a Python script to merge two Python dictionaries.

dic1 = {'a': 1, 'b': 2}
dic2 = {'c': 3, 'd': 4}


def merge(x, y):
    temp = dict(x)
    temp.update(y)
    return(temp)


print(merge(dic1, dic2))
