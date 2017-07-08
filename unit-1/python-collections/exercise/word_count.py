# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.


def word_count(string):
    # create and empty dictionary
    dictionary = {}
    # convert string to lower case and break into words
    words = string.lower().split()
    # iterate through the words
    for word in words:
        if word not in dictionary:
            # add the word if it isn't in the dictionary
            dictionary[word] = 1
        else:
            # increment the value if the word is in the dictionary
            dictionary[word] += 1

    # return dictionary
    return dictionary

string = "Hello I am a brown elephant and I like the color brown and I like saying hello"

print(word_count(string))
