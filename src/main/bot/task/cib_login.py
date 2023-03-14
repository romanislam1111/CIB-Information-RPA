from src.main.bot.page.cib_pages.login import CIBLoginPage


def cib_login(driver):
    clp = CIBLoginPage(driver=driver)
    clp.go_to_url()
    clp.set_username('E1b1234')
    clp.set_password('1234556')
    clp.scroll_down()
    clp.submit()
    clp.get_full_page_ss() 



