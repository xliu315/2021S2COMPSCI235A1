from publisher import Publisher
from Author import Author


class Book:
    def __init__(self, bookID, bookName):
        self.__title = None
        self.__book_id = None
        self.__description = None
        self.__publisher = None
        self.__authors = []
        self.__release_year = None
        self.__ebook = False
        if isinstance(bookID, int):
            self.__book_id = bookID
        else:
            raise ValueError
        if isinstance(bookName, str) and len(bookName.strip()) > 0 and bookName is not None:
            self.__title = bookName
        else:
            raise ValueError

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, name):
        if isinstance(name, str) and len(name.strip()) > 0 and name is not None:
            self.__title = name
        else:
            raise ValueError

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, des):
        if isinstance(des, str) and len(des.strip()) > 0 and des is not None:
            self.__description = des
        else:
            raise ValueError

    @property
    def book_id(self):
        return self.__book_id

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, authors):
        self.__authors = authors

    @property
    def release_year(self):
        return self.__release_year

    @release_year.setter
    def release_year(self, year):
        if isinstance(year, int) and year > 0 and year is not None:
            self.__release_year = year
        else:
            raise ValueError

    @property
    def ebook(self):
        return self.__ebook

    @ebook.setter
    def ebook(self, book):
        if isinstance(book, bool) and book is not None:
            self.__ebook = book
        else:
            raise ValueError

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, pub):
        self.__publisher = pub

    def __repr__(self):
        return f'<Book {self.__title}, book id = {self.__book_id}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return self.__book_id == other.__book_id

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return self.__book_id < other.__book_id

    def __hash__(self):
        return hash(self.__book_id)

    def add_author(self, author):
        if isinstance(author, Author) and author not in self.__authors:
            self.__authors.append(author)

    def remove_author(self, author):
        if isinstance(author, Author) and author in self.__authors:
            self.__authors.remove(author)


class Publisher:

    def __init__(self, publisher_name: str):
        self.__name = ''
        if not isinstance(publisher_name, str) or len(publisher_name.strip()) == 0:
            self.__name = "N/A"
        else:
            self.__name = publisher_name.strip()

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, publisher_name):
        # TODO
        self.__name = publisher_name

    def __repr__(self):
        # we use access via the property here
        return f'<Publisher {self.__name}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.__name == self.__name

    def __lt__(self, other):
        # TODO

        return self.__name < other.__name

    def __hash__(self):
        # TODO
        return hash(self.__name)


class Author:
    def __init__(self, authorId, author_name):
        self.coauthor_list = []
        if isinstance(authorId, int) and authorId >= 0 and authorId is not None:
            self.author_id = authorId
        else:
            raise ValueError
        if isinstance(author_name, str) and len(author_name.strip()) > 0 and author_name is not None:
            self.author_full_name = author_name
        else:
            raise ValueError

    @property
    def full_name(self):
        return self.author_full_name

    @full_name.setter
    def full_name(self, author_name):
        if isinstance(author_name, str) and len(author_name.strip()) > 0 and author_name is not None:
            self.author_full_name = author_name
        else:
            raise ValueError

    @property
    def unique_id(self):
        return self.author_id

    def __repr__(self):
        return f'<Author {self.author_full_name}, author id = {self.author_id}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.author_id == self.author_id

    def __lt__(self, other):
        return self.author_id < other.author_id

    def __hash__(self):
        return hash(self.author_id)

    def add_coauthor(self, coauthor):
        if coauthor not in self.coauthor_list:
            self.coauthor_list.append(coauthor)
            coauthor.coauthor_list.append(self)

    def check_if_this_author_coauthored_with(self, name):
        return name in self.coauthor_list
