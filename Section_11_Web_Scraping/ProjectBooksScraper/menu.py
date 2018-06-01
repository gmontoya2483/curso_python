from Section_11_Web_Scraping.ProjectBooksScraper.app import books


USER_CHOICE = '''

Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the catalogue
- 'q' to exit

Enter your choice: '''


def print_best_books():
    best_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10]  # * -1 ordena en forma descendente,

    print('--- BEST BOOKS ---')
    for book in best_books:
        print(book)


def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: (x.price, x.rating * -1))[:10]  # la tuple es multiple sort

    print('--- CHEAPEST ---')
    for book in cheapest_books:
        print(book)


books_generator = (x for x in books)


def get_next_book():
    print('--- NEXT AVAILABLE ON THE CATALOGUE ---')
    print(next(books_generator))


user_choices ={
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book
}


def print_invalid_option():
    print('--- INVALID OPTION SELECTED ---')
    print('Please choose a valid command.')


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        user_choices.get(user_input, print_invalid_option)()
        user_input = input(USER_CHOICE)


if __name__ == '__main__':
    menu()