import unittest
from book_service2 import BookService, BookNotAvailableError


class TestBookBorrowing(unittest.TestCase):

    def setUp(self):
        self.service = BookService()
        self.service.add_book(1, "Clean Code", "Robert C. Martin")

    def test_borrowing_available_book(self):
        self.service.borrow_book(1)
        self.assertTrue(self.service.is_book_borrowed(1))

    def test_borrowing_unavailable_book_raises_error(self):
        self.service.borrow_book(1)

        with self.assertRaises(BookNotAvailableError):
            self.service.borrow_book(1)

    def test_returning_book_updates_status(self):
        self.service.borrow_book(1)
        self.service.return_book(1)

        self.assertFalse(self.service.is_book_borrowed(1))


if __name__ == "__main__":
    unittest.main()

