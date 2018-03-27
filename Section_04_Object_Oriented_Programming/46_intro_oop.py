my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 88, 90,99]
}

def average_grade(student):
    avg = sum(student['grades'])/len(student['grades'])
    return avg

print (f'The grade average is {average_grade(my_student)}')

## Con Programacion orientada a objetos, uso Clases

class Student:

    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades 
    
    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Rolf Smith', [70, 88, 90, 99])
print(f'{ student_one.name } grade average is { student_one.average()}')

print(f'Grade average is { Student.average(student_one)}')



