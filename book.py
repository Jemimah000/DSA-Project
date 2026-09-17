"""
Book Model and Data Structure
Contributor: Abhishek
"""

from dataclasses import dataclass


@dataclass
class Book:
    """
    Represents a book in the library system.

    Attributes:
        book_id (int): Unique positive integer identifier for the book.
        title (str): Non-empty title of the book.
        author (str): Non-empty author of the book.
        available (bool): Availability status of the book (defaults to True).
    """
    book_id: int
    title: str
    author: str
    available: bool = True

    def __post_init__(self):
        # Validate book_id
        if not isinstance(self.book_id, int) or isinstance(self.book_id, bool):
            raise TypeError("Book ID must be an integer.")
        if self.book_id <= 0:
            raise ValueError("Book ID must be a positive integer.")

        # Validate title
        if not isinstance(self.title, str):
            raise TypeError("Title must be a string.")
        if not self.title.strip():
            raise ValueError("Title cannot be empty or blank.")

        # Validate author
        if not isinstance(self.author, str):
            raise TypeError("Author must be a string.")
        if not self.author.strip():
            raise ValueError("Author cannot be empty or blank.")

        # Validate available
        if not isinstance(self.available, bool):
            raise TypeError("Available status must be a boolean.")

    def __str__(self) -> str:
        """Returns a readable string representation of the Book."""
        status = "Available" if self.available else "Issued"
        return f"[ID: {self.book_id}] '{self.title}' by {self.author} | Status: {status}"
