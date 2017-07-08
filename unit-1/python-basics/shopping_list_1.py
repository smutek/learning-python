# make a list
shopping_list = []


# help messages
def help_messages():
    print("Enter 'DONE' to top adding items.")
    print("Enter 'SHOW' to list all items currently in the list.")
    print("Enter 'HELP' to show help.")


# show the list
def show_list():
    for item in shopping_list:
        print(item)


# add to list
def add_to_list(new_item):
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))


# print instructions
help_messages()
print("What should we get from the store?")

# ask for new items
while True:
    new_item = input("> ")

    # be able to quit
    if new_item == "DONE":
        break
    elif new_item == "SHOW":
        show_list()
        continue
    elif new_item == "HELP":
        help_messages()
        continue
    # add to list
    add_to_list(new_item)

# print list
show_list()
