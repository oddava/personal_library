import tabulate, json
from .models import Book


def pretty_print(data, header):
    print(tabulate.tabulate(data, header, "pretty"))


def dump_json(books):
    data = [{"title": book.title, "author": book.author, "year": book.year, "status": book.status} for book in books]
    with open("books.json", "w") as outfile:
        json.dump({"data": data}, outfile, indent=4)


def load_json(filename):
    with open(filename, "r") as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError:
            print(f"Error: {filename} contains invalid JSON. Returning an empty list.")
            return []

    books = [Book(book["title"], book["author"], book["year"], book["status"]) for book in data.get("data", [])]
    return books
