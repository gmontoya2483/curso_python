from bs4 import BeautifulSoup
from Section_11_Web_Scraping.ProjectBooksScraper.locators.all_books_page_locators import AllBooksPageLocators
from Section_11_Web_Scraping.ProjectBooksScraper.parsers.book_parser import BookParser


class AllBooksPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]

