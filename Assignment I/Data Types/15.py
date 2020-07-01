# Write a Python function to insert a string in the middle of a string.
# Sample function and result

def insert_string_middle(bracket, string):
    return(bracket[:int(len(bracket)/2)] + string + bracket[int(len(bracket)/2):])


print(insert_string_middle('[[]]', 'Python'))
print(insert_string_middle('{{}}', 'PHP'))
