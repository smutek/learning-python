# take a list of dictionaries as input
def string_factory(dictionaries):
    # template w/ placeholders for new strings
    template = "Hi, I'm {name} and I love to eat {food}!"
    # an empty list to hold new strings
    strings = []
    # for each dictionary in the list of dictionaries
    for dictionary in dictionaries:
        # make a new string from the dictionary using our string template
        # ** unpacks the dictionary and matches values up to the keys in
        # the template
        string = template.format(**dictionary)
        # append the new string to the list of strings
        strings.append(string)
    # return strings
    return strings

values = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]

print(string_factory(values))
# outputs:
# ["Hi, I'm Michelangelo and I love to eat PIZZA!", "Hi, I'm Garfield and I love to eat lasagna!"]
