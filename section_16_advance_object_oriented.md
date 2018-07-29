# Section 16: Advance Object Oriented Programming

[VOLVER a README.md](README.md)

## Indice

* [Introduction to this section](#introduction-to-this-section)
* [Introduction to multiple inheritance](#introduction-to-multiple-inheritance)
+ [Intro to ABC](#intro-to-abc)
* [The usefulness of ABCs](#the-usefulness-of-abcs)
* [The relationship between ABCs and interfaces](#the-relationship-between-abcs-and-interfaces)


## Introduction to this section

[Video: Introduction to this section](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9583278?start=0)


## Introduction to multiple inheritance

* user.py

``` python
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        return 'Logged in!'

    def __repr__(self):
        return f'<User { self.username }>'
```

* saveable.py

``` python
from Section_16_advance_object_oriented_programming.database import Database


class Saveable:
    def save(self):
        Database.insert(self.to_dict())

````

* admin.py

``` python
from Section_16_advance_object_oriented_programming.user import User
from Section_16_advance_object_oriented_programming.saveable import Saveable


class Admin(User, Saveable):
    def __init__(self, username, password, access):
        super(Admin, self).__init__(username, password)
        self.access = access

    def __repr__(self):
        return f'<Admin { self.username }, access { self.access }'

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'access': self.access
        }
```

* database.py

``` python
class Database:
    content = {'users': []}  # class variable accesible by all the instances

    @classmethod
    def insert(cls, data):
        cls.content['users'].append(data)

    @classmethod
    def remove(cls, finder):  # lambda x: x['username'] != 'Rolf'
        cls.content['user'] = [user for user in cls.content['users'] if not finder(user)]

    @classmethod
    def find(cls, finder): # lambda x: x['username'] == 'Rolf'
        return [user for user in cls.content['users'] if finder(user)]


```


* app.py

``` python
from Section_16_advance_object_oriented_programming.admin import Admin
from Section_16_advance_object_oriented_programming.database import Database

a = Admin('Rolf', '1234', 3)

a.save()

print(Database.find(lambda x: x['username'] == 'Rolf'))
```


**OUTPUT:**

``` console
[{'username': 'Rolf', 'password': '1234', 'access': 3}]

Process finished with exit code 0

```

[Video: Introduction to multiple inheritance](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9583280?start=0)

## Intro to ABC

Al utilizar ABC hace una clase abstracta que no puede ser instaciada. Tambien se definen los  metodos abstractos qque deben ser implemantados por la clase que hereda de la clase abstracta.

``` python
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def walk(self):
        print('Walking...')

    @abstractmethod
    def num_legs(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 4


class Monkey(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 2


dog = Dog('Pichicho')
print(dog.num_legs())

monkey = Monkey('Chita')
print(monkey.num_legs())

animal = Animal()
print(animal.num_legs())
```

**OUTPUT:**

``` console
4
Traceback (most recent call last):
2
  File "C:/Users/Gabriel/Documents/Projects/curso_python/Section_16_advance_object_oriented_programming/abc/animals.py", line 35, in <module>
    animal = Animal()
TypeError: Can't instantiate abstract class Animal with abstract methods num_legs

Process finished with exit code 1
```

[Video: Intro to ABC](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9583284?start=0)


## The usefulness of ABCs

``` python
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def walk(self):
        print('Walking...')

    @abstractmethod
    def num_legs(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 4


class Monkey(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 2


animals = [Dog('Rolf'), Monkey('Bob'), Monkey('Chita'), Dog('Boby')]
for animal in animals:
    print(isinstance(animal, Animal))
    print(animal.num_legs())

```

**OUTPUT:**
``` console
True
4
True
2
True
2
True
4

Process finished with exit code 0
```

[Video: The usefulness of ABCs](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9583294?start=0)


## The relationship between ABCs and interfaces

* admin.py

``` python
from Section_16_advance_object_oriented_programming.user import User



class Admin(User):
    def __init__(self, username, password, access):
        super(Admin, self).__init__(username, password)
        self.access = access

    def __repr__(self):
        return f'<Admin { self.username }, access { self.access }'

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'access': self.access
        }

```

* saveable.py

``` python
from abc import ABCMeta, abstractmethod

from Section_16_advance_object_oriented_programming.database import Database


class Saveable(metaclass=ABCMeta):
    def save(self):
        Database.insert(self.to_dict())

    @abstractmethod
    def to_dict(self):
        pass

```

* user.py

``` python
from Section_16_advance_object_oriented_programming.saveable import Saveable


class User(Saveable):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        return 'Logged in!'

    def __repr__(self):
        return f'<User { self.username }>'

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password
        }

```

* app.py

``` python
from Section_16_advance_object_oriented_programming.admin import Admin
from Section_16_advance_object_oriented_programming.user import User


a = Admin('Rolf', '1234', 3)
u = User('Jose', '4444')

users = [a, u]
for user in users:
    user.save()
    print(user.to_dict())
```

**OUTPUT:**

``` console
{'username': 'Rolf', 'password': '1234', 'access': 3}
{'username': 'Jose', 'password': '4444'}

Process finished with exit code 0
```

[Video: The relationship between ABCs and interfaces](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9583298?start=0)