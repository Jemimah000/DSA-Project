"""Library operations backed by a linked list and a hash index."""

from book import Book
from linked_list import LinkedList, Node


class Library:
    """Manage books stored in insertion order with average O(1) ID lookup."""

    def __init__(self):
        self.books = LinkedList()
        self.books_by_id: dict[int, Book] = {}

    def add_book(self, book: Book) -> None:
        """Add a book, rejecting an ID that is already indexed."""
        if book.book_id in self.books_by_id:
            raise ValueError(f"Book ID {book.book_id} already exists.")

        self.books.append(book)
        self.books_by_id[book.book_id] = book

    def remove_book(self, book_id: int) -> bool:
        """Remove a book from both the linked list and the hash index."""
        if book_id not in self.books_by_id:
            return False

        removed = self.books.remove_by_id(book_id)
        if removed:
            del self.books_by_id[book_id]
        return removed

    def search_by_id(self, book_id: int):
        """Return the book with ``book_id`` or ``None`` when it is missing."""
        return self.books_by_id.get(book_id)

    def issue_book(self, book_id: int) -> bool:
        """Issue an available book and report whether the operation succeeded."""
        book = self.search_by_id(book_id)
        if book is None or not book.available:
            return False

        book.available = False
        return True

    def return_book(self, book_id: int) -> bool:
        """Return an issued book and report whether the operation succeeded."""
        book = self.search_by_id(book_id)
        if book is None or book.available:
            return False

        book.available = True
        return True

    def count_books_recursive(self, node: Node | None) -> int:
        """Count nodes recursively, stopping when there is no node."""
        if node is None:
            return 0
        return 1 + self.count_books_recursive(node.next)

    def count_books(self) -> int:
        """Return the number of books currently stored."""
        return self.count_books_recursive(self.books.head)