# Section 04: Object Oriented programming

[VOLVER a README.md](README.md)

## Indice

* [Introduccion a Programacion Orientada a Objetos](#introduccion-a-programacion-orientada-a-objetos)

* [Metodos especiales - dunder methods](#metodos-especiales-dunder-methods)

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