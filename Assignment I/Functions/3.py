# Write a Python function to multiply all the numbers in a list.

list = [8, 2, 3, -1, 7]


def mul_list(list):
    temp = 1
    for i in list:
        temp = temp * i
    return temp


print(mul_list(list))
