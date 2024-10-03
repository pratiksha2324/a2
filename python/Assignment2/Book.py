from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        """Adds a new book to the library."""
        self.books.append({
            "title": title,
            "author": author,
            "year": year,
            "checked_out": False,
            "due_date": None
        })

    def checkout_book(self, title, due_date):
        """Checks out a book if available."""
        for book in self.books:
            if book['title'] == title and not book['checked_out']:
                book['checked_out'] = True
                book['due_date'] = due_date
                print(f"Checked out '{title}' until {due_date}.")
                return
        print(f"Book '{title}' is either not available or already checked out.")

    def return_book(self, title):
        """Returns a checked-out book."""
        for book in self.books:
            if book['title'] == title and book['checked_out']:
                book['checked_out'] = False
                book['due_date'] = None
                print(f"Returned '{title}'.")
                return
        print(f"Book '{title}' is not checked out.")

    def list_books(self):
        """Lists all books in the library."""
        print("Library Books:")
        for book in self.books:
            status = "Checked Out" if book['checked_out'] else "Available"
            due_date = book['due_date'] if book['due_date'] else "N/A"
            print(f"Title: {book['title']}, Author: {book['author']} ({book['year']}), Status: {status}, Due Date: {due_date}")

    def overdue_books(self):
        """Lists all overdue books."""
        current_date = datetime.now() + timedelta(days=30)
        print("Overdue Books:")
        for book in self.books:
            if book['checked_out'] and datetime.strptime(book['due_date'], '%Y-%m-%d') < current_date:
                print(f"Title: {book['title']}, Author: {book['author']} ({book['year']}), Due Date: {book['due_date']}")

# Example Usage
library = Library()
library.add_book("Brave New World", "Aldous Huxley", 1932)
library.add_book("The Catcher in the Rye", "J.D. Salinger", 1951)
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
library.checkout_book("Brave New World", "2024-08-20")
library.list_books()
library.overdue_books()
library.return_book("Brave New World")
library.list_books()
