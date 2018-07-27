import functools

user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(func):
    @functools.wraps(func)
    def secure_func(panel):
        if user.get('access_level') == 'admin':
            return func(panel)
    return secure_func  # Devuelve una función


@user_has_permission
def my_function(panel):
    return f'Password for {panel} panel is 1234'


@user_has_permission
def another():
    return 'Hello'


print(my_function('movies'))

print(another())
