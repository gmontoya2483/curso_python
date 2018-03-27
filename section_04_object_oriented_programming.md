# Section 04: Object Oriented programming

[VOLVER a README.md](README.md)

## Indice

* [Introduccion a Programacion Orientada a Objetos](#introduccion-a-programacion-orientada-a-objetos)

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