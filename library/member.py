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

class Member:
    def __init__(self, member_id, name, email, borrowed_books=None):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = borrowed_books if borrowed_books is not None else []
        
    def borrow_book(self, book_id) -> bool:
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
        return f"Member ID: {self.member_id}, Name: {self.name}, Email: {self.email}, Borrowed Books: {len(self.borrowed_books)}"