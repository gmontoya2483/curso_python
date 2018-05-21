
def five_numbers():
    i = 0
    while i < 5:
        yield i
        i += 1


if __name__ == '__main__':
    g1 = five_numbers()
    print(next(g1))
    print(next(g1))
    print(next(g1))
    print(next(g1))
    print(next(g1))

    print('\n')

    g2 = five_numbers()
    print(next(g2))
    print(next(g2))
    print(list(g2))

