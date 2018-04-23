"""
Let’s look at how we can extract patterns from text using regular expressions in Python with the `re` module.
"""

import re

#Ejemplo 1

email = 'jose@tecladocode.com'
expression = '[a-z]+'

matches = re.findall(expression, email)
print(matches)

name = matches[0]
domain = f'{matches[1]}.{matches[2]}'


# Ejemplo 2:
email = 'jose@tecladocode.com'
expression = '[a-z\.]+'

matches = re.findall(expression, email)
print(matches)

# Ejemplo 3:
"""
Let’s say you’ve got a price of an item in a strange format (e.g. extracted from a file):
"""
price = 'Price: $189.50'
expression = 'Price: \$(\d+\.\d+)'

matches = re.search(expression, price)
print(matches.group(0))  # entire match
print(matches.group(1))  # first thing around brackets