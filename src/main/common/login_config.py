from src.main.common.configuration_manager import ConfigurationManager
from src.main.common.decrypt import EncryptDecrypt
from src.main.common.exception_manager import ExceptionManager


@ExceptionManager().handle_exceptions 
def login_config():
    lgn_config = ConfigurationManager()
    return lgn_config.get_data('url'), \
            lgn_config.get_data('username'), EncryptDecrypt().Decrypt(lgn_config.get_data("omnicard_password"))
