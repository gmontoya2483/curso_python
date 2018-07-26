user = {
    'id': 1,
    'name': 'jose',
    'role': 'admin'
}


def delete_database():
    # perform deletion
    print('Database deleted!')


def check_permission(func):
    def wrapper():
        if user.get('role') == 'admin':
            return func()
        else:
            raise PermissionError('You are not an admin.')

    return wrapper


secure_delete_database = check_permission(delete_database)
print(secure_delete_database())