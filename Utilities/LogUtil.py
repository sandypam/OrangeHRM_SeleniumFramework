import logging
import os
import time


class Logger():

    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # Prevent duplicate handlers
        if self.logger.handlers:
            return

        fmt = logging.Formatter(
            '%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        curr_time = time.strftime("%Y-%m-%d")

        base_dir = os.path.dirname(__file__)
        log_dir = os.path.abspath(os.path.join(base_dir, "..", "Logs"))
        os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(log_dir, f"log_{curr_time}.txt")

        # "a" to append the logs in the same file, "w" to generate new logs and delete old one
        fh = logging.FileHandler(log_file, mode='a')
        fh.setLevel(file_level)
        fh.setFormatter(fmt)

        self.logger.addHandler(fh)