from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import urllib.request as urllib2
from selenium.webdriver.support.ui import Select
from src.main.utils.config.env_.rpa import MAX_WAIT
from src.main.common.custom_log import CUSTOM_LOGGER
from src.main.common.screenshotlog import ScreenshotHandler
from src.main.bot.page.pageutils import get_short_url
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
LOGGER_NAME = 'CIB_RPA'

actions:ActionChains 
cl = CUSTOM_LOGGER(LOGGER_NAME, file_name_ext="page")
ss_handler:ScreenshotHandler

GET_ELEMENTS_WAIT = 1
ELEMENT_DEFAULT_MAX_WAIT = 10

class BasePage:

    def __init__(self, driver):
        global ss_handler, actions
        self.driver = driver
        ss_handler = ScreenshotHandler(driver=driver)
        actions = ActionChains(driver)

    def go_to_url(self, url:str):
        try:
            msg = f"We are going to {url}"
            cl.write_log("INFO", msg)
            self.driver.get(url)
            current_url:str = self.driver.current_url
            
            if 'Not Found' in self.driver.page_source:
                raise RuntimeError ("404 Not found!")
            elif get_short_url(current_url) == get_short_url(url):
                ss_filepath = ss_handler.take_screenshot("INFO_GotoUrl")
                msg = f"Successfully got {current_url}, screenshot: {ss_filepath}"
                cl.write_log("INFO", msg)
            else:
                msg = f"Invalid or Inappropriate URL  {url}, Current URL:'{current_url}'"
                raise Exception(msg)
            
        except Exception as e:
            ss_filepath = ss_handler.take_screenshot("ERROR_GotoUrl")
            msg = f"Screenshot saved at: {ss_filepath}, \n Exception: {str(e)}"
            cl.write_log("Error", msg)
            self.close()
        
    def get_elements(self, *by):
        sleep(GET_ELEMENTS_WAIT)
        elements = WebDriverWait(self.driver, MAX_WAIT).until(
            lambda driver: self.driver.find_elements(*by))
        return elements

    def get_element(self, *by, max_wait=ELEMENT_DEFAULT_MAX_WAIT):
        try:
            element = WebDriverWait(self.driver, max_wait).until(
                lambda driver: self.driver.find_element(*by))
            #Log txt calling here
            if element is not None:
                msg = f"got a  {element.tag_name}, type: {str(element.aria_role)},  -->  Field or Name: {element.accessible_name}, -->  Tracking ID: {str(element.id)}, --> ScreenShot media location: {(ss_handler.dir)}, -->  Folder name for each run case: {ss_handler.folder_name} \n"
                
                try:  # To avoid Bangla 
                    cl.write_log('info', message=msg)  
                except:
                    msg = f"got a  {element.tag_name}, type: {str(element.aria_role)},  -->  Field or Name: {'Unknown'}, -->  Tracking ID: {str(element.id)}, --> ScreenShot media location: {(ss_handler.dir)}, -->  Folder name for each run case: {ss_handler.folder_name} \n"
                    cl.write_log('info', message=msg)  
                ss_handler.take_screenshot_of_element("ELEMENT", element)
                
                return element
            else:
                raise Exception('Element is None')
            
        except Exception as e:
            self.close()
            cl.write_log('ERROR', message=str(e)) 
         

    def scroll_down(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight / 8)")
        
    def set_value(self, ele, val):
        
        try:
            element = self.get_element(*ele)
            # element.clear()  # For Select BOXES
            element.send_keys(str(val))
            msg = 'set ' + str(val) +'\n'
            cl.write_log('info', message=msg) 
            ss_handler.take_screenshot_of_element(element.accessible_name, element) 
            
            
        except Exception as e:
            cl.write_log('error', message=str(e))
            self.close()
            raise("RAISED EXCEPTION (SET VALUE)", e) 

    
    def is_internet_on(self,url):
        import ssl
        try:
            urllib2.urlopen(url, timeout=10, context=ssl._create_unverified_context())
            return True
        except urllib2.URLError as err: 
            return False

    def select_visible_text(self, ele, val):
        element = WebDriverWait(self.driver, 100).until(lambda driver: driver.find_element(*ele))
        try:
            # element.clear()  # For Select BOXES
            Select(element).select_by_visible_text(str(val))
        except Exception as e:
            raise("RAISED EXCEPTION (SET VALUE)", e)


    def select_value(self, ele, val):
        element = WebDriverWait(self.driver, 100).until(lambda driver: driver.find_element(*ele))
        try:
            # element.clear()  # For Select BOXES
            Select(element).select_by_value(str(val))
        except Exception as e:
            raise("RAISED EXCEPTION (SET VALUE)", e)
      
    
    
    def click_btn(self, ele):
        element = self.get_element(*ele)
        element.click()

    def press_enter(self):
        actions.send_keys(Keys.ENTER)
        actions.perform()


    def get_full_page_ss(self, name='Full Page'):
        ss_handler.take_screenshot(name)
    
    def close(self):
        self.driver.close()

   