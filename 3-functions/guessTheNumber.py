import random
# grab a random number from 1-20
secretNumber = random.randint(1, 20)
print('I am thinking of a random number between 1 and 20')
# give the player 6 guesses, increment guessesTaken by 1 with each guess
for guessesTaken in range(1, 7):
    print('Take a guess...')
    guess = int(input())
    # if guess is less than the number
    if guess < secretNumber:
        print('Your guess is too low...')
    # if guess is more then the number
    elif guess > secretNumber:
        print('Your guess is too high...')
    else:
        # correct number was guessed
        break

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' tries.')
else:
    print('Nope, my number was ' + str(secretNumber))
