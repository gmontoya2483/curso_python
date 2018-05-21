# Section 11: Web Scraping

[VOLVER a README.md](README.md)

## Indice

* [Understanding HTML con BeautifulSoup](#understanding-html-con-beautifuldsoup)
* [More complex Html parsing](#more-complex-html-parsing)
* [Estructurar el parseador en forma correcta](#estructurar-el-parseador-en-forma-correcta)
* [Extraer los locators](#extraer-los-locators)
* [Entendiendo HTML usando el browser](#entendiendo-html-usando-el-browser)
* [Scrapping our first WebSite](#scrapping-our-first-website)


## Understanding HTML con BeautifulSoup

* Instalar la libreria ``beautifulsoup4``

![Python banner](documentation/add_beatifulsoup4.png)

* Ejemplo Simple como usar BeautifulSoup:

```python
from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''


simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

# Find a simple element
print(simple_soup.find('h1'))
print(simple_soup.find('h1').string)
print(simple_soup.find('li'))
print('\n')

# Find multiple elements
all_lis = simple_soup.find_all('li')
for li in all_lis:
    print(li)
    print(li.string)
print('\n')
```

**OUTPUT:**

```console
<h1>This is a title</h1>
This is a title
<li>Rolf</li>


<li>Rolf</li>
Rolf
<li>Charlie</li>
Charlie
<li>Jen</li>
Jen
<li>Jose</li>
Jose



Process finished with exit code 0
```

```python
from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''


simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)


def find_list_items():
    list_items = [item.string for item in simple_soup.find_all('li')]
    print(list_items)


def find_all_paragraphs():
    all_paragraphs = [paragraph.string for paragraph in simple_soup.find_all('p')]
    print(all_paragraphs)


def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph.string)


def find_other_paragraph():
    all_paragraphs = simple_soup.find_all('p')
    other_paragraphs = [paragraph.string for paragraph in all_paragraphs if 'subtitle' not in paragraph.attrs.get('class', [])]
    print(other_paragraphs)


if __name__ == '__main__':
    find_title()
    find_list_items()
    find_all_paragraphs()
    find_subtitle()
    find_other_paragraph()
```

**OUTPUT:**

```console
This is a title
['Rolf', 'Charlie', 'Jen', 'Jose']
['Lorem ipsum dolor sit amet. Consectetur edipiscim elit.', "Here's another p without a class"]
Lorem ipsum dolor sit amet. Consectetur edipiscim elit.
["Here's another p without a class"]

Process finished with exit code 0
```

[Video: Understanding HTML con BeautifulSoup](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477874?start=0)

## More complex Html parsing

Los ejemplos siguientes muestran como parsear objetos ``html`` utilizando ``CSS Locators``:

```python
import re
from bs4 import BeautifulSoup


ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html">
                        <img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail">
                    </a>
            </div>
            <p class="star-rating Three">
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
            </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
                <p class="price_color">£51.77</p>
                <p class="instock availability">
                    <i class="icon-ok"></i>
                    In stock
                </p>
                <form>
                    <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
                </form>
            </div>
    </article>
</li>
</body></html>
'''

soup = BeautifulSoup(ITEM_HTML, 'html.parser')


def find_item_name():
    locator = 'article.product_pod h3 a'  # CSS locator
    item_link = soup.select_one(locator)
    item_name = item_link.attrs['title']

    print(item_link)
    print(item_link.string)
    print(item_name)
    print('\n')


def find_item_link():
    locator = 'article.product_pod h3 a'  # CSS locator
    item_link = soup.select_one(locator).attrs['href']
    print(item_link)
    print('\n')


def find_item_price():
    locator = 'article.product_pod div.product_price p.price_color'  # CSS locator
    item_price = soup.select_one(locator).string
    print(item_price)

    pattern = '£(\d+\.\d+)'
    matches = re.search(pattern, item_price)
    print(matches.group(0))  # entire match
    print(float(matches.group(1)))
    print('\n')


def find_item_rating():
    locator = 'article.product_pod p.star-rating'
    star_rating_tag = soup.select_one(locator)
    classes = star_rating_tag.attrs['class']  # ['star-rating', 'Three']
    value = [class_item for class_item in classes if class_item != 'star-rating'][0]
    print(value)
    print('\n')


if __name__ == '__main__':
    find_item_name()
    find_item_link()
    find_item_price()
    find_item_rating()
```
**OUTPUT:**

```console
<a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a>
A Light in the ...
A Light in the Attic


catalogue/a-light-in-the-attic_1000/index.html


£51.77
£51.77
51.77


Three

Process finished with exit code 0
```

[Video: More complex HTML parsing](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477876?start=0)

## Estructurar el parseador en forma correcta

La idea es crear una clase que reciba la pagina o parte de la pagina y llamar propiedades de la clase para obtener los valores.

```python
import re
from bs4 import BeautifulSoup


ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html">
                        <img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail">
                    </a>
            </div>
            <p class="star-rating Three">
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
            </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
                <p class="price_color">£51.77</p>
                <p class="instock availability">
                    <i class="icon-ok"></i>
                    In stock
                </p>
                <form>
                    <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
                </form>
            </div>
    </article>
</li>
</body></html>
'''


class ParsedItem:
    """
    A class to take in an HTML page (or part of it), and find properties of an item in it
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(ITEM_HTML, 'html.parser')

    @property
    def name(self):
        locator = 'article.product_pod h3 a'  # CSS locator
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = 'article.product_pod h3 a'  # CSS locator
        item_link = self.soup.select_one(locator).attrs['href']
        return item_link

    @property
    def price(self):
        locator = 'article.product_pod div.product_price p.price_color'  # CSS locator
        item_price = self.soup.select_one(locator).string

        pattern = '£(\d+\.\d+)'
        matches = re.search(pattern, item_price)
        return float(matches.group(1))

    @property
    def rating(self):
        locator = 'article.product_pod p.star-rating'
        star_rating_tag = self.soup.select_one(locator)
        classes = star_rating_tag.attrs['class']  # ['star-rating', 'Three']
        rating_classes = [class_item for class_item in classes if class_item != 'star-rating']
        return rating_classes[0]


if __name__ == '__main__':
    item = ParsedItem(ITEM_HTML)

    print(item.name)
    print(item.link)
    print(item.rating)
    print(item.price)

```

**OUTPUT:**

```console
A Light in the Attic
catalogue/a-light-in-the-attic_1000/index.html
Three
51.77

Process finished with exit code 0
```
[Video: Estructurando el parseador de una forma m'as ordenada](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477886?start=0)

## Extraer los locators

Al generar una clase que contenga los los locators, facilita el mantenimiento del código en caso que la pagina que se esta haciendo el scrapping cambie debido a que no hay que revisar todo el código sino modificar solo los locators.

```python
import re
from bs4 import BeautifulSoup


ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html">
                        <img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail">
                    </a>
            </div>
            <p class="star-rating Three">
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
            </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
                <p class="price_color">£51.77</p>
                <p class="instock availability">
                    <i class="icon-ok"></i>
                    In stock
                </p>
                <form>
                    <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
                </form>
            </div>
    </article>
</li>
</body></html>
'''


class ParsedItemLocators:
    """
    Locators for an item in the HTML page.
    This allows us to easily see what our code will be looking at
    as well as change it quickly if we notice it is now different.
    """
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod div.product_price p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'


class ParsedItem:
    """
    A class to take in an HTML page (or part of it), and find properties of an item in it
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        locator = ParsedItemLocators.NAME_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = ParsedItemLocators.LINK_LOCATOR  # CSS locator
        item_link = self.soup.select_one(locator).attrs['href']
        return item_link

    @property
    def price(self):
        locator = ParsedItemLocators.PRICE_LOCATOR # CSS locator
        item_price = self.soup.select_one(locator).string

        pattern = '£(\d+\.\d+)'
        matches = re.search(pattern, item_price)
        return float(matches.group(1))

    @property
    def rating(self):
        locator = ParsedItemLocators.RATING_LOCATOR
        star_rating_tag = self.soup.select_one(locator)
        classes = star_rating_tag.attrs['class']  # ['star-rating', 'Three']
        rating_classes = [class_item for class_item in classes if class_item != 'star-rating']
        return rating_classes[0]


if __name__ == '__main__':
    item = ParsedItem(ITEM_HTML)

    print(item.name)
    print(item.link)
    print(item.rating)
    print(item.price)
``` 
**OUTPUT:**

```console
A Light in the Attic
catalogue/a-light-in-the-attic_1000/index.html
Three
51.77

Process finished with exit code 0
```
[Video: Separar los locators de la clase parser:](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477888?start=0)

## Entendiendo HTML usando el browser

[Video: Understanding HTML with the browser](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477890?start=0)

## Scrapping our first WebSite

> **NOTA:** Para poder abrir el contenido de una pagina web es necesario importar la librería ``requests``
```python
import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.example.com/')
print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find('h1').string)
print(soup.select_one('p a').attrs['href'])
```

**OUTPUT:**

```console
b'<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset="utf-8" />\n    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <style type="text/css">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;\n        \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 50px;\n        background-color: #fff;\n        border-radius: 1em;\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        body {\n            background-color: #fff;\n        }\n        div {\n            width: auto;\n            margin: 0 auto;\n            border-radius: 0;\n            padding: 1em;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is established to be used for illustrative examples in documents. You may use this\n    domain in examples without prior coordination or asking for permission.</p>\n    <p><a href="http://www.iana.org/domains/example">More information...</a></p>\n</div>\n</body>\n</html>\n'
Example Domain
http://www.iana.org/domains/example

Process finished with exit code 0

```
[Video: Scrapping our first WebSite](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477894?start=0)


## Referencias:
[Github - tecladocode -complete-python-course](https://github.com/tecladocode/complete-python-course/tree/master/section11/projects)