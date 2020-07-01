# Write a function that reads a CSV file. It should return a list of
# dictionaries, using the first row as key names, and each subsequent
# row as values for those keys.
# For the data in the previous example it would return:
# [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
# 'John', 'address': '54 Love Ave', 'age': 21}]

file_list = []
key = []
values = []
d = {}
result = []


def create_dic():
    file = open('file.csv', 'r')
    for line in file:
        file_list.append(line.split(','))
    file.close()
    for i in range(0, 3):
        key.append(file_list[0][i])

    for i in range(1, len(file_list)):
        values.append(file_list[i])

    for j in range(0, 2):
        for i in range(0, 3):
            d[key[i]] = values[j][i]
        result.append(d)
    return result


print(create_dic())
