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
'''
Classes:
class Book
- title, author, ISBN
class Library
- collection
- Methods: add_book, remove_book, search_book
Relationships:
- library --> Many books

'''

from enum import Enum


class CollectionType(Enum):
    BOOK = "book"

class Book:
    def __init__(self, title: str, author: str, ISBN: str):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.active = True

    def __repr__(self):
        return f"{self.title, self.author, self.ISBN, self.active}"

class Library:
    def __init__(self):
        self.collection = {
            CollectionType.BOOK: {}
        }

    def add_book(self, title: str, author: str, ISBN: str) -> Book:
        book = Book(title=title, author=author, ISBN=ISBN)
        self.collection[CollectionType.BOOK][ISBN] = book
        return book

    def remove_book(self, ISBN: str) -> bool:
        if ISBN not in self.collection[CollectionType.BOOK]:
            raise Exception(f"{ISBN} not found.")

        self.collection[CollectionType.BOOK][ISBN].active = False
        return True

    def search_book(self, keyword: str) -> list[Book]:
        books = [self.collection[CollectionType.BOOK][book.ISBN] for book in self.collection[CollectionType.BOOK].values() if keyword.lower() in book.title.lower() and book.active]
        return books or f"No books found with {keyword}."




if __name__ == '__main__':
    book_collection = Library()
    book_collection.add_book("Harry Potter 1", "JK Rowling", "1234")
    book_collection.add_book("Harry Potter 2", "JK Rowling", "12341")
    book_collection.add_book("Harry Potter 3", "JK Rowling", "1232")
    book_collection.add_book("Demons and Dragons", "Foo Bar", "1233")
    book_collection.add_book("The Best life ever", "Bar stool", "1235")
    print(book_collection.collection)
    book_collection.search_book("Harry")
    book_collection.remove_book("1233")
    book_collection.search_book("")
    book_collection.remove_book("1")
