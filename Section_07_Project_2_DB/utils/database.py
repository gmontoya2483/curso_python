"""
Concerned with storing and retrieving books from  list.
"""

books = []


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})


def list_books():
    print('Listado de Libros:')
    for book in books:
        print(f"Book Name: { book['name'] }, author: { book['author'] }, read { book['read'] }")
