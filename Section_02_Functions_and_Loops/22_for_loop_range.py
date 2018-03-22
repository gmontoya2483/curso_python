# Sequences en iterables
primes = [2, 3, 5, 7, 11]
for number in primes:
    print(f'{number} is a prime number.')


kid_ages = (3, 7, 12)
for age in kid_ages:
    print(f'I have a {age} year old kid.')


# range function: generator
print (range(20))

for i in range(20):
    print(i)


# Iterar en diccionarios
my_friends = {
    'jose': 6,
    'Rolf': 12,
    'Anne': 6
}

for key in my_friends:
    print (f'I last saw {key} {my_friends[key]} days ago')

# Solo en python 3
print(my_friends.items()) # nos da una lista de tuplas
for t in my_friends.items():
    (key, value) = t # Tuple destructuring
    print (f'I last saw {key} {value} days ago')


for (key, value) in my_friends.items():
     print (f'I last saw {key} {value} days ago')


# in keyword in iterables
who_do_i_know = 'Anne'
if who_do_i_know in my_friends:
    print ('I know Anne')
