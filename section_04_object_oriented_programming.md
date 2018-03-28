# Section 04: Object Oriented programming

[VOLVER a README.md](README.md)

## Indice

* [Introduccion a Programacion Orientada a Objetos](#introduccion-a-programacion-orientada-a-objetos)
* [Metodos especiales - dunder methods](#metodos-especiales-dunder-methods)
* [Herencia](#herencia)
* [Decorador Property](#decorador-property)
* [Decoradores classmethod y staticmethod](#decoradores-classmethod-y-staticmethod)

## Introduccion a Programacion Orientada a Objetos

```python
class Student:

    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades 

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Rolf Smith', [70, 88, 90, 99])
print(f'{ student_one.name } grade average is { student_one.average()}')

print(f'Grade average is { Student.average(student_one)}')
```

[Video: Introducción a OOP](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9417788?start=0)  
[Video: More about classes and Objects](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9417796?start=0)

## Metodos especiales (dunder methods)

```python
# __init__
# Este metodo es llamado cuando se crea un nuevo objeto
class Student:
    
    
    def __init__(self, name):
        self.name = name
    

# __class__
# Devuelve la clase a la que pertenece un objeto
movies = ['Matrix', 'finding nemo']
print(movies.__class__)
print('Hi'.__class__)



class Garage:
    def __init__(self):
        self.cars = []
    
    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, i):
        return self.cars[i]
    
    def __repr__(self):
        return f'<Garage {self.cars}>'
    
    def __str__(self):
        return f'Garage with {len(self)} cars.'


#__len__
# Este metodo debe ser definido. Si no esta definido devuelve un error

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(len(ford)) # llamada al metodo __len__

# __getitem__
# este metodo es usado para idexar un objeto. Si no esta definido devuelve error

print(ford[0])
print(ford[1])

# Al implemtar len y getitem methods, se habilitan nuevas funcionalidades
# Se puede iterar

for item in ford:
    print(item)

# __repr__
# devuelve un string que representa al objeto


# __str__
# Devuelve un string que le dice al usuario alguna informacion acerca del objeto

print(ford)
```

**Output:**

```console
C:\Users\montoya\Desktop\CursoPython\Section_04_Object_Oriented_Programming>python 51_metodos_especiales.py
<class 'list'>
<class 'str'>
2
Fiesta
Focus
Fiesta
Focus
Garage with 2 cars.
```

[Video: Magic methods](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9417802?start=0)

## Herencia

```python
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)



class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 37.5


if __name__ == '__main__':
    rolf = WorkingStudent('Rolf','MIT', 15.50)
    rolf.marks.append(56)
    rolf.marks.append(12)
    print (rolf.salary)
    print (rolf.average())
    print (rolf.weekly_salary())
```

**Output:**

```console
C:\Users\montoya\Desktop\CursoPython\Section_04_Object_Oriented_Programming>python 53_herencia.py
15.5
34.0
581.25
```

[Video: Herencia](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9417806?start=0)

## Decorador Property

El decorador property, se puede usar en methodos que no tienen parametors.
Al utilizar este decorado, el metodo puede ser llamado como una propiedad de la clase, sin utilizar los ()

```python
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    @property
    def average(self):
        return sum(self.marks)/len(self.marks)



class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary * 37.5


if __name__ == '__main__':
    rolf = WorkingStudent('Rolf','MIT', 15.50)
    rolf.marks.append(56)
    rolf.marks.append(12)
    print (rolf.salary)
    print (rolf.average)
    print (rolf.weekly_salary)
```

**Output:**

```console
C:\Users\montoya\Desktop\CursoPython\Section_04_Object_Oriented_Programming>python python 54_decorador_property.py
15.5
34.0
581.25
```

[Video: Decorador - @property](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9417822?start=0)

## Decoradores classmethod y staticmethod

* @classmethod

    Usa la clase como primer argumento y tiene acceso a la clase, pero no al objeto. La convencion es tener el primer argumento con el nombre ``cls``:

    ```python
    class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)


    my_object = Foo()
    my_object.hi()
    Foo.hi()
    ```

    **Output:**

    ```console
    Foo
    Foo
    ```

* @staticmethod

    No utiliza ni el objeto, ni la clase como primer argumento. No tiene acceso a la clase, ni al objeto:

    ```python
    class Bar:
    @staticmethod
    def hi():
        print('Hello, I don\'t take parameters.')

    my_object_bar = Bar()
    my_object_bar.hi()
    Bar.hi()
    ```

    **Output:**

    ```console
    Hello, I don't take parameters.
    Hello, I don't take parameters.
    ```

[Video: Decoradores classmethod y staticmethod](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9417826?start=0)  
[Video: Ejemplos classmethod y staticmethod](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9417828?start=0)