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
