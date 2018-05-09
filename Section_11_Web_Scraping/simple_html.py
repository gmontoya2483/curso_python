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
