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
        if self.books[book_id]["is_borrowed"]:
            raise BookNotAvailableError("Book already borrowed")

        self.books[book_id]["is_borrowed"] = True

    def return_book(self, book_id):
        self.books[book_id]["is_borrowed"] = False

    def generate_report(self):
        report_lines = []
        header = "Book ID | Title | Author | Status"
        report_lines.append(header)

        for book_id, book in self.books.items():
            status = "Borrowed" if book["is_borrowed"] else "Available"
            line = f"{book_id} | {book['title']} | {book['author']} | {status}"
            report_lines.append(line)

        return "\n".join(report_lines)

