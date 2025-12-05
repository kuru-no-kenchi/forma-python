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
from datetime import datetime

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
                self.transactions.append((member_id,member_obj.name, book_id,book_obj.title, "borrowed",book_obj.due_date))
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
    
    def get_overdue_books(self):
        overdue_books = []
        now = datetime.now()
        for book in self.books.values():
            if not book.is_borrowed or not book.due_date :
                continue
            try:
                due = datetime.strptime(book.due_date, "%d-%m-%Y")
                if now > due:
                    overdue_books.append(book)
            except ValueError:
                continue
        return overdue_books
    def get_time_left(self):
        time_left = ""
        now = datetime.now()
        for book in self.books.values():
            if not book.is_borrowed or not book.due_date:
                continue
            try:
                due = datetime.strptime(book.due_date, "%d-%m-%Y")
                days_left = (due - now).days
                if days_left < 0:
                    time_left += f", Overdue by {-days_left} days"
                else:
                    time_left += f", {days_left} days left"
            except ValueError:
                continue
        return time_left
    def generate_report(self) -> str:
        overdue_books = self.get_overdue_books()
        report_lines = ["Library Report:"]
        report_lines.append(f"Total Books: {len(self.books)}")
        report_lines.append(f"Total Members: {len(self.members)}")
        report_lines.append(f"Available Books: {len([b for b in self.books.values() if b.is_borrowed == False])}")
        report_lines.append(f"Borrowed Books: {len([b for b in self.books.values() if b.is_borrowed == True])}")
        report_lines.append(f"Active Borrowers: {len([m for m in self.members.values() if m.borrowed_books])}")
        report_lines.append(f"Overdue Books: {len(overdue_books)}")
        report_lines.append("")
        report_lines.append("Transactions:")
        for transaction in self.transactions:
            if len(transaction) == 6:
                member_id, member_name, book_id, book_title, action, due_date = transaction
            elif len(transaction) == 5:
                member_id, member_name, book_id, book_title, action = transaction
                due_date = None
            else:
                continue
            if member_id in self.members:
                member_name = self.members[member_id].name
            if book_id in self.books:
                book_title = self.books[book_id].title
            time_left = "N/A"
            if due_date:
                try:
                    due_date = datetime.strptime(due_date, "%d-%m-%Y")
                    days_left = (due_date - datetime.now()).days
                    time_left = f"{days_left} days left" if days_left >= 0 else f"Overdue by {-days_left} days"
                except Exception:
                    time_left = "N/A"

            report_lines.append(
                f"Member: {member_name} (ID: {member_id}), Book: {book_title} (ID: {book_id}), Action: {action}, Time Left: {time_left}"
            )
        if overdue_books:
            report_lines.append("")
            report_lines.append("Overdue Books:")
            for book in overdue_books:
                report_lines.append(f"- {book.title} (ID: {book.book_id}), Borrowed by: {book.borrowed_by}, Due: {book.due_date}")

        return "\n".join(report_lines)