# Section 10: Advance python development

[VOLVER a README.md](README.md)

## Indice

* [Mutability](#mutability)

## Mutability

Mutable en python es data que se puede cambiar una vez creado.  
The ``id()`` function returns the memory address.


* Ejemplo mutable object

```python
friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}
print(id(friends_last_seen))


friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}
print(id(friends_last_seen))


friends_last_seen['Rolf'] = 0
print(id(friends_last_seen))

friends_list = ['Rolf', 'Jose']
print(id(friends_list))

friends_list.append('jen')
print(id(friends_list))

```

**OUTPUT:**

```console
2482608
2482656
2482656
31001816
31001816


Process finished with exit code 0
```

>**NOTA:** Este objeto es Mutable, al modificarse matiene el mismo id. ``List`` son tambien mutables.

* Ejemplo inmutable object

```python
my_int = 5
print(id(my_int))

my_int = 7
print(id(my_int))
```

**OUTPUT:**

```console
491246704
491246736

Process finished with exit code 0
```

>**NOTA:** Integer es inmutable, al modificarse se crea un nuevo objeto, con un nuevo id.  
> Objetos inmutables: 
> * integer,
> * floats
> * strings
> * tuples




[Video: Mutability](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477736?start=0)