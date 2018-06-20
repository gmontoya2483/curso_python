import time
from threading import Thread


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

    # Single Thread
    print('---- Single Thread ----')
    start = time.time()
    ask_user()
    complex_calculation()
    print(f'Single thread total time: {time.time() - start}')
    print('\n')

    # Multiple Threads (Timepo de espera y tarea compleja)
    print('---- Multiple Threads (waiting time and complex task) ----')

    thread1 = Thread(target=complex_calculation)
    thread2 = Thread(target=ask_user)

    start = time.time()
    thread1.start()
    thread2.start()

    thread1.join()  # join le dice al thread principal que espere su finalización
    thread2.join()

    print(f'Two threads total time: {time.time() - start}')
    print('\n')

    # Single Thread ((three complex tasks)
    print('---- Single Thread (only 3 complex tasks) ----')

    complex_calculation()
    complex_calculation()
    complex_calculation()

    print(f'Single threads total time: {time.time() - start}')
    print('\n')

    # Multiple Threads (three complex tasks)
    print('---- Multiple Threads (only 3 complex tasks) ----')

    thread1 = Thread(target=complex_calculation)
    thread2 = Thread(target=complex_calculation)
    thread3 = Thread(target=complex_calculation)

    start = time.time()
    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print(f'Three threads total time: {time.time() - start}')
    print('\n')







