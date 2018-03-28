
# El decorador property, se puede usar en methodos que no tienen parametors.
# Al utilizar este decorado, el metodo puede ser llamado como una propiedad de la clase,
# sin utilizar los ()

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