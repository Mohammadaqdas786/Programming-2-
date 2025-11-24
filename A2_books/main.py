"""
Name:Mohammad Aqdas Ayyub Lonbal
Date: 13/05/2004
Brief Project Description: The program will manage a collection of books, allowing users to add,
sort, and track their reading progress. Students will use classes, handle JSON files
for saving data, and follow coding best practices while using Git for version control.
GitHub URL:https://github.com/cp1404-students/a2-books-Mohammadaqdas786
"""

import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from book import Book
from bookcollection import BookCollection


class BookApp(App):
    def build(self):
        self.collection = BookCollection()
        self.load_books()

        layout = BoxLayout(orientation='vertical')
        self.status_label = Label(text="Welcome to the Book Tracker!")
        layout.add_widget(self.status_label)

        self.title_input = TextInput(hint_text='Book Title')
        layout.add_widget(self.title_input)

        self.author_input = TextInput(hint_text='Author')
        layout.add_widget(self.author_input)

        self.pages_input = TextInput(hint_text='Number of Pages')
        layout.add_widget(self.pages_input)

        add_button = Button(text='Add Book')
        add_button.bind(on_press=self.add_book)
        layout.add_widget(add_button)

        self.book_buttons = BoxLayout(orientation='vertical')
        layout.add_widget(self.book_buttons)

        self.update_book_buttons()

        return layout

    def add_book(self, instance):
        title = self.title_input.text
        author = self.author_input.text
        try:
            pages = int(self.pages_input.text)
            if pages <= 0:
                self.status_label.text = "The book must have some pages!"
                return
        except ValueError:
            self.status_label.text = "Please enter a valid number."
            return

        if not title or not author:
            self.status_label.text = "Please complete all fields."
            return

        book = Book(title, author, pages)
        self.collection.add_book(book)
        self.update_book_buttons()
        self.title_input.text = ''
        self.author_input.text = ''
        self.pages_input.text = ''
        self.status_label.text = "Book added successfully!"

    def update_book_buttons(self):
        self.book_buttons.clear_widgets()
        for book in self.collection.books:
            button = Button(text=str(book))
            button.bind(on_press=lambda instance, b=book: self.toggle_book(b))
            self.book_buttons.add_widget(button)

    def toggle_book(self, book):
        if book.completed:
            book.mark_unread()
        else:
            book.mark_completed()
        self.update_book_buttons()

    def load_books(self):
        try:
            with open('books.json', 'r') as f:
                data = json.load(f)
                self.collection.load_books(data)
        except FileNotFoundError:
            self.status_label.text = "No books found, start adding some!"

    def on_stop(self):
        with open('books.json', 'w') as f:
            json.dump(self.collection.save_books(), f)


if __name__ == '__main__':
    BookApp().run()
