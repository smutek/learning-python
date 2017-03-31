petNames = []

while True:
    print('Enter the name of pet number ' + str(len(petNames) + 1) + ' or enter nothing to stop.')

    name = input()

    if name == '':
        break

    petNames =  petNames + [name]

print('The pet names are: ')
for name in petNames:
    print(name)

print('You have ' + str(len(petNames)) + ' pets.')
