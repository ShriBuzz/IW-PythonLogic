# Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are square of keys

def make_dic(num1, num2):
    dic = {}
    for i in range(num1, num2+1):
        dic[i] = i*i
    return dic


print(make_dic(1, 15))
