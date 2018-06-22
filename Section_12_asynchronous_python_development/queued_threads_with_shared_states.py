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
