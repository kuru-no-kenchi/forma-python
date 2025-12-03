# TODO: Create the LibrarySystem class here
#
# This is the main class that manages the entire library
#
# You will need to import:
#   - Book class from book.py
#   - Member class from member.py
#   - Utility functions from utils.py
#
# Class name: LibrarySystem
#
# Attributes:
#   - books: dictionary (key: book_id, value: Book object)
#   - members: dictionary (key: member_id, value: Member object)
#   - transactions: list (store borrowing/return history)
#
# Methods to implement:
#   - __init__(self)
#   - add_book(self, title, author, isbn) -> string (returns book_id)
#   - add_member(self, name, email) -> string (returns member_id)
#   - borrow_book(self, member_id, book_id) -> bool
#   - return_book(self, member_id, book_id) -> bool
#   - search_books(self, keyword) -> list
#   - get_member_books(self, member_id) -> list
#   - generate_report(self) -> string
#
# Start coding below:

