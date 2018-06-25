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
