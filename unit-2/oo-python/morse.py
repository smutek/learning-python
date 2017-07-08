# Let's use __str__ to turn Python code into Morse code! OK, not really,
# but we can turn class instances into a representation of their Morse code
# counterparts.
# I want you to add a __str__ method to the Letter class that loops through the
# pattern attribute of an instance and returns "dot" for every "." (period) and
# "dash" for every "_" (underscore). Join them with a hyphen.


class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        items = []
        for char in self.pattern:
            if char == ".":
                items.append("dot")
            if char == "_":
                items.append("dash")

        morse = "-".join(items)

        return morse


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)


foo = S

print(foo)