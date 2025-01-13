from collections import defaultdict
from threading import RLock # For Thread Safety
from uuid import uuid4
import re


class Book:
    def __init__(self, title: str, author: str, ISBN: str):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def __repr__(self):
        return f"Book(ISBN={self.ISBN}, title={self.title}, author={self.author})"


class Library:
    def __init__(self):
        self.books = {}  # ISBN -> Book
        self.inverted_index = defaultdict(set)  # Word -> Set of ISBNs
        self.lock = RLock()  # Thread-safety for concurrent operations

    def add_book(self, title: str, author: str) -> Book:
        with self.lock:
            ISBN = str(uuid4())
            book = Book(title=title, author=author, ISBN=ISBN)
            self.books[ISBN] = book

            # Update the inverted index
            for word in self._tokenize(title):
                self.inverted_index[word].add(ISBN)
            return book

    def remove_book(self, ISBN: str) -> bool:
        with self.lock:
            if ISBN not in self.books:
                raise KeyError(f"Book with ISBN {ISBN} not found.")

            book = self.books.pop(ISBN)

            # Remove references from the inverted index
            for word in self._tokenize(book.title):
                self.inverted_index[word].discard(ISBN)
                if not self.inverted_index[word]:  # Clean up empty entries
                    del self.inverted_index[word]
            return True

    def search_books(self, keyword: str) -> list:
        keyword = keyword.lower()
        if keyword not in self.inverted_index:
            return []

        # Retrieve books based on ISBNs from the inverted index
        return [self.books[ISBN] for ISBN in self.inverted_index[keyword]]

    def _tokenize(self, text: str) -> list:
        """Tokenize the text into words, removing punctuation and converting to lowercase."""
        return re.findall(r'\w+', text.lower())


# Example Usage
if __name__ == "__main__":
    library = Library()

    # Add books
    library.add_book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
    library.add_book("Harry Potter and the Chamber of Secrets", "J.K. Rowling")
    library.add_book("The Hobbit", "J.R.R. Tolkien")

    # Search for books
    print("Search 'Harry':", library.search_books("Harry"))
    print("Search 'Hobbit':", library.search_books("Hobbit"))

    # Remove a book
    library.remove_book(list(library.books.keys())[0])
    print("After Removal:", library.books)
