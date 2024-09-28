# Class to represent a Book
class Book:
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, Available: {self.is_available}"

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        self.is_available = True

# Class to represent a Member
class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []

    def __str__(self):
        return f"Member: {self.name}, ID: {self.membership_id}, Borrowed Books: {[book.title for book in self.borrowed_books]}"

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"Sorry, {book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} does not have {book.title}.")

# Class to represent the Library
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"Book '{title}' added to the library.")

    def register_member(self, name, membership_id):
        new_member = Member(name, membership_id)
        self.members.append(new_member)
        print(f"Member '{name}' registered.")

    def list_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(book)
        else:
            print("No books available at the moment.")

    def list_borrowed_books(self, member):
        if member.borrowed_books:
            print(f"Borrowed books by {member.name}:")
            for book in member.borrowed_books:
                print(book)
        else:
            print(f"{member.name} has not borrowed any books.")

    def list_members(self):
        if self.members:
            print("List of members:")
            for member in self.members:
                print(member)
        else:
            print("No members registered yet.")

    def find_member(self, membership_id):
        for member in self.members:
            if member.membership_id == membership_id:
                return member
        return None

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

# Main program with user input and validations
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add a new book")
        print("2. Register a new member")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. List available books")
        print("6. List borrowed books by a member")
        print("7. List members")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            library.add_book(title, author, isbn)

        elif choice == "2":
            name = input("Enter member name: ")
            membership_id = input("Enter membership ID: ")
            library.register_member(name, membership_id)

        elif choice == "3":
            if not library.books:
                print("No books available in the library. Please add books first.")
                continue
            if not library.members:
                print("No members registered. Please register a member first.")
                continue
            membership_id = input("Enter membership ID: ")
            member = library.find_member(membership_id)
            if member:
                isbn = input("Enter book ISBN: ")
                book = library.find_book(isbn)
                if book:
                    member.borrow_book(book)
                else:
                    print("Book not found.")
            else:
                print("Member not found.")

        elif choice == "4":
            if not library.books:
                print("No books available in the library.")
                continue
            if not library.members:
                print("No members registered.")
                continue
            membership_id = input("Enter membership ID: ")
            member = library.find_member(membership_id)
            if member:
                isbn = input("Enter book ISBN: ")
                book = library.find_book(isbn)
                if book:
                    member.return_book(book)
                else:
                    print("Book not found.")
            else:
                print("Member not found.")

        elif choice == "5":
            library.list_available_books()

        elif choice == "6":
            if not library.members:
                print("No members registered.")
                continue
            membership_id = input("Enter membership ID: ")
            member = library.find_member(membership_id)
            if member:
                library.list_borrowed_books(member)
            else:
                print("Member not found.")

        elif choice == "7":
            library.list_members()

        elif choice == "8":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    main()
