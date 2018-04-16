class FirstFiveGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 5:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()


class FirstFiveIterator:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.i = 0

    def __next__(self):
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i += 1
            return current
        else:
            raise StopIteration()


if __name__ == '__main__':
    my_gen = FirstFiveGenerator()
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))
    print(next(my_gen))

    print ('\n')

    my_iterator = FirstFiveIterator()
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
