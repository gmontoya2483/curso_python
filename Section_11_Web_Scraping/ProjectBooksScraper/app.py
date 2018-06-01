import requests
import logging

from Section_11_Web_Scraping.ProjectBooksScraper.pages.all_books_page import AllBooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(name)s - %(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y:%H:%M:%S',
                    level=logging.DEBUG,
                    filename='books_scrapper.log'
                    )
logger = logging.getLogger('scraping')


logger.info('Loading books list...')

page_content = requests.get('http://books.toscrape.com').content
page = AllBooksPage(page_content)

books = page.books

for page_num in range(1, page.page_count):
    url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content = requests.get(url).content

    logger.debug('Creating AllBooksPage from page content.')

    page = AllBooksPage(page_content)
    books.extend(page.books)

