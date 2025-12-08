# TODO: Create the main application interface here
#
# This file should:
# 1. Import LibrarySystem from the library package
# 2. Create a menu-driven interface
# 3. Handle user input and call appropriate methods
#
# Menu options to implement:
#   1. Add a new book
#   2. Add a new member
#   3. Borrow a book
#   4. Return a book
#   5. Search books
#   6. View member's borrowed books
#   7. Generate library report
#   8. Save data
#   9. Load data
#   10. Exit
#
# Hints:
#   - Use a while loop for the menu
#   - Use input() to get user choices
#   - Print clear instructions
#   - Handle invalid inputs with try-except
#
# Start coding below:

import library.library_system as ls
import library.utils as utils
from library.book import Book
from library.member import Member

def main():
    library = ls.LibrarySystem()
    data_file = "library_data.json"
        

    while True:
        print("\nLibrary Management System")
        print("1. Add a new book")
        print("2. Add a new member")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Search books")
        print("6. View member's borrowed books")
        print("7. Generate library report")
        print("8. Save data")
        print("9. Load data")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        try:
            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                book_id = library.add_book(title, author, isbn)
                print(f"Book added with ID: {book_id}")

            elif choice == '2':
                name = input("Enter member name: ")
                email = input("Enter member email: ")
                if utils.validate_email(email):
                    member_id = library.add_member(name, email)
                    print(f"Member added with ID: {member_id}")
                else:
                    print("Invalid email format.")

            elif choice == '3':
                member_id = input("Enter member ID: ")
                book_id = input("Enter book ID: ")
                if library.borrow_book(member_id, book_id):
                    print("Book borrowed successfully.")
                else:
                    print("Failed to borrow book.")

            elif choice == '4':
                member_id = input("Enter member ID: ")
                book_id = input("Enter book ID: ")
                if library.return_book(member_id, book_id):
                    print("Book returned successfully.")
                else:
                    print("Failed to return book.")

            elif choice == '5':
                keyword = input("Enter search keyword: ")
                results = library.search_books(keyword)
                for book in results:
                    print(book.get_info())

            elif choice == '6':
                member_id = input("Enter member ID: ")
                borrowed_books = library.get_member_books(member_id)
                for book in borrowed_books:
                    print(book.get_info())

            elif choice == '7':
                report = library.generate_report()
                print(report)

            elif choice == '8':
                data = {
                    "books_id": {book_id: Book.serialize_book(book) for book_id, book in library.books.items()},
                    "members": {member_id: Member.serialize_member(member) for member_id, member in library.members.items()},
                    "transactions": [library.serialize_transaction(tx) for tx in library.transactions]
                }
                if utils.save_to_file(data, data_file):
                    print("Data saved successfully.")
                else:
                    print("Failed to save data.")

            elif choice == '9':
                data = utils.load_from_file(data_file)
                if data:
                    library.books = {book_id: Book(**book_data) for book_id, book_data in data.get("books_id", {}).items()}
                    library.members = {member_id: Member(**member_data) for member_id, member_data in data.get("members", {}).items()}
                    library.transactions = data.get("transactions", [])
                print("Data loaded successfully.")

            elif choice == '10':
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 10.")

        except Exception as e:
            print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()