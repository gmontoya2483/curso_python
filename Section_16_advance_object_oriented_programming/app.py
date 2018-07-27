from Section_16_advance_object_oriented_programming.admin import Admin
from Section_16_advance_object_oriented_programming.database import Database

a = Admin('Rolf', '1234', 3)

a.save()

print(Database.find(lambda x: x['username'] == 'Rolf'))
