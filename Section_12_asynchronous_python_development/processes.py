import time
from multiprocessing import Process


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

    # No Processes
    print('---- Single Thread ----')
    start = time.time()
    ask_user()
    complex_calculation()
    print(f'Single thread total time: {time.time() - start}')
    print('\n')

    # 1 process
    print('---- 1 additional Process ----')

    process = Process(target=complex_calculation)

    start = time.time()

    process.start()
    ask_user()
    process.join()

    print(f'Two process total time: {time.time() - start}')
    print('\n')

    # No processes for complex tasks
    print('---- No processes for 4 complex tasks ----')

    start = time.time()

    complex_calculation()
    complex_calculation()
    complex_calculation()
    complex_calculation()

    print(f'Two process total time: {time.time() - start}')
    print('\n')

    # 2 processes for complex tasks
    print('---- 4 processes for complex tasks ----')

    process_1 = Process(target=complex_calculation)
    process_2 = Process(target=complex_calculation)
    process_3 = Process(target=complex_calculation)
    process_4 = Process(target=complex_calculation)

    start = time.time()

    process_1.start()
    process_2.start()
    process_3.start()
    process_4.start()

    process_1.join()
    process_2.join()
    process_3.join()
    process_4.join()

    print(f'Two process total time: {time.time() - start}')
    print('\n')


'''

    # 2 procesos, uno con tiempo de espera
    print('---- 2 procesos, uno con tiempo de espera ----')

    process_1 = Process(target=complex_calculation)
    process_2 = Process(target=ask_user)

    start = time.time()

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.start()

    print(f'Two process total time: {time.time() - start}')
    print('\n')
    
'''