from src.main.common.db import DataBaseManager


class TestCase():

    def _test_execute_sp(self, sp_name, data=''):


        # Test Database Layer
        
        db_object = DataBaseManager()  
        result = db_object.execute_sp(sp_name, data)
        print(result)

        # End of Test Database Layer


