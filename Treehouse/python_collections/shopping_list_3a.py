import os

# make a list
shopping_list = []


# clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# help messages
def help_messages():
    clear_screen()
    print("Enter 'DONE' to top adding items.")
    print("Enter 'SHOW' to list all items currently in the list.")
    print("Enter 'HELP' to show help.")
    print("Enter 'REMOVE' to delete an item.")


# show the list
def show_list():
    clear_screen()
    print('Here is your list.')

    for index, item in enumerate(shopping_list, start=1):
        print('{}. {}'.format(index, item))

    print('=' * 10)


# remove items from the list
def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove?\n> ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass

    show_list()


# add to list
def add_to_list(item):
    show_list()

    if len(shopping_list):
        position = input("Where should I add? {}?\n"
                         "Press ENTER to add to the end of the list\n"
                         ">".format(item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position - 1, item)
    else:
        shopping_list.append(item)

    show_list()


# print instructions
help_messages()
print("What should we get from the store?")

# ask for new items
while True:
    new_item = input("> ")

    # be able to quit
    if new_item.upper() == "DONE" or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == "SHOW":
        show_list()
        continue
    elif new_item.upper() == "HELP":
        help_messages()
        continue
    elif new_item.upper() == "REMOVE":
        remove_from_list()
        continue

    # add to list
    add_to_list(new_item)

# print list
show_list()
