import logging
from Section_10_Advance_Python_Development.Section_10_2_Ejemplo_logging_app.employee import Employee

if __name__ == '__main__':

    logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(name)s:%(lineno)d] %(message)s',
                        datefmt='%d-%m-%Y:%H:%M:%S',
                        level=logging.DEBUG,
                        filename='logging.log')
    logger = logging.getLogger(__name__)

    logger.info('Arranco el Main')

    emp_1 = Employee('John', 'Smith')
    emp_2 = Employee('Corey', 'Schafer')
    emp_3 = Employee('Jane', 'Doe')





