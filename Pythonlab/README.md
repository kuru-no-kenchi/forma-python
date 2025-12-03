# Python Lab: Library Management System

## Purpose of This Lab

Welcome to your first real-world Python project! This lab is designed to help you apply the concepts you've learned about Python syntax, Object-Oriented Programming (OOP), and modules/packages in a practical scenario.

By the end of this lab, you will have built a complete **Library Management System** that can:
- Manage books and members
- Handle book borrowing and returns
- Generate reports
- Save and load data

This project will teach you how to organize code professionally, work with multiple files, and build a maintainable application.

---

## What You Will Learn

1. **Object-Oriented Programming (OOP)**
   - Creating classes with attributes and methods
   - Encapsulation and data validation
   - Working with multiple related classes

2. **Modules and Packages**
   - Organizing code into separate files
   - Importing and using custom modules
   - Creating a package structure

3. **Python Syntax**
   - File I/O operations
   - Exception handling
   - List comprehensions and data manipulation
   - String formatting

---

## Project Structure

Your completed project should look like this:

```
Pythonlab/
│
├── README.md                    # This file
├── main.py                      # Main application file (you'll create this)
│
└── library/                     # Package directory (you'll create this)
    ├── __init__.py             # Package initialization file
    ├── book.py                 # Book class
    ├── member.py               # Member class
    ├── library_system.py       # Main library management class
    └── utils.py                # Utility functions
```

---

## Lab Steps

### Step 1: Create the Package Structure

1. Create a folder called `library` inside the `Pythonlab` directory
2. Inside the `library` folder, create an empty file called `__init__.py`
   - This file makes the folder a Python package
3. Create four empty Python files in the `library` folder:
   - `book.py`
   - `member.py`
   - `library_system.py`
   - `utils.py`

---

### Step 2: Build the Book Class (`library/book.py`)

Create a `Book` class with the following specifications:

**Attributes:**
- `book_id` (string): Unique identifier for the book
- `title` (string): Book title
- `author` (string): Author name
- `isbn` (string): ISBN number
- `is_borrowed` (boolean): Whether the book is currently borrowed (default: False)
- `borrowed_by` (string or None): Member ID who borrowed the book (default: None)

**Methods:**
- `__init__(self, book_id, title, author, isbn)`: Constructor
- `borrow(self, member_id)`: Mark book as borrowed by a member
  - Should return `True` if successful, `False` if already borrowed
- `return_book(self)`: Mark book as returned
  - Should return `True` if successful, `False` if not borrowed
- `get_info(self)`: Return a formatted string with book information
- `__str__(self)`: Return a readable string representation

**Hints:**
- Use `self.is_borrowed` to track borrowing status
- Update `self.borrowed_by` when a book is borrowed
- Reset `self.borrowed_by` to `None` when returned

---

### Step 3: Build the Member Class (`library/member.py`)

Create a `Member` class with the following specifications:

**Attributes:**
- `member_id` (string): Unique identifier for the member
- `name` (string): Member's full name
- `email` (string): Member's email address
- `borrowed_books` (list): List of book IDs currently borrowed (default: empty list)

**Methods:**
- `__init__(self, member_id, name, email)`: Constructor
- `borrow_book(self, book_id)`: Add a book to borrowed books
  - Maximum 3 books per member
  - Return `True` if successful, `False` if limit reached
- `return_book(self, book_id)`: Remove a book from borrowed books
  - Return `True` if successful, `False` if book not found
- `get_borrowed_count(self)`: Return number of books currently borrowed
- `__str__(self)`: Return a readable string representation

**Hints:**
- Use a list to store `borrowed_books`
- Check list length before allowing new borrows
- Use `list.append()` and `list.remove()` methods

---

### Step 4: Build Utility Functions (`library/utils.py`)

Create the following utility functions:

**Function 1: `generate_id(prefix)`**
- Generates a unique ID with a prefix (e.g., "BK001", "MEM001")
- Use current timestamp or random numbers
- Example: `generate_id("BK")` returns `"BK001"`

**Function 2: `validate_email(email)`**
- Validates if an email address is in correct format
- Should contain "@" and "."
- Return `True` or `False`

**Function 3: `save_to_file(data, filename)`**
- Saves data to a text file
- Use `json` module to save as JSON format
- Handle file writing exceptions

**Function 4: `load_from_file(filename)`**
- Loads data from a text file
- Return the data or empty structure if file doesn't exist
- Handle file reading exceptions

**Hints:**
- Import `json`, `datetime`, or `random` modules as needed
- Use try-except blocks for file operations
- Use `with open()` for file handling

---

### Step 5: Build the Library System Class (`library/library_system.py`)

Create a `LibrarySystem` class that manages everything:

**Attributes:**
- `books` (dictionary): Store books with book_id as key
- `members` (dictionary): Store members with member_id as key
- `transactions` (list): Store borrowing/return history

**Methods:**
- `__init__(self)`: Initialize empty collections
- `add_book(self, title, author, isbn)`: Create and add a new book
- `add_member(self, name, email)`: Create and add a new member
- `borrow_book(self, member_id, book_id)`: Process a book borrowing
  - Validate member and book exist
  - Check if book is available
  - Check if member can borrow more books
  - Update both book and member
  - Record transaction
- `return_book(self, member_id, book_id)`: Process a book return
  - Validate the borrowing record
  - Update both book and member
  - Record transaction
- `search_books(self, keyword)`: Search books by title or author
- `get_member_books(self, member_id)`: Get all books borrowed by a member
- `generate_report(self)`: Return a summary of the library status

**Hints:**
- Import `Book` and `Member` classes
- Import utility functions from `utils`
- Use dictionaries for fast lookups
- Record transactions with timestamp and action type

---

### Step 6: Create the Main Application (`main.py`)

Create a command-line interface that allows users to:

**Menu Options:**
1. Add a new book
2. Add a new member
3. Borrow a book
4. Return a book
5. Search books
6. View member's borrowed books
7. Generate library report
8. Save data
9. Load data
10. Exit

**Requirements:**
- Display a menu and get user input
- Call appropriate methods from `LibrarySystem`
- Handle invalid inputs gracefully
- Use a loop to keep the program running until user exits

**Hints:**
- Import `LibrarySystem` from the `library` package
- Use `input()` to get user choices
- Use a `while True` loop with a break condition
- Print clear instructions and feedback

---

### Step 7: Initialize the Package (`library/__init__.py`)

In the `__init__.py` file, import the main classes to make them easily accessible:

```python
# Import the main classes for easy access
from .book import Book
from .member import Member
from .library_system import LibrarySystem
```

This allows users to write:
```python
from library import Book, Member, LibrarySystem
```

Instead of:
```python
from library.book import Book
from library.member import Member
from library.library_system import LibrarySystem
```

---

## Testing Your Application

### Test Case 1: Basic Operations
1. Run your `main.py`
2. Add 2-3 books
3. Add 1-2 members
4. Borrow a book
5. Check if the book shows as borrowed
6. Return the book
7. Check if the book is available again

### Test Case 2: Validation
1. Try to borrow a book that's already borrowed
2. Try to borrow more than 3 books for one member
3. Try to return a book that wasn't borrowed
4. Try to add a member with invalid email

### Test Case 3: Data Persistence
1. Add books and members
2. Save data to file
3. Exit the program
4. Run the program again
5. Load data from file
6. Verify all data is restored

---

## Expected Output Example

```
=== Library Management System ===

1. Add a new book
2. Add a new member
3. Borrow a book
4. Return a book
5. Search books
6. View member's borrowed books
7. Generate library report
8. Save data
9. Load data
10. Exit

Enter your choice: 1

Enter book title: Python Programming
Enter author: John Smith
Enter ISBN: 978-1234567890
Book added successfully! Book ID: BK001

Enter your choice: 7

=== Library Report ===
Total Books: 5
Available Books: 3
Borrowed Books: 2
Total Members: 3
Active Borrowers: 2
```

---

## Evaluation Criteria

Your project will be evaluated on:

1. **Functionality (40%)**
   - All features work as expected
   - Proper error handling
   - Data validation

2. **Code Organization (30%)**
   - Proper use of classes and methods
   - Code split into appropriate modules
   - Proper package structure

3. **OOP Principles (20%)**
   - Proper use of encapsulation
   - Meaningful class design
   - Appropriate method names and parameters

4. **Code Quality (10%)**
   - Clear variable names
   - Proper comments where needed
   - Clean, readable code

---

## Bonus Challenges (Optional)

If you finish early, try these enhancements:

1. **Due Dates**: Add a borrowing period (e.g., 14 days) and track overdue books
2. **Fines**: Calculate fines for overdue books
3. **Book Categories**: Add categories to books and allow filtering
4. **Search Enhancement**: Add fuzzy search or partial matching
5. **Data Export**: Export reports to CSV or PDF
6. **GUI**: Create a simple GUI using `tkinter`

---

## Common Issues and Solutions

### Issue: "ModuleNotFoundError: No module named 'library'"
**Solution:** Make sure you're running `main.py` from the `Pythonlab` directory and that `__init__.py` exists in the `library` folder.

### Issue: "AttributeError" when calling methods
**Solution:** Check that you're using `self` correctly in class methods and that you've initialized all attributes in `__init__`.

### Issue: Data not saving properly
**Solution:** Make sure you're using `json.dumps()` and `json.loads()` correctly, and that your data structures are JSON-serializable.

---

## Resources

- Python Official Documentation: https://docs.python.org/3/
- Python Classes Tutorial: https://docs.python.org/3/tutorial/classes.html
- Python Modules Tutorial: https://docs.python.org/3/tutorial/modules.html
- JSON Module: https://docs.python.org/3/library/json.html

---

## Need Help?

If you're stuck:
1. Read the error messages carefully
2. Check the hints in each step
3. Review your class notes on OOP and modules
4. Ask your instructor for guidance

---

## Submission

When you're done:
1. Test all functionality thoroughly
2. Make sure all files are in the correct structure
3. Add comments to explain complex logic
4. Submit the entire `Pythonlab` folder

Good luck, and enjoy building your first real Python project!
