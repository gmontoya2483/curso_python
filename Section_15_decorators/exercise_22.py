from functools import wraps


def access_control(access_level: int):
    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(*arg, **kwargs):
            if get_current_user_role() <= access_level:
                return func(*arg, **kwargs)
            else:
                raise PermissionError('You do not have the proper access level.')

        return inner_wrapper

    return outer_wrapper


def get_current_user_role() -> int:
    return 0