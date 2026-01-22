import unittest
from book_service3 import BookService


class TestLibraryReport(unittest.TestCase):

    def setUp(self):
        self.service = BookService()
        self.service.add_book(1, "Clean Code", "Robert C. Martin")

    def test_report_contains_header(self):
        report = self.service.generate_report()
        self.assertIn("Book ID | Title | Author | Status", report)

    def test_report_contains_at_least_one_book_entry(self):
        report = self.service.generate_report()
        self.assertIn("Clean Code", report)


if __name__ == "__main__":
    unittest.main()

