def greet():
    name = input ('enter your name: ')
    print (f'Hello, { name }!!')


def check_primes(limit):
    for n in range (2, limit):
        check_if_prime(n)


def check_if_prime(num):
    for x in range(2, num):
        if num % x == 0:
            print(num, 'equals', x, '*', num//x)
            break
    else:
        # loop fell through without finding a factor
        print(num, 'is a prime number')


greet()
check_primes (100)




  


