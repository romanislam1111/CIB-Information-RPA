from src.main.bot.page.base import BasePage
from src.main.bot.locators_.google_rpa import GoogleSearchPageLocator



class SearchResultPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        
    def go_to_google(self):
        self.go_to_url(GoogleSearchPageLocator.URL)
    
    def enter_text_on_search_bar(self, value):
        self.value = value
        self.set_value(GoogleSearchPageLocator.SEARCH_BAR, value)
    
    def submit(self):
        # self.click_btn(GoogleSearchPageLocator.SUBMIT_BTN)
        self.press_enter()
    
    def take_search_result(self):
        msg = f'Google Search Result of {self.value}'
        self.get_full_page_ss(name=msg)
        
    