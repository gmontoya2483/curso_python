from .database_connection import DatabaseConnection
import sqlite3

"""
Concerned with storing and retrieving books from  a database.
"""

books_file = 'data.db'


def create_book_table():
    with DatabaseConnection(books_file) as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books (name text primary key, author text, read integer)')


def get_all_books():
    with DatabaseConnection(books_file) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * from books")
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    return books


def add_book(name, author):
    with DatabaseConnection(books_file) as connection:
        try:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO books VALUES (?, ?, 0)', (name, author))
        except sqlite3.IntegrityError:
            print('El libro ya existe!!.')


def delete_book(name):
    with DatabaseConnection(books_file) as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name=?', (name,))


def mark_book_as_read(name):
    with DatabaseConnection(books_file) as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))
