from .models import Book
from .utils import pretty_print, dump_json, load_json

class LibraryManager:
    books: list = []

    @staticmethod
    def add_book(title, author, year):
        LibraryManager.books.append(Book(title, author, year, True))
        LibraryManager.save_books()

    @staticmethod
    def borrow_book(user, title):
        for book in LibraryManager.books:
            if book.title == title:
                user.borrowed_books.append(book)
                book.status = False
                break

    @staticmethod
    def return_book(user, title):
        for book in LibraryManager.books:
            if book.title == title:
                user.borrowed_books.remove(book)
                book.status = True
                break

    @staticmethod
    def list_books():
        data = []
        for book in LibraryManager.books:
            data.append([book.title, book.author, book.year, book.status])
        header = ["Title", "Author", "Year", "Status"]
        pretty_print(data, header)

    @staticmethod
    def save_books():
        dump_json(LibraryManager.books)
        print(f"Saved {len(LibraryManager.books)} books")

    @staticmethod
    def load_books():
        books = load_json("books.json")
        LibraryManager.books = books
        print(f"Loaded {len(books)} books")