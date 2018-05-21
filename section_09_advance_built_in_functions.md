# Section 09: Advance Built in Functions

[VOLVER a README.md](README.md)

## Indice

* [Generators](#generators)
* [Generators classes and iterators](#generators-classes-and-iterators)
* [Iterables](#iterables)
* [Filter function](#filter-function)
* [Map function](#map-function)
* [any and all functions](#any-and-all-functions)
* [enumerate function](#enumerate-function)

## Generators

Un ``Generator`` es una función que recurda su estado entre las ejecuciones. El uso de generadores mejora la performance de la aplicacion ya que no bloquea una gran catidad de memoria.  

Al introducir el comando ``yield``, python detecta que estamos devolviendo un objeto generator.  

Para poder poder utilizar el este objeto, se lo debe asignar a una variable y obtener los valores siguientes con el comando ``next``.  

El comando ``list`` genera una lista del generator a partir de la posicion siguiente.


```python
def five_numbers():
    i = 0
    while i < 5:
        yield i
        i += 1


if __name__ == '__main__':
    g = five_numbers()
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))

    print('\n')

    g2 = five_numbers()
    print(next(g2))
    print(next(g2))
    print(list(g2))
```

**OUTPUT:**

```console
C:/Users/montoya/Desktop/CursoPython/Section_09_Advance_buit_in_Functions/generators.py
0
1
2
3
4

0
1
[2, 3, 4]

Process finished with exit code 0

```

[Video: Generators](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445596?start=0)


## Generators classes and iterators

Toda clase que implemente el metodo ``__next__()`` es considerada un iterator.  
No todas las clases que implementan el metodo ``__next__()`` son ``generators``. para que una clase sea considerada generator debe **generar** los datos cuando se llama al metodo ``next``.

En el ejemplo siguiente la clase ``FirstFiveGenerator`` es un ``generator`` dado que va generando los valores a medida que se llama el método ``next()``. Por otro lado la clase ``FirstFiceIterator`` no es un ``generator`` debeido a que el metodo next lee los valores de una ``Lista``.

```python
class FirstFiveGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 5:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()


class FirstFiveIterator:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.i = 0

    def __next__(self):
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i += 1
            return current
        else:
            raise StopIteration()


if __name__ == '__main__':
    my_gen = FirstFiveGenerator()
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))

    print ('\n')

    my_iterator = FirstFiveIterator()
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
```

**OUTPUT:**

```console
C:\Users\montoya\AppData\Local\Programs\Python\Python36-32\python.exe C:/Users/montoya/Desktop/CursoPython/Section_09_Advance_buit_in_Functions/generator_classes_and_iterators.py
0
1
2
3
4


1
2
3
4
5

Process finished with exit code 0

```

>**NOTA:** Un ``Iterator`` no es un ``iterable`` por lo que no se puede hacer ``for i in my_gen:`` 

[Video: generators classes and iterators](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445604?start=0)

## Iterables

El ``iterable`` es un objeto que tiene un metodo ``__iter__()``. Este método tiene que devolver un ``iterator``.

* El ``iterable`` puede ser una clase aparte como en el ejemplo siguiente:

    ```python
    class FirstFiveGenerator:
        def __init__(self):
            self.number = 0

        def __next__(self):
            if self.number < 5:
                current = self.number
                self.number += 1
                return current
            else:
                raise StopIteration()


    class FirstFiveIterable:
        def __iter__(self):
            return FirstFiveGenerator()


    if __name__ == '__main__':
        print(sum(FirstFiveIterable()))

        print('\n')

        for i in FirstFiveIterable():
            print(i)
    ```

    **OUTPUT:**

    ```console
    C:\Users\montoya\AppData\Local\Programs\Python\Python36-32\python.exe C:/Users/montoya/Desktop/CursoPython/Section_09_Advance_buit_in_Functions/iterables.py
    10


    0
    1
    2
    3
    4

    Process finished with exit code 0
    ```

* o bien, puede ser definido dentro de la clase ``iterator`` que se quiere hacer ``iterable`` (es lo recomendable):

    ```python
    class FirstFiveGenerator:
        def __init__(self):
            self.number = 0

        def __next__(self):
            if self.number < 5:
                current = self.number
                self.number += 1
                return current
            else:
                raise StopIteration()

        def __iter__(self):
            return self


    if __name__ == '__main__':
        print(sum(FirstFiveGenerator()))

        print('\n')

        for i in FirstFiveGenerator():
            print(i)
    ```

    **OUTPUT:**

        ```console
        C:\Users\montoya\AppData\Local\Programs\Python\Python36-32\python.exe C:/Users/montoya/Desktop/CursoPython/Section_09_Advance_buit_in_Functions/iterables.py
        10


        0
        1
        2
        3
        4

        Process finished with exit code 0
        ```


* Tambien se puede definir un ``iterable`` agregando los métodos  ``__len__()__`` y ``__getitem__()``, esto no sirve si el ``iterator`` es tambien un ``generator``:

    ```python
    class AnotherIterable:
        def __init__(self):
            self.cars = ['Fiesta', 'Focus']

        def __len__(self):
            return len(self.cars)

        def __getitem__(self, item):
            return self.cars[item]


    if __name__ == '__main__':
        for car in AnotherIterable():
            print(car)

    ``` 

    **OUTPUT:**

    ```console
    C:\Users\montoya\AppData\Local\Programs\Python\Python36-32\python.exe C:/Users/montoya/Desktop/CursoPython/Section_09_Advance_buit_in_Functions/iterables.py

    Fiesta
    Focus

    Process finished with exit code 0

    ```

* Generator comprehension:

```python
my_numbers_gen = (x for x in [1,2,3,4,5])

print(next(my_numbers_gen))
print(next(my_numbers_gen))
print(next(my_numbers_gen))
print(next(my_numbers_gen))

```

**OUTPUT:**

```console
C:\Users\montoya\AppData\Local\Programs\Python\Python36-32\python.exe C:/Users/montoya/Desktop/CursoPython/Section_09_Advance_buit_in_Functions/iterables.py

1
2
3
4

Process finished with exit code 0

```

[Video: Iterables](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445610?start=0)

## Filter function

La funcion ``filter()`` toma dos argumentos, el primer argumento es una ``función`` y el segundo un ``iterable``

La función ``filter()`` devuelve un generator.


```python
def starts_with_r(friend):
    return friend.startswith('R')


if __name__ == '__main__':
    friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
    start_with_r = filter(starts_with_r, friends)  # arg 1: function that returns True/False

    print(next(start_with_r))
    print(list(start_with_r))
    print(list(start_with_r))

```

**OUTPUT:**

```console
C:\Users\montoya\AppData\Local\Programs\Python\Python36-32\python.exe C:/Users/montoya/Desktop/CursoPython/Section_09_Advance_buit_in_Functions/filter.py
Rolf
['Randy']
[]

Process finished with exit code 0
```

Se puede utilizar una funcón ``lambda`` en el filter también:

```python


if __name__ == '__main__':
    friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']

    start_with_r_lambda = filter(lambda friend: friend.startswith('R'), friends)

    print(next(start_with_r_lambda))
    print(list(start_with_r_lambda))
    print(list(start_with_r_lambda))

```

**OUTPUT:**

```console
C:\Users\montoya\AppData\Local\Programs\Python\Python36-32\python.exe C:/Users/montoya/Desktop/CursoPython/Section_09_Advance_buit_in_Functions/filter.py
Rolf
['Randy']
[]

Process finished with exit code 0
```

También se puede utilizar el ``if`` en el *generator comprehansion*. esta opción es la mas performante. Además es la más ``Pythonic``

```python


if __name__ == '__main__':
    
    friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']

    start_with_r_generator_comprehension = (friend for friend in friends if friend.startswith('R'))
    
    print(next(start_with_r_generator_comprehension))
    print(list(start_with_r_generator_comprehension))
    print(list(start_with_r_generator_comprehension))

```

**OUTPUT:**

```console
C:\Users\montoya\AppData\Local\Programs\Python\Python36-32\python.exe C:/Users/montoya/Desktop/CursoPython/Section_09_Advance_buit_in_Functions/filter.py
Rolf
['Randy']
[]

Process finished with exit code 0
```

[Video: the filter() function](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445618?start=0)

## Map function

La función ``map()`` toma un ``iterable`` y devuelve un nuevo ``iterable`` donde cada elemento es modificado de acuerdo a alguna función. Nuevamente es mejor utilizar *generator comprehension*.

```python
def to_lower(friend):
    return friend.lower()


if __name__ == '__main__':
    friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']

    # Using a regular function
    friends_lower_map_regular = map(to_lower, friends)

    print(next(friends_lower_map_regular))
    print(list(friends_lower_map_regular))
    print(list(friends_lower_map_regular))

    print('\n')

    # Using map() con lambda
    friends_lower_map_lambda = map(lambda x: x.lower(), friends)

    print(next(friends_lower_map_lambda))
    print(list(friends_lower_map_lambda))
    print(list(friends_lower_map_lambda))

    print('\n')

    # Using generator comprehension
    friends_lower_generator_comprehension = (friend.lower() for friend in friends)

    print(next(friends_lower_generator_comprehension))
    print(list(friends_lower_generator_comprehension))
    print(list(friends_lower_generator_comprehension))


```

**OUTPUT:**

```console
C:\Users\montoya\AppData\Local\Programs\Python\Python36-32\python.exe C:/Users/montoya/Desktop/CursoPython/Section_09_Advance_buit_in_Functions/map.py
rolf
['jose', 'randy', 'anna', 'mary']
[]


rolf
['jose', 'randy', 'anna', 'mary']
[]


rolf
['jose', 'randy', 'anna', 'mary']
[]

Process finished with exit code 0

```

[Video: map() function](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445620?start=0)

## any and all functions

* ``any()``: toma un ``iterable`` y devuelve ``True`` si alguno de sus elementos evaluan como ``True``.

* ``all()``: toma un ``iterable`` y devuelve ``True`` si todos sus elementos eveluan como ``True``.


>**NOTA:** Los siguientes valores evaluan siempre como ``False``:  
> * `0`, ``0.00``
> * `None`
> * `[]`
> * `()`
> * `{}`
> * `False`
>  
> Cualquier otro valor evalua como ``True``


Ejemplo: 

```python
print(any([0, 1, 2, 3, 4, 5]))
print(all([0, 1, 2, 3, 4, 5]))
print(all([1, 2, 3, 4, 5]))
```

**OUTPUT:**

```console
True
False
True

Process finished with exit code 0
```

[Video: any() and all()](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445626?start=0)

## enumerate function

La funcion ``enumerate()`` nos permite tener el índice y el valor cuando se mueve a través de una lista.

```python
top_friends = ['Jose', 'Rolf', 'Anna','Santiago']

for i, friend in enumerate(top_friends):
    print(f'My top { i+1 } friend is { friend }.')
```

**OUTPUT:**

```console
My top 1 friend is Jose.
My top 2 friend is Rolf.
My top 3 friend is Anna.
My top 4 friend is Santiago.

Process finished with exit code 0
```

La función ``enumerate()`` devuelve un ``generator``, una tupla (índice, valor):

```python
top_friends = ['Jose', 'Rolf', 'Anna','Santiago']

friends_generator = enumerate(top_friends)

print(next(friends_generator))
print(list(friends_generator))
print(list(friends_generator))
```

**OUTPUT:**

```console
(0, 'Jose')
[(1, 'Rolf'), (2, 'Anna'), (3, 'Santiago')]
[]

Process finished with exit code 0
```

[Video: enumerate() function](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445628?start=0)