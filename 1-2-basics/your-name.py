name = ""
attempts = 0

while name != 'your name':
    print('Enter "your name"')
    name = input()
    attempts += 1

if attempts == 1:
    print('Great job, you got it on the first try!')
else:
    print('Thanks, but it took you ' + str(attempts) + ' tries to get it right.')

