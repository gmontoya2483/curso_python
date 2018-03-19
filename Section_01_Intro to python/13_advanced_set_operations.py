set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9, 11}

print (f'set_one: {set_one}')
print (f'set_two: {set_two}')


print(f'Intersección: {set_one.intersection(set_two)}')
print(f'Intersección (&): {set_one & set_two}')

print(f'Unión: {set_one.union(set_two)}')
print(f'Unión (|): {set_one | set_two}')

print(f'Diferencia: {set_one.difference(set_two)}')
print(f'Diferencia (-): {set_one - set_two}')


