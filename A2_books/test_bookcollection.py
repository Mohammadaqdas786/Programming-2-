import unittest
from book import Book
from bookcollection import BookCollection


class TestBookCollection( unittest.TestCase ):
    def setUp(self):
        self.collection = BookCollection()
        self.book1 = Book( "Book One", "Author One", 200 )
        self.book2 = Book( "Book Two", "Author Two", 300 )
        self.collection.add_book( self.book1 )
        self.collection.add_book( self.book2 )

    def test_add_book(self):
        self.assertEqual( len( self.collection.books ), 2 )

    def test_get_number_of_unread_pages(self):
        self.book1.mark_completed()
        self.assertEqual( self.collection.get_number_of_unread_pages(), 300 )

    def test_get_number_of_completed_pages(self):
        self.book1.mark_completed()
        self.assertEqual( self.collection.get_number_of_completed_pages(), 200 )

    def test_load_books(self):
        json_data = [
            {'title': 'Loaded Book', 'author': 'Loaded Author', 'pages': 150, 'completed': False}
        ]
        self.collection.load_books( json_data )
        self.assertEqual( len( self.collection.books ), 3 )


if __name__ == '__main__':
    unittest.main()
