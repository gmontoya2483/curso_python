from bs4 import BeautifulSoup

from Section_11_Web_Scraping.ProjectQuotesScraper.locators.quotes_page_locators import QuotesPageLocators
from Section_11_Web_Scraping.ProjectQuotesScraper.parsers.quote import QuoteParser


class QuotePage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quotes = self.soup.select(locator)
        return [QuoteParser(quote) for quote in quotes]

