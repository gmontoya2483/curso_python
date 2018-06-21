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

    pool = ProcessPoolExecutor(max_workers=3)

    with ProcessPoolExecutor(max_workers=3) as pool:
        for task in tasks:
            pool.submit(complex_calculation, task)

    print(f'Two process total time: {time.time() - start}')
