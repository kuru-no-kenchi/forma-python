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

from datetime import datetime, timedelta

class Book:
    DATE_FORMAT = "%d-%m-%Y"
    def __init__(self, book_id, title, author, isbn,category = "",is_borrowed=False, borrowed_by=None,borrow_date=None, due_date=None, return_date=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category
        self.is_borrowed = is_borrowed
        self.borrowed_by = borrowed_by
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = return_date


    def borrow(self, member_id) -> bool:
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrowed_by = member_id
            self.borrow_date = datetime.now()
            self.due_date = (datetime.now() + timedelta(days=14))
            self.return_date = None
            return True
        return False

    def return_book(self) -> bool:
        if self.is_borrowed:
            self.is_borrowed = False
            self.return_date = datetime.now()
            self.borrowed_by = None
            return True
        return False

    def get_info(self) -> str:
        status = "Borrowed" if self.is_borrowed else "Available"
        borrower_info = f", Borrowed by: {self.borrowed_by}" if self.is_borrowed else ""
        return (
            f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, "
            f"ISBN: {self.isbn}, Status: {status}{borrower_info}"
        )
    def filter_books_by_category(self, category):
        return [book for book in self.books.values() if book.category.lower() == category.lower()]

    def __str__(self) -> str:
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) from {self.category}"
    
    def serialize_book(book):
        return {
            "book_id": book.book_id,
            "title": book.title,
            "author": book.author,
            "isbn": book.isbn,
            "category": book.category,
            "is_borrowed": book.is_borrowed,
            "borrowed_by": book.borrowed_by,
            "borrow_date": book.borrow_date.strftime("%d-%m-%Y") if book.borrow_date else None,
            "due_date": book.due_date.strftime("%d-%m-%Y") if book.due_date else None,
            "return_date": book.return_date.strftime("%d-%m-%Y") if book.return_date else None,
        }
