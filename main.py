"""
Main Application Entry Point (Starter Menu Skeleton)
Contributor: Abhishek (Foundation and Starter Menu Skeleton)
"""


def display_menu():
    """Displays the numbered menu skeleton containing all eight library functions."""
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


def main():
    """Starter main loop skeleton."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            print("[Skeleton Placeholder] 1. Add Book")
        elif choice == "2":
            print("[Skeleton Placeholder] 2. Remove Book by ID")
        elif choice == "3":
            print("[Skeleton Placeholder] 3. Search Book by ID")
        elif choice == "4":
            print("[Skeleton Placeholder] 4. Search Book by Title")
        elif choice == "5":
            print("[Skeleton Placeholder] 5. Issue Book")
        elif choice == "6":
            print("[Skeleton Placeholder] 6. Return Book")
        elif choice == "7":
            print("[Skeleton Placeholder] 7. Display All Books")
        elif choice == "8":
            print("[Skeleton Placeholder] 8. Count Books (Recursive)")
        elif choice == "9":
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 9.")


if __name__ == "__main__":
    main()
