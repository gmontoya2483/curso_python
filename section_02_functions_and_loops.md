# Section 02: Functions and Loops

[VOLVER a README.md](README.md)

## Indice

* [If statements](#if-statements)
* [``bool()`` built-in function](#bool-built-in-function)
* [While loops](#while-loops)
* [For loop, range() function and in keyword](#for-loop-range-function-and-in-keyword)
* [Loops important keywords](#loops-important-keywords)
* [List slicing](#list-slicing)

## If statements

```python
programmer = True

if programmer is True:
    print ('You are awesome')
```
  
  
```python
is_programmer = False

if is_programmer:
    print('You are awesome')
else:
    print('You are not awesome. Learn some programming!')
```
  

```python
is_programmer = False
is_awesome = True 

if is_programmer:
    print('You are the best!')
elif is_awesome:
    print('You are not the best. but still awesome.')
else:
    print ('Be awesome!')
```

> As a recap, here's what we can do:  
> ``if is_programmer is True:``  
> `` if is_programmer is not True:``  
> `` if is_programmer:`` 
> `` if is_programmer is False:``  
> `` if not is_programmer:``  
> ``else:``

[Video: If statements](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9412526?start=0)

## ``bool()`` built-in function

Python has built-in functions such as ``int()``  to convert things to ``integers`` (whole numbers).  

Python also has a built-in function called ``bool()`` , used to convert things to ``Booleans`` (``True``/``False`` values).

In if statements, what happens is that the condition  is inside a bool() . Essentially something like this:

```python
if bool(is_programmer is False) is True:
    <block>
```

So:

``if 5:``  becomes ``if bool(5) is True:`` 

And:

``if 'hello, world!':``  becomes ``if bool('hello, world!') is True:``

That ensures that we're always comparing apples to apples, and not apples to oranges.

The ``bool()``  function gives us ``True``  for most things (e.g. ``bool('hello, world!')``  gives us ``True``). It only returns ``False`` for a couple things, like:

> ``bool(0)``  
> ``bool(0.0)``  
> ``bool('')  # empty string``  
> ``bool(None)``  
> ``bool([])  # empty list``  
> And a few others. Hope this clears some things up!

## While loops

* Ejemplos

```python
is_programmer = False
while not is_programmer:
    print('Learn programing')
    user_is_programmer = input('Are you a programmer yet? ')
    is_programmer = user_is_programmer == 'yes'


# repetir algo N veces
i = 0
while i < 10:
    print(f'Repeated {i} times')
    i = i + 1

temperature = 15
while temperature < 20:
    print('Heating...')
    temperature += 1 # temperature = temperature + 1
```

[Video: While loops](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9412528?start=0)

## For loop, range() function and in keyword

```python
# Sequences en iterables
primes = [2, 3, 5, 7, 11]
for number in primes:
    print(f'{number} is a prime number.')


kid_ages = (3, 7, 12)
for age in kid_ages:
    print(f'I have a {age} year old kid.')
```

```python
# range function: generator
print (range(20))

for i in range(20):
    print(i)
```

```python
# Iterar en diccionarios
my_friends = {
    'jose': 6,
    'Rolf': 12,
    'Anne': 6
}

for key in my_friends:
    print (f'I last saw {key} {my_friends[key]} days ago')
```

```python
# Solo en python 3
print(my_friends.items()) # nos da una lista de tuplas
for t in my_friends.items():
    (key, value) = t # Tuple destructuring
    print (f'I last saw {key} {value} days ago')


for (key, value) in my_friends.items():
     print (f'I last saw {key} {value} days ago')
```

```python
# in keyword in iterables
who_do_i_know = 'Anne'
if who_do_i_know in my_friends:
    print ('I know Anne')
```

[Video: for loop and range() funtion](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9413286?start=0)

## Loops important keywords

* Break

```python
# Break, sale de la ejecucion del loop
cars = ['ok', 'ok', 'ok', 'faulty', 'ok', 'ok']
for car_status in cars:
    if car_status == 'faulty':
        print('Stopping the production line')
        break
    print(f'This car is {car_status}.')
```

* Continue

```python
# Continue, continua con la proxima iteracion del loop
for num in range(2, 10):
    if num % 2 == 0:
        print(f'Found and even number, {num}')
        continue
    print(f'Found a number, {num} ')
```

* else

```python
# else en un for, se ejecuta al final del loop salvo que se haya salido por un break.

"""
The code below is a bit more advnaced (taken right from the official Python documentation, and searches for prime numbers):
"""

for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print(n, 'equals', x, '*', n//x)
      break
  else:
    # loop fell through without finding a factor
    print(n, 'is a prime number')
```

[Video: Loop important keywords](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9412530?start=0)


## List slicing

Es una forma de extraer parate de una lista y contruir una nueva en base al resultado.  
``[x:y]`` x es el indice de inicio e y es el indice final,  python el indice final no se muestra

### Ejemplos

```python
friends = ['rolf', 'jose','anna', 'charlie', 'mary']
```

* Rango positivo:

```python
print (friends[2:4])
```

**Output:**

```console
['anna', 'charlie']
```

> **Note:** Arranca de ```friends[2]``` hasta ```friend < 4```. Python no muestra el último valor.

* Números negativos:

```python
print (friends[-1])
```

**Output:**

```console
mary
```

> **Note:** Nos devuelve el último elemento de la lista.

* Rango negativo:

```python
print (friends[-3:-1])
```

**Output:**

```console
['anna', 'charlie']
```

> **Note:** Arranca de ```friends[-3]``` hasta ```friend < que el último```. Python no muestra el último valor.

* Mostrar los X últimos elementos de la lista:

```python
print (friends[-3:])
```

**Output:**

```console
['anna', 'charlie', 'mary']
```

* Mostrar los X primeros elementos de la lista:

```python
print (friends[:2])
```

**Output:**

```console
['rolf', 'jose']
```

* Mostrar desde el principio al -2, sin incluirlo:

```python
print (friends[:-2])
```

**Output:**

```console
['rolf', 'jose', 'anna']
```

* Ambos valores iguales:

```python
print (friends[1:1])
```

**Output:**

```console
[]
```

[Video: List slicing](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9412532?start=0)