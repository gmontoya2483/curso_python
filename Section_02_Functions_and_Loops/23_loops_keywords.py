
# Break, sale de la ejecucion del loop
cars = ['ok', 'ok', 'ok', 'faulty', 'ok', 'ok']
for car_status in cars:
    if car_status == 'faulty':
        print('Stopping the production line')
        break
    print(f'This car is {car_status}.')

# Continue, continua con la proxima iteracion del loop
for num in range(2, 10):
    if num % 2 == 0:
        print(f'Found and even number, {num}')
        continue
    print(f'Found a number, {num} ')


# else en un for, se ejecuta al final del loop salvo que se haya salido por un break.

"""
The code below is a bit more advnaced (taken right from the official Python documentation, and searches for prime numbers):
"""

for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print(n, 'equals', x, '*', n//x)
      break
  else:
    # loop fell through without finding a factor
    print(n, 'is a prime number')
