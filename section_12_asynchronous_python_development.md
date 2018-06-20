# Section 12: Web Scraping

[VOLVER a README.md](README.md)

## Indice

* [Introduction to this section](#introduction-to-this-section)
* [Dining philosophers Problem](#dining-philosophers-problem)
* [Processes and Threads](#processes-and-threads)
* [Python GIL](#python-gil)
* [Ejemplo de Threads en Python](#ejemplo-de-threads-en-python)
* [Usando concurrent Feature - ThreadPoolExecutor](#sando-concurrent-feature-threadpoolexecutor)
* [DO NOT KILL THREADS](#do-not-kill-threads)


## Introduction to this section

No es posible ejecutar Multiples cosas a la vez en ``Python``, pero se puede simular. Es decir Python no es ``Multithread``.

**Glosario:**

* ``Synchronous``: actions that happen one after another. Programming as we've seen it until now is synchronous, because each line executes after the previous one.  

* ``Asynchronous``: actions that don't necessary happen after one another, or that can happen in arbitrary order ("without synchrony").
Concurrency: The ability of our programs to run things in different order every time the program runs, without affecting the final outcome.
Parallelism: Running two or more things at the same time.  

* ``Thread``: A line of code execution that can run in one of your computer's cores.  

* ``Process``: One of more threads and the resources they need (e.g. network connection, mouse pointer, hard drive access, or even the core(s) in which the thread(s) run).  

* ``GIL``: A key, critical, important resource in any Python program. Only one is created per Python process, so it's unique in each.  

[Video: Introduction to this section](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9489792?start=0)


## Dining philosophers Problem

[Video: Dining philosophers Problem](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9489740?start=0)


## Processes and Threads

[Video: Processes and Threads](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9489742?start=0)


## Python GIL

***GIL: Global Interpreter Lock.***

Dado que en ``Python`` no hay multi threads, el objetivo de los Threads es reducir el tiempo de espera.
Por otro lado si todos los threads estan haciendo cosas y no hay timepos de espera el uso de thread no va a ser beneficioso.


[Video: Python GIL](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9489744?start=0)


## Ejemplo de Threads en Python


```Python

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


    # Multiple Threads (dos tareas complejas)
    print('---- Multiple Threads (only 2 complex tasks) ----')

    thread1 = Thread(target=complex_calculation)
    thread2 = Thread(target=complex_calculation)

    start = time.time()
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f'Three threads total time: {time.time() - start}')
    print('\n')
```

**OUTPUT:**

```console
---- Single Thread ----
Enter your name: jose
Hello, jose
ask_user, 3.303330183029175
Started calculating...
complex calculating, 10.154015302658081
Single thread total time: 13.457345485687256


---- Multiple Threads (waiting time and complex task ----
Started calculating...
Enter your name: jose
Hello, jose
ask_user, 3.8133809566497803
complex calculating, 9.687968492507935
Two threads total time: 9.688968658447266


---- Multiple Threads (only 2 complex tasks ----
Started calculating...
Started calculating...
complex calculating, 17.946794509887695
complex calculating, 18.562856197357178
Three threads total time: 18.569857120513916



Process finished with exit code 0
```

[Video: Ejemplo Threads en Python](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9489746?start=0)

## Usando concurrent Feature - ThreadPoolExecutor

```python
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
```

**OUTPUT:**

```console
---- Multiple Threads (ThreadPoolExecutor) ----
Started calculating...
Enter your name: jose
Hello, jose
ask_user, 2.9872984886169434
complex calculating, 9.172917127609253
Two threads total time: 9.173917055130005



Process finished with exit code 0
```

[Video: Usando concurrent Feature - ThreadPoolExecutor](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9489748?start=0)


## DO NOT KILL THREADS

[Video: Don´t kill threads](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9489750?start=0)