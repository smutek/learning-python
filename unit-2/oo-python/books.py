class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '{}: {}'.format(self.title, self.author)


class Bookcase:
    def __init__(self, books=None):
        self.books = books

    @classmethod
    def create_bookcase(cls, book_list):
        books = []
        for title, author in book_list:
            books.append(Book(title, author))
        return cls(books)


class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __iter__(self):
        yield from self.pattern

    def __str__(self):
        output = []
        for blip in self:
            if blip == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)

    @classmethod
    def from_string(cls, string):
        split_string = str.split('-')
        output = []
        for blip in string:
            if blip == 'dot':
                output.append('.')
            else:
                output.append('_')
        return cls(output)



class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)