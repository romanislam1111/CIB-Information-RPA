from src.main.bot.page.google_rpa.search_result import SearchResultPage

#Return Something 
def google_search(driver, search="key"):
    
    sr = SearchResultPage(driver)
    sr.go_to_google()
    sr.enter_text_on_search_bar(search)
    sr.submit()
    sr.take_search_result()
    sr.close()