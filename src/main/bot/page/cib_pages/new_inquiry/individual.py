from src.main.bot.page.cib_pages.new_inquiry.base import NewInquiryPage
from src.main.bot.locators_.cib.login_locators import CIBLoginPageLocator 

class IndividualNewInquiryPage(NewInquiryPage):

    def set_title(self, tilt):
        self.set_value(CIBLoginPageLocator.TITLE, tilt) 
    
    def set_name(self, name):
        self.set_value(CIBLoginPageLocator.NAME, name) 
    
    def set_father_title(self, ftilt): 
        self.set_value(CIBLoginPageLocator.FATHER_TITLE, ftilt) 

    def set_father_name(self, fname): 
        self.set_value(CIBLoginPageLocator.FATHER_NAME, fname)  

    def set_mother_title(self, mtilt): 
        self.set_value(CIBLoginPageLocator.MOTHER_TITLE, mtilt) 
    
    def set_mother_name(self, mname): 
        self.set_value(CIBLoginPageLocator.MOTHER_NAME, mname)
    
    def set_spouse_title(self, st): 
        self.set_value(CIBLoginPageLocator.SPOUSE_TITLE, st) 
    
    def set_spouse_name(self, sm): 
        self.set_value(CIBLoginPageLocator.SPOUSE_NAME, sm)
    
    def set_nid(self, nid): 
        self.set_value(CIBLoginPageLocator.NID, nid) 
    
    
    