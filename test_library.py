import unittest

from book import Book
from library import Library
from linked_list import LinkedList
from title_search import search_by_title


class TestBook(unittest.TestCase):
    def test_valid_book_creation(self):
        book = Book(1, "Python Basics", "Alice")
        self.assertEqual(book.book_id, 1)
        self.assertEqual(book.title, "Python Basics")
        self.assertEqual(book.author, "Alice")
        self.assertTrue(book.available)

    def test_invalid_book_id_rejected(self):
        with self.assertRaises(ValueError):
            Book(0, "Python", "Alice")

    def test_blank_title_and_author_rejected(self):
        with self.assertRaises(ValueError):
            Book(2, "   ", "Alice")

        with self.assertRaises(ValueError):
            Book(3, "Python", " ")


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.books = [Book(1, "A", "Author 1"), Book(2, "B", "Author 2"), Book(3, "C", "Author 3")]
        self.linked_list = LinkedList()
        for book in self.books:
            self.linked_list.append(book)

    def test_append_and_traverse(self):
        self.assertEqual([book.book_id for book in self.linked_list.traverse()], [1, 2, 3])

    def test_remove_by_id_from_head_middle_tail(self):
        self.assertTrue(self.linked_list.remove_by_id(1))
        self.assertEqual([book.book_id for book in self.linked_list.traverse()], [2, 3])

        self.assertTrue(self.linked_list.remove_by_id(2))
        self.assertEqual([book.book_id for book in self.linked_list.traverse()], [3])

        self.assertTrue(self.linked_list.remove_by_id(3))
        self.assertEqual(self.linked_list.traverse(), [])

    def test_remove_missing_id_returns_false(self):
        self.assertFalse(self.linked_list.remove_by_id(99))

    def test_empty_list_behaves_correctly(self):
        empty_list = LinkedList()
        self.assertEqual(empty_list.traverse(), [])
        self.assertFalse(empty_list.remove_by_id(1))


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book_and_duplicate_rejection(self):
        book = Book(1, "Data Structures", "John")
        self.library.add_book(book)
        self.assertEqual(self.library.count_books(), 1)

        with self.assertRaises(ValueError):
            self.library.add_book(Book(1, "Algorithms", "Jane"))

    def test_search_by_id_returns_missing_and_found(self):
        book = Book(10, "Python", "Alice")
        self.library.add_book(book)

        self.assertIsNotNone(self.library.search_by_id(10))
        self.assertIsNone(self.library.search_by_id(99))

    def test_issue_and_return_book(self):
        self.library.add_book(Book(11, "Java", "Sam"))

        self.assertTrue(self.library.issue_book(11))
        self.assertFalse(self.library.issue_book(11))

        self.assertTrue(self.library.return_book(11))
        self.assertFalse(self.library.return_book(11))

    def test_return_and_issue_missing_or_invalid_book(self):
        self.assertFalse(self.library.issue_book(1))
        self.assertFalse(self.library.return_book(1))

    def test_remove_book_keeps_hash_index_in_sync(self):
        self.library.add_book(Book(5, "C++", "Mina"))
        self.library.add_book(Book(6, "DBMS", "Ravi"))

        self.assertTrue(self.library.remove_book(5))
        self.assertIsNone(self.library.search_by_id(5))
        self.assertEqual(self.library.count_books(), 1)
        self.assertFalse(self.library.remove_book(5))

    def test_count_books_recursive_for_empty_single_and_multiple(self):
        self.assertEqual(self.library.count_books(), 0)

        self.library.add_book(Book(1, "Only Book", "Author"))
        self.assertEqual(self.library.count_books(), 1)

        self.library.add_book(Book(2, "Second", "Author"))
        self.library.add_book(Book(3, "Third", "Author"))
        self.assertEqual(self.library.count_books(), 3)


class TestTitleSearch(unittest.TestCase):
    def test_empty_book_list_returns_empty_list(self):
        self.assertEqual(search_by_title([], "Python"), [])

    def test_missing_title_returns_empty_list(self):
        books = [Book(1, "C++", "A"), Book(2, "Java", "B")]
        self.assertEqual(search_by_title(books, "Python"), [])

    def test_title_search_is_case_insensitive(self):
        books = [Book(1, "Python Basics", "A"), Book(2, "java", "B"), Book(3, "PYTHON BASICS", "C")]
        matches = search_by_title(books, "python basics")
        self.assertEqual(sorted(book.book_id for book in matches), [1, 3])

    def test_duplicate_titles_return_all_matches(self):
        books = [
            Book(10, "Algorithms", "A"),
            Book(2, "Algorithms", "B"),
            Book(7, "Data Structures", "C"),
            Book(9, "Algorithms", "D"),
        ]
        matches = search_by_title(books, "algorithms")
        self.assertEqual(sorted(book.book_id for book in matches), [2, 9, 10])

    def test_single_match_returns_one_book(self):
        books = [Book(1, "Math", "A"), Book(2, "Physics", "B")]
        matches = search_by_title(books, "math")
        self.assertEqual([book.book_id for book in matches], [1])


if __name__ == "__main__":
    unittest.main()
