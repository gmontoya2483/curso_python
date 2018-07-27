import functools

user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(access_level):
    def my_decorator(func):
        @functools.wraps(func)
        def secure_func(panel):
            if user.get('access_level') == access_level:
                return func(panel)
        return secure_func
    return my_decorator


@user_has_permission('admin')
def my_function(panel):
    return f'Password for {panel} panel is 1234'


print(my_function('movies'))
