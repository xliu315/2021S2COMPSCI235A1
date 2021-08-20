import json
from domainmodel.book import Book
from domainmodel.publisher import Publisher
from domainmodel.Author import Author

class BooksJSONReader:
    def __init__(self, books_file_name, authors_file_name):
        self.__books = list()
        self.__books_file_name = books_file_name
        self.__authors_file_name = authors_file_name

    @property
    def dataset_of_books(self):
        return self.__books

    def read_json_files(self):
        author_dict = dict()
        with open(self.__authors_file_name) as f:
            for line in f.readlines():
                author_data = json.loads(line)
                author_dict[int(author_data['author_id'])] = author_data['name']

        with open(self.__books_file_name) as f:
            for line in f.readlines():
                data = json.loads(line)
                book = Book(int(data['book_id']), data['title'])
                book.description = data['description']
                book.publisher = Publisher(data['publisher'])

                if data['is_ebook'] == 'true':
                    book.ebook = True
                else:
                    book.ebook = False

                if len(data['publication_year']) != 0:
                    book.release_year = int(data['publication_year'])

                for author_info in data['authors']:
                    author_id = int(author_info['author_id'])
                    author = Author(int(author_id), author_dict[author_id])
                    book.add_author(author)
                self.__books.append(book)


def main():
    authors_filename = '/data/book_authors_excerpt.json'
    books_filename = '/data/comic_books_excerpt.json'
    reader = BooksJSONReader(books_filename, authors_filename)
    reader.read_json_files()

    print(reader.dataset_of_books[0])
    print(reader.dataset_of_books[10])
    print(reader.dataset_of_books[19])
    print(reader.dataset_of_books[4].publisher)
    print(reader.dataset_of_books[15].authors[0])
main()