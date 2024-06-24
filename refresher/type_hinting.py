from typing import List

from refresher.class_composition import Book


def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)


print(list_avg([1, 2, 3, 4, 5]))


class Book():
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, page_count: int, book_type: str):
        self.name = name
        self.page_count = page_count
        self.book_type = book_type

    def __str__(self) -> str:
        return f"Book {self.name}"

    @classmethod
    def hardcover(cls, name: str, page_count: int) -> "Book":
        return cls(name, page_count, cls.TYPES[0])

    @classmethod
    def paperback(cls, name: str, page_count: int) -> "Book":
        return cls(name, page_count, cls.TYPES[1])


class Bookshelf:
    def __init__(self, *books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)} books."


print(Book.TYPES)

book = Book("Harry Potter", 456, "hardcover")
print(book.name)
print(book)

hardcover_book = Book.hardcover("Harry Potter", 234)
paperback_book = Book.paperback("Harry Potter", 456)

print(hardcover_book)
print(paperback_book)
