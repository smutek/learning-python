# Create a function named combiner that takes a single argument,
# which will be a list made up of strings and numbers.

# Return a single string that is a combination of all of the strings
# in the list and then the sum of all of the numbers. For example, with
# the input ["apple", 5.2, "dog", 8], combiner would return "appledog13.2".


def combiner(input=[]):
    # vars
    strings = ""
    ints = 0

    for item in input:
        # first check to see if this is a number
        if isinstance(item, (int, float)):
            # increment the ints variable
            ints = ints + item
        # if this is a string
        if isinstance(item, str):
            # join the current string to the existing
            strings = strings + item

    output = strings + str(ints)
    return output


print(combiner(["apple", 5.2, "dog", 8]))
