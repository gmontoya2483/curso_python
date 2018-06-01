import re
import logging

from Section_11_Web_Scraping.ProjectBooksScraper.locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')


class BookParser:
    """
    A class to take in an HTML page (or part of it), and find properties of an item in it
    """

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created...')
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name}, £{self.price}, ({self.rating} stars) >'

    @property
    def name(self):
        logger.debug('Finding book name...')
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        logger.debug(f'Found book name, `{item_name}`.')
        return item_name

    @property
    def link(self):
        logger.debug('Finding book link...')
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator).attrs['href']
        logger.debug(f'Found book link, `{item_link}`.')
        return item_link

    @property
    def price(self):
        logger.debug('Finding book price...')
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string  # £51.77
        logger.debug(f'Found book price str, `{item_price}`.')

        pattern = '£(\d+\.\d+)'
        matches = re.search(pattern, item_price)
        price = float(matches.group(1))
        logger.debug(f'Found book price float, `{price}`.')
        return price

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']  # ['star-rating', 'Three']
        rating_classes = [class_item for class_item in classes if class_item != 'star-rating']
        logger.debug(f'Found book rating str, `{rating_classes[0]}`.')
        rating_number = BookParser.RATINGS.get(rating_classes[0])
        logger.debug(f'Found book rating int, `{rating_number}`.')
        return rating_number

