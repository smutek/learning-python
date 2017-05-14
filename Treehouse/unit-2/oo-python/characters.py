import random


class Thief:

    sneaky = True

    # constructor! - name, sneaky, and a dictionary of
    # user supplied key value pairs ( key word args (kwargs))
    def __init__(self, name, sneaky=True, **kwargs):
        self.name = name
        self.sneaky = sneaky

        for key, value in kwargs.items():
            # 3 args, the instance to st on (self)
            # the attribute to set, and the value to give it
            # This is helpful because we don't know the names
            # of the attributes that the user may supply
            setattr(self, key, value)

    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))

    def hide(self, light_level):
        return self.sneaky and light_level < 10


# quiz question
class RaceCar:
    def __init__(self, color, fuel_remaining, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining

        for key, value in kwargs.items():
            setattr(self, key, value)

    laps = 0

    def run_lap(self, length):
        self.laps += 1

        self.fuel_remaining = self.fuel_remaining - length * 0.125