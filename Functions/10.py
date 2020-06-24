# Write a Python program to print the even numbers from a given list.

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_even(x):
    new_list = []
    for i in x:
        if i % 2 == 0:
            new_list.append(i)
    return new_list


print(get_even(x))
