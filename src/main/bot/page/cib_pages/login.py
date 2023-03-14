from src.main.bot.page.base import BasePage
from src.main.bot.locators_.cib.login_locators import CIBLoginPageLocator

class CIBLoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_url(self):
        return super().go_to_url(CIBLoginPageLocator.URL)
    
    def set_username(self, usr_name):
        self.set_value(CIBLoginPageLocator.USERNAME, usr_name)
    
    def set_password(self, pwd):
        self.set_value(CIBLoginPageLocator.PASSWORD, pwd)
    
    def calcuate_captcha(self, val):
        self.get_elements(CIBLoginPageLocator.CAPTCHA_TEXT)
        
    def set_captcha(self):
        ... 
        # will be doing soon
    
    def submit(self):
        self.click_btn(CIBLoginPageLocator.LOGIN_BTN) 

    def set_password(self, pwd):
        self.set_value(CIBLoginPageLocator.PASSWORD, pwd)
    
    def set_password(self, pwd):
        self.set_value(CIBLoginPageLocator.PASSWORD, pwd)
    