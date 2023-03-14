import sys
from src.main.common.db import DataBaseManager  
from datetime import datetime

class BaseModel():
    
    def __init__(self) -> None:
        self.db = DataBaseManager()
        
    def exe_sp(self, sp_name, param={}):
        print(f'{datetime.now().strftime("%H:%I:%S %p")}: {sp_name} {" "*20}', end='\r')
        sys.stdout.write("\033[K") # To clear previous console output till end of line
        
        res = self.db.execute_sp(sp_name, param)
        if len(res)<1: 
            self.is_data_found = False
            return [{}]
        else: 
            self.is_data_found = True
            return res
    
   
   