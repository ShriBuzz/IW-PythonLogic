# Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).

string = "red, white, black, red, green, black"
seperate = string.split(",")
remove_repeat = list(set(seperate))
sorted_list = sorted(remove_repeat)
print(", ".join(sorted_list))
