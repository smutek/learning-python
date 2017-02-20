# Collatz sequence


def collatz(number):
    if number % 2 == 0:
        # if the input is even divide by 2
        output = number / 2
    else:
        # if the input is odd multiply it by 3 and add 1
        output = number * 3 + 1
    # return the output
    return output

# get a number from the user
print('Enter a number...')
number = int(input())
# run the number through the function
result = collatz(number)
# set a counter
count = 1
# get the result
print(result)
# if the result is not 1
while result != 1:
    # run it through the function
    result = collatz(result)
    # increment the counter
    count += 1
    # print the result
    print(result)

# the number has reached 1- - print the result
print(result)
print(str(count) + ' steps.')
