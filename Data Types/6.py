# Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.

# Not complete
string = 'The lyrics is not that poor!'
first = "not"
second = "poor"
replace = "good"
list = string.split()
temp = ""
for i in range(len(list)):
    if(list[i] == first):
        temp = temp + " poor"
        break
    else:
        temp = temp + " " + list[i]
print(temp)
