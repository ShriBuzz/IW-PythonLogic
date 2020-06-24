# Write a Python program to convert a tuple to a string.

def to_string(tup):
    str = ''.join(tup)
    return str


tup = ("a", "b", "c")
print(to_string(tup))
