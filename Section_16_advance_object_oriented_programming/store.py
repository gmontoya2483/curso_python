from Section_16_advance_object_oriented_programming.database import Database


class Store:
    def to_dic(self):
        pass

    def save(self):
        Database.insert(self.to_dic())
