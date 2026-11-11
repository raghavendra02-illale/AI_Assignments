
import csv
import json
from pathlib import Path


class Book:
    def __init__(self, title, author, copies=1):
        if not title.strip():
            raise ValueError("Please enter a book title.")

        if copies < 0:
            raise ValueError("Number of copies cannot be negative.")

        self.title = title.strip()
        self.author = author.strip()
        self.__copies = int(copies)

    def show_copies(self):
        return self.__copies

    def increase_copies(self, count=1):
        if count <= 0:
            raise ValueError("Enter a valid number of copies.")
        self.__copies += count

    def issue_book(self):
        if self.__copies == 0:
            return False

        self.__copies -= 1
        return True

    def receive_book(self):
        self.__copies += 1

    def get_details(self):
        return {
            "title": self.title,
            "author": self.author,
            "copies": self.__copies
        }

    def __str__(self):
        return f"Book: {self.title} | Author: {self.author} | Available: {self.__copies}"


class Library:
    def __init__(self):
        self.book_collection = {}

    def insert_book(self, book):
        if book.title in self.book_collection:
            old_book = self.book_collection[book.title]

            if old_book.author != book.author:
                raise ValueError("This title already belongs to another author.")

            if book.show_copies() > 0:
                old_book.increase_copies(book.show_copies())

        else:
            self.book_collection[book.title] = book

    def display_books(self):
        if not self.book_collection:
            print("No books are available in the library.")
            return

        for book in self.book_collection.values():
            print(book)

    def issue_book(self, title):
        selected_book = self.book_collection.get(title)

        if selected_book is None:
            raise KeyError(f"Book is not available: {title}")

        if not selected_book.issue_book():
            raise ValueError(f"All copies have been borrowed: {title}")

        return selected_book

    def receive_book(self, title):
        selected_book = self.book_collection.get(title)

        if selected_book is None:
            raise KeyError(f"Book not found: {title}")

        selected_book.receive_book()
        return selected_book

    def save_data(self, filename="library.json"):
        with open(filename, "w", encoding="utf-8") as file:
            data = [book.get_details() for book in self.book_collection.values()]
            json.dump(data, file, indent=4)

    def load_data(self, filename="library.json"):
        file_path = Path(filename)

        if not file_path.exists():
            raise FileNotFoundError(filename)

        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        self.book_collection = {}

        for item in data:
            book = Book(item["title"], item["author"], item["copies"])
            self.insert_book(book)

    def save_csv(self, filename="library.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["title", "author", "copies"]
            )

            writer.writeheader()

            for book in self.book_collection.values():
                writer.writerow(book.get_details())

    @staticmethod
    def read_file(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()


def run_library():
    library = Library()

    library.insert_book(Book("Python Basics", "A. Teacher", 2))
    library.insert_book(Book("Learning OOP", "B. Teacher", 1))
    library.insert_book(Book("Python Basics", "A. Teacher", 1))

    print("Library Book Details:")
    library.display_books()

    try:
        library.issue_book("Python Basics")
        library.receive_book("Python Basics")

    except (KeyError, ValueError) as error:
        print("Operation error:", error)

    library.save_data()
    library.save_csv()

    print("\nLibrary information saved successfully.")

    new_library = Library()
    new_library.load_data()

    print("\nBooks loaded from JSON file:")
    new_library.display_books()


if __name__ == "__main__":
    try:
        run_library()

    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        print("Error occurred:", error)
