# Write a Python program to count the number of characters (character
# frequency) in a string. Sample String : google.com'
val = "google.com"
count = {}
for letter in val:
    if letter not in count:
        count[letter] = 1
    else:
        count[letter] = count[letter] + 1
print(count)
