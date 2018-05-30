import requests
from Section_11_Web_Scraping.ProjectBooksScraper.pages.all_books_page import AllBooksPage


if __name__ == '__main__':
    req = requests.get('http://books.toscrape.com')
    print(req.status_code)
    page = AllBooksPage(req.content)

    books = page.books

    for book in books:
        print(book)