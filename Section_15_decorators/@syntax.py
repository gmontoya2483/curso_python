user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(func):  # Recibe una función
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
    return secure_func  # Devuelve una función


@user_has_permission
def my_function():
    """
    Allowsto retrive the password
    :return:
    """
    return 'Password for admin panel is 1234'


@user_has_permission
def another():
    pass


print(my_function())
print(my_function.__name__)
print(my_function.__doc__)

print(another.__name__)
