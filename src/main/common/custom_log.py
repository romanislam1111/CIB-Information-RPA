import datetime
import os 
from src.main.utils.config.env_.common_env import LOG_DIR
from src.main.model.custom_logger import DB_LOGGER
INSERT_INTO_DB = False

class CUSTOM_LOGGER:
    
    def __init__(self, channel,file_name_ext):
        self.channel = channel
        self.file_name_ext=file_name_ext

    def write_log(self, level_name, message):

        # FORMAT logs\ERROR.log
        # 16-Nov-2022 12:47:41 ---- INFO: --> ERROR MSG
        # write log to file 
        _date = datetime.datetime.today().strftime('%d_%b_%Y')  
        _y_m = datetime.datetime.today().strftime('%b_%Y')        

        _dir = LOG_DIR + self.channel+'\\'+_y_m
        
        if not os.path.exists(_dir): os.makedirs(_dir)
        
        file_dir = _dir+'\\'+ self.file_name_ext + _date+'.log'
        f = open(file_dir,'a+')
        now = datetime.datetime.now().strftime('%I:%M:%S %p')
        full_msg = f'{now} - {self.channel} - {level_name} - {message}\r'
        f.write(full_msg) 
        f.close()

        # write log to db
        log_dict = {
            'channel':  self.channel ,
            'level': level_name,
            'message': message,
            'source': self.file_name_ext 
        }
        if INSERT_INTO_DB:
            DB_LOGGER().insert_log_message(log_dict)