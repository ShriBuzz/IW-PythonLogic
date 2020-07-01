# Write a Python function that takes a list of words and returns the length of the
# longest one.
words = ["A", "quick", "brown", "fox"]
print(max(len(word) for word in words))
