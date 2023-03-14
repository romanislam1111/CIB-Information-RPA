import os
import time

LOG_DIR = 'logs/media/' 

class ScreenshotHandler:

    @staticmethod
    def get_folders_cnt_in_dir(dir):
        all_info = os.walk(dir)
        a = [item for item in all_info]
        return len(a[0][1])
    
    @staticmethod
    def get_files_cnt_in_dir(dir):
        all_info = os.walk(dir)
        a = [item for item in all_info]
        return len(a[0][2])


    def __init__(self, driver, dir='screenshot'):
        self.driver = driver
        self.dir = LOG_DIR + dir 
        self.timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
        
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
        cnt =  ScreenshotHandler.get_folders_cnt_in_dir(self.dir)
        self.folder_name = f"Run__{str(cnt+1)}__t_{self.timestamp}" 
        

    #Didn't use this argument
    def take_screenshot(self, screenshotfield):
        ssgo = f'{screenshotfield}_{self.timestamp}.png'
        new_ss_folder = os.path.join(self.dir, self.folder_name)
        os.makedirs(new_ss_folder, exist_ok=True)
        ssgo = f"Step_{ScreenshotHandler.get_files_cnt_in_dir(new_ss_folder)+1}_{ssgo}"
        filepath = os.path.join(new_ss_folder, ssgo)
        self.driver.save_screenshot(filepath)
        return filepath
        

    
    def take_screenshot_of_element(self, screenshotfield, element):
        ssgo = f'{screenshotfield}_{self.timestamp}.png'
        new_ss_folder = os.path.join(self.dir, self.folder_name)
        os.makedirs(new_ss_folder, exist_ok=True)
        ssgo = f"Step_{ScreenshotHandler.get_files_cnt_in_dir(new_ss_folder)+1}_{ssgo}"
        filepath = os.path.join(new_ss_folder, ssgo)

        element.screenshot(filepath) 
        

        return filepath 
    
    