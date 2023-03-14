import logging
from src.main.common.configuration_manager import ConfigurationManager
import os
from datetime import datetime
from src.main.utils.config.env_.common_env import LOG_DIR
# logging.basicConfig(level=logging.INFO, filename=f'{_dir}/{_date}.log', format="%(asctime)s ---- %(levelname)s: -->  %(message)s", datefmt='%d-%b-%Y %H:%M:%S')

class Log():

    def __init__(self):
        self._dir = LOG_DIR
        self._date = datetime.today().strftime('%d_%b_%Y')        
        'skip' if os.path.exists(self._dir) else os.makedirs(self._dir)
        self.log_file_extension = ".log"

    def set_level(self,logger, level):
        if level == 'CRITICAL':
            logger.setLevel(logging.CRITICAL)
        elif level == 'ERROR':
            logger.setLevel(logging.ERROR)
        elif level == 'WARNING':
            logger.setLevel(logging.WARNING)
        elif level == 'INFO':
            logger.setLevel(logging.INFO)
        elif level == 'DEBUG':
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.NOTSET)
        

    def get_logger(self,log_file_name='', logger_name='default_logger', level='ERROR', formatter=False ):

        if log_file_name == '':
            log_file_name = self._dir + self._date + self.log_file_extension
        else:
            log_file_name = self._dir+ log_file_name + self.log_file_extension

        logger = logging.getLogger(logger_name)
        self.set_level(logger, level)
        if not formatter: 
            formatter = logging.Formatter("%(name)s: %(asctime)s ---- %(levelname)s: -->  %(message)s", datefmt='%d-%b-%Y %H:%M:%S')
           
        file_handler = logging.FileHandler(log_file_name)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        return logger