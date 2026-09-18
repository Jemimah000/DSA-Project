"""Linked-list storage for library books."""

from collections.abc import Iterator
from typing import Optional


class Node:
    """A linked-list node containing one book."""

    def __init__(self, book, next: Optional["Node"] = None):
        self.book = book
        self.next = next


class LinkedList:
    """Singly linked list that stores books in insertion order."""

    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, book) -> None:
        """Add a book to the end of the list."""
        new_node = Node(book)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def remove_by_id(self, book_id) -> bool:
        """Remove the first book with ``book_id`` and report whether it existed."""
        previous = None
        current = self.head

        while current is not None:
            if current.book.book_id == book_id:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next

        return False

    def traverse(self) -> list:
        """Return all stored books from head to tail."""
        return [book for book in self]

    def __iter__(self) -> Iterator:
        """Iterate over stored books from head to tail."""
        current = self.head
        while current is not None:
            yield current.book
            current = current.next
