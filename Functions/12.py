# Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number

import random


def rand_mul(n):
    return n*random.randint(1, 10)


print(rand_mul(3))
