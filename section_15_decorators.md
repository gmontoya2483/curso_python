# Section 15: Decorators

[VOLVER a README.md](README.md)

## Indice

* [Introduction to this section](#introduction-to-this-section)
* [A simple decorator](#a-simple-decorator)
* [@ syntax](#@-syntax)
* [Functools wraps](#functools-wraps)

## Introduction to this section

[Video: Introduction to this section](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9490878?start=0)

## A simple decorator

Los ``Decorators`` son high order functions que tienen la particularidad que devulven otra función.
Una función high order, es aquella que recive como argumentos funciones.

```python
user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(func):  # Recibe una función
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
    return secure_func  # Devuelve una función


def my_function():
    return 'Password for admin panel is 1234'


my_secure_function = user_has_permission(my_function)
print(my_secure_function())
```

**OUTPUT:**

```console
Password for admin panel is 1234

Process finished with exit code 0

```


[Video: A simple decorator](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9490858?start=0)


## @ syntax

``` python
user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(func):  # Recibe una función
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
    return secure_func  # Devuelve una función


@user_has_permission
def my_function():
    """
    Allowsto retrive the password
    :return:
    """
    return 'Password for admin panel is 1234'


@user_has_permission
def another():
    pass


print(my_function())
print(my_function.__name__)
print(my_function.__doc__)

print(another.__name__)
```

**OUTPUT:**

```console
Password for admin panel is 1234
secure_func
None
secure_func

Process finished with exit code 0
```

> **NOTA:** como se puede ver, el @ reemplaza a la funcion por lo que tanto el ``__name__`` como ``__doc__`` hacen referencia a ``secure_func`` y no a ``my_function``


[Video: Using the @ syntax](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9490860?start=0)


## Functools wraps

Una forma de mantener nuestro nombre de función y de doc

``` python
import functools

user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(func):
    @functools.wraps(func)
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
    return secure_func  # Devuelve una función


@user_has_permission
def my_function():
    """
    Allowsto retrive the password
    :return:
    """
    return 'Password for admin panel is 1234'


@user_has_permission
def another():
    pass


print(my_function())
print(my_function.__name__)
print(my_function.__doc__)

print(another.__name__)
```

**OUTPUT:**

```console
Password for admin panel is 1234
my_function

    Allowsto retrive the password
    :return:

another

Process finished with exit code 0
```



[Video: Functools wraps](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9490864?start=0)