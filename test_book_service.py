import unittest
from book_service import BookService, DuplicateBookError


class TestBookService(unittest.TestCase):

    def setUp(self):
        self.service = BookService()

    def test_successful_book_addition(self):
        self.service.add_book(1, "Clean Code", "Robert C. Martin")
        book = self.service.get_book(1)

        self.assertIsNotNone(book)
        self.assertEqual(book["title"], "Clean Code")
        self.assertEqual(book["author"], "Robert C. Martin")

    def test_duplicate_book_addition_raises_error(self):
        self.service.add_book(1, "Clean Code", "Robert C. Martin")

        with self.assertRaises(DuplicateBookError):
            self.service.add_book(1, "The Pragmatic Programmer", "Andrew Hunt")


if __name__ == "__main__":
    unittest.main()

