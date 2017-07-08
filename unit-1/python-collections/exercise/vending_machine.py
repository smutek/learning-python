sodas = ['Pepsi', 'Cherry Coke', 'Sprite']
chips = ['Doritos', 'Fritos']
candy = ['Snickers', 'M&Ms', 'Twizzlers']

while True:

    choice = input('Would you like a SODA, CHIPS, or CANDY?').lower()

    try:
        if choice == 'soda':
            snack = sodas.pop()
        elif choice == 'chips':
            snack = chips.pop()
        elif choice == 'candy':
            snack = candy.pop()
        else:
            print('Sorry, that was not a choice')
            continue

    except IndexError:
        print('Sorry, no more {}'.format(choice))

    else:
        print("Here's your {}: {}".format(choice, snack))
