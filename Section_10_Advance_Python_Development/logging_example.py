import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(name)s - %(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y:%H:%M:%S',
                    level=logging.DEBUG,
                    filename='logging.log'
                    )
logger = logging.getLogger(__name__)

logger.debug("This is a debug log")
logger.info("This is an info log")
logger.critical("This is critical")
logger.error("An error occurred")
