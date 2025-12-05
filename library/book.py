# TODO: Create the Book class here
#
# Class name: Book
#
# Attributes:
#   - book_id: string
#   - title: string
#   - author: string
#   - isbn: string
#   - is_borrowed: boolean (default False)
#   - borrowed_by: string or None (default None)
#
# Methods to implement:
#   - __init__(self, book_id, title, author, isbn)
#   - borrow(self, member_id) -> bool
#   - return_book(self) -> bool
#   - get_info(self) -> string
#   - __str__(self) -> string
#
# Start coding below:

from datetime import datetime,timedelta

class Book:
    def __init__(self, book_id, title, author, isbn,is_borrowed=False, borrowed_by=None,borrow_date=None,due_date=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed
        self.borrowed_by = borrowed_by
        self.borrow_date = borrow_date
        self.due_date = due_date

    def borrow(self, member_id) -> bool:
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrowed_by = member_id
            self.borrow_date = datetime.now().strftime("%d-%m-%Y")
            self.due_date = (datetime.now() + timedelta(days=14)).strftime("%d-%m-%Y")
            return True
        return False

    def return_book(self) -> bool:
        if self.is_borrowed:
            self.is_borrowed = False
            self.borrowed_by = None
            self.borrow_date = None
            self.due_date = None
            return True
        return False

    def get_info(self) -> str:
        status = "Borrowed" if self.is_borrowed else "Available"
        borrower_info = f", Borrowed by: {self.borrowed_by}" if self.is_borrowed else ""
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}{borrower_info}"

    def __str__(self) -> str:
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
    
