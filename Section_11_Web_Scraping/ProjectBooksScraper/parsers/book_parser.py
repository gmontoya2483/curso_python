import re
from Section_11_Web_Scraping.ProjectBooksScraper.locators.book_locators import BookLocators


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
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name}, £{self.price}, ({self.rating} stars) >'

    @property
    def name(self):
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator).attrs['href']
        return item_link

    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string  # £51.77

        pattern = '£(\d+\.\d+)'
        matches = re.search(pattern, item_price)
        return float(matches.group(1))

    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']  # ['star-rating', 'Three']
        rating_classes = [class_item for class_item in classes if class_item != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])
        return rating_number

