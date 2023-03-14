from src.main.bot.page.base import BasePage
from src.main.bot.locators_.cib.login_locators import CIBLoginPageLocator 

class NewInquiryPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def set_subject_role(self, val):
        self.select_visible_text(CIBLoginPageLocator.SUBJECT_ROLE, val)

    def set_type_of_finance(self, tof):
        self.select_visible_text(CIBLoginPageLocator.TYPE_OF_FINANCE, tof) 
    
    def set_number_of_installment(self, noi):
        self.set_value(CIBLoginPageLocator.NUMBER_OF_INSTALLMENT, noi) 

    def set_installment_amount(self, im):
        self.set_value(CIBLoginPageLocator.INSTALLMENT_AMOUNT, im) 

    def set_total_finance_amount(self, tfa):
        self.set_value(CIBLoginPageLocator.TOTAL_FINANCE_AMOUNT, tfa)  
    
    def set_periodicity_payment(self, pop): 
        self.set_value(CIBLoginPageLocator.PERIODICITY_OF_PAYMMENT, pop) 

    def set_tin(self, tin): 
        self.set_value(CIBLoginPageLocator.TIN, tin)
    
    