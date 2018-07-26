user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(func):  # Recibe una función
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
    return secure_func  # Devuelve una función


def my_function():
    return 'Password for admin panel is 1234'


my_secure_function = user_has_permission(my_function)
print(my_secure_function())
