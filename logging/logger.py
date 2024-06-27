import logging
from config import LOG_FILE_PATH

logging.basicConfig(filename=LOG_FILE_PATH, level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def get_logger(name):
    return logging.getLogger(name)
