# Section 01: Introcducción

[VOLVER a README.md](README.md)

## Indice

* [Usar ``repl.it``](#usar-replit)
* [Numbers and printing](#numbers-and-printing)
* [Strings and string formating](#strings-and-string-formating)
* [Getting user input](#getting-user-input)
* [Booleans y comparaciones](#booleans-y-comparaciones)
* [List, tuples and sets](#list-tuples-and-sets)
* [Operaciones avanzadas con sets](#operaciones-avanzadas-con-sets)

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

## Booleans y comparaciones

```python
    truthy = True
    falsy = False

    age = 20
    is_over_age = age>=18
    is_under_age = age < 18
    is_twenty = age == 20

    my_number = 5
    user_number = int(input("Enter a number: "))
    print (f'Are the same: {my_number == user_number}')
    print (f'Are not the same: {my_number != user_number}')

    # -- Combining booleans --
    verdadero = True and True
    falso = True and False
    false = False and False

    """
   `or` is used to get the second value if the first one is False. If the first one is True, it gets the first one.
    por ejemplo:

    cmp = True or 18 -> cmp = True
    cmp = False or 18 -> cmp = 18
    """

    verdadero = True or False
    verdadero = False or True
    verdadero = True or True
    falso = False or False

    # -- Invertir
    verdadero = not False # True
    false = not True # False
```

[Video: Booleans y comapraciones](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9412516?start=0)

## List, tuples and sets

1. **Lists**
    * Se puede acceder a los lementos de la Lista a través del índice:
        ```python
        my_list_variable = ['hello', 'hi', 'nice to meet you']
        print(my_list_variable)
        print (my_list_variable[0]) 
        ```

        **Output:**

        ```console
        ['hello', 'hi', 'nice to meet you']
        hello
        ```
    * Se pueden agregar elementos a una Lista:
        ```python
        my_list_variable.append('another string')
        print(my_list_variable)
        ```
        **Output:**

        ``
        ['hello', 'hi', 'nice to meet you', 'another string']
        ``

2. **Tuples**

    * Las Tuplas de un único valor deben finalizar con una coma:
        ```python
        my_short_tuple_variable = ('hello',)
        print(my_short_tuple_variable)
        ```

        **Output:**  

        ``
        ('hello',)
        ``

    * Se puede acceder a los lementos de la tupla a través del índice:
        ```python
        my_tuple_variable = ('hello', 'hi', 'nice to meet you')
        print(my_tuple_variable)
        print (my_tuple_variable[0])
        ```

        **Output:**

        ```console
        ('hello', 'hi', 'nice to meet you')
        hello
        ```

    * No se pueden agregar elementos en una tupla:
        ```python
        my_tuple_variable.append('another string')
        print(my_tuple_variable)
        ```

        **Output:**
        ```console
        Traceback (most recent call last):
            File "11_lists_tuples_sets.py", line 21, in <module>
            my_tuple_variable.append('another string')
        AttributeError: 'tuple' object has no attribute 'append'
        ```

    * Las tuplas se puede concatenar:
        ```python
        my_tuple_variable = my_tuple_variable + ('another string',)
        print (my_tuple_variable)
        ```

        **Output:**

        ``
        ('hello', 'hi', 'nice to meet you', 'another string')
        ``

        >**NOTA:** El resultado es similar a agregar un nuevo elemento.

3. **Sets**

    * Los set no tienen orden:
        ```python
        # Sets
        my_set_variable = {'hello', 'hi', 'nice to meet you'}
        print(my_set_variable)
        ```

        **Output:**

        ``
        {'nice to meet you', 'hi', 'hello'}
        ``

    * No se puede acceder a los items por indice:

        ```python
        print (my_set_variable[0])
        ```

        **Output:**

        ```consolo
        Traceback (most recent call last):
            File "11_lists_tuples_sets.py", line 26, in <module>
                print (my_set_variable[0])
        TypeError: 'set' object does not support indexing
        ```

    * Se puede agregar un nuevo elemento a un set:
        ```python
        my_set_variable.add('another string')
        print(my_set_variable)
        ```

        **Output:**

        ``
        {'hello', 'hi', 'another string', 'nice to meet you'}
        ``

    * Los sets no permiten valores duplicados
        ```python
        my_set_variable.add('hello')
        print(my_set_variable)
        ```

        **Output:**

        ``
        {'hi', 'hello', 'nice to meet you', 'another string'}
        ``

[Video: Listas, tuplas y sets](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9412520?start=0)

## Operaciones avanzadas con sets

```python
set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9, 11}

print (f'set_one: {set_one}')
print (f'set_two: {set_two}')


print(f'Intersección: {set_one.intersection(set_two)}')
print(f'Intersección (&): {set_one & set_two}')

print(f'Unión: {set_one.union(set_two)}')
print(f'Unión (|): {set_one | set_two}')

print(f'Diferencia: {set_one.difference(set_two)}')
print(f'Diferencia (-): {set_one - set_two}')
```

**Output:**

```console
set_one: {1, 2, 3, 4, 5}
set_two: {1, 3, 5, 7, 9, 11}
Intersección: {1, 3, 5}
Intersección (&): {1, 3, 5}
Unión: {1, 2, 3, 4, 5, 7, 9, 11}
Unión (|): {1, 2, 3, 4, 5, 7, 9, 11}
Diferencia: {2, 4}
Diferencia (-): {2, 4}
```

[Video: Operaciones avanzadas con sets](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9412522?start=0)


