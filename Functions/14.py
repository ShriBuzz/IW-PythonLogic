# Write a Python program to sort a list of dictionaries using Lambda.

sort = lambda dic: sorted(dic, key=lambda x: x['a'])
lis = [{'a':2,'b': 5}, {'a':6,'b': 2},{'a':1,'b': 0},{'a':3,'b': 4},]

print(sort(lis))