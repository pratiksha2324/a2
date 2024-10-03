class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {'Available' if self.available else 'Not Available'}"


class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"Sorry, {book.title} is currently not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} does not have {book.title}")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s borrowed books:")
            for book in self.borrowed_books:
                print(f"  - {book}")
        else:
            print(f"{self.name} has not borrowed any books.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"Added {new_book}")

    def register_member(self, name, membership_id):
        new_member = Member(name, membership_id)
        self.members.append(new_member)
        print(f"Registered new member: {name}")

    def list_available_books(self):
        available_books = [book for book in self.books if book.available]
        if available_books:
            print("Available books in the library:")
            for book in available_books:
                print(f"  - {book}")
        else:
            print("No books are currently available.")

    def find_member(self, membership_id):
        for member in self.members:
            if member.membership_id == membership_id:
                return member
        return None


# Example usage
library = Library()

# Adding books
library.add_book("1984", "George Orwell", "12345")
library.add_book("To Kill a Mockingbird", "Harper Lee", "67890")

# Registering members
library.register_member("Alice", "M001")
library.register_member("Bob", "M002")

# Borrowing and returning books
member = library.find_member("M001")
if member:
    library.list_available_books()
    member.borrow_book(library.books[0])  # Borrowing '1984'
    member.list_borrowed_books()

# Listing available books after borrowing
library.list_available_books()

# Returning the book
member.return_book(library.books[0])

library.list_available_books()
