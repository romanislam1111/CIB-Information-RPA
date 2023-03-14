from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from src.main.utils.config.env_.common_env import USE_WDM, CHROME_DRIVER_PATH

def local():

    _options = Options()
    _options.add_experimental_option("detach", True)
    _options.add_argument('--ignore-certificate-errors')
    
    if USE_WDM ==1:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                chrome_options= _options
                                )
        driver.maximize_window()
        return driver
    else:
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH,
                                  chrome_options= _options)
        driver.maximize_window()
        return driver 
    
