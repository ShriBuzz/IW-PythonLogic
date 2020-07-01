# Write a Python program to count the occurrences of each word in a given
# sentence.

string = input()
counts = {}
words = string.split()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)
