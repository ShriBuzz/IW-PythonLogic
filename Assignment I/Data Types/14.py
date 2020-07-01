# Write a Python function to create the HTML string with tags around the
# word(s).

def add_tags(tag, text):
    return('<'+tag+'>'+text+'</'+tag+'>')


print(add_tags('b', 'Python Tutorial'))
