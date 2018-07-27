class Database:
    content = {'users': []}  # class variable accesible by all the instances

    @classmethod
    def insert(cls, data):
        cls.content['users'].append(data)

    @classmethod
    def remove(cls, finder):  # lambda x: x['username'] != 'Rolf'
        cls.content['user'] = [user for user in cls.content['users'] if not finder(user)]

    @classmethod
    def find(cls, finder): # lambda x: x['username'] == 'Rolf'
        return [user for user in cls.content['users'] if finder(user)]
