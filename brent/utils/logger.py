import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file, level=logging.INFO, max_bytes=10*1024*1024, backup_count=5):
    """
    Setup a logger with a specified name, log file, and logging level.

    :param name: The name of the logger.
    :param log_file: The file to write logs to.
    :param level: The logging level.
    :param max_bytes: The maximum size of the log file before it gets rotated.
    :param backup_count: The number of backup log files to keep.
    :return: The configured logger.
    """
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create log directory if it does not exist
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(level)

    # Create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger

