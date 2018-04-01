"""
Concerned with storing and retrieving books from  list.
"""

books = []


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})


def list_books():
    return books


def delete_book(name):
    global books
    books = [book for book in books if book['name'].lower() != name.lower()]


def mark_book_as_read(name):
    for book in books:
        if book['name'].lower() == name.lower():
            book['read'] = True
