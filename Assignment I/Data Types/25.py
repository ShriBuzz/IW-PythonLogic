# Write a Python program to check whether all dictionaries in a list are empty or
# not.

def is_emplty(list):
    for dict in list:
        if dict:
            return False
    return True


print(is_emplty([{}, {}, {}]))
print(is_emplty([{1, 2}, {}, {}]))
