my_string = "Hello, world!"
print(my_string)

single_quote_string = 'Hello, world!'

string_with_qoutes = "Hello, it's me." # Cuando se utiliza un ' en el string si o si se deben usar ""
another_with_quotes = 'He said "You are amazing!" yesterday.' # Cuando se utiliza un " en el string si o si se deben usar ''

escaped_quotes = "He said \"You are amazing\" yesterday."

#------ String formating -----

# concatenacion
name = 'Jose'
greeting = 'Hello, ' + name
print(greeting)

# f strings
another_greeting = f'Hello, {name}'
print(another_greeting)

# Format
format_greeting = 'How are you, {}?'.format(name)
print(format_greeting)

"""
Recomendación: Si se utiliza python 3.6 o superior utilizar los f strings, 
si se utiliza python 3.5 o inferior utilizar format. 
Tratar de no usar la concatenación
"""



