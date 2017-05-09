# reversing a string, see http://stackoverflow.com/a/931095

def stringcases(string):
    formats = (string.upper(), string.lower(), string.title(), string[::-1])
    return formats

print(stringcases("Row row row your boat down the stream"))
