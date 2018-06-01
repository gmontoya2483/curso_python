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
    for book in best_books:
        print(book)


def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: (x.price, x.rating * -1))[:10]  # la tuple es multiple sort
    for book in cheapest_books:
        print(book)


books_generator = (x for x in books)


def get_next_book():
    print(next(books_generator))


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'b':
            print('--- BEST ---')
            print_best_books()
        elif user_input == 'c':
            print('--- CHEAPEST ---')
            print_cheapest_books()
        elif user_input == 'n':
            print('--- NEXT BOOK IN CATALOGUE ---')
            get_next_book()
        else:
            print('--- INVALID OPTION SELECTED ---')

        user_input = input(USER_CHOICE)


if __name__ == '__main__':
    menu()