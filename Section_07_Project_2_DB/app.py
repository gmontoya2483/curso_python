from utils import database
import os

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit


Your choice: """


def menu():

    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()

        elif user_input == 'l':
            list_books()

        elif user_input == 'r':
            prompt_read_book()

        elif user_input == 'd':
            prompt_delete_book()

        else:
            print("Unknown command - Please try again.")

        user_input = input(USER_CHOICE)
    else:
        print("Stopping program...")


def prompt_add_book():
    """
    Ask for book name and author
    :return:
    """
    name = input('Enter the book name: ')
    author = input('Enter the author: ')

    database.add_book(name, author)


def list_books():
    """
    Show all the book in our list
    :return:
    """
    books = database.get_all_books()
    print('List of books:')
    for book in books:
        read = 'YES' if book['read'] == '1' else 'NO'
        print(f"{ book['name'].title() } by { book['author'].title() }, read: { read }")


def prompt_read_book():
    """
    Ask for book name and change it to 'Read' in our list
    :return:
    """
    name = input('Enter the name of the book you just finished reading: ')
    database.mark_book_as_read(name)


def prompt_delete_book():
    """
    Ask for book name and delete it to 'Read' in our list
    :return:
    """
    name = input('Enter the name of the book you wish to delete: ')
    database.delete_book(name)


if __name__ == '__main__':
    database.create_book_table()
    menu()
