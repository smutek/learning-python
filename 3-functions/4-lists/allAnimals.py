animalNames = []

while True:
    print('Enter the name of animal ' + str(len(animalNames) + 1) + ', (or press enter to stop)')
    name = input()

    if name == '':
        break

    animalNames += [name]

print('The animal names are:')

for name in animalNames:
    print(' ' + name)
