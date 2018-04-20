# Section 10: Advance python development

[VOLVER a README.md](README.md)

## Indice

* [Mutability](#mutability)
* [Argument Mutability](#argument-mutability)
* [Default values for parameters](#default-values-for-parameters)
* [Mutable default arguments - Bad idea](#mutable-default-arguments)
* [Argument unpacking](#argument-unpacking)
* [Collections](#collections)

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



## Argument Mutability

Si se pasa como argumento un objeto mutable, y se realiza una modificacion del objeto. Se modifica el objeto original. (iagual que pasar un valor por referencia en C)

```python
friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}


def see_friend(friends, name):
    print(id(friends))
    friends[name] = 0


print(id(friends_last_seen))
print(id(friends_last_seen['Rolf']))
print(friends_last_seen)

print('\n')

see_friend(friends_last_seen, 'Rolf')
print(id(friends_last_seen['Rolf']))
print(id(friends_last_seen))
print(friends_last_seen)

```

**OUTPUT:**

```console
4448688
502453776
{'Rolf': 31, 'Jen': 1, 'Anne': 7}


4448688
502453280
4448688
{'Rolf': 0, 'Jen': 1, 'Anne': 7}

Process finished with exit code 0

```

Por otro lado, si el objeto es inmutable, y se lo pasa como argumento las modificaciones que se hagan en la funcion no van a afectar al objeto original. (igual que pasar un parametro por valor en C)


```python
def increase_age(current_age):
    print(id(current_age))
    current_age = current_age + 1
    print(current_age)

age = 20

print(id(age))
print(age)

print('\n')

increase_age(age)
print(id(age))
print(age)
```

**OUTPUT:**

```console
505468256
20


505468256
21
505468256
20

Process finished with exit code 0
```

[Video: Argument mutability](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477742?start=0)


## Default values for parameters

Los parametros que tienen default values deben ir al final, no puede haber parametros que no tienen valores por default despues de los que los tienen.

```python
accounts = {
    'checking': 1956.00,
    'savings': 3695.50
}


def add_balance(amount: float, name: str = 'checking') -> float:
    """Function to update the balance of an account and return the new balnce."""
    accounts[name] += amount
    return accounts[name]


if __name__ == '__main__':
    add_balance(500.00, 'savings')
    print(accounts['savings'])

    add_balance(100.00)
    print(accounts['checking'])

```

**OUTPUT:**

```console
4195.5
2056.0

Process finished with exit code 0
```

[Video: Default values for parameters](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477748?start=0)

## Mutable default arguments

Esto es algo que se debe tratar de evitar. El objeto mutable es creado en la definición y es compartido cada vez que la funcion es llamada:

```python

def create_account(name: str, holder: str, account_holders: list = []):
    account_holders.append(holder)
    print(id(account_holders))
    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }


if __name__ == '__main__':
    a1 = create_account('checking', 'Rolf')
    a2 = create_account('savings', 'Jen')

    print(a2)
```

**OUTPUT:**

```console
6557648
6557648
{'name': 'savings', 'main_account_holder': 'Jen', 'account_holders': ['Rolf', 'Jen']}

Process finished with exit code 0
```

Como se puede ver en el output, cada vez que se llama a la funcion ``create_acoount()`` el id de la lista es el mismo. Por otro lado, al imprimir ``a2`` la lista ``account_holders`` tiene a ``Rolf`` que fue agregado al crearse la cuanta ``a1``-  

[Video: Mutable default arguments (Una mala idea)](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477754?start=0)

## Argument unpacking

```python
accounts = {
    'checking': 1956.00,
    'savings': 3695.50
}


users = [
    {'username': 'Rolf', 'password': '123'},
    {'username': 'blabla', 'password': '1234'}
]


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


def add_balance(amount: float, name: str = 'checking') -> float:
    """Function to update the balance of an account and return the new balnce."""
    accounts[name] += amount
    return accounts[name]


if __name__ == '__main__':
    transactions = [
        (-180.67, 'checking'),
        (-220.00, 'checking'),
        (220.00, 'savings'),
        (-15.70, 'checking'),
        (-23.90, 'checking'),
        (-13.00, 'checking'),
        (1579.50, 'checking'),
        (-600.50, 'checking'),
        (600.50, 'savings'),
    ]

    # Normal
    for t in transactions:
        add_balance(t[0], t[1])

    # Unpacking arguments *
    for t in transactions:
        add_balance(*t)

    # naming the arguments
    for t in transactions:
        add_balance(amount=t[0], name=t[1])

    # Deconstruction
    for t in transactions:
        amount, name = t
        add_balance(amount, name)

    # Name argument unpacking **
    user_objects = [User(**data) for data in users] # Es lo mismo que: [User(username = data['username', password= data['password']) for data in users]
```

[Video: Argument unpacking](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477756?start=0)

## Collections

* **Queue: (cola)** Se puede agregar elementos al final que quitarlos del principios.

* **stack: (pila)** Se agregan elementos al final y se quitan del final.

* **counter:** permite contar cosas.

```python
from collections import Counter

device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]
temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.0])
```

**OUTPUT:**

```console
2

Process finished with exit code 0
```

* **defaultdict:** Nunca va a dar una excepción ``KeyError``, en lugar devuelve el valor de una fuanción

```python
from collections import defaultdict

coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

alma_maters = defaultdict(list)


for coworker, place  in coworkers:
    alma_maters[coworker].append(place)

print(alma_maters)
print(alma_maters['Anne'])
print(alma_maters)
```

**OUTPUT:**

```console
defaultdict(<class 'list'>, {'Rolf': ['MIT', 'Cambridge'], 'Jen': ['Oxford'], 'Charlie': ['Manchester']})
[]
defaultdict(<class 'list'>, {'Rolf': ['MIT', 'Cambridge'], 'Jen': ['Oxford'], 'Charlie': ['Manchester'], 'Anne': []})

Process finished with exit code 0
```

* **Ordered Dict:** Muestra el contenido en el ordern que fue insertado. Permite hacer ``move_to_end`` y ``popitem``.

```python
from collections import OrderedDict

o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 10
o['Jen'] = 3

print(o)  # keys are always in the order in which they were inserted

o.move_to_end('Rolf')
o.move_to_end('Jose', last=False)

print(o)

o.popitem()  # Pop off the last item from the list

print(o)
```

**OUTPUT:**

```console
OrderedDict([('Rolf', 6), ('Jose', 10), ('Jen', 3)])
OrderedDict([('Jose', 10), ('Jen', 3), ('Rolf', 6)])
OrderedDict([('Jose', 10), ('Jen', 3)])

Process finished with exit code 0

```

* **namedtuple:** Igual a una tupla, pero cada elemento tiene un nombre y la tupla en si mismo también tiene un nombre.

```python
from collections import namedtuple

# Normal Tuples

account = ('checking', 1850.90)

print(account[0])  # name
print(account[1])  # balance

print('\n')

# named tuples

Account = namedtuple('Account', ['name', 'balance'])
account = Account('checking', 1850.90)
print(account.name)
print(account.balance)
print(account)

```

**OUTPUT:**

```console

checking
1850.9


checking
1850.9
Account(name='checking', balance=1850.9)

Process finished with exit code 0

```

* **Double ended queue: (deque)** Una queue en la que se puede agregar o remover objeteos de ambos lados.

```python
from collections import deque

friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))

friends.append('Jose')
friends.appendleft('Anthony')
print(friends)

friends.pop()
print(friends)

friends.popleft()
print(friends)
```

**OUTPUT:**

```console
deque(['Anthony', 'Rolf', 'Charlie', 'Jen', 'Anna', 'Jose'])
deque(['Anthony', 'Rolf', 'Charlie', 'Jen', 'Anna'])
deque(['Rolf', 'Charlie', 'Jen', 'Anna'])

Process finished with exit code 0
```

[Video: Queues](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477758?start=0)  
[Video: Collections](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477762?start=0)