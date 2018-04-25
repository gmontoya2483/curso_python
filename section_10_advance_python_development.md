# Section 10: Advance python development

[VOLVER a README.md](README.md)

## Indice

* [Mutability](#mutability)
* [Argument Mutability](#argument-mutability)
* [Default values for parameters](#default-values-for-parameters)
* [Mutable default arguments - Bad idea](#mutable-default-arguments)
* [Argument unpacking](#argument-unpacking)
* [Collections](#collections)
* [Timezones, datetime](#timezones-and-datetime)
* [Timing your code](#timing-your-code)
* [Regular expressions](#regular-expressions)
* [Logging](#logging)

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

# Timezones and datetime

En ``Python`` existen dos tipos de entidades de fecha.

* **Naive**: objetos fecha y hora que no conocen acerca del timezone.

    ```python
    from datetime import datetime

    ahora_naive = datetime.now()
    print(ahora_naive)
    ```

    **OUTPUT:**

    ```console
    2018-04-23 10:14:13.435581

    Process finished with exit code 0
    ```

* **Aware**: objetos fecha y hora que conocen acerca del timezone.

    ```python
    ahora_aware = datetime.now(timezone.utc)
    print(ahora_aware)
    ```

    **OUTPUT:**
    ```console
    2018-04-23 08:14:13.435581+00:00

    Process finished with exit code 0
    ```

* Time delta

```python
from datetime import datetime, timezone, timedelta

today = datetime.now(timezone.utc)
print(f' Ahora: { today }')

later = today + timedelta(hours=3)
print(f' Mas tarde: { later }')

tomorrow = today + timedelta(days=1)
print(f' Manana: { tomorrow }')

yesterday = today + timedelta(days=-1)
print(f' Ayer: { yesterday }')
```

**OUTPUT:**
```console
 Ahora: 2018-04-23 08:33:47.290263+00:00
 Mas tarde: 2018-04-23 11:33:47.290263+00:00
 Manana: 2018-04-24 08:33:47.290263+00:00
 Ayer: 2018-04-22 08:33:47.290263+00:00

Process finished with exit code 0
```

* ``strftime()`` and ``strptime()``

```python
today = datetime.now(timezone.utc)
print(f"Ahora Formatted: { today.strftime('%d-%m-%Y %H:%M') }")  # string format time

user_date = input('Enter the date in YYYY-mm_dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d')  # string parse time
print(user_date)
```

**OUTPUT:**
```console
Ahora Formatted: 23-04-2018 08:43
Enter the date in YYYY-mm_dd format: 2010-05-25
2010-05-25 00:00:00

Process finished with exit code 0
```

* Más sobre Naive ``date()``

```python
import datetime

d = datetime.date(2016, 7, 24)
print(d)
print('\n')

tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.day)
print(tday.month)
print(tday.weekday())  # (Monday 0  Sunday 6)
print(tday.isoweekday())  # (Monday 1  Sunday 7)
```

**OUTPUT:**

```console
2016-07-24


2018-04-24
2018
24
4
1
2

Process finished with exit code 0
```

* Más sobre ``timedelta()``

```python
# Time deltas
tday = datetime.date.today()
tdelta = datetime.timedelta(days=7)
print(f'Today: { tday }')
print(f'+ 7 days: { tday + tdelta }')
print(f'- 7 days: { tday - tdelta }')
print('\n')

# Calculando el delta
bday = datetime.date(2019, 1, 9)
tday = datetime.date.today()
till_bday = bday - tday

print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())
```

**OUTPUT:**

```console
Today: 2018-04-24
+ 7 days: 2018-05-01
- 7 days: 2018-04-17


260 days, 0:00:00
260
22464000.0

Process finished with exit code 0
```

* Más sobre ``time()``

```python
import datetime

# time
t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)
```

**OUTPUT:**

```console
09:30:45.100000
9
30
45
100000

Process finished with exit code 0
```

* Más sobre ``datetime()``

```python
import datetime

# date time
dt = datetime.datetime(2017, 5, 23, 13, 26, 40, 100000)
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)

print(dt.weekday())
print(dt.isoweekday())
print(dt.isocalendar())

print(dt.time())
print(dt.date())
print('\n')
```

**OUTPUT:**

```console
02017-05-23 13:26:40.100000
2017
5
23
13
1
2
(2017, 21, 2)
13:26:40.100000
2017-05-23

Process finished with exit code 0
```

* constructores de ``datetime()``

```python
# date time constructors
dt_fix_date = datetime.datetime(2017, 5, 23, 13, 26, 40, 100000)

dt_today = datetime.datetime.today()  # Return the current local time without considering the time zone
dt_now = datetime.datetime.now()  # Nos da la opcion de pasarle el time zone.
dt_utcnow = datetime.datetime.utcnow()

print(f'fixed date: { dt_fix_date }')
print(f'date today: { dt_today }')
print(f'date now: { dt_now }')
print(f'date utcnow: { dt_utcnow }')
```

**OUTPUT:**

```console
fixed date: 2017-05-23 13:26:40.100000
date today: 2018-04-24 14:20:28.246844
date now: 2018-04-24 14:20:28.246843
date utcnow: 2018-04-24 12:20:28.246843

Process finished with exit code 0
```

* Uso de la libreria ``pytz`` para el manejo de timezones

Instalar la libreria:

```console
pip install pytz
```

Crear un ``datetime`` que sea **Timezone aware**:  

```python
import datetime
import pytz

# Crear un datetime tz aware
dt_fix_date_aware = datetime.datetime(206, 7, 27,12, 30,45, tzinfo=pytz.UTC)
print(f'Fixed date tz aware UTC: { dt_fix_date_aware }')

# usar el now, con el parametro del tz
dt_now_aware = datetime.datetime.now(tz=pytz.UTC)
print(f'Now date tz aware UTC: { dt_now_aware }')

# usar el now, con el parametro del tz
vienna_tz = pytz.timezone('Europe/Vienna')
dt_vienna_now_aware = datetime.datetime.now(tz=vienna_tz)
print(f'Now date in Vienna aware: { dt_vienna_now_aware }')


# usar el utcnow(), y aplicarle el tz
dt_utcnow_aware = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(f'utcnow tz aware replace(UTC): { dt_utcnow_aware }')

print('\n')
```

**OUTPUT:**

```console
Fixed date tz aware UTC: 0206-07-27 12:30:45+00:00
Now date tz aware UTC: 2018-04-25 09:24:02.154239+00:00
Now date in Vienna aware: 2018-04-25 11:24:02.424266+02:00
utcnow tz aware replace(UTC): 2018-04-25 09:24:02.424266+00:00

Process finished with exit code 0
```

Convertir un ``datetime`` aware a diferentes **timeszones**:  

```python
# Convertir a diferentes time zones
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
dt_vienna = dt_utcnow.astimezone(pytz.timezone('Europe/Vienna'))
dt_bs_as = dt_utcnow.astimezone(pytz.timezone('America/Argentina/Buenos_Aires'))

print(f'UTC : { dt_utcnow }')
print(f'US/Mountain : { dt_mtn }')
print(f'Europe/Vienna : { dt_vienna }')
print(f'America/Argentina/Buenos_Aires : { dt_bs_as }')

print('\n')
```

**OUTPUT:**

```console
UTC : 2018-04-25 08:55:13.516114+00:00
US/Mountain : 2018-04-25 02:55:13.516114-06:00
Europe/Vienna : 2018-04-25 10:55:13.516114+02:00
America/Argentina/Buenos_Aires : 2018-04-25 05:55:13.516114-03:00

Process finished with exit code 0
```

Convertir un ``datetime`` **Naive** a **Aware**:  

```python
# Convertir un datetime Naive a Aware
dt_vienna_naive = datetime.datetime.now()
vienna_tz = pytz.timezone('Europe/Vienna')
dt_vienna_aware = vienna_tz.localize(dt_vienna_naive)
dt_utc_aware = dt_vienna_aware.astimezone(pytz.timezone('UTC'))

print(f'Local datetime (naive) : { dt_vienna_naive }')
print(f'Europe/Vienna (aware) : { dt_vienna_aware }')
print(f'utc (aware) : { dt_utc_aware }')

print('\n')
```

**OUTPUT:**

```console
Local datetime (naive) : 2018-04-25 10:55:13.700114
Europe/Vienna (aware) : 2018-04-25 10:55:13.700114+02:00
utc (aware) : 2018-04-25 08:55:13.700114+00:00

Process finished with exit code 0
```

Darle formato a los ``datetime``:  

```python
# Formating dates
dt = dt_utcnow.astimezone(pytz.timezone('Europe/Vienna'))
print(f'ISO Format : { dt.isoformat() }')
print(f"'%B %d, %Y': { dt.strftime('%B %d, %Y')}")

print('\n')
```

**OUTPUT:**

```console
ISO Format : 2018-04-25T10:55:13.516114+02:00
'%B %d, %Y': April 25, 2018

Process finished with exit code 0
```

Convertir un ``str`` a un ``datetime``:  

```python
# Convertir un string a un datetime
dt_str = 'July 26, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(f'Date from String: { dt }')
```

**OUTPUT:**

```console
Date from String: 2016-07-26 00:00:00

Process finished with exit code 0
```

Como averiguar todos los **Timezones**:  

```python
# Avriguar todos los timezones
for tz in pytz.all_timezones:
    print(tz)
```
**OUTPUT:**

```console
Africa/Abidjan
Africa/Accra
Africa/Addis_Ababa
Africa/Algiers
Africa/Asmara
Africa/Asmera
Africa/Bamako
Africa/Bangui
Africa/Banjul
Africa/Bissau
Africa/Blantyre
Africa/Brazzaville
Africa/Bujumbura
Africa/Cairo
Africa/Casablanca
Africa/Ceuta
Africa/Conakry
Africa/Dakar
Africa/Dar_es_Salaam
Africa/Djibouti
Africa/Douala
Africa/El_Aaiun
Africa/Freetown
Africa/Gaborone
Africa/Harare
Africa/Johannesburg
Africa/Juba

etc ...

Process finished with exit code 0
```



[Video: Timezones](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477766?start=0)  
[Video: Date and Times](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477768?start=0)  
[Datetime-cheatsheet](Datetime-cheatsheet.pdf)  
[Video: How to work with dates, times, timedeltas and Timezones](https://www.youtube.com/watch?v=eirjjyP2qcQ&index=24&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)

# Timing your code

```python
import time, timeit


def power(limit):
    return [x**2 for x in range(limit)]


def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()

    print(f'Start: { start }')
    print(f'End: { end }')
    print(f'Duration: { end - start }')


if __name__ == '__main__':

    # Option 1: rodeando la funcion start y end y calcular la diferencia
    start = time.time()
    p = power(50000)
    end = time.time()

    print(f'Start: { start }')
    print(f'End: { end }')
    print(f'Duration: { end - start }')
    print('\n')

    # Option 2: user una funcion y pasar la funcion como parametro
    measure_runtime(lambda : power(50000))
    print('\n')

    # Option 3: usar timeit
    duration = timeit.timeit("[x**2 for x in range(10)]")
    print(f'Duration { duration }')
    print('\n')

```

**OUTPUT:**

```console
Start: 1524475613.7985554
End: 1524475613.8185554
Duration: 0.019999980926513672


Start: 1524475613.8185554
End: 1524475613.8385553
Duration: 0.019999980926513672


Duration 3.656821846180259



Process finished with exit code 0
```

[Video: timing your code](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477770?start=0)


# Regular expressions

Componentes básicos de ``regex``:
* ``.`` "cualquiercosa" (un caracter)- letras, numeros, simboles... etc, pero **no** nuevas lineas.  
* ``+`` "uno o más de"
* ``*`` "zero o más de"
* ``?`` "zero o uno de"
* ``[]`` "[abc] a, b ó c"


```python
#Ejemplo 1

email = 'jose@tecladocode.com'
expression = '[a-z]+'

matches = re.findall(expression, email)
print(matches)

name = matches[0]
domain = f'{matches[1]}.{matches[2]}'


# Ejemplo 2:
email = 'jose@tecladocode.com'
expression = '[a-z\.]+'

matches = re.findall(expression, email)
print(matches)

# Ejemplo 3:
"""
Let’s say you’ve got a price of an item in a strange format (e.g. extracted from a file):
"""
price = 'Price: $189.50'
expression = 'Price: \$(\d+\.\d+)'

matches = re.search(expression, price)
print(matches.group(0))  # entire match
print(matches.group(1))  # first thing around brackets
```

**OUTPUT:**

```console
['jose', 'tecladocode', 'com']
['jose', 'tecladocode.com']
Price: $189.50
189.50

Process finished with exit code 0
```

[Video: regular expression](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477774?start=0)  
[WebSite: RegExr](https://regexr.com/)  
[Python 3: re documentation](https://docs.python.org/3/library/re.html)  

## Logging

* Logging Levels:  

>**CRITICAL:** 50  
>**ERROR:** 40  
>**WARNING:** 30  
>**INFO:** 20  
>**DEBUG:** 10  
>**NOTSET:** 0  

Example:  

```python
import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(name)s - %(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y:%H:%M:%S',
                    level=logging.DEBUG,
                    filename='logging.log'
                    )
logger = logging.getLogger(__name__)

logger.debug("This is a debug log")
logger.info("This is an info log")
logger.critical("This is critical")
logger.error("An error occurred")

```

```console
25-04-2018:14:48:00 DEBUG    [__main__ - logging_example.py:10] This is a debug log
25-04-2018:14:48:00 INFO     [__main__ - logging_example.py:11] This is an info log
25-04-2018:14:48:00 CRITICAL [__main__ - logging_example.py:12] This is critical
25-04-2018:14:48:00 ERROR    [__main__ - logging_example.py:13] An error occurred
```

[Video: Introducción a logging](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477778?start=15)  
[Video: Loggear en archivos y otras caracteristicas](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477780?start=0)  
[Python Documentation](https://docs.python.org/3/library/logging.html)
