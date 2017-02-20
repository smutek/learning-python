def spam():
    global eggs
    eggs = 'spam' # set global

def bacon():
    eggs = 'bacon'

def ham():
    print(eggs)

eggs = 42
spam()
print(eggs)
