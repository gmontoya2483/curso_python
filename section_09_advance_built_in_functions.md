# Section 07: Databases

[VOLVER a README.md](README.md)

## Indice

* [Generators](#generators)
* [Generators classes and iterators](#generators-classes-and-iterators)


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

Toda clase que implemente el metodo ``__next__`` es considerada un iterator.  
No todas las clases que implementan el metodo ``__next__`` son ``generators``. para que una clase sea considerada generator debe **generar** los datos cuando se llama al metodo ``next``.

En el ejemplo siguiente la clase ``FirstFiveGenerator`` es un ``generator`` dado que va generando los valores a medida que se llama el método ``next``. Por otro lado la clase ``FirstFiceIterator`` no es un ``generator`` debeido a que el metodo next lee los valores de una ``Lista``.

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