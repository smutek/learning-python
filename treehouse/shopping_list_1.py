# make a list
shopping_list = []


# help messages
def help_messages():
    print("Enter 'DONE' to top adding items.")
    print("Enter 'SHOW' to list all items currently in the list.")
    print("Enter 'HELP' to show help.")


# show the list
def show_list(x):
    for list_item in x:
        print(list_item)

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
        show_list(shopping_list)
    elif new_item == "HELP":
        help_messages()
    else:
        # add to list
        shopping_list.append(new_item)

# print list
show_list(shopping_list)
