# Section 02: Functions and Loops

[VOLVER a README.md](README.md)

## Indice

* [If statements](#if-statements)
* [``bool()`` built-in function](#bool-built-in-function)
* [While loops](#while-loops)



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
