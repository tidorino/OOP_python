"""
Refactor the provided code, so there is a separate class called Library, which contains books and has
a method called find_book(title) that returns the book with the given title.
Remove the unnecessary code from the Book class.

"""


class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        # self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f'Book title "{self.title}" from {book.author}'


class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def find_book(self, title):
        try:
            return [book for book in self.books if book.title == title][0]
        except IndexError:
            return 'Book not found'


