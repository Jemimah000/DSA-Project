# Book Finder and Library Manager

## Project Overview

This project is a Python-based library management system that stores books in a linked list while also keeping a dictionary-based index for fast ID lookup. It allows users to add, remove, search, issue, return, display, and count books. The application demonstrates several important data structures and algorithms: linked list traversal, hashing, recursion, sorting, and binary search.

Each book has a unique Book ID, title, author, and availability status. The system prevents duplicate IDs and validates user input to keep the data consistent.

## File Structure

```text
DSA-Project/
├── book.py
├── linked_list.py
├── library.py
├── title_search.py
├── main.py
├── test_library.py
├── README.md
└── __pycache__/
```

## Data Structures and DSA Concepts Used

### 1. Linked List
The books are stored in a singly linked list in insertion order. This makes display and traversal easy and demonstrates how nodes connect through the `next` pointer.

- `Node` stores one `Book` object and a reference to the next node.
- `LinkedList` supports append and remove operations.
- Traversal is used to display books and to count them recursively.

### 2. Hashing with Dictionary
A dictionary keeps `book_id` mapped to the corresponding `Book` instance. This gives average-case `O(1)` lookup for ID-based search, issue, and return operations.

- `Library.books_by_id` stores the hash index.
- Duplicate IDs are rejected before insertion.
- Removal updates both the linked list and the hash table so they stay synchronized.

### 3. Recursion
The total number of books is computed by recursively visiting each node until the end of the list. The base case is when the node is `None`, returning `0`.

### 4. Sorting and Binary Search
Title search does not modify the original list order. Instead, it creates a temporary sorted list based on normalized title text and uses binary search to locate a matching title quickly.

- Titles are compared case-insensitively.
- Duplicate titles are found by scanning left and right around the match.
- This demonstrates how binary search needs sorted data to work correctly.

## Implementation Approach

1. `Book` model
   - Stores `book_id`, `title`, `author`, and `available`.
   - Validates positive ID and non-empty fields.
   - Provides a readable string representation.

2. `LinkedList`
   - Maintains head-to-tail node ordering.
   - Appends new books and removes books by ID.
   - Supports iteration for display and other features.

3. `Library`
   - Uses a linked list to keep insertion order.
   - Uses a dictionary for quick ID lookup.
   - Handles add/remove, issue/return, and recursive counting.

4. `search_by_title`
   - Copies all books into a temporary list.
   - Sorts by lowercase title and then by ID.
   - Uses binary search to locate one matching title.
   - Scans around that found position to collect all identical titles.

5. `main.py`
   - Provides a console menu for all library operations.
   - Validates user input and handles invalid IDs or menu choices safely.

## Complexity Analysis

| Operation | Data structure | Time complexity | Extra space |
| --- | --- | --- | --- |
| Add book | Linked list + dictionary | Average `O(1)` | `O(1)` |
| Search by ID | Hash table / dictionary | Average `O(1)` | `O(1)` |
| Remove by ID | Linked list traversal | `O(n)` | `O(1)` |
| Display all books | Linked list traversal | `O(n)` | `O(1)` excluding output |
| Issue/return book | Dictionary lookup | Average `O(1)` | `O(1)` |
| Count books recursively | Linked list recursion | `O(n)` | `O(n)` call stack |
| Search by title | Sorting + binary search | `O(n log n + k)` | `O(n)` |

Here, `k` is the number of books with the matching title. The extra temporary list is created during the search and is not kept permanently.

## Edge Cases Covered

The project includes handling for the following edge cases:

- Empty library
- Duplicate Book ID
- Missing Book ID
- Missing title match
- Book already issued
- Book already available
- Removal from head, middle, and tail
- One-book library
- Duplicate titles in the title search
- Blank or invalid input values

## Test Cases Included

The automated tests cover:

- Valid and invalid `Book` creation
- Duplicate ID rejection
- Linked list append and removal
- Issue/return success and failure conditions
- Recursive count for empty, single, and many books
- ID search for present and missing books
- Case-insensitive title lookup
- Duplicate title matching
- Empty search result handling

## How to Run

```bash
python main.py
python -m unittest test_library.py
```

## Summary

This project combines several fundamental computer science ideas into one practical application: data validation, linked-list storage, dictionary-based indexing, recursive counting, and title-based search using sorting and binary search. It is structured so the library logic stays consistent and easy to test, while the user interface remains simple and interactive.


Demo Link : https://drive.google.com/file/d/1f-PBvy6yOof5lh33NPm5VkK1K4P4E_d9/view?usp=drive_link