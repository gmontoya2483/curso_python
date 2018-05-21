# Section 11: Web Scraping

[VOLVER a README.md](README.md)

## Indice

* [Understanding HTML con BeautifulSoup](#understanding-html-con-beautifuldsoup)


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