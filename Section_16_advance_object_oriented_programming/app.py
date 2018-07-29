from Section_16_advance_object_oriented_programming.admin import Admin
from Section_16_advance_object_oriented_programming.user import User


a = Admin('Rolf', '1234', 3)
u = User('Jose', '4444')

users = [a, u]
for user in users:
    user.save()
    print(user.to_dict())
