"""
Main Application Entry Point

"""

from book import Book
from library import Library
from title_search import search_by_title


def display_menu():
    """Display the library management menu."""
    print("\n" + "=" * 45)
    print("      LIBRARY MANAGEMENT SYSTEM MENU")
    print("=" * 45)
    print("1. Add Book")
    print("2. Remove Book by ID")
    print("3. Search Book by ID")
    print("4. Search Book by Title")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Display All Books")
    print("8. Count Books (Recursive)")
    print("9. Exit")
    print("=" * 45)


def get_book_id():
    """Get a valid numeric Book ID from the user."""
    while True:
        try:
            return int(input("Enter Book ID: ").strip())
        except ValueError:
            print("Invalid Book ID! Please enter a number.")


def add_book(library):
    """Add a new book to the library."""
    try:
        book_id = get_book_id()
        title = input("Enter Book Title: ").strip()
        author = input("Enter Author Name: ").strip()

        book = Book(book_id, title, author)
        library.add_book(book)

        print("Book added successfully!")

    except (ValueError, TypeError) as error:
        print(f"Error: {error}")


def remove_book(library):
    """Remove a book using its ID."""
    book_id = get_book_id()

    if library.remove_book(book_id):
        print("Book removed successfully!")
    else:
        print("Book not found.")


def search_book_by_id(library):
    """Search for a book using its ID."""
    book_id = get_book_id()

    book = library.search_by_id(book_id)

    if book is not None:
        print("\nBook Found:")
        print(book)
    else:
        print("Book not found.")


def search_book_by_title(library):
    """Search for books using their title."""
    title = input("Enter Book Title: ").strip()

    books = list(library.books)

    matches = search_by_title(books, title)

    if matches:
        print(f"\nFound {len(matches)} book(s):")
        for book in matches:
            print(book)
    else:
        print("No books found with that title.")


def issue_book(library):
    """Issue a book using its ID."""
    book_id = get_book_id()

    book = library.search_by_id(book_id)

    if book is None:
        print("Book not found.")
    elif not book.available:
        print("Book is already issued.")
    else:
        library.issue_book(book_id)
        print("Book issued successfully!")


def return_book(library):
    """Return a book using its ID."""
    book_id = get_book_id()

    book = library.search_by_id(book_id)

    if book is None:
        print("Book not found.")
    elif book.available:
        print("Book is already available.")
    else:
        library.return_book(book_id)
        print("Book returned successfully!")


def display_all_books(library):
    """Display all books in the library."""
    books = list(library.books)

    if not books:
        print("Library is empty.")
        return

    print("\nAll Books:")
    print("-" * 70)

    for book in books:
        print(book)

    print("-" * 70)


def count_books(library):
    """Display the total number of books using recursion."""
    total = library.count_books()
    print(f"Total number of books: {total}")


def main():
    """Run the Library Management System."""
    library = Library()

    while True:
        display_menu()

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            add_book(library)

        elif choice == "2":
            remove_book(library)

        elif choice == "3":
            search_book_by_id(library)

        elif choice == "4":
            search_book_by_title(library)

        elif choice == "5":
            issue_book(library)

        elif choice == "6":
            return_book(library)

        elif choice == "7":
            display_all_books(library)

        elif choice == "8":
            count_books(library)

        elif choice == "9":
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please select an option between 1 and 9.")


if __name__ == "__main__":
    main()