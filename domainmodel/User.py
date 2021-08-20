from Author import Author
from book import Book
from Review import Review
from publisher import Publisher

class User:
    def __init__(self, user, password):
        self.__user_name = None
        self.__password = None
        self.__read_books = []
        self.__reviews = []
        self.__pages_read = 0
        if isinstance(user, str) and len(user.strip()) > 0:
            self.__user_name = user.strip().lower()
        else:
            self.__user_name = None
        if isinstance(password, str) and len(password.strip()) >= 7:
            self.__password = password
        else:
            self.__password = None

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password(self):
        return self.__password

    @property
    def read_books(self):
        return self.__read_books

    @property
    def reviews(self):
        return self.__reviews

    @property
    def pages_read(self):
        return self.__pages_read

    def read_a_book(self, book):
        if isinstance(book, Book):
            if book not in self.__read_books:
                self.__read_books.append(book)
                self.__pages_read += book.num_pages

    def add_review(self, review):
        if isinstance(review, Review):
            if review not in self.__reviews:
                self.__reviews.append(review)

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__user_name == other.__user_name

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(self.__user_name)
