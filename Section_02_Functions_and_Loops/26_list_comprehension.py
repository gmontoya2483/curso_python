# Pythonic way of construction a list

numbers = list(range(10))
print(numbers)


doubled_numbers = []
for num in numbers:
    doubled_numbers.append(num * 2)
print(doubled_numbers)

# usando list comprhension
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)

phrases = [f'I am {age} years old.' for age in doubled_numbers]
print(phrases)


names_list = ['John', 'Rolf', 'Anne']
lowercase_names = [name.lower() for name in names_list]
print (lowercase_names)

## List comprehension con condicionales
even_numbers = [num for num in range(20) if num % 2 == 0]
print (even_numbers)


friends = ['rolf', 'anna', 'charlie']
guests = ['Jose', 'Rolf', 'ruth', 'Charlie', 'Michael']


present_friends = [name.capitalize() for name in friends if name.lower() in [n.lower() for n in guests]]
print (present_friends)