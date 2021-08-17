from publisher import Publisher
from Author import Author
class Book:
    def __init__(self, bookID, bookName):
        self.title = ''
        self.book_id = bookID
        self.description = ''
        self.publisher = Publisher(bookName)
        self.authors = []
        self.release_year = 0
        self.ebook = True

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, name):
        if isinstance(name, str) and len(name.strip()) > 0 and name is not None:
            self.title = name
        else:
            raise ValueError

    def __repr__(self):
        return f'<Book {self.title}, book id = {self.book_id}>'

    def add_author(self, author):
        if isinstance(author, Author) and author not in self.authors:
            self.authors.append(author)

def main():
    book = Book(84765876, "Harry Potter")
    print(book)

    publisher = Publisher("Bloomsbury")
    book.publisher = publisher
    print(book.publisher)

    author = Author(635, "J.K. Rowling")
    book.add_author(author)
    print(book.authors)
main()