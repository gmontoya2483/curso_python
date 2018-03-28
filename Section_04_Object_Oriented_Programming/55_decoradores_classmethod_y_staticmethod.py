
# Instance method (usa al objeto como primer argumento)

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks)/len(self.marks)

rolf = Student('Rolf','MIT')
rolf.marks.append(56)
rolf.marks.append(12)

print (rolf.average())
print (Student.average(rolf)) # se le pasa rolf como parametro self

# Class method (usa la clase como primer argumento)

class Foo:
    
    @classmethod
    def hi(cls):
        print(cls.__name__)

my_object = Foo()
my_object.hi()
Foo.hi()

# Static method (no usa nada como primer argumento) 

class Bar:
    @staticmethod
    def hi():
        print('Hello, I don\'t take parameters.')

my_object_bar = Bar()
my_object_bar.hi()
Bar.hi()








    