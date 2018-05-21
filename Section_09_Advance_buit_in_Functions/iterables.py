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

    def __iter__(self):
        return self


class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]


if __name__ == '__main__':
    print(sum(FirstFiveGenerator()))

    print('\n')

    for i in FirstFiveGenerator():
        print(i)

    print('\n')

    for car in AnotherIterable():
        print(car)


    # Generator comprenhension

    my_numbers_gen = (x for x in [1,2,3,4,5])
    print(next(my_numbers_gen))
    print(next(my_numbers_gen))
    print(next(my_numbers_gen))
    print(next(my_numbers_gen))


