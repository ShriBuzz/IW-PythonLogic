# Write a Python program to remove an item from a tuple.

def removefrom(tup, element):
    my_list = list(tup)
    my_list.remove(element)
    return tuple(my_list)


tup = (1, 2, 3)
print(removefrom(tup, 2))
