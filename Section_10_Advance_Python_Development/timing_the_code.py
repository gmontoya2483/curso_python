import time, timeit


def power(limit):
    return [x**2 for x in range(limit)]


def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()

    print(f'Start: { start }')
    print(f'End: { end }')
    print(f'Duration: { end - start }')


if __name__ == '__main__':

    # Option 1: rodeando la funcion start y end y calcular la diferencia
    start = time.time()
    p = power(50000)
    end = time.time()

    print(f'Start: { start }')
    print(f'End: { end }')
    print(f'Duration: { end - start }')
    print('\n')

    # Option 2: user una funcion y pasar la funcion como parametro
    measure_runtime(lambda : power(50000))
    print('\n')

    # Option 3: usar timeit
    duration = timeit.timeit("[x**2 for x in range(10)]")
    print(f'Duration { duration }')
    print('\n')
