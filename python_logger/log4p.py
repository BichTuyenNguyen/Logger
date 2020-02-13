import logging
from datetime import datetime

LEVELS = {
    'info': logging.INFO,
}

class Logger:
    def __init__(self):
        log_name = r'logs\logger_{date}.log'.format(date=datetime.now().strftime('%d%m%Y'))
        self.logger = logging.basicConfig(filename=log_name,
                                          filemode='a',
                                          format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                                          datefmt='%H:%M:%S',
                                          level=logging.DEBUG)

    def start_log(self):
        self.logger = logging.info("start logging...")

    def finish_log(self):
        self.logger = logging.info("finish log!")

    def print_log(self, level, message):
        self.logger = logging.log(level, message)


# LEVELS = {
#     LevelType.DEBUG: logging.DEBUG,
#     LevelType.INFO: logging.INFO,
#     LevelType.WARNING: logging.WARNING,
#     LevelType.ERROR: logging.ERROR,
#     LevelType.CRITICAL: logging.CRITICAL,
# }

