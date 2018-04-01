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
    database.list_books()


def prompt_read_book():
    """
    Ask for book name and change it to 'Read' in our list
    :return:
    """
    pass


def prompt_delete_book():
    """
    Ask for book name and delete it to 'Read' in our list
    :return:
    """
    pass


if __name__ == '__main__':
    menu()