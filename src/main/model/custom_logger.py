from src.main.model.base import  BaseModel


class DB_LOGGER(BaseModel):
     
     def insert_log_message(self, log_dict):
        data = {
            'channel': log_dict['channel'] ,
            'level': log_dict['level'],
            'message': log_dict['message'] ,
            'source': log_dict['source'] 
        }

        self.exe_sp(sp_name='insert_into_rpalogs_activitylogs', param=data)