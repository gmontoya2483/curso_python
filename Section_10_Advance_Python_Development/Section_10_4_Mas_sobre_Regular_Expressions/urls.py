import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

if __name__ == '__main__':

    # Creación de grupos
    pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
    matches = pattern.finditer(urls)
    for match in matches:
        print(match)
        print(match.group(0))
        print(match.group(1))
        print(match.group(2))
        print(match.group(3))
    print('\n')

    # Substitutions
    pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
    subbed_urls = pattern.sub(r'\2\3', urls)
    print(subbed_urls)
    print('\n')




