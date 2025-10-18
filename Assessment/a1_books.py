"""
CP1404 Assignment 1 - Books to Read
Name: [Your Name Here]
Date Started: [Date]
GitHub URL: [Your GitHub URL]
"""

# Constants for book status
UNREAD = 'u'
COMPLETED = 'c'

# Menu choice constants
MENU_DISPLAY = 'D'
MENU_ADD = 'A'
MENU_COMPLETE = 'C'
MENU_QUIT = 'Q'

# File constants
FILENAME = "books.csv"


def main():
    """Main program to manage a reading list of books."""
    print( "Books to Read 1.0 by [Your Name Here]" )
    books = load_books( FILENAME )
    print( f"{len( books )} books loaded." )

    # Main menu loop
    menu_choice = ""
    while menu_choice.upper() != MENU_QUIT:
        display_menu()
        menu_choice = input( ">>> " ).strip()

        if menu_choice.upper() == MENU_DISPLAY:
            display_books( books )
        elif menu_choice.upper() == MENU_ADD:
            add_book( books )
        elif menu_choice.upper() == MENU_COMPLETE:
            complete_book( books )
        elif menu_choice.upper() == MENU_QUIT:
            save_books( FILENAME, books )
            print( f"{len( books )} books saved to {FILENAME}" )
            print( '"So many books, so little time. Frank Zappa"' )
        else:
            print( "Invalid menu choice" )


def display_menu():
    """Display the main menu options."""
    print( "Menu:" )
    print( f"{MENU_DISPLAY} - Display books" )
    print( f"{MENU_ADD} - Add a new book" )
    print( f"{MENU_COMPLETE} - Complete a book" )
    print( f"{MENU_QUIT} - Quit" )


def load_books(filename):
    """Load books from CSV file into a list of lists.

    Args:
        filename: The name of the CSV file to load from

    Returns:
        A list of lists where each book is [title, author, pages(int), status]
    """
    books = []
    with open( filename, 'r' ) as file:
        for line in file:
            parts = line.strip().split( ',' )
            # Convert pages to integer for calculations
            books.append( [parts[0], parts[1], int( parts[2] ), parts[3]] )
    return books


def save_books(filename, books):
    """Save books to CSV file.

    Args:
        filename: The name of the CSV file to save to
        books: List of lists containing book data
    """
    with open( filename, 'w' ) as file:
        for book in books:
            file.write( f"{book[0]},{book[1]},{book[2]},{book[3]}\n" )


def display_books(books):
    """Display all books with completion status and reading statistics.

    Books are displayed with proper column alignment based on the longest
    title and author in the list. Unread books are marked with *.

    Args:
        books: List of lists containing book data
    """
    if not books:
        print( "No books in the list." )
        return

    # Calculate column widths for neat alignment
    max_title_length = max( len( book[0] ) for book in books )
    max_author_length = max( len( book[1] ) for book in books )

    # Sort: completed books first, then by title alphabetically
    sorted_books = sorted( books, key=lambda x: (x[3], x[0]) )

    # Track unread statistics
    unread_pages = 0
    unread_count = 0

    # Display each book with proper formatting
    for i, book in enumerate( sorted_books, 1 ):
        title, author, pages, status = book
        mark = "*" if status == UNREAD else " "
        print( f"{mark}{i}. {title:{max_title_length}} by {author:{max_author_length}} {pages:>4} pages" )

        if status == UNREAD:
            unread_pages += pages
            unread_count += 1

    # Display reading statistics
    if unread_count > 0:
        print( f"You still need to read {unread_pages} pages in {unread_count} books." )
    else:
        print( "No books left to read. Why not add a new book?" )


def add_book(books):
    """Add a new book to the collection with input validation.

    Prompts for title, author, and pages with appropriate error checking.
    New books are always marked as unread.

    Args:
        books: List of lists containing book data
    """
    # Get and validate title
    title = get_non_blank_input( "Title: " )

    # Get and validate author
    author = get_non_blank_input( "Author: " )

    # Get and validate pages
    pages = get_positive_integer( "Number of Pages: " )

    # Add new book as unread
    books.append( [title, author, pages, UNREAD] )
    print( f"{title} by {author} ({pages} pages) added." )


def get_non_blank_input(prompt):
    """Get non-blank input from user with validation.

    Args:
        prompt: The prompt message to display to the user

    Returns:
        A non-blank string entered by the user
    """
    user_input = ""
    while not user_input:
        user_input = input( prompt ).strip()
        if not user_input:
            print( "Input can not be blank" )
    return user_input


def get_positive_integer(prompt):
    """Get a positive integer from user with validation.

    Args:
        prompt: The prompt message to display to the user

    Returns:
        A positive integer entered by the user
    """
    number = None
    while number is None:
        try:
            number_input = input( prompt ).strip()
            number = int( number_input )
            if number <= 0:
                print( "Number must be > 0" )
                number = None
        except ValueError:
            print( "Invalid input - please enter a valid number" )
            number = None
    return number


def complete_book(books):
    """Mark a book as completed with validation.

    Displays the book list, prompts for a book number, and marks it as completed.
    Validates that the book number is valid and the book is not already completed.

    Args:
        books: List of lists containing book data
    """
    # Check if there are any unread books
    unread_books = [book for book in books if book[3] == UNREAD]

    if not unread_books:
        print( "No unread books - well done!" )
        return

    # Display current books and statistics
    display_books( books )

    # Get and validate book number
    book_number = None
    while book_number is None:
        try:
            number_input = input( "Enter the number of a book to mark as completed\n>>> " ).strip()
            book_number = int( number_input )

            # Sort books the same way as display for correct numbering
            sorted_books = sorted( books, key=lambda x: (x[3], x[0]) )

            # Validate book number
            if book_number <= 0:
                print( "Number must be > 0" )
                book_number = None
            elif book_number > len( sorted_books ):
                print( "Invalid book number" )
                book_number = None
            else:
                selected_book = sorted_books[book_number - 1]

                # Check if book is already completed
                if selected_book[3] == COMPLETED:
                    print( "That book is already completed" )
                    book_number = None
                else:
                    # Find the book in the original list and mark as completed
                    for book in books:
                        if book == selected_book:
                            book[3] = COMPLETED
                            print( f"{book[0]} by {book[1]} completed!" )
                            break
        except ValueError:
            print( "Invalid input - please enter a valid number" )
            book_number = None


if __name__ == '__main__':
    main()