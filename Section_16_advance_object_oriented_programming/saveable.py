from Section_16_advance_object_oriented_programming.database import Database


class Saveable:
    def save(self):
        Database.insert(self.to_dict())
