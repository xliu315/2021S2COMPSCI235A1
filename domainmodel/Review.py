from book import Book
from datetime import datetime

class Review:
    def __init__(self, book, review_text, rating):
        self.__book = None
        self.__rating = None
        self.__review_text = "N/A"
        self.__timestamp = datetime.now()

        if isinstance(book, Book):
            self.__book = book

        if isinstance(rating, int) and 1 <= rating <= 5:
            self.__rating = rating
        else:
            raise ValueError

        if isinstance(review_text, str) and len(review_text.strip()) > 0 and review_text is not None:
            self.__review_text = review_text.strip()

    @property
    def book(self):
        return self.__book

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp

    def __repr__(self):
        return f"<Book {self.__book},\nrating = {self.__rating},\ntimestamp = {self.__timestamp}>"

    def __eq__(self, other):
        return (
                    self.__book == other.__book and self.__review_text == other.__review_text and self.__rating == other.rating and self.timestamp == other.__timestamp)
