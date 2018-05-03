import logging
import time

from logging.handlers import RotatingFileHandler


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # agregar el rotating handler
    handler = RotatingFileHandler('test_rotating.log', maxBytes=20, backupCount=3)
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    for i in range(10):
        logger.info(f'Este es el log: { i }')
        time.sleep(1.5)
