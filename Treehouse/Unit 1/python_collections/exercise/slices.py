# generate list of numbers 1-20
numbers = list(range(20))


# return first four items
def first_4(iterable):
    return iterable[0:4]


# return first four and lat four
def first_and_last_4(iterable):
    return iterable[0:4] + iterable[-4::]


# return only odd numbers
def odds(iterable):
    return iterable[1::2]


# return even numbers in reverse order
def reverse_evens(iterable):
    evens = iterable[::2]
    return evens[::-1]


# return a string with first half of letters lower case
# and second half upper case
def silly_case(string):
    half = int(len(string)//2)
    return string[:half].lower() + string[half:].upper()


print(first_4(numbers))
print(first_and_last_4(numbers))
print(odds(numbers))
print(reverse_evens(numbers))
print(silly_case('James Anton Smutek'))
