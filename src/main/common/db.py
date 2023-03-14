from src.main.common.configuration_manager import ConfigurationManager
from src.main.common.decrypt import EncryptDecrypt
from src.main.common.exception_manager import ExceptionManager
import pyodbc
from src.main.common import log_manager
logger = log_manager.db_error_logger()
from src.main.utils.config.env_.db_env import SERVER_NAME, PORT, DB_USERNAME, DB_PASSWORD, DB_NAME, ODBC_VERSION


class DataBaseManager():
    
    def __init__(self):
        """For connecting to the database
        """   
        
        self.ServerName = SERVER_NAME
        self.Port = PORT
        self.Database  = DB_NAME
        self.UserId = DB_USERNAME
        self.Password = DB_PASSWORD
        self.odbc_driver_version =  ODBC_VERSION

        
        self.conn_string = 'DRIVER={ODBC Driver '+self.odbc_driver_version+' for SQL Server};SERVER=' + self.ServerName.strip() + ',' +\
             self.Port.strip() + ';DATABASE=' + self.Database.strip() + ';UID=' + self.UserId.strip() + ';PWD=' +\
                  self.Password.strip() + '; TrustServerCertificate=Yes;'
    

    @ExceptionManager().handle_exceptions 
    def _format_sp_result(self):
        self.results = []
        columns = [column[0] for column in self.crs.description]
        for row in self.crs.fetchall():
            self.results.append(dict(zip(columns, row)))
            
        
            
                 
            
    # @ExceptionManager().handle_exceptions    
    def execute_sp(self, procedureName, param={}):
        conn = ''    
        try:
            conn = pyodbc.connect(self.conn_string, autocommit=True)
        except pyodbc.OperationalError as err:
            logger.critical(err)
            raise (err)    
              
        paramList = ""
        paramValue = []
        
        # print(procedureName, paramValue)
        
        with conn.cursor() as self.crs:  
            for key in param:
                
                paramList += " @" + key + "=?, "
                paramValue.append(param[key])
                
            if len(paramList)>=2:
                paramList = paramList[:-2]
                procedureName = procedureName + paramList
            
            
            if param == {}:
                self.crs.execute(procedureName)
            else:    
                self.crs.execute(procedureName, paramValue)
            
            try:
                # self.results = []
                # columns = [column[0] for column in self.crs.description]
                # for row in self.crs.fetchall():
                #     self.results.append(dict(zip(columns, row)))
                self.result =  self._format_sp_result()
            except:
                pass
            finally:
                self.crs.commit()
                #conn.close()
                del self.crs 
                return self.results
            

