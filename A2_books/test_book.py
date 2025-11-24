import unittest
from A2_books.book import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("Test Title", "Test Author", 300)

    def test_str(self):
        self.assertEqual(str(self.book), "Test Title by Test Author - 300 pages (Unread)")

    def test_mark_completed(self):
        self.book.mark_completed()
        self.assertTrue(self.book.completed)

    def test_mark_unread(self):
        self.book.mark_completed()
        self.book.mark_unread()
        self.assertFalse(self.book.completed)

    def test_is_long(self):
        self.assertFalse(self.book.is_long())
        long_book = Book("Long Book", "Author", 600)
        self.assertTrue(long_book.is_long())


if __name__ == '__main__':
    unittest.main()
