import requests
from Section_11_Web_Scraping.ProjectBooksScraper.pages.all_books_page import AllBooksPage

page_content = requests.get('http://books.toscrape.com').content
page = AllBooksPage(page_content)

books = page.books


