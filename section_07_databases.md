# Section 07: Databases

[VOLVER a README.md](README.md)

## Indice

* [Milestone: Project 2 (en memoria)](#milestone-project-2-en-memoria)
* [Milestone: Project 2 (en un CSV file)](#milestone-project-2-en-un-csv-file)
* [Milestone: Project 2 (en un Json file)](#milestone-project-2-en-un-json-file)
* [Developing Context Manager](#developing-context-manager)

## Milestone: Project 2 (en memoria)

[Video: Intro a Milestone Project 2](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445314?start=0)  
[Video: Milestone Project 2 with list](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445318?start=0)

## Milestone: Project 2 (en un CSV file)

[Video: Milestone Project 2 with a csv file](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445320?start=0)

## Milestone: Project 2 (en un Json file)

[Video: Milestone Project 2 with a JSON file](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445324?start=0)

## Developing context manager

```python
import sqlite3

class DatabaseConnection:

    def __init__(self, database):
        self.database = database
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.database)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()

```


```python
from .database_connection import DatabaseConnection

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
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES (?, ?, 0)', (name, author))


def delete_book(name):
    with DatabaseConnection(books_file) as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name=?', (name,))


def mark_book_as_read(name):
    with DatabaseConnection(books_file) as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))
```


[Video: Developing Context Manager](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445376?start=0)
[Video: Errors Context Manager](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445380?start=0)
