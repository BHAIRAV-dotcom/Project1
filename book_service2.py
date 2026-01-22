class DuplicateBookError(Exception):
    pass


class BookNotAvailableError(Exception):
    pass


class BookService:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise DuplicateBookError("Duplicate Book ID")

        self.books[book_id] = {
            "title": title,
            "author": author,
            "is_borrowed": False
        }

    def borrow_book(self, book_id):
        book = self.books.get(book_id)

        if book["is_borrowed"]:
            raise BookNotAvailableError("Book already borrowed")

        book["is_borrowed"] = True

    def return_book(self, book_id):
        book = self.books.get(book_id)
        book["is_borrowed"] = False

    def is_book_borrowed(self, book_id):
        return self.books[book_id]["is_borrowed"]

