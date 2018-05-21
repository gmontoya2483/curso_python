import logging
import Section_10_Advance_Python_Development.Section_10_1_Mas_Sobre_Logging.employee

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('sample.log')
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def add(x, y):
    """ Add Function """
    return x + y


def subtract(x, y):
    """ Subtract Function """
    return x - y


def multiply(x, y):
    """ Multiply Function """
    return x * y


def divide(x, y):
    """ Divide Function """
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by Zero')
    else:
        return result


num_1 = 20
num_2 = 0

add_result = add(num_1, num_2)
logger.debug(f'Add: { num_1 } + { num_2 } = { add_result }')

sub_result = subtract(num_1, num_2)
logger.debug(f'Sub: { num_1 } - { num_2 } = { sub_result }')

mul_result = multiply(num_1, num_2)
logger.debug(f'Mul: { num_1 } * { num_2 } = { mul_result }')

div_result = divide(num_1, num_2)
logger.debug(f'Div: { num_1 } / { num_2 } = { div_result }')


