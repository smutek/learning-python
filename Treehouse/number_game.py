# import random module from std lib
import random


def game():

    # gen a random number between 1-10
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        try:
            # get a number guess from player
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("That isn't a number!")
        else:
            # compare 2 numbers
            if guess == secret_num:
                print("Good job! My number was {}".format(secret_num))
                break
            elif guess < secret_num:
                print("Wrong, my number is higher than {}".format(guess))
            else:
                # print hit or miss
                print("Wrong, my number is lower than {}.".format(guess))
            guesses.append(guess)
    else:
        print("You blew it, my number was {}".format(secret_num))
    play_again = input("Do you want to play again? Y/n ")
    if play_again.lower() != "n":
        game()
    else:
        print("Take care!")

game()
