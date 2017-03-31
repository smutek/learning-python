def spam(divideBy):
    try:
        return 42 / divideBy
    # exception for zero division errors
    except ZeroDivisionError:
        print('Error, invalid argument')

print(spam(2))
print(spam(12))
# will throw zero division error
print(spam(0))
print(spam(1))
