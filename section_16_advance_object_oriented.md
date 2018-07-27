# Section 16: Advance Object Oriented Programming

[VOLVER a README.md](README.md)

## Indice

* [Introduction to this section](#introduction-to-this-section)


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