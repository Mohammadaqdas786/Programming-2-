"""This file is book class with attributes of the books title,author,number of page."""

class Book:
    def __init__(self, title, author, pages, status="u"):
        self.title = title
        self.author = author
        self.pages = pages
        self.status = status  # 'u' for unread, 'c' for completed

    def mark_completed(self):
        self.status = "c"

    def mark_unread(self):
        self.status = "u"

    def is_long(self):
        return self.pages >= 500

    def __str__(self):
        return f"{self.title} by {self.author} ({self.pages} pages) - {'Completed' if self.status == 'c' else 'Unread'}"