class ReversedStr(str):
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self


# quiz
class Double(int):
    def __new__(*args, **kwargs):
        instance = int.__new__(*args, **kwargs)
        return instance * 2
