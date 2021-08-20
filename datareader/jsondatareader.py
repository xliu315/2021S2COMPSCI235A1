import json


class BooksJSONReader:

    def __init__(self, books_file_name, authors_file_name):
        self.__books = list()
        self.__bookFileName = books_file_name
        self.__authorsFileName = authors_file_name

    @property
    def dataset_of_books(self) -> list:
        return self.__books

    def read_json_files(self):
        author_dict = dict()
        with open(self.__authorsFileName) as file:
            for line in file.readlines():
                data = json.loads(line)
                author_dict[int(data['author_id'])] = data['name']

        with open(self.__bookFileName) as file:
            for line in file.readlines():
                data = json.loads(line)
                book = Book(int(data['book_id']), data['title'])
                book.description = data['description']
                book.publisher = Publisher(data['publisher'])
                if data['is_ebook'] == 'true':
                    book.ebook = True
                else:
                    book.ebook = False

                pub_year = data['publication_year']
                if len(pub_year) != 0:
                    book.release_year = int(pub_year)

                for info in data['authors']:
                    author_id = int(info['author_id'])
                    author = Author(author_id, author_dict[author_id])
                    book.add_author(author)
                self.__books.append(book)

