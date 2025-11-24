"""This file shows the BookCollection class."""

import json
from book import Book


class BookCollection:
    def __init__(self):
        self.books = []

    def load_books(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for item in data:
                    try:
                        book = Book(item['title'], item['author'], item['pages'], item['status'])
                        self.books.append(book)
                    except KeyError as e:
                        print(f"Missing key in book data: {e}")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty book collection.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Please check the file format.")
