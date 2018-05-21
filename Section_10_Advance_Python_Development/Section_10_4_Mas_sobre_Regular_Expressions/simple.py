import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

321--555-4321
321-555-4321
123.555.1234
123*555*1234

800-555-4321
900-555-4321

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'


if __name__ == '__main__':

    # Búsqueda simple
    pattern = re.compile(r'abc')
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)

    print(text_to_search[1:4])
    print('\n')

    # Buscar los .
    pattern = re.compile(r'\.')
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)
    print('\n')


    # Buscar digitos
    pattern = re.compile(r'\d')
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)
    print('\n')

    # Buscar <> digitos
    pattern = re.compile(r'\D')
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)
    print('\n')


    # Buscar Word Characters (a-z, A-Z, 0-9, _)
    pattern = re.compile(r'\w')
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)
    print('\n')

    # Buscar <> Word Characters
    pattern = re.compile(r'\W')
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)
    print('\n')

    # Buscar numeros de telefono
    pattern = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)
    print('\n')

    # Buscar apellidos
    pattern = re.compile(r'(Mr|Ms|Mrs).?\s[A-Z]\w*')
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)
        print(match.group(0))
        print(match.group(1))

    print('\n')




