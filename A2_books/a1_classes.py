""" This file to use the Book and BookCollection classes"""


from bookcollection import BookCollection
from A2_books.book import Book


# Main function
def main():
    print("Book to Read 1.0 by Mohammad Aqdas Ayyub Lonbal")
    book_collection = BookCollection()
    book_collection.load_books('books.json')

    while True:
        display_menu()
        user_choice = input(">>> ").lower()

        if user_choice == "d":
            display_books(book_collection)
        elif user_choice == "a":
            add_book(book_collection)
        elif user_choice == "c":
            complete_book(book_collection)
        elif user_choice == "q":
            book_collection.save_books('books.json')
            print('Books saved to books.json')
            print('So many books, so little time. Frank Zappa')
            break
        else:
            print("Invalid choice. Please try again.")


# Function to display the menu
def display_menu():
    print("Menu:")
    print("D - Display books")
    print("A - Add a new book")
    print("C - Complete a book")
    print("Q - Quit")


# Function to display the list of books
def display_books(book_collection):
    print("Books to Read 1.0 by Mohammad Aqdas Ayyub Lonbal")
    unread_count = book_collection.get_unread_count()
    total_pages_remaining = book_collection.get_total_pages_remaining()
    for index, book in enumerate(book_collection.books, 1):
        print(f"{index}. {book}")
    print(f"You still need to read {total_pages_remaining} pages in {unread_count} books.")


# Function to add a new book to the list
def add_book(book_collection):
    print("Add a new book:")
    while True:
        title = input("Title: ").strip()
        if not title:
            print("Input cannot be blank")
            continue

        author = input("Author: ").strip()
        if not author:
            print("Input cannot be blank")
            continue

        while True:
            try:
                pages = int(input("Number of Pages: ").strip())
                if pages <= 0:
                    print("Number must be > 0")
                    continue
                break
            except ValueError:
                print("Invalid input - please enter a valid number")

        book = Book(title, author, pages)
        book_collection.add_book(book)
        print(f"{title} by {author} ({pages} pages) added.")
        break


# Function to mark a book as completed
def complete_book(book_collection):
    display_books(book_collection)
    unread_books = [index for index, book in enumerate(book_collection.books, 1) if book.status == "u"]
    if not unread_books:
        print("No unread books - well done!")
        return
    while True:
        try:
            book_choice = int(input("Enter the number of the book to mark as completed: "))
            if book_choice not in unread_books:
                raise ValueError("Invalid book number")
            break
        except ValueError as e:
            print("Error:", e)
    book_collection.books[book_choice - 1].mark_completed()
    print(f"{book_collection.books[book_choice - 1].title} marked as completed.")


if __name__ == "__main__":
    main()
