import random


# Super Class
# The super() function lets us call a bit of code from the parent class
# inside our own class. This is really helpful when you need to override
# a method from the superclass, defining your own version, but keep the
# effects of the parent class's version of the code.
#
# For more about super() than you probably want to know at this point, check
# out this blog post from the excellent Raymond Hettinger.
# https://rhettinger.wordpress.com/2011/05/26/super-considered-super/


class Character:
    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)


class Thief(Character):
    def __init__(self, name, sneaky=True, **kwargs):
        super().__init__(name, **kwargs)
        self.sneaky = sneaky

    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))

    def hide(self, light_level):
        return self.sneaky and light_level < 10


class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)


class SortedInventory(Inventory):

    def add_item(self, item):
        super().add_item(item)
        self.slots.sort()
