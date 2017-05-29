# make a subclass of list. Name it Liar.
# Override the __len__ method so that it always returns the wrong
# number of items in the list. For example, if a list has 5 members,
# the Liar class might say it has 8 or 2.
# You'll probably need super() for this.


class Liar(list):
    def __len__(self):
        real_length = super().__len__()
        return real_length + 10
