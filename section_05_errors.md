# Section 04: Object Oriented programming

[VOLVER a README.md](README.md)

## Indice

* [Introduccion](#introduccion)
* [Built-in errors](#built-in-errors)
* [Raising erros](#raising-errors)
* [Creando nuestros propios errores y docstrings](#creando-nuestros-propios-errores-y-docstrings)

## Introduccion

[Video: Introducción a errores en python](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445238?start=0)

## Built-in errors

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
