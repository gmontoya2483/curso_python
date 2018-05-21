from Section_11_Web_Scraping.ProjectQuotesScraper.locators.quote_locators import QuoteLocators
from bs4 import BeautifulSoup


class QuoteParser:
    """
    Given one of the specific quote divs, find out the data about the quote (quote content, author, tags).
    """

    def __init__(self, page_section: BeautifulSoup):
        self.page_section = page_section

    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}>'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.page_section.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.page_section.select_one(locator).string

    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        return [tag.string for tag in self.page_section.select(locator)]






