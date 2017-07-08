import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

# Match matches from the beginning of the string
# Use search is matching anywhere else in the string
# the r character stands for "raw" string, which means
# something is more raw or some shit
# print(re.match(r'Love', data))
# print(re.search(r'Kenneth', data))

# print(re.findall(r'\(?\d{3}\)?-?\s? \d{3}-\d{4}', data))
# print(re.findall(r'\w*, \w+', data))


# the first chink of this set, up till the @ symbol, marks
# the first portion of the email address - if says we can
# have -'s, characters \w numbers \d and dots
# []+ searches for 1 or more of whatever is inside []

# print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))

# find treehouse
# the \b \b (word boundaries) is saying, find the stuff in the []'s, but only
# where it appears in between word boundaries. The {9} is saying the string
# should be 9 characters long
# print(re.findall(r'\b[trehous]{9}\b', data, re.IGNORECASE))


# print(re.findall(r'\b@[-\w\d.]*'  # First a word boundary, an @, and then any number of chars
#                 r'[^giv\t]+'  # Ignore 1+ instances of 'g', 'o', or 'v' and a tab
#                 r'\b',  # match another word boundary
#                 data, re.VERBOSE|re.IGNORECASE))

# print(re.findall(
#    r'\b[-\w]+,'  # First a word boundary, an @, and then any number of chars
#    r'\s'  # Find 1 white space
#    r'[-\w ]+'  # 1+ hyphens and chars and explicit spaces
#    r'[^\t\n]',  # ignore tabs and new lines
#    data, re.X))

line = re.compile(r''
                  r'^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t'  # Last & First names
                  r'(?P<email>[-\w\d.+]+@[-\w\d.]+)\t'  # Email
                  r'(?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t'  # Phone
                  r'(?P<job>[\w\s]+,\s[\w\s.]+)\t?'  # Job & Company
                  r'(?P<twitter>@[\w\d]+)?$'  # Twitter
                  r'', re.X | re.M)

#print(line.search(data).groupdict())

# for match in line.finditer(data):
#    print('{first} {last} <{email}>'.format(**match.groupdict()))


string = '''Stewart Pinchback, Pinckney Benton: 18
Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22'''

players = re.search(r''
                    r'^(?P<last_name>[\w ]+),\s'  # last_name
                    r'(?P<first_name>[\w ]+):\s'  # first_name
                    r'(?P<score>[\d]+)$'  # score
                    r'', string, re.X | re.M)

print(players.groupdict())
