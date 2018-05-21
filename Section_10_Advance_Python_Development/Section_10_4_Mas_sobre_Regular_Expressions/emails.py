import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
gabi.montoya@gmail.com.ar
'''

if __name__ == '__main__':

    pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    matches = pattern.finditer(emails)
    for match in matches:
        print(match)
        print(match.group(0))