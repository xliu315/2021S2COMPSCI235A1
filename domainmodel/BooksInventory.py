from Author import Author
from book import Book
from publisher import Publisher

class BooksInventory:
    def __init__(self):
        self.__bookId = {}
        self.__id_price = {}

    def add_book(self, book, price, nr_books_in_stock):
        if book.book_id not in self.__id_price.keys():
            self.__id_price[book.book_id] = [price, nr_books_in_stock]
            self.__bookId[book.title] = [price, nr_books_in_stock]
        else:
            count = self.__id_price[book.book_id][1]
            self.__id_price[book.book_id] = [price, nr_books_in_stock + count, book]

    def remove_book(self, book_id):
        if book_id in self.__id_price.keys():
            self.__id_price.pop(book_id)
        else:
            return None

    def find_book(self, book_id):
        if book_id in self.__id_price.keys():
            return self.__id_price[book_id][2]
        else:
            return None

    def find_price(self, book_id):
        if book_id in self.__id_price.keys():
            return self.__id_price[book_id][0]
        else:
            return None

    def find_stock_count(self, book_id):
        if book_id in self.__id_price.keys():
            return self.__id_price[book_id][1]
        else:
            return None

    def search_book_by_title(self, title):
        if title in self.__bookId.keys():
            return self.find_book(self.__bookId[title])
        else:
            return None

def main():
    inventory = BooksInventory()

    publisher1 = Publisher("Avatar Press")

    book1 = Book(17, "Lord of the Rings")
    book1.publisher = publisher1

    book2 = Book(64, "Our Memoires")
    book2.publisher = publisher1

    inventory.add_book(book1, 20, 7)
    inventory.add_book(book2, 30, 2)

    print(inventory.find_price(64))
    print(inventory.find_stock_count(17))
    print(inventory.find_book(99))

main()