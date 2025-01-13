'''
Problem: Design a simple Library Management System

Imagine you're tasked with designing a Library Management System. Your design should support the following features:

A Book class that contains attributes like title, author, and ISBN.
A Library class that can hold a collection of books and allow operations like adding, removing, and searching for books by title, author, or ISBN.
Requirements:

Implement the Book and Library classes.
Use appropriate methods to add, remove, and search for books.
Consider what happens when a book is removed: should it be marked as removed or completely deleted from the system?
Should the Library class use any specific data structure to store the books? Explain why or why not.
Follow-Up:

How would you modify the system to allow multiple libraries with different sets of books, and how would you handle searching across multiple libraries?
'''




from collections import defaultdict


class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.removed = False  # To mark if a book is removed

    def get_book(self) -> dict:
        return {"title": self.title, "author": self.author, "ISBN": self.ISBN}

    def mark_removed(self):
        self.removed = True

class Library:
    def __init__(self):
        self.books_by_title = {}
        self.books_by_author = {}
        self.books_by_isbn = {}

    def add_book(self, book: Book):
        # Store the book in all three dictionaries
        self.books_by_title[book.title] = book
        self.books_by_author[book.author] = book
        self.books_by_isbn[book.ISBN] = book

    def remove_book(self, title: str, author: str, isbn: str):
        if title in self.books_by_title:
            self.books_by_title[title].mark_removed()
        if author in self.books_by_author:
            self.books_by_author[author].mark_removed()
        if isbn in self.books_by_isbn:
            self.books_by_isbn[isbn].mark_removed()

    def get_book_by_title(self, title: str):
        return self.books_by_title.get(title)

    def get_book_by_author(self, author: str):
        return self.books_by_author.get(author)

    def get_book_by_isbn(self, isbn: str):
        return self.books_by_isbn.get(isbn)

    def display_books(self):
        # Display books that are not removed
        for book in self.books_by_title.values():
            if not book.removed:
                print(book.get_book())


class ScienceLibrary(Library):
    def __init__(self):
        super().__init__()

    def add_science_book(self, book: Book):
        if "Science" in book.title:  # Assuming a book is of the "Science" genre if the title contains "Science"
            self.add_book(book)
        else:
            print(f"{book.title} is not a Science book.")


if __name__ == '__main__':
    # Create a list of books
    book1 = Book('Harry Potter1', "JK Rowling1", "1231231231")
    book2 = Book('Harry Potter2', "JK Rowling2", "1231231232")
    book3 = Book('Harry Potter3', "JK Rowling3", "1231231233")
    book4 = Book('Harry Potter4', "JK Rowling4", "1231231234")
    book5 = Book('Harry Potter5', "JK Rowling5", "1231231235")
    book6 = Book('Harry Potter6', "JK Rowling6", "1231231236")
    book7 = Book('Harry Potter7', "JK Rowling7", "1231231237")

    # Create a library and add books to it
    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)
    library.add_book(book6)
    library.add_book(book7)

    # Get books by title, author, and ISBN
    print(library.get_book_by_title("Harry Potter1").get_book())
    print(library.get_book_by_author("JK Rowling1").get_book())
    print(library.get_book_by_isbn("1231231231").get_book())

    # Display all books
    print("\nAll Books in Library:")
    library.display_books()

    # Remove a book
    library.remove_book("Harry Potter8", "JK Rowling8", "1231231238")  # This book doesn't exist

    # Display books after removal
    print("\nBooks after removal attempt:")
    library.display_books()




'''
Notes:
1. The Use of defaultdict
While defaultdict is useful for automatically initializing values, it may not be the most appropriate data structure for the Library. This is because defaultdict is typically used to handle missing keys, and in your case, the books should be stored in a way that allows for efficient searching by title, author, or ISBN.
Recommendation:
Instead of using defaultdict, a better structure might be to use a dictionary of dictionaries, or to maintain three separate dictionaries (one for each property: title, author, and ISBN) for faster lookup. Here's why:

Efficient Searching: Using three dictionaries allows you to access books by any of the three properties in constant time, i.e., O(1).
Avoiding Overwriting: In your current implementation, a book is stored in multiple places (by title, author, ISBN), which can lead to overwriting issues when the title, author, or ISBN is duplicated.
2. Storing Books Efficiently
Currently, you are storing books in multiple places based on title, author, and ISBN, which introduces redundancy and the potential for errors (e.g., if there are two books with the same title but different authors, your dictionary will overwrite the previous one). A better approach is to store the book by each property (title, author, ISBN) in separate dictionaries.

Recommended Structure:
You can have three dictionaries:

books_by_title: for searching by title
books_by_author: for searching by author
books_by_isbn: for searching by ISBN
This way, each dictionary will contain the unique keys and map directly to the Book object.

Key Changes:
Separate Dictionaries for Title, Author, and ISBN: Books are now stored separately by each property for faster lookups.
Marking a Book as Removed: Instead of deleting the book from all dictionaries, we mark the book as "removed" and prevent it from being displayed. This allows us to retain historical data and easily track removed books.
display_books Method: Added a method to display books that are not marked as removed.
4. Multiple Libraries (Subclassing)
To extend this system to multiple libraries (e.g., libraries for different genres), you can subclass Library. Here's an example of how you might implement a ScienceLibrary subclass:


'''