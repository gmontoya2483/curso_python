from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def walk(self):
        print('Walking...')

    @abstractmethod
    def num_legs(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 4


class Monkey(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 2


animals = [Dog('Rolf'), Monkey('Bob'), Monkey('Chita'), Dog('Boby')]
for animal in animals:
    print(isinstance(animal, Animal))
    print(animal.num_legs())

