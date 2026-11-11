
"""Basic local checks for the Mini Library System. Run: python check.py"""

import tempfile
from pathlib import Path
from library_system import Book, Library


def main():
    library = Library()

    # Add books with the same title
    library.add_book(Book("Python", "Teacher", 2))
    library.add_book(Book("Python", "Teacher", 3))

    assert library.books["Python"].get_copies() == 5

    # Borrow a book
    library.borrow_book("Python")
    assert library.books["Python"].get_copies() == 4

    # Return a book
    library.return_book("Python")
    assert library.books["Python"].get_copies() == 5

    # Test JSON and CSV file creation
    with tempfile.TemporaryDirectory() as temp_dir:
        json_path = Path(temp_dir) / "library.json"
        csv_path = Path(temp_dir) / "library.csv"

        library.save_json(json_path)
        library.export_csv(csv_path)

        loaded = Library()
        loaded.load_json(json_path)

        assert loaded.books["Python"].get_copies() == 5
        assert csv_path.exists()

    # Check missing book error
    try:
        library.borrow_book("Missing book")
    except KeyError:
        pass
    else:
        raise AssertionError("Missing book should raise KeyError")

    print("All green")


if __name__ == "__main__":
    main()
