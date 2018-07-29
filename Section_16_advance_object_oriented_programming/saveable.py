from abc import ABCMeta, abstractmethod

from Section_16_advance_object_oriented_programming.database import Database


class Saveable(metaclass=ABCMeta):
    def save(self):
        Database.insert(self.to_dict())

    @abstractmethod
    def to_dict(self):
        pass
