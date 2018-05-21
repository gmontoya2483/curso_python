import requests
from Section_11_Web_Scraping.ProjectQuotesScraper.pages.quotes_page import QuotePage


if __name__ == '__main__':
    page_content = requests.get('http://quotes.toscrape.com').content
    page = QuotePage(page_content)

    for quote in page.quotes:
        print(quote)
