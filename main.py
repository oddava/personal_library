from library import User, LibraryManager

library = LibraryManager()
library.add_book("Sherlock Holmes", "Arthur Conan Doyle", 1892)

library.load_books()

while True:
    print("Greetings, welcome to my personal library!\n")
    name = input("What is your name? ")
    user = User(name)

    # Menu
    while True:
        cmd = input("What would you like to do? \n"
                    "1. All books\n"
                    "2. Borrow book\n"
                    "3. Return book\n"
                    "4. Borrowed books\n"
                    "5. Exit\n")

        match cmd:
            case "1":
                library.list_books()
                cn = input("Press any key to continue... ")
                if cn:
                    continue
            case "2":
                name = input("Please enter the book name: ")
                for book in library.books:
                    if book.title.lower() == name.lower() and book.status:
                        library.borrow_book(user, book.title)
                        print("Successfully borrowed " + book.title)
                        library.save_books()
                        break
                    if not book.status:
                        print("Book " + book.title + " not found.")
                    print("Invalid book name.")

                    cn = input("Press any key to continue... ")
                    if cn:
                        continue
            case "3":
                b_name = input("Please enter the book name: ")
                for book in library.books:
                    if book.title.lower() == b_name.lower():
                        library.return_book(user, book.title)
                        print("Successfully returned " + book.title)
                        library.save_books()
                        break
                    print("Something went wrong.")

                    cn = input("Press any key to continue... ")
                    if cn:
                        continue
            case "4":
                user.list_books()
                cn = input("Press any key to continue... ")
                if cn:
                    continue
            case "5":
                print("Thank you for using my personal library.")
                exit()
            case _:
                print("Invalid command.")