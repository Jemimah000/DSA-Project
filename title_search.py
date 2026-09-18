"""Search for books by title using binary search and handling duplicates."""

from book import Book


def search_by_title(books: list[Book], title: str) -> list[Book]:
    """
    Finds all books matching a title using binary search.

    This function is designed to be beginner-friendly and demonstrate key DSA
    concepts. It first sorts a temporary copy of the book list. Then, it uses
    binary search to find one book with a matching title. Finally, it scans
    left and right from that book's position to find all other books with the
    same title.

    Args:
        books: A list of Book objects.
        title: The title to search for (case-insensitive).

    Returns:
        A list of all Book objects with the matching title, or an empty list.
    """
    # Handle the edge case of an empty list of books to avoid errors.
    if not books:
        return []

    # 1. Normalization: Prepare the search title for case-insensitive comparison.
    normalized_search_title = title.lower()

    # 2. Temporary Sorting: Create a sorted copy of the books list.
    # We sort by title (case-insensitively) as the primary key and book_id as
    # the secondary key. This doesn't change the original list.
    sorted_books = sorted(books, key=lambda book: (book.title.lower(), book.book_id))

    # 3. Binary Search: Find the index of *one* book that matches the title.
    found_index = -1
    low = 0
    high = len(sorted_books) - 1

    while low <= high:
        # Calculate the middle index to divide the list in half.
        mid = (low + high) // 2
        mid_title = sorted_books[mid].title.lower()

        if mid_title == normalized_search_title:
            # A match is found! Store its index and stop the binary search.
            found_index = mid
            break
        elif mid_title < normalized_search_title:
            # The title we're looking for is in the upper half.
            low = mid + 1
        else:
            # The title we're looking for is in the lower half.
            high = mid - 1

    # If binary search did not find any match, return an empty list.
    if found_index == -1:
        return []

    # 4. Scanning for Duplicates: Collect all books with the same title.
    # The binary search finds just one match, but there may be others next to it
    # because the list is sorted.

    matches = [sorted_books[found_index]]

    # Scan left from the found index.
    left = found_index - 1
    while left >= 0 and sorted_books[left].title.lower() == normalized_search_title:
        matches.append(sorted_books[left])
        left -= 1

    # Scan right from the found index.
    right = found_index + 1
    while right < len(sorted_books) and sorted_books[right].title.lower() == normalized_search_title:
        matches.append(sorted_books[right])
        right += 1

    return matches