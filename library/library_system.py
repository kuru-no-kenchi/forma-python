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

from library import book, member, utils

class LibrarySystem:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.transactions = []

    def add_book(self, title, author, isbn) -> str:
        book_id = utils.generate_id("BK")
        new_book = book.Book(book_id, title, author, isbn)
        self.books[book_id] = new_book
        return book_id

    def add_member(self, name, email) -> str:
        member_id = utils.generate_id("MB")
        new_member = member.Member(member_id, name, email)
        self.members[member_id] = new_member
        return member_id

    def borrow_book(self, member_id, book_id) -> bool:
        if member_id in self.members and book_id in self.books:
            member_obj = self.members[member_id]
            book_obj = self.books[book_id]
            if member_obj.borrow_book(book_id) and book_obj.borrow(member_id):
                self.transactions.append((member_id,member_obj.name, book_id,book_obj.title, "borrowed"))
                return True
        return False

    def return_book(self, member_id, book_id) -> bool:
        if member_id in self.members and book_id in self.books:
            member_obj = self.members[member_id]
            book_obj = self.books[book_id]
            if member_obj.return_book(book_id) and book_obj.return_book():
                self.transactions.append((member_id,member_obj.name, book_id,book_obj.title, "returned"))
                return True
        return False

    def search_books(self, keyword) -> list:
        result = []
        for book_obj in self.books.values():
            if (keyword.lower() in book_obj.title.lower() or
                keyword.lower() in book_obj.author.lower() or
                keyword.lower() in book_obj.isbn.lower()):
                result.append(book_obj)
        return result

    def get_member_books(self, member_id) -> list:
        if member_id in self.members:
            member_obj = self.members[member_id]
            return [self.books[book_id] for book_id in member_obj.borrowed_books]
        return []

    def generate_report(self) -> str:
        report_lines = ["Library Report:"]
        report_lines.append(f"Total Books: {len(self.books)}")
        report_lines.append(f"Total Members: {len(self.members)}")
        report_lines.append(f"Available Books: {len([b for b in self.books.values() if b.is_borrowed == False])}")
        report_lines.append(f"Borrowed Books: {len([b for b in self.books.values() if b.is_borrowed == True])}")
        report_lines.append(f"Active Borrowers: {len([m for m in self.members.values() if m.borrowed_books])}")
        report_lines.append("Transactions:")
        for member_id,member_name, book_id, book_title, action in self.transactions:
            member_name = self.members[member_id].name
            book_title = self.books[book_id].title
            report_lines.append(
            f"Member: {member_name} (ID: {member_id}), Book: {book_title} (ID: {book_id}), Action: {action}"
            )

        return "\n".join(report_lines)