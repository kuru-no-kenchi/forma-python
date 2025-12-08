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
from datetime import datetime, timedelta

class LibrarySystem:
    FINE_PER_DAY = 5
    def serialize_transaction(self,tx):
        return [
            tx[0],                       
            tx[1],                       
            tx[2],                    
            tx[3].strftime("%d-%m-%Y") if isinstance(tx[3], datetime) else tx[3],
            tx[4].strftime("%d-%m-%Y") if isinstance(tx[4], datetime) else tx[4],
        ]

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
                self.transactions.append(
                    (member_id, book_id, "borrowed", datetime.now().strftime("%d-%m-%Y"), book_obj.due_date)
                )
                return True
        return False

    def return_book(self, member_id, book_id) -> bool:
        if member_id in self.members and book_id in self.books:
            member_obj = self.members[member_id]
            book_obj = self.books[book_id]
            if member_obj.return_book(book_id) and book_obj.return_book():
                self.transactions.append(
                    (member_id, book_id, "returned", datetime.now().strftime("%d-%m-%Y"), None)
                )
                return True
        return False

    def search_books(self, keyword) -> list:
        keyword = keyword.lower()
        return [
            b for b in self.books.values()
            if keyword in b.title.lower() or keyword in b.author.lower() or keyword in b.isbn.lower()
        ]

    def get_member_books(self, member_id) -> list:
        if member_id in self.members:
            return [self.books[b_id] for b_id in self.members[member_id].borrowed_books]
        return []

    def get_overdue_books(self):
        overdue = []
        now = datetime.now()
        for b in self.books.values():
            if not b.is_borrowed or not b.due_date:
                continue
            try:
                due = datetime.strptime(b.due_date, "%d-%m-%Y")
                if now > due:
                    overdue.append(b)
            except Exception:
                continue
        return overdue
    
    def calculate_fine(self, book):
        if not book.due_date:
            return 0
        if isinstance(book.due_date, datetime):
            due = book.due_date
        else:
            try:
                due = datetime.strptime(book.due_date, "%d-%m-%Y")
            except Exception:
                return 0
        today = datetime.now()
        days_overdue = (today - due).days
        return max(0, days_overdue * self.FINE_PER_DAY)

    def generate_report(self) -> str:
        overdue_books = self.get_overdue_books()
        report_lines = []
        report_lines.append("===== LIBRARY REPORT =====")
        report_lines.append(f"Total Books: {len(self.books)}")
        report_lines.append(f"Total Members: {len(self.members)}")
        report_lines.append(f"Available Books: {len([b for b in self.books.values() if not b.is_borrowed])}")
        report_lines.append(f"Borrowed Books: {len([b for b in self.books.values() if b.is_borrowed])}")
        report_lines.append(f"Active Borrowers: {len([m for m in self.members.values() if m.borrowed_books])}")
        report_lines.append(f"Overdue Books: {len(overdue_books)}")
        report_lines.append("")
        report_lines.append("---- TRANSACTIONS ----")

        for member_id, book_id, action, action_date, due_date in self.transactions:

            member_name = self.members[member_id].name if member_id in self.members else "Unknown"
            book_title  = self.books[book_id].title  if book_id in self.books else "Unknown"

            time_left = "N/A"

            if due_date:
                try:
                    if isinstance(due_date, datetime):
                        due = due_date
                    else:
                        due = datetime.strptime(due_date, "%d-%m-%Y")

                    days_remaining = (due - datetime.now()).days

                    if days_remaining >= 0:
                        time_left = f"{days_remaining} days left"
                    else:
                        time_left = f"Overdue by {-days_remaining} days"
                except Exception:
                    time_left = "N/A"

            report_lines.append(
                f"- {action_date}: The member {member_name} (ID {member_id}) {action} "
                f"the book '{book_title}' (ID {book_id}) | Time Left: {time_left}"
            )

        if overdue_books:
            report_lines.append("")
            report_lines.append("---- OVERDUE BOOKS ----")
            for b in overdue_books:
                fine = self.calculate_fine(b)
                report_lines.append(
                    f"{b.title} (ID: {b.book_id}) | Borrowed by: {b.borrowed_by} | "
                    f"Due: {b.due_date} | Fine: {fine} MAD"
                )

        return "\n".join(report_lines)

