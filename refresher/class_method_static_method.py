class ClassTest:
    def instance_method(self):
        print(f"Called instance method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls}")

    @staticmethod
    def static_method():
        print(f"Called static method")

test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)
ClassTest.class_method()
ClassTest.static_method()

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}>"

    @classmethod
    def hardcover(cls, name, weight):
        return cls(name, Book.TYPES[0], weight)

    @classmethod
    def paperback(cls, name, weight):
        return cls(name, Book.TYPES[1], weight)


print(Book.TYPES)

book = Book("Harry Potter", "hardcover", 1500)
print(book.name)
print(book)

hardcover_book = Book.hardcover("Harry Potter", 1500)
paperback_book = Book.paperback("Harry Potter", 1500)

print(hardcover_book)
print(paperback_book)
