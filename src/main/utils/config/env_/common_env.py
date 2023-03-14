import os
from dotenv import load_dotenv


load_dotenv(r'env_\settings.env')
LOG_DIR = os.getenv('LOG_DIR')



load_dotenv(r'env_\rpa.env')

MAX_WAIT = float(os.getenv('MAX_WAIT'))
RPA_VERSION = int(os.getenv('RPA_VERSION'))
USE_WDM = int(os.getenv('USE_WDM'))
CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')