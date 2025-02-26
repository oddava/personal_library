import tabulate

class Book:
    def __init__(self, title, author, year, status):
        self.title = title
        self.author = author
        self.year = year
        self.status: bool = status

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.year}, {self.status})"

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def list_books(self):
        data = []
        for book in self.borrowed_books:
            data.append([book.title, book.author, book.year])
        header = ["Title", "Author", "Year"]
        print(tabulate.tabulate(data, header, "pretty"))