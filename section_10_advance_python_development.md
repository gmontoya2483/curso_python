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
* [Mas sobre logging](#mas-sobre-logging)
* [Ejemplo como usar los logs en una applicacion](#ejemplo-como-usar-los-logs-en-una-applicacion)
* [Ejemplo Rotating Log](#ejemplo-rotating-Log)
* [Mas sobre Regular Expressions](#mas-sobre-regular-expressions)

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

## Mas sobre logging

### Niveles de Logs

* ``DEBUG``: Detailed information, typically of interest only when diagnosing problems.
* ``INFO``: Confirmation that things are working as expected.
* ``WARNING``: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
* ``ERROR``: Due to a more serious problem, the software has not been able to perform some function.
* ``CRITICAL``: A serious error, indicating that the program itself may be unable to continue running.

El nivel por defecto es ``WARNING``

### Basic Logs

* Ejemplo de un Logging basico - No hay import a otros modulos, por lo tanto no hay conflictos con los archivos de logs.

```Python
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='test.log',
                    format='%(asctime)s: %(levelname)s: %(message)s')


def add(x, y):
    """ Add Function """
    return x + y


def subtract(x, y):
    """ Subtract Function """
    return x - y


def multiply(x, y):
    """ Multiply Function """
    return x * y


def divide(x, y):
    """ Divide Function """
    return x / y


num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logging.debug(f'Add: { num_1 } + { num_2 } = { add_result }')

sub_result = subtract(num_1, num_2)
logging.debug(f'Sub: { num_1 } - { num_2 } = { sub_result }')

mul_result = multiply(num_1, num_2)
logging.debug(f'Mul: { num_1 } * { num_2 } = { mul_result }')

div_result = divide(num_1, num_2)
logging.debug(f'Div: { num_1 } / { num_2 } = { div_result }')
```

**Log File:**

```Console
2018-05-02 13:50:56,895: DEBUG: Add: 20 + 10 = 30
2018-05-02 13:50:56,896: DEBUG: Sub: 20 - 10 = 10
2018-05-02 13:50:56,896: DEBUG: Mul: 20 * 10 = 200
2018-05-02 13:50:56,896: DEBUG: Div: 20 / 10 = 2.0
```

* Ejemplo de un Logging basico - No hay import a otros modulos, por lo tanto no hay conflictos con los archivos de logs.

```python
import logging

logging.basicConfig(level=logging.INFO,
                    filename='employee.log',
                    format='%(asctime)s: %(levelname)s: %(message)s')

class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')
```

**Log File:**

```Console
2018-05-02 13:57:06,883: INFO: Created Employee: John Smith - John.Smith@email.com
2018-05-02 13:57:06,884: INFO: Created Employee: Corey Schafer - Corey.Schafer@email.com
2018-05-02 13:57:06,884: INFO: Created Employee: Jane Doe - Jane.Doe@email.com
```

* Ejemplo Avanzado de logs.  
En este caso una archivo de python importa otro archivo. Si se quieren loguear los modulos en difeentes archivos es necesario utilizar ``logger`` y ``FileHandler``  
Utilizando **Handlers** también nos permite loggear en multiples salidas.  
Utilizando el **logger**, se puede mostrar el traceback de una exception utilizando la función ``logger.exception()``

``simple_log_sample.py``

```python
import logging
import Section_10_1_Mas_Sobre_Logging.employee

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('sample.log')
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def add(x, y):
    """ Add Function """
    return x + y


def subtract(x, y):
    """ Subtract Function """
    return x - y


def multiply(x, y):
    """ Multiply Function """
    return x * y


def divide(x, y):
    """ Divide Function """
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by Zero')
    else:
        return result


num_1 = 20
num_2 = 0

add_result = add(num_1, num_2)
logger.debug(f'Add: { num_1 } + { num_2 } = { add_result }')

sub_result = subtract(num_1, num_2)
logger.debug(f'Sub: { num_1 } - { num_2 } = { sub_result }')

mul_result = multiply(num_1, num_2)
logger.debug(f'Mul: { num_1 } * { num_2 } = { mul_result }')

div_result = divide(num_1, num_2)
logger.debug(f'Div: { num_1 } / { num_2 } = { div_result }')
```

``employee.py``

```python
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('employee.log')
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

formater = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
file_handler.setFormatter(formater)


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info(f'Created Employee: { self.fullname } - {self.email}')

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')
```

Al ejecutar ``simple_log_sample.py`` importa ``employee.py`` y se crea un archivo de log para cada archivo de python. Además los logs de ``simple_log_sample.py`` se muestran en cosola.

**sample.log**

```console
2018-05-02 15:30:42,702: DEBUG: __main__: Add: 20 + 0 = 20
2018-05-02 15:30:42,703: DEBUG: __main__: Sub: 20 - 0 = 20
2018-05-02 15:30:42,703: DEBUG: __main__: Mul: 20 * 0 = 0
2018-05-02 15:30:42,703: ERROR: __main__: Tried to divide by Zero
Traceback (most recent call last):
  File "C:/Users/montoya/Desktop/CursoPython/Section_10_1_Mas_Sobre_Logging/simple_log_sample.py", line 35, in divide
    result = x / y
ZeroDivisionError: division by zero
2018-05-02 15:30:42,704: DEBUG: __main__: Div: 20 / 0 = None
```

**employee.log**

```console
2018-05-02 15:30:42,698: INFO: Section_10_1_Mas_Sobre_Logging.employee: Created Employee: John Smith - John.Smith@email.com
2018-05-02 15:30:42,698: INFO: Section_10_1_Mas_Sobre_Logging.employee: Created Employee: Corey Schafer - Corey.Schafer@email.com
2018-05-02 15:30:42,698: INFO: Section_10_1_Mas_Sobre_Logging.employee: Created Employee: Jane Doe - Jane.Doe@email.com
```

[Video: Logging Basics](https://www.youtube.com/watch?v=-ARI4Cz-awo&index=0&list=PL-osiE80TeTv5x_nJb-mtaEKg9Gi_-Nsh)  
[Video: Advance Logging](https://www.youtube.com/watch?v=jxmzY9soFXg&index=1&list=PL-osiE80TeTv5x_nJb-mtaEKg9Gi_-Nsh)

## Ejemplo como usar los logs en una applicacion

**app.py**

```python
import logging
from Section_10_Advance_Python_Development.Section_10_2_Ejemplo_logging_app.employee import Employee

if __name__ == '__main__':

    logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(name)s:%(lineno)d] %(message)s',
                        datefmt='%d-%m-%Y:%H:%M:%S',
                        level=logging.DEBUG,
                        filename='logging.log')
    logger = logging.getLogger(__name__)

    logger.info('Arranco el Main')

    emp_1 = Employee('John', 'Smith')
    emp_2 = Employee('Corey', 'Schafer')
    emp_3 = Employee('Jane', 'Doe')
```

**employee.py**

```python
import logging

logger = logging.getLogger(__name__)


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info(f'Created Employee: { self.fullname } - {self.email}')

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
```

**logging.log**

```console
02-05-2018:16:21:04 INFO     [__main__ - app.py:12] Arranco el Main
02-05-2018:16:21:04 INFO     [Section_10_Advance_Python_Development.Section_10_2_Ejemplo_logging_app.employee - employee.py:13] Created Employee: John Smith - John.Smith@email.com
02-05-2018:16:21:04 INFO     [Section_10_Advance_Python_Development.Section_10_2_Ejemplo_logging_app.employee - employee.py:13] Created Employee: Corey Schafer - Corey.Schafer@email.com
02-05-2018:16:21:04 INFO     [Section_10_Advance_Python_Development.Section_10_2_Ejemplo_logging_app.employee - employee.py:13] Created Employee: Jane Doe - Jane.Doe@email.com
02-05-2018:16:23:02 INFO     [__main__:12] Arranco el Main
02-05-2018:16:23:02 INFO     [Section_10_Advance_Python_Development.Section_10_2_Ejemplo_logging_app.employee:13] Created Employee: John Smith - John.Smith@email.com
02-05-2018:16:23:02 INFO     [Section_10_Advance_Python_Development.Section_10_2_Ejemplo_logging_app.employee:13] Created Employee: Corey Schafer - Corey.Schafer@email.com
02-05-2018:16:23:02 INFO     [Section_10_Advance_Python_Development.Section_10_2_Ejemplo_logging_app.employee:13] Created Employee: Jane Doe - Jane.Doe@email.com
```

## Ejemplo Rotating Log

### RotatingFileHandler

La clase ``RotatingFileHandler`` nos permite crear objetos ``logging handler`` que tienen la habilidad de rotar los archivos de logs de acuerdo al tamano, especificandole la propiedad ``maxBytes``.  
Tambien se le debe agregar la propiedad ``backupCount`` que va a servir para agregar los contadores '.1','.2', '.3', etc. Esta propiedad es la cantidad maxima de backup que se van a guardar.  

* Ejemplo:

```python
import logging
import time

from logging.handlers import RotatingFileHandler


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # agregar el rotating handler
    handler = RotatingFileHandler('test_rotating.log', maxBytes=20, backupCount=3)
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    for i in range(10):
        logger.info(f'Este es el log: { i }')
        time.sleep(1.5)
```

**Output**

``test_rotating.log``  
``test_rotating.log.1``  
``test_rotating.log.2``  
``test_rotating.log.3`` 

### TimedRotatingFileHandler

La clase ``RotatingFileHandler`` nos permite crear objetos ``logging handler`` que tienen la habilidad de rotar los archivos de logs de acuerdo al tiempo que ha pasado, especificandole la propiedad ``when`` y la propiedad ``interval``.  

Se le puede asignar a la propiedad ``when`` los siguientes valores:

* **'s'** segundo
* **'m'** minuto
* **'h'** hora
* **'d'** dia
* **'w0' - 'w1' (0 = Lunes)** día de la semana  
* **'midnight'** a la medianoche

Cuando se especifica **w** el valor pasado como ``interval`` no es tenido en cuenta.

Tambien se le debe agregar la propiedad ``backupCount`` para determinar la cantidad maxima de backup que se van a guardar. A cada backup se le va a agregar un timestamp con el siguiente formato: ``%Y-%m-%d_%H-%M-%S``

* Ejemplo

```python
import logging
import time

from logging.handlers import TimedRotatingFileHandler


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # agregar el rotating handler
    handler = TimedRotatingFileHandler('test_timed_rotating.log', when='m', interval=1, backupCount=3)
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    for i in range(4):
        logger.info(f'Este es el log: { i }')
        time.sleep(75)
```

**Output:**

``test_timed_rotating.log``  
``test_timed_rotating.log.2018-05-03_12-35``  
``test_timed_rotating.log.2018-05-03_12-36``  
``test_timed_rotating.log.2018-05-03_12-37`` 

## Mas sobre Regular Expressions


### Raw string

No tiene en cuenta los caracteres de escape.  
Ejemplo:

```Python
print('\tTab')
print(r'\tTab')
```

**Output:**

```console
	Tab
\tTab

Process finished with exit code 0
```

### Ejemplos de Regex

```python
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

321--555-4321
321-555-4321
123.555.1234
123*555*1234

800-555-4321
900-555-4321

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'
```

* Búsqueda simple:

```python
if __name__ == '__main__':

    # Búsqueda simple
    pattern = re.compile(r'abc')
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)

    print(text_to_search[1:4])
```

**Output:**

```console
<_sre.SRE_Match object; span=(1, 4), match='abc'>
abc

Process finished with exit code 0
```

* Buscar los . :

```python
if __name__ == '__main__':

    # Búsqueda simple
    pattern = re.compile(r'\.')
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)
```

**Output:**

```console
<_sre.SRE_Match object; span=(113, 114), match='.'>
<_sre.SRE_Match object; span=(134, 135), match='.'>
<_sre.SRE_Match object; span=(170, 171), match='.'>
<_sre.SRE_Match object; span=(174, 175), match='.'>
<_sre.SRE_Match object; span=(223, 224), match='.'>
<_sre.SRE_Match object; span=(254, 255), match='.'>
<_sre.SRE_Match object; span=(267, 268), match='.'>

Process finished with exit code 0
```

* Buscar Numeros de Telefono :

```python
if __name__ == '__main__':

    # Buscar numeros de telefono
    pattern = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)
    print('\n')
```

**Output:**

```console
<_sre.SRE_Match object; span=(154, 166), match='321-555-4321'>
<_sre.SRE_Match object; span=(167, 179), match='123.555.1234'>
<_sre.SRE_Match object; span=(194, 206), match='800-555-4321'>
<_sre.SRE_Match object; span=(207, 219), match='900-555-4321'>

Process finished with exit code 0
```

* Buscar Apellidos :

```python
if __name__ == '__main__':

    # Buscar apellidos
    pattern = re.compile(r'(Mr|Ms|Mrs).?\s[A-Z]\w*')
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)
        print(match.group(0))
        print(match.group(1))

    print('\n')
```

**Output:**

```console
<_sre.SRE_Match object; span=(221, 232), match='Mr. Schafer'>
Mr. Schafer
Mr
<_sre.SRE_Match object; span=(233, 241), match='Mr Smith'>
Mr Smith
Mr
<_sre.SRE_Match object; span=(242, 250), match='Ms Davis'>
Ms Davis
Ms
<_sre.SRE_Match object; span=(251, 264), match='Mrs. Robinson'>
Mrs. Robinson
Mrs
<_sre.SRE_Match object; span=(265, 270), match='Mr. T'>
Mr. T
Mr

Process finished with exit code 0
```

* Buscar e-mails :

```python
import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
gabi.montoya@gmail.com.ar
'''

if __name__ == '__main__':

    pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    matches = pattern.finditer(emails)
    for match in matches:
        print(match)
        print(match.group(0))
```

**Output:**

```console
<_sre.SRE_Match object; span=(1, 24), match='CoreyMSchafer@gmail.com'>
CoreyMSchafer@gmail.com
<_sre.SRE_Match object; span=(25, 53), match='corey.schafer@university.edu'>
corey.schafer@university.edu
<_sre.SRE_Match object; span=(54, 83), match='corey-321-schafer@my-work.net'>
corey-321-schafer@my-work.net
<_sre.SRE_Match object; span=(84, 109), match='gabi.montoya@gmail.com.ar'>
gabi.montoya@gmail.com.ar

Process finished with exit code 0
```

* Buscar urls, groups y substitutions :

```python
import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

if __name__ == '__main__':

    # Creación de grupos
    pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
    matches = pattern.finditer(urls)
    for match in matches:
        print(match)
        print(match.group(0))
        print(match.group(1))
        print(match.group(2))
        print(match.group(3))
    print('\n')

    # Substitutions
    pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
    subbed_urls = pattern.sub(r'\2\3', urls)
    print(subbed_urls)
    print('\n')
```

**Output:**

```console
<_sre.SRE_Match object; span=(1, 23), match='https://www.google.com'>
https://www.google.com
www.
google
.com
<_sre.SRE_Match object; span=(24, 42), match='http://coreyms.com'>
http://coreyms.com
None
coreyms
.com
<_sre.SRE_Match object; span=(43, 62), match='https://youtube.com'>
https://youtube.com
None
youtube
.com
<_sre.SRE_Match object; span=(63, 83), match='https://www.nasa.gov'>
https://www.nasa.gov
www.
nasa
.gov



google.com
coreyms.com
youtube.com
nasa.gov


Process finished with exit code 0
```


[Video: Regular Expressions (Regex) Tutorial: How to Match Any Pattern of Text](https://www.youtube.com/watch?v=sa-TUpSx1JA)  
[Video: Regex](https://www.youtube.com/watch?v=K8L6KVGG-7o&index=29&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)
