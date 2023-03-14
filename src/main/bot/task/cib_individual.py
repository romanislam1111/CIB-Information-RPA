from src.main.bot.page.cib_pages.new_inquiry.individual import IndividualNewInquiryPage 
from src.main.bot.page.cib_pages.new_inquiry.base import NewInquiryPage 

def new_inquiry(driver):
    
    base_nip = NewInquiryPage (driver=driver) 
    individual_inp = IndividualNewInquiryPage (driver=driver)
    
    base_nip.set_subject_role('Borrower')
    base_nip.set_type_of_finance('Bai-Muazzal (Instalment Payment)')
    base_nip.set_number_of_installment('4')
    base_nip.set_installment_amount('1000') 
    base_nip.scroll_down()
    base_nip.set_total_finance_amount('10') 
    base_nip.set_periodicity_payment('Fortnight installments-15 days') 
    
    individual_inp.set_title('Mr.')
    individual_inp.set_name('Roman') 
    individual_inp.set_father_title('Mr.')
    individual_inp.set_father_name('Kamal Hossain') 
    individual_inp.set_mother_title('Mrs.')  
    individual_inp.set_mother_name('Sufia Begum') 
    base_nip.scroll_down()

    individual_inp.set_spouse_title('Mrs.') 
    individual_inp.set_spouse_name('Charlette') 
    
    base_nip.scroll_down()
    
    individual_inp.set_nid('24739546012')
    base_nip.set_tin('1234567890')
    base_nip.get_full_page_ss() 

    individual_inp.get_full_page_ss()