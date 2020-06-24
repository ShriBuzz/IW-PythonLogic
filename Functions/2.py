# Write a Python function to sum all the numbers in a list.

list = [8, 2, 3, 0, 7]


def sum_list(list):
    temp = 0
    for i in list:
        temp = temp + i
    return temp


print(sum_list(list))
