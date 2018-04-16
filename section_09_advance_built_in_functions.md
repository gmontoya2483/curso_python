# Section 07: Databases

[VOLVER a README.md](README.md)

## Indice

* [Generators](#generators)


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

