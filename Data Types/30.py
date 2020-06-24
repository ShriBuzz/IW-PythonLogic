# Write a Python script to check whether a given key already exists in a
# dictionary.

def key_in(dic, key):
    if key in dic:
        return "already exists"
    else:
        return "does not exists"


dic = {"a": 1, "b": 2}
print(key_in(dic, "x"))
print(key_in(dic, "b"))
