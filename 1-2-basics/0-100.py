# Sum of all numbers from 0 to 100

# set total to zero
total = 0
# for each number from 0 - 100
for number in range(101):
    # add the current total to the current number
    total = total + number
# print the answer
print(total)

# count from 0 to 100 by steps of 25
for i in range(0, 101, 25):
    print(i)
# count backwards from 100 to 0 in steps of 25
for i in range(100, 0, -25):
    print(i)
