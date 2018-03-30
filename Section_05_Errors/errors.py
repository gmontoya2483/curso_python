
class MyCustomError(TypeError):
    """
    Esta es un custom error que muestra un codigo de Error
    Error Code NNN: Mensaje
    """

    def __init__(self, message, code):
        super().__init__(f'Error Code { code }: { message }')
        self.code = code


if __name__ == '__main__':

    error = MyCustomError('Probar doc string', 500)
    print(error.__doc__)

    raise MyCustomError('Este es un custom error', 500)
