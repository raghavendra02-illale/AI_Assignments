
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        self.borrowed = 0

    def show_book(self):
        print("Book Name:", self.title)
        print("Author:", self.author)
        print("Available Copies:", self.copies)
        print("Borrowed Copies:", self.borrowed)

    def borrow_book(self):
        if self.copies > 0:
            self.copies = self.copies - 1
            self.borrowed = self.borrowed + 1
            print("Book borrowed successfully!")
        else:
            print("No copies available.")

    def return_book(self):
        if self.borrowed > 0:
            self.copies = self.copies + 1
            self.borrowed = self.borrowed - 1
            print("Book returned successfully!")
        else:
            print("No borrowed copies to return.")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        copies = int(input("Enter number of copies: "))

        if copies <= 0:
            print("Enter at least one copy.")
            return

        if title in self.books:
            if self.books[title].author == author:
                self.books[title].copies += copies
                print("Book copies added successfully!")
            else:
                print("A book with this title already exists with a different author.")
        else:
            self.books[title] = Book(title, author, copies)
            print("Book added successfully!")

    def show_books(self):
        print("\nLibrary:", self.name)

        if len(self.books) == 0:
            print("No books available.")
        else:
            for book in self.books.values():
                print("--------------------")
                book.show_book()

    def borrow_book(self):
        title = input("Enter book title to borrow: ")

        if title in self.books:
            self.books[title].borrow_book()
        else:
            print("Book not found in this library.")

    def return_book(self):
        title = input("Enter book title to return: ")

        if title in self.books:
            self.books[title].return_book()
        else:
            print("Book not found in this library.")


# Create multiple libraries
libraries = {}

while True:
    print("\n===== LIBRARY MANAGEMENT =====")
    print("1. Create Library")
    print("2. Select Library")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter library name: ")

        if name in libraries:
            print("Library already exists.")
        else:
            libraries[name] = Library(name)
            print("Library created successfully!")

    elif choice == "2":
        name = input("Enter library name: ")

        if name not in libraries:
            print("Library not found.")
        else:
            library = libraries[name]

            while True:
                print("\n===== ", library.name, " =====")
                print("1. Add Book")
                print("2. Show Books")
                print("3. Borrow Book")
                print("4. Return Book")
                print("5. Back to Main Menu")

                option = input("Enter your choice: ")

                if option == "1":
                    library.add_book()

                elif option == "2":
                    library.show_books()

                elif option == "3":
                    library.borrow_book()

                elif option == "4":
                    library.return_book()

                elif option == "5":
                    break

                else:
                    print("Invalid choice.")

    elif choice == "3":
        print("Thank you for using the Library System!")
        break

    else:
        print("Invalid choice. Try again.")
