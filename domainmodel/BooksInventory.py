from Author import Author
from book import Book
from publisher import Publisher

class BooksInventory:
    def __init__(self):
        self.__bookId = {}
        self.__id_price = {}

    def add_book(self, book, price, nr_books_in_stock):
        if book.book_id not in self.__id_price.keys():
            self.__id_price[book.book_id] = [price, nr_books_in_stock, book]
            self.__bookId[book.title] = book.book_id
        else:
            count = self.__id_price[book.book_id][1]
            self.__id_price[book.book_id] = [price, nr_books_in_stock + count, book]
            self.__bookId[book.title] = book.book_id

    def remove_book(self, book_id):
        if book_id not in self.__id_price.keys():
            return None
        else:
            self.__id_price.pop(book_id)

    def find_book(self, book_id):
        if book_id not in self.__id_price.keys():
            return None
        else:
            return self.__id_price[book_id][2]

    def find_price(self, book_id):
        if book_id not in self.__id_price.keys():
            return None
        else:
            return self.__id_price[book_id][0]

    def find_stock_count(self, book_id):
        if book_id not in self.__id_price.keys():
            return None
        else:
            return self.__id_price[book_id][1]

    def search_book_by_title(self, title):
        if title not in self.__bookId.keys():
            return None
        else:
            book_id = self.__bookId[title]
            return self.find_book(book_id)

def main():
    inventory = BooksInventory()

    publisher1 = Publisher("Avatar Press")

    book1 = Book(17, "Lord of the Rings")
    book1.publisher = publisher1

    book2 = Book(64, "Our Memoires")
    book2.publisher = publisher1

    book3 = Book(23, "Stome Coming")
    book3.publisher = publisher1
    #book , price , inventory
    inventory.add_book(book1, 20, 7)
    inventory.add_book(book2, 30, 2)
    inventory.add_book(book3, 200, 100)

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