from selenium.webdriver.common.by import By
from src.main.utils.config.env_.rpa import URL, SEARCH_BAR_XPATH, SUBMIT_BTN

class GoogleSearchPageLocator:
    URL = URL
    SEARCH_BAR = (By.XPATH, SEARCH_BAR_XPATH)
    SUBMIT_BTN = (By.XPATH, SUBMIT_BTN)
   
    
