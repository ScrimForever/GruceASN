import logging

def start_log():
    logger = logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    return logger

def write_info(message):
    write = logging.info(message)
    return

def write_warning(message):
    write = logging.warning(message)
    return


