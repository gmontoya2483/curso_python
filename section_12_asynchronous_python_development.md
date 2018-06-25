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
* [Documentacion adicional](#documentacion-adicional)
* [Dealing with shared state in Threads - BE CAREFUL](#dealing-with-shared-state-in-threads-be-careful)
* [Queuing in Threads with shared state](#queuing-in-threads-with-shared-state)
* [Using Generators instead of Threads](#using-generators-instead-of-threads)
* [Single threaded task scheduler](#single-threaded-task-scheduler)
* [Yielding from another iterator](#yielding-from-another-iterator)
* [Receiving data through yield](#receiving-data-through-yield)
* [Async and await keywords](#async-and-await-keywords)
* [Documentacion adicional](#documentacion-adicional)

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

## Multiprocessing


El ``Multiprocessing`` es ideal para ejecutar varias tareas complejas por separado como se muestra en los siguientes ejemplos:

```python
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
```

**OUTPUT:**

```console
---- Single Thread ----
Enter your name: jose
Hello, jose
ask_user, 2.9649999141693115
Started calculating...
complex calculating, 8.81000018119812
Single thread total time: 11.775000095367432


---- 1 additional Process ----
Enter your name: jos
Hello, jos
ask_user, 2.175999879837036
Started calculating...
complex calculating, 8.97100019454956
Two process total time: 11.30899977684021


---- No processes for 4 complex tasks ----
Started calculating...
complex calculating, 8.785000085830688
Started calculating...
complex calculating, 8.759000062942505
Started calculating...
complex calculating, 8.745000123977661
Started calculating...
complex calculating, 8.86300015449524
Two process total time: 35.1540002822876


---- 4 processes for complex tasks ----
Started calculating...
Started calculating...
Started calculating...
Started calculating...
complex calculating, 18.062999963760376
complex calculating, 18.215999841690063
complex calculating, 18.725000143051147
complex calculating, 18.889999866485596
Two process total time: 19.23199987411499


Process finished with exit code 0
```

> **NOTA:** No se debe utilizar multi processing cuando una tarea tiene tiempo de espera a que por eljemplo el usuario introduza alguna información, dado que los procesos no tienen ancceso a lo recursos de la main thread.

```python
 # 2 2 procesos, uno con tiempo de espera
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
```
**OUTPUT:**

```console
--- 2 procesos, uno con tiempo de espera ---
Started calculating...
Enter your name: Process Process-3:
Traceback (most recent call last):
  File "C:\Users\montoya\AppData\Local\Programs\Python\Python36-32\lib\multiprocessing\process.py", line 258, in _bootstrap
    self.run()
  File "C:\Users\montoya\AppData\Local\Programs\Python\Python36-32\lib\multiprocessing\process.py", line 93, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\montoya\Desktop\CursoPython\Section_12_asynchronous_python_development\processes.py", line 7, in ask_user
    user_input = input('Enter your name: ') # Esta instruccion tiene un gran tiempo de espera
EOFError: EOF when reading a line
complex calculating, 8.74887490272522
Traceback (most recent call last):
  File "C:/Users/montoya/Desktop/CursoPython/Section_12_asynchronous_python_development/processes.py", line 56, in <module>
    process_2.start()
  File "C:\Users\montoya\AppData\Local\Programs\Python\Python36-32\lib\multiprocessing\process.py", line 99, in start
    assert self._popen is None, 'cannot start a process twice'
AssertionError: cannot start a process twice

Process finished with exit code 1
```

[Video: Multiprocessing in Python](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9489754?start=0)


## Usando concurrent Feature - ProcessPoolExecutor

```python

import time
from concurrent.futures import ProcessPoolExecutor


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
    start = time.time()

    with ProcessPoolExecutor(max_workers=3) as pool:
        pool.submit(complex_calculation)
        pool.submit(complex_calculation)
        pool.submit(complex_calculation)

    print(f'Two process total time: {time.time() - start}')

```

**OUTPUT:**

```console
Started calculating...
Started calculating...
Started calculating...
complex calculating, 17.967000007629395
complex calculating, 18.013999938964844
complex calculating, 18.13099980354309
Two process total time: 18.642000198364258

Process finished with exit code 0
```

### Otros ejemplos

```python
import time
from concurrent.futures import ProcessPoolExecutor


def complex_calculation(num):
    start = time.time()
    print(f'Started calculating ({num})...')
    [x**2 for x in range(20000000)]
    print(f'complex calculating ({num}), {time.time() - start}')


if __name__ == '__main__':
    start = time.time()

    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    with ProcessPoolExecutor(max_workers=3) as pool:
        for task in tasks:
            pool.submit(complex_calculation, task)

    print(f'Two process total time: {time.time() - start}')

```

**OUTPUT:**

```console
Started calculating (1)...
Started calculating (2)...
Started calculating (3)...
complex calculating (3), 14.684000015258789
Started calculating (4)...
complex calculating (1), 14.809999942779541
Started calculating (5)...
complex calculating (2), 14.845999717712402
Started calculating (6)...
complex calculating (5), 13.858000040054321
Started calculating (7)...
complex calculating (6), 14.222000360488892
Started calculating (8)...
complex calculating (4), 14.424999952316284
Started calculating (9)...
complex calculating (7), 14.620999813079834
Started calculating (10)...
complex calculating (9), 14.493000268936157
complex calculating (8), 14.585999727249146
complex calculating (10), 9.216999769210815
Two process total time: 52.938000202178955

Process finished with exit code 0
```

```python
import time
from concurrent.futures import ProcessPoolExecutor, as_completed


def complex_calculation(num):
    start = time.time()
    print(f'Started calculating ({num})...')
    [x**2 for x in range(20000000)]
    print(f'complex calculating ({num}), {time.time() - start}')
    return f'Processed ({num})'


if __name__ == '__main__':
    start = time.time()

    tasks = [1, 2, 3, 4, 5]

    pool = ProcessPoolExecutor(max_workers=3)
    futures = []
    resultados = []

    for task in tasks:
        futures.append(pool.submit(complex_calculation, task))

    for x in as_completed(futures):
        print(x.result())
        resultados.append(x.result())

    print(f'Several process total time: {time.time() - start}')
    print(resultados)
```

**OUTPUT:**

```console
Started calculating (1)...
Started calculating (2)...
Started calculating (3)...
complex calculating (2), 14.387438535690308
Started calculating (4)...
Processed (2)
complex calculating (3), 14.644464015960693
Started calculating (5)...
Processed (3)
complex calculating (1), 14.729472637176514
Processed (1)
complex calculating (4), 10.781078100204468
Processed (4)
complex calculating (5), 10.598059892654419
Processed (5)
Several process total time: 25.66256594657898
['Processed (2)', 'Processed (3)', 'Processed (1)', 'Processed (4)', 'Processed (5)']

Process finished with exit code 0
```


[Video: concurrent Feature - ProcessPoolExecutor](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9489758?start=0)


## Dealing with shared state in Threads - BE CAREFUL

Hay que ser cuidadoso cuando se hace multithreading y se utilizan recursos compartidos, como se puede ver en el siguiente ejemplo (donde se agregaron demoras en forma adrede), el resultado no es el esperado.

```python
import time, random
from threading import Thread

counter = 0


def increment_counter():
    global counter
    time.sleep(random.random())
    counter += 1
    time.sleep(random.random())
    print(f'New counter value: {counter}')
    time.sleep(random.random())
    print('------------')


for x in range(10):
    t = Thread(target=increment_counter)
    time.sleep(random.random())
    t.start()

``` 

**OUTPUT:**

```console
New counter value: 2
------------
New counter value: 2
------------
New counter value: 5
New counter value: 6
------------
------------
New counter value: 6
New counter value: 6
------------
------------
New counter value: 8
------------
New counter value: 8
------------
New counter value: 9
------------
New counter value: 10
------------

Process finished with exit code 0
```

[Video: Dealing with shared state in Threads](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9489764?start=0)

## Queuing in Threads with shared state

Para poder solucionar el uso de recursos compartidos es necesarios utilizar diferentes ``queues``. La propiedad que tiene ``Queue.queue`` es que una vez que un thread toma el recurso lo lockea y no puede ser accedido por otro.

```python
import time
import random
import queue
from threading import Thread

counter = 0
job_queue = queue.Queue()  # things to be printed out
counter_queue = queue.Queue()  # amounts by which to increase counter


def increment_manager():
    global counter
    while True:
        increment = counter_queue.get()  # This waits until an item is available and then LOCKS the queue
        time.sleep(random.random())
        old_counter = counter
        time.sleep(random.random())
        counter = old_counter + increment
        time.sleep(random.random())
        job_queue.put((f'New counter value is {counter}', '-----------'))
        time.sleep(random.random())
        counter_queue.task_done()  # this unlocks the queue
        time.sleep(random.random())


def printer_manager():
    while True:
        for line in job_queue.get():
            print(line)
            time.sleep(random.random())
        job_queue.task_done()


def increment_counter():
    counter_queue.put(1)


if __name__ == '__main__':

    # printer_manager and increment_manager run continuously because of the `daemon` flag.
    Thread(target=increment_manager, daemon=True).start()
    Thread(target=printer_manager, daemon=True).start()

    worker_threads = [Thread(target=increment_counter) for thread in range(10)]

    for thread in worker_threads:
        thread.start()

    for thread in worker_threads:
        thread.join()

    counter_queue.join()  # wait for counter_queue to be empty
    job_queue.join()  # wait for job_queue to be empty
```

**OUTPUT:**

```console
New counter value is 1
-----------
New counter value is 2
-----------
New counter value is 3
-----------
New counter value is 4
-----------
New counter value is 5
-----------
New counter value is 6
-----------
New counter value is 7
-----------
New counter value is 8
-----------
New counter value is 9
-----------
New counter value is 10
-----------

Process finished with exit code 0
```

[VIDEO: Queuing in Threads with shared state](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9489768?start=0)


## Using Generators instead of Threads

* Ejemplo del uso de generators:

````python
def countdown(n):
    while n > 0:
        yield n
        n -= 1


if __name__ == '__main__':
    c1 = countdown(10)
    c2 = countdown(20)
    print(next(c1))
    print(next(c2))
    print(next(c1))
    print(next(c2))
````

**OUTPUT:**
````console
10
20
9
19

Process finished with exit code 0
````

[Video: Using Generators instead of Threads](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9489766?start=0)


## Single threaded task scheduler

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1


if __name__ == '__main__':
    tasks = [countdown(10), countdown(5), countdown(20)]

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Task finished')
```

**OUTPUT:**
````console
10
5
20
9
4
19
8
3
18
7
2
17
6
1
16
5
Task finished
15
4
14
3
13
2
12
1
11
Task finished
10
9
8
7
6
5
4
3
2
1
Task finished

Process finished with exit code 0
````

[Video: Using Generators instead of Threads](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9489774?start=0)


## Yielding from another iterator

```python
from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def get_friend():
    yield from friends


def greet(g):
    while True:
        try:
            friend = next(g)
            yield f'HELLO {friend}'
        except StopIteration:
            pass


if __name__ == '__main__':
    friends_generator = get_friend()
    g = greet(friends_generator)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(friends_generator))
```

**OUTPUT:**
````console
HELLO Rolf
HELLO Jose
HELLO Charlie
Jen

Process finished with exit code 0
````

[Video: Yielding from another iterator](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9489776?start=0)


## Receiving data through yield

* Ejemplo Simple:

```python
def greet():
    friend = yield
    print(f'Hello, {friend}')


if __name__ == '__main__':
    g = greet()
    g.send(None)  # priming the generator
    g.send('Adam')
```

**OUTPUT:**
````console
Hello, Adam
Traceback (most recent call last):
  File "C:/Users/montoya/Desktop/CursoPython/Section_12_asynchronous_python_development/generators_receiving_data_throgh_yield.py", line 9, in <module>
    g.send('Adam')
StopIteration

Process finished with exit code 1
````


````python
from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(g):
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)


if __name__ == '__main__':
    greeter = greet(friend_upper())
    greeter.send(None)
    greeter.send('Hello')
    greeter.send('Hola')
    greeter.send('Chau')
````

**OUTPUT:**
````console
Hello ROLF
Hola JOSE
Chau CHARLIE

Process finished with exit code 0
````

[Video: Receiving data through yield](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9489778?start=0)

## Async and await keywords

[Async and await keywords](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9489780?start=0)

```python
from collections import deque
from types import coroutine

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    print('Starting...')
    await g
    print('Ending....')


if __name__ == '__main__':
    greeter = greet(friend_upper())
    greeter.send(None)
    greeter.send('Hello')
    greeter.send('Hola')
    greeter.send('Chau')
    greeter.send('Chau')
    greeter.send('Chau')
```

**OUTPUT:**
````console
Starting...
Hello ROLF
Hola JOSE
Chau CHARLIE
Chau JEN
Chau ANNA
Ending....
Traceback (most recent call last):
  File "C:/Users/montoya/Desktop/CursoPython/Section_12_asynchronous_python_development/async_await.py", line 28, in <module>
    greeter.send('Chau')
StopIteration

Process finished with exit code 1
````

## Documentacion adicional

[PYTHON: A QUICK INTRODUCTION TO THE CONCURRENT.FUTURES MODULE](http://masnun.com/2016/03/29/python-a-quick-introduction-to-the-concurrent-futures-module.html)  
[David Beazley - Python Concurrency From the Ground Up: LIVE! - PyCon 2015](https://www.youtube.com/watch?reload=9&v=MCs5OvhV9S4)  
[Keynote David Beazley - Topics of Interest (Python Asyncio)](https://www.youtube.com/watch?v=ZzfHjytDceU)  
[Raymond Hettinger, Keynote on Concurrency, PyBay 2017](https://www.youtube.com/watch?v=9zinZmE3Ogk)

