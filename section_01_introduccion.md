# Section 01: Introcducción

[VOLVER a README.md](README.md)

## Indice

* [Usar ``repl.it``](#usar-replit)
* [Numbers and printing](#numbers-and-printing)
* [Strings and string formating](#strings-and-string-formating)
* [Getting user input](#getting-user-input)


## Usar ``repl.it``

1. Ir a ``https://repl.it``
2. Registrarse (use cuanta de github)

## Numbers and printing

```python
    a = 1
    b = 2
    c = 3

    my_sum = a + b
    another_sum = 5 + 10

    """
    Las variables puenden contener letras, numeros y underscores
    Pero no pueden empezar con numeros
    """

    # Comentario de una linea


    math_operators = 1 + 3 * 4 / 2 - 2
    print (math_operators)


    float_division = 12 / 3
    print (float_division)

    integer_division = 12 // 3
    print (integer_division)

    division_with_reminder = 12 // 5
    print (division_with_reminder)

    remminder = 12 % 5
    print (remminder)


    x = 37
    remminder = x % 2
    print (remminder)

```

[Video: Numbers and printing](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9412506?start=0)

## Strings and string formating

```python
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
```

[Video: Strings and string formating](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9412510?start=0)

## Getting user input

```python
    your_name = input('Ingrese su nombre: ')

    print(f'Hello {your_name}!!')

    age = int(input('Ingrese su edad: '))
    months = age * 12
    seconds = age * 365 * 24 * 60 *60
    print(f'Usted ha vivido {months} meses.')
    print(f'Usted ha vivido {seconds} segundos.')
```

[Video: Getting user input](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9412514?start=0)