def remember(thing):

    # open file
    file = open("database.txt", "a")
    # write thing to file
    file.write(thing + "\n")
    # close file
    file.close()

if __name__ == '__main__':
    remember(input("What should I remember?"))
