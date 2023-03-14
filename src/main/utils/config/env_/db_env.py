import os
from dotenv import load_dotenv
from src.main.common.decrypt import EncryptDecrypt
encrypt_decrypt = EncryptDecrypt()


# load_dotenv(r'env_\nid.env')
load_dotenv(r'env_\db.env')

## DB INFO 
SERVER_NAME = encrypt_decrypt.Decrypt(os.getenv('SERVER_NAME'))
PORT = encrypt_decrypt.Decrypt(os.getenv('PORT'))
DB_USERNAME = encrypt_decrypt.Decrypt(os.getenv('DB_USERNAME'))
DB_PASSWORD = encrypt_decrypt.Decrypt(os.getenv('DB_PASSWORD'))
DB_NAME = encrypt_decrypt.Decrypt(os.getenv('DB_NAME'))
ODBC_VERSION = os.getenv('ODBC_VERSION')
