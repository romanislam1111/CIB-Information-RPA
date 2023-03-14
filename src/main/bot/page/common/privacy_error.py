from src.main.bot.page.base import BasePage
from main.bot.locators_.google_rpa import PrivacyErrorPageLocators
from src.main.common.log_manager import application_logger

class PrivacyErrorPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    
    def click_advanced_btn(self):
        self.get_element(*PrivacyErrorPageLocators.ADVANCED_BUTTON).click()

    def click_proceed_link(self):
        self.get_element(*PrivacyErrorPageLocators.PROCEED_LINK).click()

    
    def is_in_this_page(self):
        # return "TIN Verification".lower() in (self.driver.page_source).lower()
        try:
            self.get_element(*PrivacyErrorPageLocators.WARNING_ICON, max_wait=3)
            return True
        except Exception as e:
            application_logger.error(f'Privacy error page not loaded {e}')
            return False

    def handle_privacy_error_page(self):
        if self.is_in_this_page:
            self.click_advanced_btn()
            self.click_proceed_link()
        