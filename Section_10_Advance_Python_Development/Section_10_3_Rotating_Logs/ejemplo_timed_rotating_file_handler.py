import logging
import time

from logging.handlers import TimedRotatingFileHandler


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # agregar el rotating handler
    handler = TimedRotatingFileHandler('test_timed_rotating.log', when='m', interval=1, backupCount=3)
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    for i in range(4):
        logger.info(f'Este es el log: { i }')
        time.sleep(75)
