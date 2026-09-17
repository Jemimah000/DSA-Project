# Book Finder and Library Manager

## Project Overview

This Python console application manages a small library. Users can add, remove, search, issue, return, display, and count books. It demonstrates a Linked List, Hashing, Binary Search, and Recursion.

Each book stores a Book ID, title, author, and availability status. Book IDs are unique; multiple books may have the same title.

## Suggested Python Structure

```text
DSA-Project/
├── book.py             # Book data class — Abhishek
├── linked_list.py      # Node and linked-list operations — Yogesh
├── library.py          # Hashing, issue/return, recursive count — Jemimah
├── title_search.py     # Sorted title data and binary search — Dhanyalakshmi
├── main.py             # Menu integration and input handling — Sibiraj
├── test_library.py     # Combined tests
└── README.md
```

This file split reduces merge conflicts. Each member mainly edits their own file and makes only small agreed integration changes.

## Team Work Plan

| Member | Main coding task | DSA ownership | Tests | Why it matters |
| --- | --- | --- | --- | --- |
| **Abhishek** | Create Book model, validation, starter menu helpers | Book/node foundation | Valid and invalid book details | Defines data used by every feature |
| **Yogesh** | Create Node/LinkedList; add, remove, display | Linked List | Empty, one-book, and all removal positions | Implements collection management |
| **Jemimah** | Create hash index, ID search, issue/return, recursive count | Hashing and Recursion | Duplicate/missing ID, issue/return states, count | Implements fast lookup and book status |
| **Dhanyalakshmi** | Create sorted title view and binary search | Binary Search | Missing, case-insensitive, duplicate titles | Implements required title searching |
| **Sibiraj** | Integrate menu, input errors, end-to-end tests | All-concept integration | Full user flow and invalid input | Makes the program usable as one application |

Every member writes production code, tests their part, commits it, and explains it in the demo. Testing/documentation are shared duties, not anyone's only task.

## Tasks for Each Member

### 1. Abhishek — Book Model and Foundation

**Files:** `book.py`, starter `main.py`

- Create a `Book` class or `@dataclass` with `book_id`, `title`, `author`, and `available=True`.
- Validate positive ID and non-empty title/author.
- Add `__str__()` for readable display.
- Create a numbered menu skeleton containing all eight functions.
- Test valid Book creation, invalid ID, blank fields, and default Available status.

**Demo:** Explain that the Book structure is the data stored inside every linked-list node.

### 2. Yogesh — Linked List Operations

**File:** `linked_list.py`

- Create `Node(book, next)` and `LinkedList` with `head`.
- Implement `append(book)`, `remove_by_id(book_id)`, `traverse()`, and a helper/iterator returning stored books.
- Correctly remove a head, middle, last, only node, or missing ID.
- Test empty list, one book, multiple books, and every removal case.

**Demo:** Explain traversal from `head` through `next`, and how removal reconnects the previous node to the next node.

### 3. Jemimah — Hashing, Issue/Return, and Recursion

**File:** `library.py`

- Create `Library`, using Yogesh's `LinkedList` and `books_by_id = {}` dictionary.
- Implement `add_book(book)` and reject duplicate IDs before adding.
- Implement `search_by_id(book_id)`, `issue_book(book_id)`, and `return_book(book_id)`.
- When a book is removed, delete it from both the linked list and dictionary.
- Implement `count_books_recursive(node)` with base case `if node is None: return 0`, plus public `count_books()`.
- Test duplicate/missing IDs, issue twice, return twice, removal synchronization, and empty/one/many recursive counts.

**Demo:** Explain that Python's dictionary is a hash table, so Book ID search is average `O(1)`, and explain recursion's base case.

### 4. Dhanyalakshmi — Title Search with Binary Search

**File:** `title_search.py`

- Create `search_by_title(books, title)`.
- Make a temporary list sorted by `book.title.lower()` and then Book ID; do not alter the linked-list display order.
- Use binary search to find one matching normalized title.
- Scan left/right from the found item to return every book with the same title.
- Test empty library, missing title, case-insensitive title, one match, and duplicate titles.

**Demo:** Explain that binary search requires sorted data, and that neighbouring matches are collected for duplicate titles.

### 5. Sibiraj — Menu Integration and Final Testing

**Files:** `main.py`, `test_library.py`, final README updates

- Connect Add, Remove, ID Search, Title Search, Issue, Return, Display, Recursive Count, and Exit to their modules.
- Handle invalid choices and non-numeric IDs without crashing.
- Add end-to-end tests: add → ID search → title search → issue → return → remove → verify missing.
- Run all tests and fix only necessary integration issues.
- Add final run instructions and complexity notes.

**Demo:** Show one complete user flow and explain that integration tests check all structures stay consistent after changes.

## One-Day Implementation Plan

| Time | Member(s) | Deliverable |
| --- | --- | --- |
| 9:00–10:00 | Abhishek | `book.py`, folders, menu skeleton, model tests |
| 10:00–11:30 | Yogesh | `linked_list.py`, add/remove/traverse, tests |
| 11:30–1:00 | Jemimah | `library.py`, hashing, issue/return, recursion, tests |
| 2:00–3:15 | Dhanyalakshmi | `title_search.py`, sort + binary search, tests |
| 3:15–4:30 | Sibiraj | Full menu, end-to-end tests, safe input handling |
| 4:30–5:00 | All | Pull latest `main`, run tests, practise demo |

If someone finishes early, they should help test completed code and not change another member's module without agreement.

## Handover Order

**Abhishek → Yogesh → Jemimah → Dhanyalakshmi → Sibiraj**

1. Abhishek completes `Book` and menu skeleton. Yogesh pulls latest `main` and uses the exact Book fields.
2. Yogesh completes `LinkedList`. Jemimah pulls `main` and uses it as the source of truth.
3. Jemimah completes `Library`. Dhanyalakshmi pulls `main` and reads books without altering the hash index.
4. Dhanyalakshmi completes title search. Sibiraj pulls `main` and connects public methods to the UI.
5. Sibiraj completes integration; everyone pulls final `main`, runs tests, and checks the demo.

Do not rename public fields/methods or change previous behavior without informing the owner.

## Git Workflow

```bash
git clone <repository-url>
cd DSA-Project
git checkout main
git pull origin main
git checkout -b feature/<your-name>

# Make assigned changes and run tests
git add book.py linked_list.py library.py title_search.py main.py test_library.py README.md
git commit -m "feat: add <your feature>"
git push -u origin feature/<your-name>
```

Create and merge a pull request into `main`. The next member then runs:

```bash
git checkout main
git pull origin main
git checkout -b feature/<next-member-name>
```

## Required Edge Cases

- Empty library: display, search, and count work safely.
- Duplicate Book ID: reject the new book.
- Missing Book ID/title: show “not found.”
- Already issued book: do not issue again.
- Already available book: do not return again.
- Only one book: removal and count work.
- Duplicate titles: return every matching book.

## Complexity Analysis

| Operation | DSA used | Time complexity | Extra space |
| --- | --- | --- | --- |
| Add book / duplicate check | Hash table + linked list | Average `O(1)` | `O(1)` per book |
| Search by Book ID | Hash table/dictionary | Average `O(1)` | `O(1)` |
| Remove by ID | Linked-list traversal | `O(n)` | `O(1)` |
| Display books | Linked-list traversal | `O(n)` | `O(1)` excluding output |
| Issue/return | Hash table/dictionary | Average `O(1)` | `O(1)` |
| Recursive count | Recursion on linked list | `O(n)` | `O(n)` call stack |
| Search by title | Sort temporary list + binary search | `O(n log n + k)` | `O(n + k)` |

`k` is the number of books with the matching title. Sorting is included because the temporary title list is rebuilt for each search.

## How to Run

```bash
python main.py
python -m unittest test_library.py
```

## Final Submission Checklist

- [ ] All five members have committed code
- [ ] Add, remove, display, issue, and return work
- [ ] Linked List traversal is used for display
- [ ] Dictionary hashing is used for Book ID search
- [ ] Sorted title data and Binary Search are used for title search
- [ ] Recursive count has a clear base case
- [ ] Required edge cases are tested
- [ ] README and complexity analysis are complete
- [ ] Final demo is prepared
