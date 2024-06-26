class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."

shelf = Bookshelf(30)

class Book():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book = Book("Python")
book2 = Book("Python2")

bookshelf = Bookshelf(book, book2)
print(bookshelf)