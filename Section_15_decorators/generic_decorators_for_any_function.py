import functools

user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(func):
    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user.get('access_level') == 'admin':
            return func(*args, **kwargs)
    return secure_func


@user_has_permission
def my_function(panel):
    return f'Password for {panel} panel is 1234'


@user_has_permission
def another():
    return 'Hello'


print(my_function('movies'))
print(another())
