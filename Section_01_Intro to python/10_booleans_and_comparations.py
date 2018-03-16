truthy = True
falsy = False

age = 20
is_over_age = age>=18
is_under_age = age < 18
is_twenty = age == 20

my_number = 5
user_number = int(input("Enter a number: "))
print (f'Are the same: {my_number == user_number}')
print (f'Are not the same: {my_number != user_number}')

# -- Combining booleans --
verdadero = True and True
falso = True and False
false = False and False

verdadero = True or False
verdadero = False or True
verdadero = True or True
falso = False or False

# -- Invertir
verdadero = not False # True
false = not True # False



