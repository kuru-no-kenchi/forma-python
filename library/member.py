# TODO: Create the Member class here
#
# Class name: Member
#
# Attributes:
#   - member_id: string
#   - name: string
#   - email: string
#   - borrowed_books: list (default empty list)
#
# Methods to implement:
#   - __init__(self, member_id, name, email)
#   - borrow_book(self, book_id) -> bool (max 3 books)
#   - return_book(self, book_id) -> bool
#   - get_borrowed_count(self) -> int
#   - __str__(self) -> string
#
# Start coding below:

from enum import member


class Member:
    def __init__(self, member_id, name, email, borrowed_books=None):
        self.member_id = member_id
        self.name = name
        self.email = email
        if borrowed_books is None:
            self.borrowed_books = []
        else:
            self.borrowed_books = list(borrowed_books)

    def borrow_book(self, book_id) -> bool:
        if book_id in self.borrowed_books:
            return False
        if len(self.borrowed_books) < 3:
            self.borrowed_books.append(book_id)
            return True
        return False
    
    def return_book(self, book_id) -> bool:
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True
        return False

    def get_borrowed_count(self) -> int:
        return len(self.borrowed_books)

    def __str__(self) -> str:
        return (f"Member ID: {self.member_id}, Name: {self.name}, "
                f"Email: {self.email}, Borrowed Books: {len(self.borrowed_books)}")
    
    def serialize_member(member):
        return {
            "member_id": member.member_id,
            "name": member.name,
            "email": member.email,
            "borrowed_books": member.borrowed_books
        }
