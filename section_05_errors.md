
# Section 05: Errors in Python

[VOLVER a README.md](README.md)

## Indice

* [Introduccion](#introduccion)
* [Built-in errors](#built-in-errors)
* [Raising erros](#raising-errors)
* [Creando nuestros propios errores y docstrings](#creando-nuestros-propios-errores-y-docstrings)
* [Dealing with errors](#dealing-with-errors)
* [Success block and re-raising exceptions](#success-block-and-re-raising-exceptions)
* [Debugging en PyCharm](#debugging-en-pycharm)

## Introduccion

[Video: Introducción a errores en python](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445238?start=0)

## Built-in errors

* ``IndexError``
* ``KeyError``
* ``NameError``
* ``AttributeError``
* ``NotImplementedError``
* ``RuntimeError``
* ``SyntaxError``
* ``IndentationError``
* ``TabError``
* ``TypeError``
* ``ValueError``
* ``ImportError``
* ``DeprecationWarning``


[Video: Built-in errors](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445244?start=0)

## Raising erros

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car { self.make } {self.model }>'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the garage, '
                            f'but you can only add `Car` objects')

        self.cars.append(car)


if __name__ == '__main__':
    ford = Garage()

    car = Car('Ford', 'Fiesta')
    print(car)

    ford.add_car(car)
    print(len(ford))
```

[Video: Raising errors](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445250?start=0)


## Creando nuestros propios errores y docstrings


Se puede crear un error extendiende a algún ``Built-in Error`` o extendiendo de la clase ``Exception``.

```python

class MyCustomError(TypeError):
    """
    Esta es un custom error que muestra un codigo de Error
    Error Code NNN: Mensaje
    """

    def __init__(self, message, code):
        super().__init__(f'Error Code { code }: { message }')
        self.code = code


if __name__ == '__main__':

    error = MyCustomError('Probar doc string', 500)
    print(error.__doc__)

    raise MyCustomError('Este es un custom error', 500)

```

**Outpup:**  

```console
C:\Users\montoya\AppData\Local\Programs\Python\Python36-32\python.exe C:/Users/montoya/Desktop/CursoPython/Section_05_Errors/errors.py

    Esta es un custom error que muestra un codigo de Error
    Error Code NNN: Mensaje
    
Traceback (most recent call last):
  File "C:/Users/montoya/Desktop/CursoPython/Section_05_Errors/errors.py", line 18, in <module>
    raise MyCustomError('Este es un custom error', 500)
__main__.MyCustomError: Error Code 500: Este es un custom error

Process finished with exit code 1
```

> **NOTA:** El multiline ``docstring`` tiene que ser colocado debajo de la definicion de la clase. Este string se utiliza para documentar que realiza la clase.

[Video: Creando nuestros propios errores](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445258?start=0)

## Dealing with errors

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car { self.make } {self.model }>'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the garage, '
                            f'but you can only add `Car` objects')

        self.cars.append(car)


if __name__ == '__main__':
    ford = Garage()

    car = Car('Ford', 'Fiesta')
    print(car)
    ford.add_car(car)

    try:
        ford.add_car('Focus')
    except TypeError:
        print('Your car is not a Car!!')
    except ValueError:
        print('Something weird happened!!')
    finally:
        print("Este bloque se ejecuta siempre al final del try. Haya o no haya un error")

```

**Output:**

```console
C:\Users\montoya\AppData\Local\Programs\Python\Python36-32\python.exe C:/Users/montoya/Desktop/CursoPython/Section_05_Errors/app.py
<Car Ford Fiesta>
Your car is not a Car!!
Este bloque se ejecuta siempre al final del try. Haya o no haya un error

Process finished with exit code 0

```

[Video: Dealing with errors](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445260?start=0)

## Success block and re-raising exceptions

```python
class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement

    def __repr__(self):
        return f'<User {self.name}>'


def email_engaged_user (user):
    try:
        perform_calculation(user.engagement_metrics)
    except KeyError:
        print('Incorrect values provided to our calculation function.')
        # raise este raise haria un re raise de la exception para obtener el trace, pero interrumpe la ejecucion
    else:  # El else dentro del try, se ejecuta si no hubo ningun error. A diferencia del finally que se ejecuta siempre
        send_engagement_notification(user)
    finally:
        print('Print finally.')


def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2


def send_engagement_notification(user):
    print(f'Notification sent to { user }.')


if __name__ == '__main__':
    my_user = User('Rolf', {'clicks': 61, 'hits': 100})
    email_engaged_user(my_user)
```

[Video: The sucess block and re-raising exceptions](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445266?start=0)

## Debugging en PyCharm

[Video: Debugging en PyCharm](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445270?start=0)