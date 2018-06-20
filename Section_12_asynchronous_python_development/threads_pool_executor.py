import time
from concurrent.futures import ThreadPoolExecutor

def ask_user():
    start = time.time()
    user_input = input('Enter your name: ') # Esta instruccion tiene un gran tiempo de espera
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user, {time.time() - start}')


def complex_calculation():
    start = time.time()
    print('Started calculating...')
    [x**2 for x in range(20000000)]
    print(f'complex calculating, {time.time() - start}')


if __name__ == '__main__':

    # Multiple Threads (ThreadPoolExecutor)
    print('---- Multiple Threads (ThreadPoolExecutor) ----')

    start = time.time()

    with ThreadPoolExecutor(max_workers=2) as pool:
        pool.submit(complex_calculation)
        pool.submit(ask_user)

    print(f'Two threads total time: {time.time() - start}')
    print('\n')

