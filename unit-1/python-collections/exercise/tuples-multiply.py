# *args means the function takes a any number of arguments, even none
def multiply(*numbers):
    # start off with a base of 1 to multiply by
    product = 1
    # run through each number that was passed
    for number in numbers:
        # current number, product = current number, (current number * mult product)
        # The right side of the argument unpacks itself into the variables on the
        # left side. Number becomes the current product, and product becomes number * product
        # Ie. a, b = b, a - in this case a, b = b, a * b
        number, product = product, number * product

    return product

print(multiply(5,13,100, 46))