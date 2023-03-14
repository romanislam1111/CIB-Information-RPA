from src.main.bot import driver_setup
from src.main.bot.task.cib_login import cib_login 
from src.main.bot.task.cib_individual import new_inquiry

driver = driver_setup.local()
cib_login(driver=driver) 
new_inquiry (driver=driver) 
